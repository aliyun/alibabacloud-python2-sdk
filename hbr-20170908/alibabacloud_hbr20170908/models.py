# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class OtsDetail(TeaModel):
    def __init__(self, table_names=None):
        self.table_names = table_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(OtsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class OtsTableRestoreDetail(TeaModel):
    def __init__(self, batch_channel_count=None, index_name_suffix=None, overwrite_existing=None,
                 re_generate_auto_increment_pk=None, restore_index=None, restore_search_index=None, search_index_name_suffix=None):
        self.batch_channel_count = batch_channel_count  # type: int
        self.index_name_suffix = index_name_suffix  # type: str
        self.overwrite_existing = overwrite_existing  # type: bool
        self.re_generate_auto_increment_pk = re_generate_auto_increment_pk  # type: bool
        self.restore_index = restore_index  # type: bool
        self.restore_search_index = restore_search_index  # type: bool
        self.search_index_name_suffix = search_index_name_suffix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OtsTableRestoreDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_channel_count is not None:
            result['BatchChannelCount'] = self.batch_channel_count
        if self.index_name_suffix is not None:
            result['IndexNameSuffix'] = self.index_name_suffix
        if self.overwrite_existing is not None:
            result['OverwriteExisting'] = self.overwrite_existing
        if self.re_generate_auto_increment_pk is not None:
            result['ReGenerateAutoIncrementPK'] = self.re_generate_auto_increment_pk
        if self.restore_index is not None:
            result['RestoreIndex'] = self.restore_index
        if self.restore_search_index is not None:
            result['RestoreSearchIndex'] = self.restore_search_index
        if self.search_index_name_suffix is not None:
            result['SearchIndexNameSuffix'] = self.search_index_name_suffix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchChannelCount') is not None:
            self.batch_channel_count = m.get('BatchChannelCount')
        if m.get('IndexNameSuffix') is not None:
            self.index_name_suffix = m.get('IndexNameSuffix')
        if m.get('OverwriteExisting') is not None:
            self.overwrite_existing = m.get('OverwriteExisting')
        if m.get('ReGenerateAutoIncrementPK') is not None:
            self.re_generate_auto_increment_pk = m.get('ReGenerateAutoIncrementPK')
        if m.get('RestoreIndex') is not None:
            self.restore_index = m.get('RestoreIndex')
        if m.get('RestoreSearchIndex') is not None:
            self.restore_search_index = m.get('RestoreSearchIndex')
        if m.get('SearchIndexNameSuffix') is not None:
            self.search_index_name_suffix = m.get('SearchIndexNameSuffix')
        return self


class Report(TeaModel):
    def __init__(self, failed_files=None, skipped_files=None, success_files=None, total_files=None):
        self.failed_files = failed_files  # type: str
        self.skipped_files = skipped_files  # type: str
        self.success_files = success_files  # type: str
        self.total_files = total_files  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Report, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_files is not None:
            result['FailedFiles'] = self.failed_files
        if self.skipped_files is not None:
            result['SkippedFiles'] = self.skipped_files
        if self.success_files is not None:
            result['SuccessFiles'] = self.success_files
        if self.total_files is not None:
            result['TotalFiles'] = self.total_files
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedFiles') is not None:
            self.failed_files = m.get('FailedFiles')
        if m.get('SkippedFiles') is not None:
            self.skipped_files = m.get('SkippedFiles')
        if m.get('SuccessFiles') is not None:
            self.success_files = m.get('SuccessFiles')
        if m.get('TotalFiles') is not None:
            self.total_files = m.get('TotalFiles')
        return self


class Rule(TeaModel):
    def __init__(self, backup_type=None, destination_region_id=None, destination_retention=None, disabled=None,
                 do_copy=None, retention=None, rule_name=None, schedule=None):
        self.backup_type = backup_type  # type: str
        self.destination_region_id = destination_region_id  # type: str
        self.destination_retention = destination_retention  # type: long
        self.disabled = disabled  # type: bool
        self.do_copy = do_copy  # type: bool
        self.retention = retention  # type: long
        self.rule_name = rule_name  # type: str
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Rule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class AddContainerClusterRequest(TeaModel):
    def __init__(self, cluster_type=None, description=None, identifier=None, name=None, network_type=None):
        # The type of the cluster. Only Container Service for Kubernetes (ACK) clusters are supported.
        self.cluster_type = cluster_type  # type: str
        # The description of the cluster.
        self.description = description  # type: str
        # The ID of the cluster that you want to register.
        self.identifier = identifier  # type: str
        # The name of the cluster.
        self.name = name  # type: str
        # The network type of the cluster. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: a virtual private cloud (VPC)
        self.network_type = network_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddContainerClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.description is not None:
            result['Description'] = self.description
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.name is not None:
            result['Name'] = self.name
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class AddContainerClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, code=None, message=None, request_id=None, success=None, token=None):
        # The ID of the cluster.
        self.cluster_id = cluster_id  # type: str
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success  # type: bool
        # The token that is used to register the Hybrid Backup Recovery (HBR) client in the cluster.
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddContainerClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class AddContainerClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddContainerClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddContainerClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddContainerClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachNasFileSystemRequest(TeaModel):
    def __init__(self, create_time=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, file_system_id=None):
        self.create_time = create_time  # type: str
        self.cross_account_role_name = cross_account_role_name  # type: str
        self.cross_account_type = cross_account_type  # type: str
        self.cross_account_user_id = cross_account_user_id  # type: long
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachNasFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class AttachNasFileSystemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachNasFileSystemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AttachNasFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachNasFileSystemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachNasFileSystemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachNasFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelBackupJobRequest(TeaModel):
    def __init__(self, job_id=None, vault_id=None):
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelBackupJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CancelBackupJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelBackupJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelBackupJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelBackupJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelBackupJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelBackupJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRestoreJobRequest(TeaModel):
    def __init__(self, restore_id=None, vault_id=None):
        # The ID of the restore job.
        self.restore_id = restore_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRestoreJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CancelRestoreJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The value 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: indicates that the request is successful.
        # *   false: indicates that the request fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRestoreJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelRestoreJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelRestoreJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelRestoreJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelRestoreJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, resource_id=None, resource_type=None):
        # The ID of the new resource group. You can view the available resource groups in the Resource Management console.
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The ID of the resource. The value of this parameter varies with the resource type. For example, if the ResourceType parameter is set to vault, the ResourceId parameter specifies the ID of the backup vault.
        self.resource_id = resource_id  # type: str
        # The type of the resource. Valid values:
        # 
        # *   **vault**: backup vault
        # *   **client**: backup client
        # *   **hanainstance**: SAP HANA instance
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRoleRequest(TeaModel):
    def __init__(self, check_role_type=None, cross_account_role_name=None, cross_account_user_id=None):
        self.check_role_type = check_role_type  # type: str
        self.cross_account_role_name = cross_account_role_name  # type: str
        self.cross_account_user_id = cross_account_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_role_type is not None:
            result['CheckRoleType'] = self.check_role_type
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckRoleType') is not None:
            self.check_role_type = m.get('CheckRoleType')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        return self


class CheckRoleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckRoleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckRoleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupJobRequest(TeaModel):
    def __init__(self, backup_type=None, cluster_id=None, container_cluster_id=None, container_resources=None,
                 cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None, detail=None, exclude=None, include=None,
                 initiated_by_ack=None, instance_id=None, job_name=None, options=None, retention=None, source_type=None,
                 speed_limit=None, vault_id=None):
        # The backup type. Valid values:
        # 
        # *   **COMPLETE**: full backup
        # *   **INCREMENTAL**: incremental backup
        self.backup_type = backup_type  # type: str
        # The ID of the cluster.
        self.cluster_id = cluster_id  # type: str
        # The ID of the cluster. This parameter is required only if you set the **SourceType** parameter to **CONTAINER**.
        self.container_cluster_id = container_cluster_id  # type: str
        # The cluster resources. This parameter is required only if you set the **SourceType** parameter to **CONTAINER**.
        self.container_resources = container_resources  # type: str
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        self.detail = detail  # type: dict[str, any]
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value must be 1 to 255 characters in length.
        self.include = include  # type: str
        # This parameter specifies whether to initiate the request by using Container Service for Kubernetes (ACK). Default value: false.
        self.initiated_by_ack = initiated_by_ack  # type: bool
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the backup job.
        self.job_name = job_name  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a source path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options  # type: str
        # The retention period of the backup data. Unit: days.
        self.retention = retention  # type: long
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **UDM_ECS**: ECS instances
        # *   **CONTAINER**: containers
        self.source_type = source_type  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies the throttling rules. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_cluster_id is not None:
            result['ContainerClusterId'] = self.container_cluster_id
        if self.container_resources is not None:
            result['ContainerResources'] = self.container_resources
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.options is not None:
            result['Options'] = self.options
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerClusterId') is not None:
            self.container_cluster_id = m.get('ContainerClusterId')
        if m.get('ContainerResources') is not None:
            self.container_resources = m.get('ContainerResources')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupJobShrinkRequest(TeaModel):
    def __init__(self, backup_type=None, cluster_id=None, container_cluster_id=None, container_resources=None,
                 cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None, detail_shrink=None, exclude=None,
                 include=None, initiated_by_ack=None, instance_id=None, job_name=None, options=None, retention=None,
                 source_type=None, speed_limit=None, vault_id=None):
        # The backup type. Valid values:
        # 
        # *   **COMPLETE**: full backup
        # *   **INCREMENTAL**: incremental backup
        self.backup_type = backup_type  # type: str
        # The ID of the cluster.
        self.cluster_id = cluster_id  # type: str
        # The ID of the cluster. This parameter is required only if you set the **SourceType** parameter to **CONTAINER**.
        self.container_cluster_id = container_cluster_id  # type: str
        # The cluster resources. This parameter is required only if you set the **SourceType** parameter to **CONTAINER**.
        self.container_resources = container_resources  # type: str
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        self.detail_shrink = detail_shrink  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value must be 1 to 255 characters in length.
        self.include = include  # type: str
        # This parameter specifies whether to initiate the request by using Container Service for Kubernetes (ACK). Default value: false.
        self.initiated_by_ack = initiated_by_ack  # type: bool
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the backup job.
        self.job_name = job_name  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a source path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options  # type: str
        # The retention period of the backup data. Unit: days.
        self.retention = retention  # type: long
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **UDM_ECS**: ECS instances
        # *   **CONTAINER**: containers
        self.source_type = source_type  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **ECS_FILE**. This parameter specifies the throttling rules. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupJobShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_cluster_id is not None:
            result['ContainerClusterId'] = self.container_cluster_id
        if self.container_resources is not None:
            result['ContainerResources'] = self.container_resources
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.options is not None:
            result['Options'] = self.options
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerClusterId') is not None:
            self.container_cluster_id = m.get('ContainerClusterId')
        if m.get('ContainerResources') is not None:
            self.container_resources = m.get('ContainerResources')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupJobResponseBody(TeaModel):
    def __init__(self, code=None, job_id=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBackupJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBackupJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBackupJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequestRule(TeaModel):
    def __init__(self, backup_type=None, destination_region_id=None, destination_retention=None, disabled=None,
                 do_copy=None, retention=None, rule_name=None, schedule=None):
        # The backup type.
        self.backup_type = backup_type  # type: str
        # The ID of the region to which data is replicated.
        self.destination_region_id = destination_region_id  # type: str
        # The retention period of the backup data in geo-redundancy mode. Unit: days.
        self.destination_retention = destination_retention  # type: long
        # Specifies whether to enable the rule.
        self.disabled = disabled  # type: bool
        # Specifies whether to enable cross-region replication.
        self.do_copy = do_copy  # type: bool
        # The retention period of the backup data. Unit: days.
        self.retention = retention  # type: long
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The backup policy. Format: I|{startTime}|{interval}. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is complete. For example, I|1631685600|P1D specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds. interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPlanRequestRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateBackupPlanRequest(TeaModel):
    def __init__(self, backup_type=None, bucket=None, change_list_path=None, create_time=None,
                 cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None, dest_data_source_detail=None,
                 dest_data_source_id=None, dest_source_type=None, detail=None, disabled=None, exclude=None, file_system_id=None,
                 include=None, instance_id=None, instance_name=None, keep_latest_snapshots=None, options=None,
                 ots_detail=None, path=None, plan_name=None, prefix=None, retention=None, rule=None, schedule=None,
                 source_type=None, speed_limit=None, udm_region_id=None, vault_id=None):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the name of the OSS bucket.
        self.bucket = bucket  # type: str
        # The configurations of the incremental file synchronization. This parameter is required for data synchronization only.
        self.change_list_path = change_list_path  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **NAS**. This parameter specifies the time to create the file system. The value must be a UNIX timestamp. Unit: seconds.
        self.create_time = create_time  # type: long
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        self.dest_data_source_detail = dest_data_source_detail  # type: dict[str, any]
        self.dest_data_source_id = dest_data_source_id  # type: str
        self.dest_source_type = dest_source_type  # type: str
        # The details about ECS instance backup. The value is a JSON string.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are enhanced SSDs (ESSDs).
        # *   appConsistent: specifies whether to enable application consistency. If you set this parameter to true, you must also specify the preScriptPath and postScriptPath parameters.
        # *   preScriptPath: the path to the prescript file.
        # *   postScriptPath: the path to the postscript file.
        self.detail = detail  # type: dict[str, any]
        self.disabled = disabled  # type: bool
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value can be up to 255 characters in length.
        self.exclude = exclude  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **NAS**. This parameter specifies the ID of the NAS file system.
        self.file_system_id = file_system_id  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value can be up to 255 characters in length.
        self.include = include  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the Tablestore instance.
        self.instance_name = instance_name  # type: str
        # Specifies whether to enable the "Keep at least one backup version" feature. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a backup path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before the system sets this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail  # type: OtsDetail
        # The backup paths.
        self.path = path  # type: list[str]
        # The name of the backup schedule. The name must be 1 to 64 characters in length. The name of a backup schedule for each type of data source must be unique within a backup vault.
        self.plan_name = plan_name  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to back up. After a prefix is specified, only objects whose names start with the prefix are backed up.
        self.prefix = prefix  # type: str
        # The retention period of backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # The rules of the backup schedule.
        self.rule = rule  # type: list[CreateBackupPlanRequestRule]
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the `{startTime}` parameter and the subsequent backup jobs at an interval that is specified in the `{interval}` parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is complete. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backs up Elastic Compute Service (ECS) files.
        # *   **OSS**: backs up Object Storage Service (OSS) buckets.
        # *   **NAS**: backs up Apsara File Storage NAS file systems.
        # *   **OTS**: backs up Tablestore instances.
        # *   **UDM_ECS**: backs up ECS instances.
        self.source_type = source_type  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the throttling rules. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit  # type: str
        # The region in which the ECS instance that you want to back up resides.
        self.udm_region_id = udm_region_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = OtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = CreateBackupPlanRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupPlanShrinkRequestRule(TeaModel):
    def __init__(self, backup_type=None, destination_region_id=None, destination_retention=None, disabled=None,
                 do_copy=None, retention=None, rule_name=None, schedule=None):
        # The backup type.
        self.backup_type = backup_type  # type: str
        # The ID of the region to which data is replicated.
        self.destination_region_id = destination_region_id  # type: str
        # The retention period of the backup data in geo-redundancy mode. Unit: days.
        self.destination_retention = destination_retention  # type: long
        # Specifies whether to enable the rule.
        self.disabled = disabled  # type: bool
        # Specifies whether to enable cross-region replication.
        self.do_copy = do_copy  # type: bool
        # The retention period of the backup data. Unit: days.
        self.retention = retention  # type: long
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The backup policy. Format: I|{startTime}|{interval}. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is complete. For example, I|1631685600|P1D specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds. interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPlanShrinkRequestRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateBackupPlanShrinkRequest(TeaModel):
    def __init__(self, backup_type=None, bucket=None, change_list_path=None, create_time=None,
                 cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None, dest_data_source_detail_shrink=None,
                 dest_data_source_id=None, dest_source_type=None, detail_shrink=None, disabled=None, exclude=None, file_system_id=None,
                 include=None, instance_id=None, instance_name=None, keep_latest_snapshots=None, options=None,
                 ots_detail_shrink=None, path=None, plan_name=None, prefix=None, retention=None, rule=None, schedule=None,
                 source_type=None, speed_limit=None, udm_region_id=None, vault_id=None):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the name of the OSS bucket.
        self.bucket = bucket  # type: str
        # The configurations of the incremental file synchronization. This parameter is required for data synchronization only.
        self.change_list_path = change_list_path  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **NAS**. This parameter specifies the time to create the file system. The value must be a UNIX timestamp. Unit: seconds.
        self.create_time = create_time  # type: long
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        self.dest_data_source_detail_shrink = dest_data_source_detail_shrink  # type: str
        self.dest_data_source_id = dest_data_source_id  # type: str
        self.dest_source_type = dest_source_type  # type: str
        # The details about ECS instance backup. The value is a JSON string.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are enhanced SSDs (ESSDs).
        # *   appConsistent: specifies whether to enable application consistency. If you set this parameter to true, you must also specify the preScriptPath and postScriptPath parameters.
        # *   preScriptPath: the path to the prescript file.
        # *   postScriptPath: the path to the postscript file.
        self.detail_shrink = detail_shrink  # type: str
        self.disabled = disabled  # type: bool
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value can be up to 255 characters in length.
        self.exclude = exclude  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **NAS**. This parameter specifies the ID of the NAS file system.
        self.file_system_id = file_system_id  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value can be up to 255 characters in length.
        self.include = include  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the Tablestore instance.
        self.instance_name = instance_name  # type: str
        # Specifies whether to enable the "Keep at least one backup version" feature. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a backup path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before the system sets this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink  # type: str
        # The backup paths.
        self.path = path  # type: list[str]
        # The name of the backup schedule. The name must be 1 to 64 characters in length. The name of a backup schedule for each type of data source must be unique within a backup vault.
        self.plan_name = plan_name  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to back up. After a prefix is specified, only objects whose names start with the prefix are backed up.
        self.prefix = prefix  # type: str
        # The retention period of backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # The rules of the backup schedule.
        self.rule = rule  # type: list[CreateBackupPlanShrinkRequestRule]
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the `{startTime}` parameter and the subsequent backup jobs at an interval that is specified in the `{interval}` parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is complete. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backs up Elastic Compute Service (ECS) files.
        # *   **OSS**: backs up Object Storage Service (OSS) buckets.
        # *   **NAS**: backs up Apsara File Storage NAS file systems.
        # *   **OTS**: backs up Tablestore instances.
        # *   **UDM_ECS**: backs up ECS instances.
        self.source_type = source_type  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the throttling rules. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit  # type: str
        # The region in which the ECS instance that you want to back up resides.
        self.udm_region_id = udm_region_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateBackupPlanShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.dest_data_source_detail_shrink is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail_shrink
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail_shrink = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = CreateBackupPlanShrinkRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, plan_id=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the backup schedule.
        self.plan_id = plan_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBackupPlanResponseBody

    def validate(self):
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


class CreateClientsRequest(TeaModel):
    def __init__(self, alert_setting=None, client_info=None, resource_group_id=None, use_https=None, vault_id=None):
        # The alert settings. Valid value: INHERITED, which indicates that the HBR client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting  # type: str
        # The installation information of the HBR clients.
        self.client_info = client_info  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # Specifies whether to transmit data over HTTPS. Valid values:
        # 
        # *   true: transmits data over HTTPS.
        # *   false: transmits data over HTTP.
        self.use_https = use_https  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateClientsResponseBodyInstanceStatusesInstanceStatus(TeaModel):
    def __init__(self, instance_id=None, valid_instance=None):
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether an HBR client can be installed on the ECS instance. Valid values:
        # 
        # *   true: An HBR client can be installed on the ECS instance.
        # *   false: An HBR client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientsResponseBodyInstanceStatusesInstanceStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class CreateClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(self, instance_status=None):
        self.instance_status = instance_status  # type: list[CreateClientsResponseBodyInstanceStatusesInstanceStatus]

    def validate(self):
        if self.instance_status:
            for k in self.instance_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClientsResponseBodyInstanceStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceStatus'] = []
        if self.instance_status is not None:
            for k in self.instance_status:
                result['InstanceStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_status = []
        if m.get('InstanceStatus') is not None:
            for k in m.get('InstanceStatus'):
                temp_model = CreateClientsResponseBodyInstanceStatusesInstanceStatus()
                self.instance_status.append(temp_model.from_map(k))
        return self


class CreateClientsResponseBody(TeaModel):
    def __init__(self, code=None, instance_statuses=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The status of the ECS instance. If you specify more than one instance IDs in the request and the status of an ECS instance does not meet the requirements to install an HBR client, an error message is returned based on the value of this parameter.
        self.instance_statuses = instance_statuses  # type: CreateClientsResponseBodyInstanceStatuses
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        if self.instance_statuses:
            self.instance_statuses.validate()

    def to_map(self):
        _map = super(CreateClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_statuses is not None:
            result['InstanceStatuses'] = self.instance_statuses.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceStatuses') is not None:
            temp_model = CreateClientsResponseBodyInstanceStatuses()
            self.instance_statuses = temp_model.from_map(m['InstanceStatuses'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClientsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClientsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHanaBackupPlanRequest(TeaModel):
    def __init__(self, backup_prefix=None, backup_type=None, cluster_id=None, database_name=None, plan_name=None,
                 resource_group_id=None, schedule=None, vault_id=None):
        # The backup prefix.
        self.backup_prefix = backup_prefix  # type: str
        # The backup type. Valid values:
        # 
        # *   COMPLETE: full backup
        # *   INCREMENTAL: incremental backup
        # *   DIFFERENTIAL: differential backup
        self.backup_type = backup_type  # type: str
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The name of the backup plan.
        self.plan_name = plan_name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHanaBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateHanaBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, plan_id=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message  # type: str
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHanaBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHanaBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHanaBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHanaBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHanaInstanceRequest(TeaModel):
    def __init__(self, alert_setting=None, ecs_instance_id=None, hana_name=None, host=None, instance_number=None,
                 password=None, resource_group_id=None, sid=None, use_ssl=None, user_name=None, validate_certificate=None,
                 vault_id=None):
        # The alert settings. Valid value: INHERITED, which indicates that the backup client sends alert notifications in the same way as the backup vault.
        self.alert_setting = alert_setting  # type: str
        # The IDs of ECS instances that host the SAP HANA instance to be registered. HBR installs backup clients on the specified ECS instances.
        self.ecs_instance_id = ecs_instance_id  # type: str
        # The name of the SAP HANA instance.
        self.hana_name = hana_name  # type: str
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host  # type: str
        # The instance number of the SAP HANA system.
        self.instance_number = instance_number  # type: int
        # The password that is used to connect with the SAP HANA database.
        self.password = password  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The security identifier (SID) of the SAP HANA database.
        # 
        # For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?spm=a2c4g.11186623.0.0.55c34b4ftZeXNK)
        self.sid = sid  # type: str
        # Specifies whether to connect with the SAP HANA database over Secure Sockets Layer (SSL).
        self.use_ssl = use_ssl  # type: bool
        # The username of the SYSTEMDB database.
        self.user_name = user_name  # type: str
        # Specifies whether to verify the SSL certificate of the SAP HANA database.
        self.validate_certificate = validate_certificate  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHanaInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.hana_name is not None:
            result['HanaName'] = self.hana_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateHanaInstanceResponseBody(TeaModel):
    def __init__(self, cluster_id=None, code=None, message=None, request_id=None, success=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHanaInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHanaInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHanaInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHanaInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHanaInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHanaRestoreRequest(TeaModel):
    def __init__(self, backup_id=None, backup_prefix=None, check_access=None, clear_log=None, cluster_id=None,
                 database_name=None, log_position=None, master_client_id=None, mode=None, recovery_point_in_time=None,
                 sid_admin=None, source=None, source_cluster_id=None, system_copy=None, use_catalog=None, use_delta=None,
                 vault_id=None, volume_id=None):
        # The ID of the backup.
        self.backup_id = backup_id  # type: long
        # The backup prefix.
        self.backup_prefix = backup_prefix  # type: str
        # Specifies whether to validate the differential backup and log backup. Valid values: true and false. If you set the value to true, HBR checks whether the required differential backup and log backup are available before the restore job starts. If the differential backup or log backup is unavailable, HBR does not start the restore job.
        self.check_access = check_access  # type: bool
        # Specifies whether to delete all log entries from the log area after the log entries are restored. Valid values: true and false. If you set the value to false, all log entries are deleted from the log area after the log entries are restored.
        self.clear_log = clear_log  # type: bool
        # The ID of the SAP HANA instance that you want to restore.
        self.cluster_id = cluster_id  # type: str
        # The name of the database that you want to restore.
        self.database_name = database_name  # type: str
        # The log position to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position  # type: long
        # The ID of the client where the primary node of the SAP HANA resides.
        self.master_client_id = master_client_id  # type: str
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: restores the database to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: restores the database to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: restores the database to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: restores the database to a specified log position.
        self.mode = mode  # type: str
        # The point in time to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_POINT_IN_TIME**. HBR restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time  # type: long
        # The SID admin account that is created by SAP HANA.
        self.sid_admin = sid_admin  # type: str
        # The name of the source system. This parameter specifies the name of the source database that you want to restore. You must set the parameter in the `<Source database name>@SID` format.
        self.source = source  # type: str
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id  # type: str
        # Specifies whether to restore the database to a different instance.
        self.system_copy = system_copy  # type: bool
        # Specifies whether to use a catalog backup to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_SPECIFIC_BACKUP**. If you do not use a catalog backup, you must specify the prefix of a backup file. Then, HBR finds the backup file based on the specified prefix and restores the backup file.
        self.use_catalog = use_catalog  # type: bool
        # Specifies whether to use a differential backup or an incremental backup to restore the database. Valid values: true and false. If you want to use a differential backup or an incremental backup to restore the database, set the value to true. If you set the value to false, HBR uses a log backup to restore the database.
        self.use_delta = use_delta  # type: bool
        # The ID of the vault.
        self.vault_id = vault_id  # type: str
        # The ID of the volume that you want to restore. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHanaRestoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.check_access is not None:
            result['CheckAccess'] = self.check_access
        if self.clear_log is not None:
            result['ClearLog'] = self.clear_log
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.log_position is not None:
            result['LogPosition'] = self.log_position
        if self.master_client_id is not None:
            result['MasterClientId'] = self.master_client_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time
        if self.sid_admin is not None:
            result['SidAdmin'] = self.sid_admin
        if self.source is not None:
            result['Source'] = self.source
        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id
        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy
        if self.use_catalog is not None:
            result['UseCatalog'] = self.use_catalog
        if self.use_delta is not None:
            result['UseDelta'] = self.use_delta
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('CheckAccess') is not None:
            self.check_access = m.get('CheckAccess')
        if m.get('ClearLog') is not None:
            self.clear_log = m.get('ClearLog')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')
        if m.get('MasterClientId') is not None:
            self.master_client_id = m.get('MasterClientId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')
        if m.get('SidAdmin') is not None:
            self.sid_admin = m.get('SidAdmin')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')
        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')
        if m.get('UseCatalog') is not None:
            self.use_catalog = m.get('UseCatalog')
        if m.get('UseDelta') is not None:
            self.use_delta = m.get('UseDelta')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        return self


class CreateHanaRestoreResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, restore_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the restore job.
        self.restore_id = restore_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHanaRestoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHanaRestoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHanaRestoreResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHanaRestoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHanaRestoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail(TeaModel):
    def __init__(self, fetch_slice_size=None, full_on_increment_fail=None):
        self.fetch_slice_size = fetch_slice_size  # type: long
        self.full_on_increment_fail = full_on_increment_fail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail(TeaModel):
    def __init__(self, cluster_id=None, fetch_slice_size=None, full_on_increment_fail=None):
        self.cluster_id = cluster_id  # type: str
        self.fetch_slice_size = fetch_slice_size  # type: long
        self.full_on_increment_fail = full_on_increment_fail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail(TeaModel):
    def __init__(self, adv_policy=None, use_vss=None):
        self.adv_policy = adv_policy  # type: bool
        self.use_vss = use_vss  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adv_policy is not None:
            result['AdvPolicy'] = self.adv_policy
        if self.use_vss is not None:
            result['UseVSS'] = self.use_vss
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvPolicy') is not None:
            self.adv_policy = m.get('AdvPolicy')
        if m.get('UseVSS') is not None:
            self.use_vss = m.get('UseVSS')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail(TeaModel):
    def __init__(self, inventory_cleanup_policy=None, inventory_id=None):
        # Whether delete inventory file after backup.
        # - **NO_CLEANUP**: Do not delete.
        # - **DELETE_CURRENT**: Delete current.
        # - **DELETE_CURRENT_AND_PREVIOUS**: Delete all.
        self.inventory_cleanup_policy = inventory_cleanup_policy  # type: str
        # OSS inventory name.
        # - If you want to back up more than 100 million OSS objects, we recommend that you use inventories to accelerate incremental backup. Storage fees for inventory lists are included into your OSS bills.
        # - OSS inventory file generation takes time. The backup may fail before the OSS inventory file is generated. You can wait for the next cycle to execute.
        self.inventory_id = inventory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_cleanup_policy is not None:
            result['InventoryCleanupPolicy'] = self.inventory_cleanup_policy
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InventoryCleanupPolicy') is not None:
            self.inventory_cleanup_policy = m.get('InventoryCleanupPolicy')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail(TeaModel):
    def __init__(self, app_consistent=None, disk_id_list=None, enable_fs_freeze=None, enable_writers=None,
                 exclude_disk_id_list=None, post_script_path=None, pre_script_path=None, ram_role_name=None, snapshot_group=None,
                 timeout_in_seconds=None):
        # Specifies whether to enable application consistency. You can enable application consistency only if all disks are ESSDs.
        self.app_consistent = app_consistent  # type: bool
        # The IDs of the disks that need to be protected. If all disks need to be protected, this parameter is empty.
        self.disk_id_list = disk_id_list  # type: list[str]
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies whether to enable Linux fsfreeze to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        self.enable_fs_freeze = enable_fs_freeze  # type: bool
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies whether to create application-consistent snapshots. Valid values:
        # 
        # *   true: creates application-consistent snapshots.
        # *   false: creates file system-consistent snapshots.
        # 
        # Default value: true.
        self.enable_writers = enable_writers  # type: bool
        # The IDs of the disks that do not need to be protected. If the DiskIdList parameter is not empty, this parameter is ignored.
        self.exclude_disk_id_list = exclude_disk_id_list  # type: list[str]
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the path of the post-thaw scripts that are executed after application-consistent snapshots are created.
        self.post_script_path = post_script_path  # type: str
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the path of the pre-freeze scripts that are executed before application-consistent snapshots are created.
        self.pre_script_path = pre_script_path  # type: str
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the name of the RAM role that is required to create application-consistent snapshots.
        self.ram_role_name = ram_role_name  # type: str
        # Specifies whether to create a snapshot-consistent group. You can create a snapshot-consistent group only if all disks are enhanced SSDs (ESSDs).
        self.snapshot_group = snapshot_group  # type: bool
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.timeout_in_seconds = timeout_in_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_consistent is not None:
            result['AppConsistent'] = self.app_consistent
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.enable_fs_freeze is not None:
            result['EnableFsFreeze'] = self.enable_fs_freeze
        if self.enable_writers is not None:
            result['EnableWriters'] = self.enable_writers
        if self.exclude_disk_id_list is not None:
            result['ExcludeDiskIdList'] = self.exclude_disk_id_list
        if self.post_script_path is not None:
            result['PostScriptPath'] = self.post_script_path
        if self.pre_script_path is not None:
            result['PreScriptPath'] = self.pre_script_path
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.snapshot_group is not None:
            result['SnapshotGroup'] = self.snapshot_group
        if self.timeout_in_seconds is not None:
            result['TimeoutInSeconds'] = self.timeout_in_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppConsistent') is not None:
            self.app_consistent = m.get('AppConsistent')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('EnableFsFreeze') is not None:
            self.enable_fs_freeze = m.get('EnableFsFreeze')
        if m.get('EnableWriters') is not None:
            self.enable_writers = m.get('EnableWriters')
        if m.get('ExcludeDiskIdList') is not None:
            self.exclude_disk_id_list = m.get('ExcludeDiskIdList')
        if m.get('PostScriptPath') is not None:
            self.post_script_path = m.get('PostScriptPath')
        if m.get('PreScriptPath') is not None:
            self.pre_script_path = m.get('PreScriptPath')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SnapshotGroup') is not None:
            self.snapshot_group = m.get('SnapshotGroup')
        if m.get('TimeoutInSeconds') is not None:
            self.timeout_in_seconds = m.get('TimeoutInSeconds')
        return self


class CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions(TeaModel):
    def __init__(self, common_file_system_detail=None, common_nas_detail=None, file_detail=None, oss_detail=None,
                 udm_detail=None):
        self.common_file_system_detail = common_file_system_detail  # type: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail
        self.common_nas_detail = common_nas_detail  # type: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail
        self.file_detail = file_detail  # type: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail
        # The advanced options for OSS backup.
        self.oss_detail = oss_detail  # type: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail
        # The details of ECS instance backup.
        self.udm_detail = udm_detail  # type: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail

    def validate(self):
        if self.common_file_system_detail:
            self.common_file_system_detail.validate()
        if self.common_nas_detail:
            self.common_nas_detail.validate()
        if self.file_detail:
            self.file_detail.validate()
        if self.oss_detail:
            self.oss_detail.validate()
        if self.udm_detail:
            self.udm_detail.validate()

    def to_map(self):
        _map = super(CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_file_system_detail is not None:
            result['CommonFileSystemDetail'] = self.common_file_system_detail.to_map()
        if self.common_nas_detail is not None:
            result['CommonNasDetail'] = self.common_nas_detail.to_map()
        if self.file_detail is not None:
            result['FileDetail'] = self.file_detail.to_map()
        if self.oss_detail is not None:
            result['OssDetail'] = self.oss_detail.to_map()
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonFileSystemDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m['CommonFileSystemDetail'])
        if m.get('CommonNasDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsCommonNasDetail()
            self.common_nas_detail = temp_model.from_map(m['CommonNasDetail'])
        if m.get('FileDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsFileDetail()
            self.file_detail = temp_model.from_map(m['FileDetail'])
        if m.get('OssDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m['OssDetail'])
        if m.get('UdmDetail') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m['UdmDetail'])
        return self


class CreatePolicyBindingsRequestPolicyBindingList(TeaModel):
    def __init__(self, advanced_options=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, data_source_id=None, policy_binding_description=None, source=None, source_type=None):
        # Advanced options.
        self.advanced_options = advanced_options  # type: CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The source Alibaba Cloud account ID when backup across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The ID of the data source.
        self.data_source_id = data_source_id  # type: str
        # The description of the association.
        self.policy_binding_description = policy_binding_description  # type: str
        # The prefix of the path to the folder that you want to back up. By default, the entire OSS bucket is backed up.
        self.source = source  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type  # type: str

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()

    def to_map(self):
        _map = super(CreatePolicyBindingsRequestPolicyBindingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = CreatePolicyBindingsRequestPolicyBindingListAdvancedOptions()
            self.advanced_options = temp_model.from_map(m['AdvancedOptions'])
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class CreatePolicyBindingsRequest(TeaModel):
    def __init__(self, policy_binding_list=None, policy_id=None):
        # The data sources that you want to bind to the backup policy.
        self.policy_binding_list = policy_binding_list  # type: list[CreatePolicyBindingsRequestPolicyBindingList]
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str

    def validate(self):
        if self.policy_binding_list:
            for k in self.policy_binding_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePolicyBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyBindingList'] = []
        if self.policy_binding_list is not None:
            for k in self.policy_binding_list:
                result['PolicyBindingList'].append(k.to_map() if k else None)
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy_binding_list = []
        if m.get('PolicyBindingList') is not None:
            for k in m.get('PolicyBindingList'):
                temp_model = CreatePolicyBindingsRequestPolicyBindingList()
                self.policy_binding_list.append(temp_model.from_map(k))
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class CreatePolicyBindingsShrinkRequest(TeaModel):
    def __init__(self, policy_binding_list_shrink=None, policy_id=None):
        # The data sources that you want to bind to the backup policy.
        self.policy_binding_list_shrink = policy_binding_list_shrink  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyBindingsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_binding_list_shrink is not None:
            result['PolicyBindingList'] = self.policy_binding_list_shrink
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyBindingList') is not None:
            self.policy_binding_list_shrink = m.get('PolicyBindingList')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class CreatePolicyBindingsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyBindingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePolicyBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePolicyBindingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolicyBindingsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePolicyBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyV2RequestRulesRetentionRules(TeaModel):
    def __init__(self, advanced_retention_type=None, retention=None, which_snapshot=None):
        # The type of the special retention rule. Valid values:
        # 
        # *   **WEEKLY**: weekly backups
        # *   **MONTHLY**: monthly backups
        # *   **YEARLY**: yearly backups
        self.advanced_retention_type = advanced_retention_type  # type: str
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # Specifies which backup is retained based on the special retention rule. Only the first backup can be retained.
        self.which_snapshot = which_snapshot  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyV2RequestRulesRetentionRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.which_snapshot is not None:
            result['WhichSnapshot'] = self.which_snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('WhichSnapshot') is not None:
            self.which_snapshot = m.get('WhichSnapshot')
        return self


class CreatePolicyV2RequestRules(TeaModel):
    def __init__(self, backup_type=None, keep_latest_snapshots=None, replication_region_id=None, retention=None,
                 retention_rules=None, rule_type=None, schedule=None):
        # This parameter is required only if you set the **RuleType** parameter to **BACKUP**. This parameter specifies the backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # This parameter is required only if you set the **RuleType** parameter to **REPLICATION**. This parameter specifies the ID of the destination region.
        self.replication_region_id = replication_region_id  # type: str
        # This parameter is required only if you set the **RuleType** parameter to **TRANSITION** or **REPLICATION**.
        # 
        # *   If the **RuleType** parameter is set to **TRANSITION**, this parameter specifies the retention period of the backup data. Minimum value: 1. Maximum value: 364635. Unit: days.
        # *   If the **RuleType** parameter is set to **REPLICATION**, this parameter specifies the retention period of remote backups. Minimum value: 1. Maximum value: 364635. Unit: days.
        self.retention = retention  # type: long
        # This parameter is required only if you set the **RuleType** parameter to **TRANSITION**. This parameter specifies the special retention rules.
        self.retention_rules = retention_rules  # type: list[CreatePolicyV2RequestRulesRetentionRules]
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type.
        # 
        # *   **BACKUP**: backup rule
        # *   **TRANSITION**: lifecycle rule
        # *   **REPLICATION**: replication rule
        self.rule_type = rule_type  # type: str
        # This parameter is required only if you set the **RuleType** parameter to **BACKUP**. This parameter specifies the backup schedule settings. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is complete. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str

    def validate(self):
        if self.retention_rules:
            for k in self.retention_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePolicyV2RequestRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.replication_region_id is not None:
            result['ReplicationRegionId'] = self.replication_region_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['RetentionRules'] = []
        if self.retention_rules is not None:
            for k in self.retention_rules:
                result['RetentionRules'].append(k.to_map() if k else None)
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('ReplicationRegionId') is not None:
            self.replication_region_id = m.get('ReplicationRegionId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.retention_rules = []
        if m.get('RetentionRules') is not None:
            for k in m.get('RetentionRules'):
                temp_model = CreatePolicyV2RequestRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k))
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreatePolicyV2Request(TeaModel):
    def __init__(self, policy_description=None, policy_name=None, rules=None):
        # The description of the backup policy.
        self.policy_description = policy_description  # type: str
        # The name of the backup policy.
        self.policy_name = policy_name  # type: str
        # The rules in the backup policy.
        self.rules = rules  # type: list[CreatePolicyV2RequestRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePolicyV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = CreatePolicyV2RequestRules()
                self.rules.append(temp_model.from_map(k))
        return self


class CreatePolicyV2ShrinkRequest(TeaModel):
    def __init__(self, policy_description=None, policy_name=None, rules_shrink=None):
        # The description of the backup policy.
        self.policy_description = policy_description  # type: str
        # The name of the backup policy.
        self.policy_name = policy_name  # type: str
        # The rules in the backup policy.
        self.rules_shrink = rules_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyV2ShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')
        return self


class CreatePolicyV2ResponseBody(TeaModel):
    def __init__(self, code=None, message=None, policy_id=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePolicyV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePolicyV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolicyV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReplicationVaultRequest(TeaModel):
    def __init__(self, description=None, redundancy_type=None, replication_source_region_id=None,
                 replication_source_vault_id=None, vault_name=None, vault_region_id=None, vault_storage_class=None):
        # The description of the backup vault. The description must be 0 to 255 characters in length.
        self.description = description  # type: str
        # The data redundancy type of the backup vault. Valid values:
        # 
        # - LRS: Locally redundant storage (LRS) is enabled for the backup vault. HBR stores the copies of each object on multiple devices of different facilities in the same zone. This way, HBR ensures data durability and availability even if hardware failures occur.
        # - ZRS: Zone-redundant storage (ZRS) is enabled for the backup vault. HBR uses the multi-zone mechanism to distribute data across three zones within the same region. If a zone becomes unavailable, the data can still be accessed.
        self.redundancy_type = redundancy_type  # type: str
        # The ID of the region where the source vault resides.
        self.replication_source_region_id = replication_source_region_id  # type: str
        # The ID of the source vault.
        self.replication_source_vault_id = replication_source_vault_id  # type: str
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        self.vault_name = vault_name  # type: str
        # The ID of the region where the backup vault resides.
        self.vault_region_id = vault_region_id  # type: str
        # The storage type of the backup vault. Valid value: **STANDARD**. The value indicates standard storage.
        self.vault_storage_class = vault_storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReplicationVaultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type
        if self.replication_source_region_id is not None:
            result['ReplicationSourceRegionId'] = self.replication_source_region_id
        if self.replication_source_vault_id is not None:
            result['ReplicationSourceVaultId'] = self.replication_source_vault_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')
        if m.get('ReplicationSourceRegionId') is not None:
            self.replication_source_region_id = m.get('ReplicationSourceRegionId')
        if m.get('ReplicationSourceVaultId') is not None:
            self.replication_source_vault_id = m.get('ReplicationSourceVaultId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')
        return self


class CreateReplicationVaultResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None, vault_id=None):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The message that is returned. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success  # type: bool
        # The ID of the initialization task used to initialize the backup vault.
        # 
        # You can call the DescribeTask operation to query the status of an initialization task.
        self.task_id = task_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReplicationVaultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateReplicationVaultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateReplicationVaultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReplicationVaultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateReplicationVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRestoreJobRequest(TeaModel):
    def __init__(self, cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None,
                 exclude=None, failback_detail=None, include=None, initiated_by_ack=None, options=None, ots_detail=None,
                 restore_type=None, snapshot_hash=None, snapshot_id=None, source_type=None, target_bucket=None,
                 target_container=None, target_container_cluster_id=None, target_create_time=None, target_file_system_id=None,
                 target_instance_id=None, target_instance_name=None, target_path=None, target_prefix=None, target_table_name=None,
                 target_time=None, udm_detail=None, udm_region_id=None, vault_id=None):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The paths to the files that you do not want to restore. No files in the specified paths are restored. The value must be 1 to 255 characters in length.
        self.exclude = exclude  # type: str
        self.failback_detail = failback_detail  # type: dict[str, any]
        # The paths to the files that you want to restore. All files in the specified paths are restored. The value must be 1 to 255 characters in length.
        self.include = include  # type: str
        # Specifies whether to initiate the request by using Container Service for Kubernetes (ACK). Default value: false.
        self.initiated_by_ack = initiated_by_ack  # type: bool
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail  # type: OtsTableRestoreDetail
        # The type of the restore destination. Valid values:
        # 
        # *   **ECS_FILE**: restores data to Elastic Compute Service (ECS) files.
        # *   **OSS**: restores data to Object Storage Service (OSS) buckets.
        # *   **NAS**: restores data to Apsara File Storage NAS file systems.
        # *   **OTS_TABLE**: restores data to Tablestore instances.
        # *   **UDM_ECS_ROLLBACK**: restores data to ECS instances.
        self.restore_type = restore_type  # type: str
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash  # type: str
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **OSS**. This parameter specifies the name of the OSS bucket to which you want to restore data.
        self.target_bucket = target_bucket  # type: str
        # The details about the container to which you want to restore data.
        self.target_container = target_container  # type: str
        # The ID of the container cluster to which you want to restore data.
        self.target_container_cluster_id = target_container_cluster_id  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **NAS**. This parameter specifies the time when the file system is created.
        self.target_create_time = target_create_time  # type: long
        # This parameter is required only if the **RestoreType** parameter is set to **NAS**. This parameter specifies the ID of the file system to which you want to restore data.
        self.target_file_system_id = target_file_system_id  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **ECS_FILE**. This parameter specifies the ID of the ECS instance to which you want to restore data.
        self.target_instance_id = target_instance_id  # type: str
        # The name of the Tablestore instance to which you want to restore data.
        self.target_instance_name = target_instance_name  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **ECS_FILE**. This parameter specifies the destination file path.
        self.target_path = target_path  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to restore.
        self.target_prefix = target_prefix  # type: str
        # The name of the table that stores the restored data.
        self.target_table_name = target_table_name  # type: str
        # The time when data is restored to the Tablestore instance. The value must be a UNIX timestamp. Unit: seconds.
        self.target_time = target_time  # type: long
        # The details of ECS instance backup.
        self.udm_detail = udm_detail  # type: dict[str, any]
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the region to which you want to restore data.
        self.udm_region_id = udm_region_id  # type: str
        # The ID of the backup vault to which the backup snapshot belongs.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()

    def to_map(self):
        _map = super(CreateRestoreJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.failback_detail is not None:
            result['FailbackDetail'] = self.failback_detail
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_container is not None:
            result['TargetContainer'] = self.target_container
        if self.target_container_cluster_id is not None:
            result['TargetContainerClusterId'] = self.target_container_cluster_id
        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time
        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        if self.target_time is not None:
            result['TargetTime'] = self.target_time
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FailbackDetail') is not None:
            self.failback_detail = m.get('FailbackDetail')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = OtsTableRestoreDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetContainer') is not None:
            self.target_container = m.get('TargetContainer')
        if m.get('TargetContainerClusterId') is not None:
            self.target_container_cluster_id = m.get('TargetContainerClusterId')
        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')
        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')
        if m.get('UdmDetail') is not None:
            self.udm_detail = m.get('UdmDetail')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateRestoreJobShrinkRequest(TeaModel):
    def __init__(self, cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None,
                 exclude=None, failback_detail_shrink=None, include=None, initiated_by_ack=None, options=None,
                 ots_detail_shrink=None, restore_type=None, snapshot_hash=None, snapshot_id=None, source_type=None,
                 target_bucket=None, target_container=None, target_container_cluster_id=None, target_create_time=None,
                 target_file_system_id=None, target_instance_id=None, target_instance_name=None, target_path=None, target_prefix=None,
                 target_table_name=None, target_time=None, udm_detail_shrink=None, udm_region_id=None, vault_id=None):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The paths to the files that you do not want to restore. No files in the specified paths are restored. The value must be 1 to 255 characters in length.
        self.exclude = exclude  # type: str
        self.failback_detail_shrink = failback_detail_shrink  # type: str
        # The paths to the files that you want to restore. All files in the specified paths are restored. The value must be 1 to 255 characters in length.
        self.include = include  # type: str
        # Specifies whether to initiate the request by using Container Service for Kubernetes (ACK). Default value: false.
        self.initiated_by_ack = initiated_by_ack  # type: bool
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink  # type: str
        # The type of the restore destination. Valid values:
        # 
        # *   **ECS_FILE**: restores data to Elastic Compute Service (ECS) files.
        # *   **OSS**: restores data to Object Storage Service (OSS) buckets.
        # *   **NAS**: restores data to Apsara File Storage NAS file systems.
        # *   **OTS_TABLE**: restores data to Tablestore instances.
        # *   **UDM_ECS_ROLLBACK**: restores data to ECS instances.
        self.restore_type = restore_type  # type: str
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash  # type: str
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **OSS**. This parameter specifies the name of the OSS bucket to which you want to restore data.
        self.target_bucket = target_bucket  # type: str
        # The details about the container to which you want to restore data.
        self.target_container = target_container  # type: str
        # The ID of the container cluster to which you want to restore data.
        self.target_container_cluster_id = target_container_cluster_id  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **NAS**. This parameter specifies the time when the file system is created.
        self.target_create_time = target_create_time  # type: long
        # This parameter is required only if the **RestoreType** parameter is set to **NAS**. This parameter specifies the ID of the file system to which you want to restore data.
        self.target_file_system_id = target_file_system_id  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **ECS_FILE**. This parameter specifies the ID of the ECS instance to which you want to restore data.
        self.target_instance_id = target_instance_id  # type: str
        # The name of the Tablestore instance to which you want to restore data.
        self.target_instance_name = target_instance_name  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **ECS_FILE**. This parameter specifies the destination file path.
        self.target_path = target_path  # type: str
        # This parameter is required only if the **RestoreType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to restore.
        self.target_prefix = target_prefix  # type: str
        # The name of the table that stores the restored data.
        self.target_table_name = target_table_name  # type: str
        # The time when data is restored to the Tablestore instance. The value must be a UNIX timestamp. Unit: seconds.
        self.target_time = target_time  # type: long
        # The details of ECS instance backup.
        self.udm_detail_shrink = udm_detail_shrink  # type: str
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the region to which you want to restore data.
        self.udm_region_id = udm_region_id  # type: str
        # The ID of the backup vault to which the backup snapshot belongs.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRestoreJobShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.failback_detail_shrink is not None:
            result['FailbackDetail'] = self.failback_detail_shrink
        if self.include is not None:
            result['Include'] = self.include
        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_container is not None:
            result['TargetContainer'] = self.target_container
        if self.target_container_cluster_id is not None:
            result['TargetContainerClusterId'] = self.target_container_cluster_id
        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time
        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        if self.target_time is not None:
            result['TargetTime'] = self.target_time
        if self.udm_detail_shrink is not None:
            result['UdmDetail'] = self.udm_detail_shrink
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FailbackDetail') is not None:
            self.failback_detail_shrink = m.get('FailbackDetail')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetContainer') is not None:
            self.target_container = m.get('TargetContainer')
        if m.get('TargetContainerClusterId') is not None:
            self.target_container_cluster_id = m.get('TargetContainerClusterId')
        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')
        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')
        if m.get('UdmDetail') is not None:
            self.udm_detail_shrink = m.get('UdmDetail')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateRestoreJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, restore_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the restore job.
        self.restore_id = restore_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRestoreJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRestoreJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRestoreJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRestoreJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRestoreJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTempFileUploadUrlRequest(TeaModel):
    def __init__(self, file_name=None):
        # The name of the file to be uploaded.
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTempFileUploadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateTempFileUploadUrlResponseBody(TeaModel):
    def __init__(self, bucket_name=None, code=None, endpoint=None, expire_time=None, message=None,
                 oss_access_key_id=None, policy=None, request_id=None, signature=None, success=None, temp_file_key=None):
        # The name of the OSS bucket to which the file is uploaded.
        self.bucket_name = bucket_name  # type: str
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The endpoint that is used to upload the file to OSS.
        self.endpoint = endpoint  # type: str
        # The expiration time of the signature that is used to upload the file to OSS. This value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time  # type: long
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The AccessKey ID that is used to upload the file to OSS.
        self.oss_access_key_id = oss_access_key_id  # type: str
        # The policy that is used to upload the file to OSS.
        self.policy = policy  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The signature that is used to upload the file to OSS.
        self.signature = signature  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The key that is used to upload the file to OSS.
        self.temp_file_key = temp_file_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTempFileUploadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.code is not None:
            result['Code'] = self.code
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.message is not None:
            result['Message'] = self.message
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.success is not None:
            result['Success'] = self.success
        if self.temp_file_key is not None:
            result['TempFileKey'] = self.temp_file_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TempFileKey') is not None:
            self.temp_file_key = m.get('TempFileKey')
        return self


class CreateTempFileUploadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTempFileUploadUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTempFileUploadUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTempFileUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVaultRequest(TeaModel):
    def __init__(self, description=None, encrypt_type=None, kms_key_id=None, vault_name=None, vault_region_id=None,
                 vault_storage_class=None, vault_type=None):
        # The description of the backup vault. The description must be 0 to 255 characters in length.
        self.description = description  # type: str
        # The method that is used to encrypt the source data. This parameter is valid only if you set the VaultType parameter to STANDARD or OTS_BACKUP. Valid values:
        # 
        # *   **HBR_PRIVATE**: The source data is encrypted by using the built-in encryption method of Hybrid Backup Recovery (HBR).
        # *   **KMS**: The source data is encrypted by using Key Management Service (KMS).
        self.encrypt_type = encrypt_type  # type: str
        # The customer master key (CMK) created in KMS or the alias of the key. This parameter is required only if you set the EncryptType parameter to KMS.
        self.kms_key_id = kms_key_id  # type: str
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        self.vault_name = vault_name  # type: str
        # The ID of the region where the backup vault resides.
        self.vault_region_id = vault_region_id  # type: str
        # The storage type of the backup vault. Valid value: **STANDARD**, which indicates standard storage.
        self.vault_storage_class = vault_storage_class  # type: str
        # The type of the backup vault. Valid value
        # 
        # *   **STANDARD**: standard backup vault
        # *   **OTS_BACKUP**: backup vault for Tablestore
        self.vault_type = vault_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVaultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class
        if self.vault_type is not None:
            result['VaultType'] = self.vault_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')
        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')
        return self


class CreateVaultResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None, vault_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the initialization task used to initialize the backup vault. You can call the DescribeTask operation to query the status of an initialization task.
        self.task_id = task_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVaultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class CreateVaultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVaultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVaultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupClientRequest(TeaModel):
    def __init__(self, client_id=None):
        # The ID of the backup client.
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class DeleteBackupClientResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: indicates that the request is successful.
        # *   false: indicates that the request fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupClientResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBackupClientResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBackupClientResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBackupClientResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBackupClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupClientResourceRequest(TeaModel):
    def __init__(self, client_ids=None):
        # The IDs of HBR clients. The value can be a JSON array that consists of up to 100 client IDs. Separate the IDs with commas (,).
        self.client_ids = client_ids  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupClientResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        return self


class DeleteBackupClientResourceShrinkRequest(TeaModel):
    def __init__(self, client_ids_shrink=None):
        # The IDs of HBR clients. The value can be a JSON array that consists of up to 100 client IDs. Separate the IDs with commas (,).
        self.client_ids_shrink = client_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupClientResourceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        return self


class DeleteBackupClientResourceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupClientResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBackupClientResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBackupClientResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBackupClientResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBackupClientResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupPlanRequest(TeaModel):
    def __init__(self, plan_id=None, require_no_running_jobs=None, source_type=None, vault_id=None):
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        self.require_no_running_jobs = require_no_running_jobs  # type: bool
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **UDM_ECS**: ECS instances
        # *   **OTS**: Tablestore instances
        self.source_type = source_type  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.require_no_running_jobs is not None:
            result['RequireNoRunningJobs'] = self.require_no_running_jobs
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequireNoRunningJobs') is not None:
            self.require_no_running_jobs = m.get('RequireNoRunningJobs')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBackupPlanResponseBody

    def validate(self):
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


class DeleteClientRequest(TeaModel):
    def __init__(self, client_id=None, resource_group_id=None, vault_id=None):
        self.client_id = client_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteClientResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClientResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClientResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClientResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClientResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHanaBackupPlanRequest(TeaModel):
    def __init__(self, cluster_id=None, plan_id=None, resource_group_id=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHanaBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteHanaBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHanaBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteHanaBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHanaBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHanaBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHanaInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, resource_group_id=None, sid=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The SID of the SAP HANA database. You must specify a valid SID. The SID must be three characters in length and start with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        self.sid = sid  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHanaInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteHanaInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHanaInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteHanaInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHanaInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHanaInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHanaInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyBindingRequest(TeaModel):
    def __init__(self, data_source_ids=None, policy_id=None, source_type=None):
        # The IDs of the data sources that you want to disassociate from the backup policy.
        self.data_source_ids = data_source_ids  # type: list[str]
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DeletePolicyBindingShrinkRequest(TeaModel):
    def __init__(self, data_source_ids_shrink=None, policy_id=None, source_type=None):
        # The IDs of the data sources that you want to disassociate from the backup policy.
        self.data_source_ids_shrink = data_source_ids_shrink  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyBindingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DeletePolicyBindingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyBindingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePolicyBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePolicyBindingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyBindingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePolicyBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyV2Request(TeaModel):
    def __init__(self, policy_id=None):
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeletePolicyV2ResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePolicyV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePolicyV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(self, client_id=None, force=None, instance_id=None, snapshot_id=None, source_type=None, token=None,
                 vault_id=None):
        # The ID of the backup client. If you delete a backup file for Elastic Compute Service (ECS) instances, you must set one of the **InstanceId** and ClientId parameters.
        self.client_id = client_id  # type: str
        # Specifies whether to forcibly delete the most recent backup file. Valid values:
        # 
        # *   true: The system forcibly deletes the last backup file.
        # *   false: The system does not forcibly delete the last backup file. Default value: false.
        self.force = force  # type: bool
        # The ID of the ECS instance. If you delete a backup file for Elastic Compute Service (ECS) instances, you must set one of the **ClientId** and InstanceId parameters.
        self.instance_id = instance_id  # type: str
        # The ID of the backup file.
        self.snapshot_id = snapshot_id  # type: str
        # The type of the backup source. Valid values:
        # 
        # *   **ECS_FILE**: indicates backup files for ECS instances.
        # *   **OSS**: indicates backup files for Object Storage Service (OSS) buckets.
        # *   **NAS**: indicates the backup files for Apsara File Storage NAS file systems.
        self.source_type = source_type  # type: str
        # The token.
        self.token = token  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.force is not None:
            result['Force'] = self.force
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.token is not None:
            result['Token'] = self.token
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: indicates that the request is successful.
        # *   false: indicates that the request fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSnapshotResponseBody

    def validate(self):
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


class DeleteVaultRequest(TeaModel):
    def __init__(self, resource_group_id=None, token=None, vault_id=None):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The token.
        self.token = token  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVaultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.token is not None:
            result['Token'] = self.token
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DeleteVaultResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request is successful.
        # *   false: The request failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVaultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteVaultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVaultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVaultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupClientsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key  # type: str
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupClientsRequestTag, self).to_map()
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


class DescribeBackupClientsRequest(TeaModel):
    def __init__(self, client_ids=None, client_type=None, cluster_id=None, cross_account_role_name=None,
                 cross_account_type=None, cross_account_user_id=None, instance_ids=None, page_number=None, page_size=None, tag=None):
        # The IDs of HBR clients.
        self.client_ids = client_ids  # type: list[str]
        # The type of the HBR client. Valid values:
        # 
        # *   **ECS_CLIENT**: HBR client for Elastic Compute Service (ECS) file backup
        # *   **CONTAINER_CLIENT**: HBR client for container backup
        self.client_type = client_type  # type: str
        # The ID of the cluster for the backup.
        self.cluster_id = cluster_id  # type: str
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The IDs of ECS instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The tags.
        self.tag = tag  # type: list[DescribeBackupClientsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeBackupClientsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeBackupClientsShrinkRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key  # type: str
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupClientsShrinkRequestTag, self).to_map()
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


class DescribeBackupClientsShrinkRequest(TeaModel):
    def __init__(self, client_ids_shrink=None, client_type=None, cluster_id=None, cross_account_role_name=None,
                 cross_account_type=None, cross_account_user_id=None, instance_ids_shrink=None, page_number=None, page_size=None,
                 tag=None):
        # The IDs of HBR clients.
        self.client_ids_shrink = client_ids_shrink  # type: str
        # The type of the HBR client. Valid values:
        # 
        # *   **ECS_CLIENT**: HBR client for Elastic Compute Service (ECS) file backup
        # *   **CONTAINER_CLIENT**: HBR client for container backup
        self.client_type = client_type  # type: str
        # The ID of the cluster for the backup.
        self.cluster_id = cluster_id  # type: str
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The IDs of ECS instances.
        self.instance_ids_shrink = instance_ids_shrink  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The tags.
        self.tag = tag  # type: list[DescribeBackupClientsShrinkRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupClientsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeBackupClientsShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeBackupClientsResponseBodyClientsSettings(TeaModel):
    def __init__(self, alert_on_partial_complete=None, data_network_type=None, data_proxy_setting=None,
                 max_cpu_core=None, max_memory=None, max_worker=None, proxy_host=None, proxy_password=None, proxy_port=None,
                 proxy_user=None, use_https=None):
        self.alert_on_partial_complete = alert_on_partial_complete  # type: bool
        # The type of the endpoint on the data plane. Valid values:
        # 
        # *   **PUBLIC**: Internet
        # *   **VPC**: virtual private cloud (VPC)
        # *   **CLASSIC**: classic network
        self.data_network_type = data_network_type  # type: str
        # The proxy configuration on the data plane. Valid values:
        # 
        # *   **DISABLE**: The proxy is not used.
        # *   \*\*USE_CONTROL_PROXY \*\* (default value): The configuration is the same as that on the control plane.
        # *   **CUSTOM**: The configuration is customized (HTTP).
        self.data_proxy_setting = data_proxy_setting  # type: str
        # The number of CPU cores used by a single backup job. The value 0 indicates that the number is unlimited.
        self.max_cpu_core = max_cpu_core  # type: str
        self.max_memory = max_memory  # type: long
        # The number of concurrent backup jobs. The value 0 indicates that the number is unlimited.
        self.max_worker = max_worker  # type: str
        # The custom host IP address of the proxy server on the data plane.
        self.proxy_host = proxy_host  # type: str
        # The custom password of the proxy server on the data plane.
        self.proxy_password = proxy_password  # type: str
        # The custom host port of the proxy server on the data plane.
        self.proxy_port = proxy_port  # type: int
        # The custom username of the proxy server on the data plane.
        self.proxy_user = proxy_user  # type: str
        # Indicates whether data on the data plane is transmitted over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupClientsResponseBodyClientsSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_on_partial_complete is not None:
            result['AlertOnPartialComplete'] = self.alert_on_partial_complete
        if self.data_network_type is not None:
            result['DataNetworkType'] = self.data_network_type
        if self.data_proxy_setting is not None:
            result['DataProxySetting'] = self.data_proxy_setting
        if self.max_cpu_core is not None:
            result['MaxCpuCore'] = self.max_cpu_core
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.max_worker is not None:
            result['MaxWorker'] = self.max_worker
        if self.proxy_host is not None:
            result['ProxyHost'] = self.proxy_host
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_port is not None:
            result['ProxyPort'] = self.proxy_port
        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertOnPartialComplete') is not None:
            self.alert_on_partial_complete = m.get('AlertOnPartialComplete')
        if m.get('DataNetworkType') is not None:
            self.data_network_type = m.get('DataNetworkType')
        if m.get('DataProxySetting') is not None:
            self.data_proxy_setting = m.get('DataProxySetting')
        if m.get('MaxCpuCore') is not None:
            self.max_cpu_core = m.get('MaxCpuCore')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MaxWorker') is not None:
            self.max_worker = m.get('MaxWorker')
        if m.get('ProxyHost') is not None:
            self.proxy_host = m.get('ProxyHost')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')
        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        return self


class DescribeBackupClientsResponseBodyClientsTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key  # type: str
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupClientsResponseBodyClientsTags, self).to_map()
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


class DescribeBackupClientsResponseBodyClients(TeaModel):
    def __init__(self, appliance=None, arch_type=None, backup_status=None, client_id=None, client_type=None,
                 client_version=None, created_time=None, hostname=None, instance_id=None, instance_name=None,
                 last_heart_beat_time=None, max_client_version=None, os_type=None, private_ip_v4=None, settings=None, status=None,
                 tags=None, updated_time=None, zone_id=None):
        # Indicates whether the HBR client is installed on an all-in-one PC that integrates hardware and monitoring program. Valid values:
        # 
        # *   true: The HBR client is installed on an all-in-one PC that integrates hardware and monitoring program.
        # *   false: The HBR client is not installed on an all-in-one PC that integrates hardware and monitoring program.
        self.appliance = appliance  # type: bool
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the system architecture where the HBR client resides. Valid values:
        # 
        # *   **amd64**\
        # *   **386**\
        self.arch_type = arch_type  # type: str
        # The protection status of the HBR client. Valid values:
        # 
        # *   **UNPROTECTED**: The HBR client is not protected.
        # *   **PROTECTED**: The HBR client is protected.
        self.backup_status = backup_status  # type: str
        # The ID of the HBR client.
        self.client_id = client_id  # type: str
        # The type of the HBR client. Valid value: **ECS_CLIENT**, which indicates an HBR client for ECS file backup.
        self.client_type = client_type  # type: str
        # The version number of the HBR client.
        self.client_version = client_version  # type: str
        # The time when the HBR client was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The hostname of the HBR client.
        self.hostname = hostname  # type: str
        # The ID of the instance.
        # 
        # *   If the HBR client is used to back up ECS files, this parameter indicates the ID of an ECS instance.
        # *   If the HBR client is used to back up on-premises files, this parameter indicates the hardware fingerprint that is generated based on the system information.
        self.instance_id = instance_id  # type: str
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the name of the ECS instance.
        self.instance_name = instance_name  # type: str
        # The last heartbeat time of the HBR client. The value is a UNIX timestamp. Unit: seconds.
        self.last_heart_beat_time = last_heart_beat_time  # type: long
        # The latest version number of the HBR client.
        self.max_client_version = max_client_version  # type: str
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the operating system type of the HBR client. Valid values:
        # 
        # *   **windows**\
        # *   **linux**\
        self.os_type = os_type  # type: str
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the internal IP address of the ECS instance.
        self.private_ip_v4 = private_ip_v4  # type: str
        # The configuration information of the HBR client.
        self.settings = settings  # type: DescribeBackupClientsResponseBodyClientsSettings
        # The status of the HBR client. Valid values:
        # 
        # *   **REGISTERED**: The HBR client is registered.
        # *   **ACTIVATED**: The HBR client is enabled.
        # *   **DEACTIVATED**: The HBR client fails to be enabled.
        # *   **INSTALLING**: The HBR client is being installed.
        # *   **INSTALL_FAILED**: The HBR client fails to be installed.
        # *   **NOT_INSTALLED**: The HBR client is not installed.
        # *   **UPGRADING**: The HBR client is being upgraded.
        # *   **UPGRADE_FAILED**: The HBR client fails to be upgraded.
        # *   **UNINSTALLING**: The HBR client is being uninstalled.
        # *   **UNINSTALL_FAILED**: The HBR client fails to be uninstalled.
        # *   **STOPPED**: The HBR client is out of service.
        # *   **UNKNOWN**: The HBR client is disconnected.
        self.status = status  # type: str
        # The tag information.
        self.tags = tags  # type: list[DescribeBackupClientsResponseBodyClientsTags]
        # The time when the HBR client was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the zone of the HBR client.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.settings:
            self.settings.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupClientsResponseBodyClients, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appliance is not None:
            result['Appliance'] = self.appliance
        if self.arch_type is not None:
            result['ArchType'] = self.arch_type
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.max_client_version is not None:
            result['MaxClientVersion'] = self.max_client_version
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.private_ip_v4 is not None:
            result['PrivateIpV4'] = self.private_ip_v4
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Appliance') is not None:
            self.appliance = m.get('Appliance')
        if m.get('ArchType') is not None:
            self.arch_type = m.get('ArchType')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('MaxClientVersion') is not None:
            self.max_client_version = m.get('MaxClientVersion')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PrivateIpV4') is not None:
            self.private_ip_v4 = m.get('PrivateIpV4')
        if m.get('Settings') is not None:
            temp_model = DescribeBackupClientsResponseBodyClientsSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeBackupClientsResponseBodyClientsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeBackupClientsResponseBody(TeaModel):
    def __init__(self, clients=None, code=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        # The HBR clients.
        self.clients = clients  # type: list[DescribeBackupClientsResponseBodyClients]
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned HBR clients that meet the specified conditions.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = DescribeBackupClientsResponseBodyClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupClientsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupClientsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupJobs2RequestFilters(TeaModel):
    def __init__(self, key=None, operator=None, values=None):
        # The key in the filter. Valid values:
        # 
        # *   **RegionId**: the ID of a region
        # *   **PlanId**: the ID of a backup plan
        # *   **JobId**: the ID of a backup job
        # *   **VaultId**: the ID of a backup vault
        # *   **InstanceId**: the ID of an ECS instance
        # *   **Bucket**: the name of an OSS bucket
        # *   **FileSystemId**: the ID of a file system
        # *   **Status**: the status of a backup job
        # *   **CreatedTime**: the start time of a backup job
        # *   **CompleteTime**: the end time of a backup job
        # *   **InstanceName**: the name of a Tablestore instance
        self.key = key  # type: str
        # The matching method. Default value: IN. This parameter specifies the operator that you want to use to match a key and a value in the filter. Valid values:
        # 
        # *   **EQUAL**: equal to
        # *   **NOT_EQUAL**: not equal to
        # *   **GREATER_THAN**: greater than
        # *   **GREATER_THAN_OR_EQUAL**: greater than or equal to
        # *   **LESS_THAN**: less than
        # *   **LESS_THAN_OR_EQUAL**: less than or equal to
        # *   **BETWEEN**: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        # *   **IN**: specifies an array as a collection. The results must fall within the collection.
        # 
        # > If you specify the **CompleteTime** parameter as a key to query backup jobs, you cannot use the IN operator to perform a match.
        self.operator = operator  # type: str
        # The variable values of the filter.
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupJobs2RequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeBackupJobs2Request(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None, sort_direction=None, source_type=None):
        # The keys in the filter.
        self.filters = filters  # type: list[DescribeBackupJobs2RequestFilters]
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **ASCEND**: sorts the results in ascending order
        # *   **DESCEND** (default value): sorts the results in descending order
        self.sort_direction = sort_direction  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        # *   **UDM_ECS_DISK**: ECS disks
        self.source_type = source_type  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupJobs2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeBackupJobs2RequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList(TeaModel):
    def __init__(self, disk_native_snapshot_id=None):
        self.disk_native_snapshot_id = disk_native_snapshot_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_native_snapshot_id is not None:
            result['DiskNativeSnapshotId'] = self.disk_native_snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskNativeSnapshotId') is not None:
            self.disk_native_snapshot_id = m.get('DiskNativeSnapshotId')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail(TeaModel):
    def __init__(self, destination_native_snapshot_error_message=None, destination_native_snapshot_id=None,
                 destination_native_snapshot_progress=None, destination_native_snapshot_status=None, destination_retention=None,
                 destination_snapshot_id=None, disk_native_snapshot_id_list=None, do_copy=None, native_snapshot_id=None):
        # The information about the remote replication failure.
        self.destination_native_snapshot_error_message = destination_native_snapshot_error_message  # type: str
        # The ID of the remote replication snapshot.
        self.destination_native_snapshot_id = destination_native_snapshot_id  # type: str
        # The progress of the remote replication.
        self.destination_native_snapshot_progress = destination_native_snapshot_progress  # type: int
        # The state of the remote replication.
        self.destination_native_snapshot_status = destination_native_snapshot_status  # type: str
        # The retention period of the remote replication backup.
        self.destination_retention = destination_retention  # type: long
        # The ID of the remote replication backup.
        self.destination_snapshot_id = destination_snapshot_id  # type: str
        # The mapping between snapshots and disks.
        self.disk_native_snapshot_id_list = disk_native_snapshot_id_list  # type: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList
        # Indicates whether remote replication is enabled.
        self.do_copy = do_copy  # type: bool
        # The ID of the backup snapshot.
        self.native_snapshot_id = native_snapshot_id  # type: str

    def validate(self):
        if self.disk_native_snapshot_id_list:
            self.disk_native_snapshot_id_list.validate()

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_native_snapshot_error_message is not None:
            result['DestinationNativeSnapshotErrorMessage'] = self.destination_native_snapshot_error_message
        if self.destination_native_snapshot_id is not None:
            result['DestinationNativeSnapshotId'] = self.destination_native_snapshot_id
        if self.destination_native_snapshot_progress is not None:
            result['DestinationNativeSnapshotProgress'] = self.destination_native_snapshot_progress
        if self.destination_native_snapshot_status is not None:
            result['DestinationNativeSnapshotStatus'] = self.destination_native_snapshot_status
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.destination_snapshot_id is not None:
            result['DestinationSnapshotId'] = self.destination_snapshot_id
        if self.disk_native_snapshot_id_list is not None:
            result['DiskNativeSnapshotIdList'] = self.disk_native_snapshot_id_list.to_map()
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.native_snapshot_id is not None:
            result['NativeSnapshotId'] = self.native_snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationNativeSnapshotErrorMessage') is not None:
            self.destination_native_snapshot_error_message = m.get('DestinationNativeSnapshotErrorMessage')
        if m.get('DestinationNativeSnapshotId') is not None:
            self.destination_native_snapshot_id = m.get('DestinationNativeSnapshotId')
        if m.get('DestinationNativeSnapshotProgress') is not None:
            self.destination_native_snapshot_progress = m.get('DestinationNativeSnapshotProgress')
        if m.get('DestinationNativeSnapshotStatus') is not None:
            self.destination_native_snapshot_status = m.get('DestinationNativeSnapshotStatus')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('DestinationSnapshotId') is not None:
            self.destination_snapshot_id = m.get('DestinationSnapshotId')
        if m.get('DiskNativeSnapshotIdList') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList()
            self.disk_native_snapshot_id_list = temp_model.from_map(m['DiskNativeSnapshotIdList'])
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('NativeSnapshotId') is not None:
            self.native_snapshot_id = m.get('NativeSnapshotId')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail(TeaModel):
    def __init__(self, table_names=None):
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names  # type: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames

    def validate(self):
        if self.table_names:
            self.table_names.validate()

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_names is not None:
            result['TableNames'] = self.table_names.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableNames') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames()
            self.table_names = temp_model.from_map(m['TableNames'])
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths(TeaModel):
    def __init__(self, path=None):
        self.path = path  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobsBackupJob(TeaModel):
    def __init__(self, actual_bytes=None, actual_files=None, actual_items=None, backup_type=None, bucket=None,
                 bytes_done=None, bytes_total=None, change_list_path=None, client_id=None, complete_time=None,
                 create_time=None, created_time=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, dest_data_source_detail=None, dest_data_source_id=None, dest_source_type=None, detail=None,
                 error_message=None, exclude=None, file_system_id=None, files_done=None, files_total=None, identifier=None,
                 include=None, instance_id=None, instance_name=None, items_done=None, items_total=None, job_id=None,
                 job_name=None, options=None, ots_detail=None, paths=None, plan_id=None, prefix=None, progress=None,
                 source_type=None, speed=None, speed_limit=None, start_time=None, status=None, table_name=None,
                 updated_time=None, vault_id=None):
        # The actual amount of data that is backed up after the system removes duplicate files. Unit: bytes.
        self.actual_bytes = actual_bytes  # type: long
        # The number of files that are actually processed.
        self.actual_files = actual_files  # type: long
        # The actual number of objects that are backed up by the backup job. This parameter is returned only if the value of **SourceType** is **ECS_FILE**.
        self.actual_items = actual_items  # type: long
        # The backup type. Only **COMPLETE** may be returned, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # The name of the OSS bucket that is backed up. This parameter is returned only if the value of **SourceType** is **OSS**.
        self.bucket = bucket  # type: str
        # The actual amount of data that is generated by incremental backups. Unit: bytes.
        self.bytes_done = bytes_done  # type: long
        # The total amount of data that is backed up from the data source. Unit: bytes.
        self.bytes_total = bytes_total  # type: long
        # The configurations of the incremental file synchronization. This parameter is returned only for data synchronization.
        self.change_list_path = change_list_path  # type: str
        # The ID of the backup client. This parameter is returned only if the value of **SourceType** is **ECS_FILE**.
        self.client_id = client_id  # type: str
        # The time when the backup job was complete. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.complete_time = complete_time  # type: long
        # The time when the file system was created. This parameter is returned only if the value of **SourceType** is **NAS**. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time  # type: long
        # The time when the backup job was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_time = created_time  # type: long
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # The backup type. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The data source details at the destination. This parameter is returned only for data synchronization.
        self.dest_data_source_detail = dest_data_source_detail  # type: str
        # The data source ID at the destination. This parameter is returned only for data synchronization.
        self.dest_data_source_id = dest_data_source_id  # type: str
        # The data source type at the destination. This parameter is returned only for data synchronization.
        self.dest_source_type = dest_source_type  # type: str
        # The details of the ECS instance backup job.
        self.detail = detail  # type: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail
        # The error message that is returned for the backup job.
        self.error_message = error_message  # type: str
        # The paths to the files that are excluded from the backup job. This parameter is returned only if the value of **SourceType** is **ECS_FILE**. The value can be up to 255 characters in length.
        self.exclude = exclude  # type: str
        # The ID of the NAS file system. This parameter is returned only if the value of **SourceType** is **NAS**.
        self.file_system_id = file_system_id  # type: str
        # The number of files that have been processed.
        self.files_done = files_done  # type: long
        # The total number of files to be processed.
        self.files_total = files_total  # type: long
        # The identifier of the cluster that is backed up in the container backup job. This parameter is returned only if the value of SourceType is CONTAINER. If the cluster is a Container Service for Kubernetes (ACK) cluster, the value of this parameter is the ACK cluster ID.
        self.identifier = identifier  # type: str
        # The paths to the files that are included in the backup job.
        self.include = include  # type: str
        # The ID of the ECS instance. This parameter is returned only if the value of **SourceType** is **NAS**.
        self.instance_id = instance_id  # type: str
        # The name of the Tablestore instance.
        self.instance_name = instance_name  # type: str
        # The number of objects that are backed up. This parameter is returned only if the value of **SourceType** is **ECS_FILE**.
        self.items_done = items_done  # type: long
        # The total number of objects in the data source. This parameter is returned only if the value of **SourceType** is **ECS_FILE**.
        self.items_total = items_total  # type: long
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The name of the backup job.
        self.job_name = job_name  # type: str
        # Indicates whether Windows Volume Shadow Copy Service (VSS) is used to define a source path. This parameter is returned only if the value of **SourceType** is **ECS_FILE**.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   A value of `["UseVSS":true]` indicates that the consistency between the source data and backup data is ensured while data changes occur in the source data.
        # *   If VSS is used, multiple directories cannot be backed up at a time.
        self.options = options  # type: str
        # The details of the Tablestore instance.
        self.ots_detail = ots_detail  # type: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail
        # The source paths.
        self.paths = paths  # type: DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The prefix of objects that are backed up. This parameter is returned only if the value of **SourceType** is **OSS**.
        self.prefix = prefix  # type: str
        # The backup progress. Valid values: 0 to 10000. For example, a value of 10000 indicates that the progress is 100%.
        self.progress = progress  # type: int
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS file.
        # *   **OSS**: OSS bucket.
        # *   **NAS**: NAS file system.
        self.source_type = source_type  # type: str
        # The average speed at which data is backed up. Unit: KB/s.
        self.speed = speed  # type: long
        # The throttling rules. This parameter is returned only if the value of **SourceType** is **ECS_FILE**. Format: `{start}:{end}:{bandwidth}`. Multiple throttling rules are separated by vertical bars (`|`). The time ranges of the throttling rules cannot overlap.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit  # type: str
        # The time when the backup job started. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time  # type: long
        # The state of the backup job. Valid values:
        # 
        # *   **COMPLETE**\
        # *   **PARTIAL_COMPLETE**\
        # *   **FAILED**\
        self.status = status  # type: str
        # The name of the table in the Tablestore instance.
        self.table_name = table_name  # type: str
        # The time when the backup job was last updated. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.updated_time = updated_time  # type: long
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.ots_detail:
            self.ots_detail.validate()
        if self.paths:
            self.paths.validate()

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBodyBackupJobsBackupJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.actual_files is not None:
            result['ActualFiles'] = self.actual_files
        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.files_done is not None:
            result['FilesDone'] = self.files_done
        if self.files_total is not None:
            result['FilesTotal'] = self.files_total
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.items_done is not None:
            result['ItemsDone'] = self.items_done
        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.paths is not None:
            result['Paths'] = self.paths.to_map()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('ActualFiles') is not None:
            self.actual_files = m.get('ActualFiles')
        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FilesDone') is not None:
            self.files_done = m.get('FilesDone')
        if m.get('FilesTotal') is not None:
            self.files_total = m.get('FilesTotal')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')
        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Paths') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths()
            self.paths = temp_model.from_map(m['Paths'])
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeBackupJobs2ResponseBodyBackupJobs(TeaModel):
    def __init__(self, backup_job=None):
        self.backup_job = backup_job  # type: list[DescribeBackupJobs2ResponseBodyBackupJobsBackupJob]

    def validate(self):
        if self.backup_job:
            for k in self.backup_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBodyBackupJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupJob'] = []
        if self.backup_job is not None:
            for k in self.backup_job:
                result['BackupJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup_job = []
        if m.get('BackupJob') is not None:
            for k in m.get('BackupJob'):
                temp_model = DescribeBackupJobs2ResponseBodyBackupJobsBackupJob()
                self.backup_job.append(temp_model.from_map(k))
        return self


class DescribeBackupJobs2ResponseBody(TeaModel):
    def __init__(self, backup_jobs=None, code=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        # The backup jobs that meet the specified conditions.
        self.backup_jobs = backup_jobs  # type: DescribeBackupJobs2ResponseBodyBackupJobs
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned backup jobs that meet the specified conditions.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.backup_jobs:
            self.backup_jobs.validate()

    def to_map(self):
        _map = super(DescribeBackupJobs2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_jobs is not None:
            result['BackupJobs'] = self.backup_jobs.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupJobs') is not None:
            temp_model = DescribeBackupJobs2ResponseBodyBackupJobs()
            self.backup_jobs = temp_model.from_map(m['BackupJobs'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupJobs2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupJobs2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupJobs2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupJobs2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlansRequestFilters(TeaModel):
    def __init__(self, key=None, values=None):
        # The keys in the filter. Valid values:
        # 
        # *   **regionId**: the ID of a region
        # *   **planId**: the ID of a backup plan
        # *   **sourceType**: the type of a data source
        # *   **vaultId**: the ID of a backup vault
        # *   **instanceName**: the name of an instance
        # *   **instanceId**: the ID of an instance
        # *   **planName**: the name of a backup plan
        self.key = key  # type: str
        # The values that you want to match in the filter.
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeBackupPlansRequest(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None, source_type=None):
        # The filter.
        self.filters = filters  # type: list[DescribeBackupPlansRequestFilters]
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeBackupPlansRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail(TeaModel):
    def __init__(self, table_names=None):
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names  # type: DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames

    def validate(self):
        if self.table_names:
            self.table_names.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_names is not None:
            result['TableNames'] = self.table_names.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableNames') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames()
            self.table_names = temp_model.from_map(m['TableNames'])
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths(TeaModel):
    def __init__(self, path=None):
        self.path = path  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource(TeaModel):
    def __init__(self, extra=None, resource_id=None, source_type=None):
        # Additional information about the data source.
        self.extra = extra  # type: str
        # The ID of the data source.
        self.resource_id = resource_id  # type: str
        # The type of the data source. Valid value: **UDM_DISK**.
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource  # type: list[DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource]

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule(TeaModel):
    def __init__(self, backup_type=None, destination_region_id=None, destination_retention=None, disabled=None,
                 do_copy=None, retention=None, rule_id=None, rule_name=None, schedule=None):
        # The backup type. **COMPLETE** indicates full backup.
        self.backup_type = backup_type  # type: str
        # The ID of the region in which the remote backup vault resides.
        self.destination_region_id = destination_region_id  # type: str
        # The retention period of the backup data in remote backup mode. Unit: days.
        self.destination_retention = destination_retention  # type: long
        # Indicates whether the policy is disabled.
        self.disabled = disabled  # type: bool
        # Indicates whether the snapshot data is backed up to the backup vault.
        self.do_copy = do_copy  # type: bool
        # The retention period of the backup data. Unit: days.
        self.retention = retention  # type: long
        # The ID of the policy.
        self.rule_id = rule_id  # type: str
        # The name of the policy.
        self.rule_name = rule_name  # type: str
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified by `{startTime}` and the subsequent backup jobs at an interval that is specified by `{interval}`. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   `startTime`: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   `interval`: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule  # type: list[DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule]

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo(TeaModel):
    def __init__(self, keep_after_trial_expiration=None, trial_expire_time=None, trial_start_time=None,
                 trial_vault_release_time=None):
        # Indicates whether you are billed based on the pay-as-you-go method after the free trial ends.
        self.keep_after_trial_expiration = keep_after_trial_expiration  # type: bool
        # The expiration time of the free trial.
        self.trial_expire_time = trial_expire_time  # type: long
        # The start time of the free trial.
        self.trial_start_time = trial_start_time  # type: long
        # The time when the free-trial backup vault was released.
        self.trial_vault_release_time = trial_vault_release_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_after_trial_expiration is not None:
            result['KeepAfterTrialExpiration'] = self.keep_after_trial_expiration
        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time
        if self.trial_start_time is not None:
            result['TrialStartTime'] = self.trial_start_time
        if self.trial_vault_release_time is not None:
            result['TrialVaultReleaseTime'] = self.trial_vault_release_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeepAfterTrialExpiration') is not None:
            self.keep_after_trial_expiration = m.get('KeepAfterTrialExpiration')
        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')
        if m.get('TrialStartTime') is not None:
            self.trial_start_time = m.get('TrialStartTime')
        if m.get('TrialVaultReleaseTime') is not None:
            self.trial_vault_release_time = m.get('TrialVaultReleaseTime')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlan(TeaModel):
    def __init__(self, backup_source_group_id=None, backup_type=None, bucket=None, change_list_path=None,
                 client_id=None, cluster_id=None, create_time=None, created_time=None, cross_account_role_name=None,
                 cross_account_type=None, cross_account_user_id=None, data_source_id=None, dest_data_source_detail=None,
                 dest_data_source_id=None, dest_source_type=None, detail=None, disabled=None, exclude=None, file_system_id=None,
                 include=None, instance_group_id=None, instance_id=None, instance_name=None, keep_latest_snapshots=None,
                 latest_execute_job_id=None, options=None, ots_detail=None, paths=None, plan_id=None, plan_name=None, prefix=None,
                 resources=None, retention=None, rules=None, schedule=None, source_type=None, speed_limit=None,
                 trial_info=None, updated_time=None, vault_id=None):
        # The ID of the data source group.
        self.backup_source_group_id = backup_source_group_id  # type: str
        # The backup type. **COMPLETE** indicates full backup.
        self.backup_type = backup_type  # type: str
        # This parameter is valid only when **SourceType** is set to **OSS**. This parameter indicates the name of the OSS bucket.
        self.bucket = bucket  # type: str
        # The configurations of the incremental file synchronization. This parameter is required only for data synchronization.
        self.change_list_path = change_list_path  # type: str
        # The ID of the backup client.
        self.client_id = client_id  # type: str
        # The ID of the client group.
        self.cluster_id = cluster_id  # type: str
        # This parameter is valid only when **SourceType** is set to **NAS**. This parameter indicates the time when the file system was created. This value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time  # type: long
        # The time when the backup plan was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Indicates whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT
        # *   CROSS_ACCOUNT
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The ID of the data source.
        self.data_source_id = data_source_id  # type: str
        # The data source details at the destination. This parameter is required only for data synchronization.
        self.dest_data_source_detail = dest_data_source_detail  # type: str
        # The data source ID at the destination. This parameter is required only for data synchronization.
        self.dest_data_source_id = dest_data_source_id  # type: str
        # The data source type at the destination. This parameter is required only for data synchronization.
        self.dest_source_type = dest_source_type  # type: str
        # The details about ECS instance backup.
        self.detail = detail  # type: str
        # Indicates whether the backup plan is disabled. Valid values:
        # 
        # *   true: The backup plan is disabled.
        # *   false: The backup plan is enabled.
        self.disabled = disabled  # type: bool
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the backup job.
        self.exclude = exclude  # type: str
        # This parameter is valid only when **SourceType** is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id  # type: str
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the paths to the files that are backed up.
        self.include = include  # type: str
        # The ID of the instance group.
        self.instance_group_id = instance_group_id  # type: str
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the Tablestore instance.
        self.instance_name = instance_name  # type: str
        # Indicates whether the feature of keeping at least one backup version is enabled. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # The latest execution job id of plan.
        self.latest_execute_job_id = latest_execute_job_id  # type: str
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates whether VSS is used to define a source path.
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail  # type: DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail
        # The source paths. This parameter is valid only when **SourceType** is set to **ECS_FILE**.
        self.paths = paths  # type: DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The name of the backup plan.
        self.plan_name = plan_name  # type: str
        # This parameter is valid only when **SourceType** is set to **OSS**. This parameter indicates the prefix of the objects that are backed up.
        self.prefix = prefix  # type: str
        # The backup resources. This parameter is valid only for disk backup.
        self.resources = resources  # type: DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources
        # The retention period of the backup data. Unit: days.
        self.retention = retention  # type: long
        # The backup policies. This parameter is valid only for disk backup.
        self.rules = rules  # type: DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified by `{startTime}` and the subsequent backup jobs at an interval that is specified by `{interval}`. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the throttling rules. Format: `{start}|{end}|{bandwidth}`. Multiple throttling rules are separated with vertical bars (`|`). A time range cannot overlap with another one.
        # 
        # *   start: the start hour.
        # *   end: the end hour.
        # *   bandwidth: the bandwidth. Unit: KB.
        self.speed_limit = speed_limit  # type: str
        # The free trial information.
        self.trial_info = trial_info  # type: DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo
        # The time when the backup plan was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.paths:
            self.paths.validate()
        if self.resources:
            self.resources.validate()
        if self.rules:
            self.rules.validate()
        if self.trial_info:
            self.trial_info.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_source_group_id is not None:
            result['BackupSourceGroupId'] = self.backup_source_group_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail
        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id
        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.latest_execute_job_id is not None:
            result['LatestExecuteJobId'] = self.latest_execute_job_id
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.paths is not None:
            result['Paths'] = self.paths.to_map()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.trial_info is not None:
            result['TrialInfo'] = self.trial_info.to_map()
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupSourceGroupId') is not None:
            self.backup_source_group_id = m.get('BackupSourceGroupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')
        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')
        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('LatestExecuteJobId') is not None:
            self.latest_execute_job_id = m.get('LatestExecuteJobId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Paths') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths()
            self.paths = temp_model.from_map(m['Paths'])
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Resources') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('Rules') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('TrialInfo') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo()
            self.trial_info = temp_model.from_map(m['TrialInfo'])
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
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
    def __init__(self, backup_plans=None, code=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        # The queried backup plans.
        self.backup_plans = backup_plans  # type: DescribeBackupPlansResponseBodyBackupPlans
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned backup plans that meet the specified conditions.
        self.total_count = total_count  # type: long

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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPlans') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlans()
            self.backup_plans = temp_model.from_map(m['BackupPlans'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupPlansResponseBody

    def validate(self):
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


class DescribeClientsRequest(TeaModel):
    def __init__(self, client_id=None, client_type=None, cluster_id=None, page_number=None, page_size=None,
                 resource_group_id=None, source_type=None, vault_id=None):
        # The ID of the backup client.
        self.client_id = client_id  # type: str
        # The type of the backup client. Valid value:**ECS_AGENT**, which indicates an SAP HANA backup client.
        self.client_type = client_type  # type: str
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The type of the data source. Valid value:**HANA**, which indicates SAP HANA backup.
        self.source_type = source_type  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeClientsResponseBodyClientsClient(TeaModel):
    def __init__(self, alert_setting=None, client_id=None, client_name=None, client_type=None, client_version=None,
                 cluster_id=None, created_time=None, instance_id=None, instance_name=None, max_version=None, network_type=None,
                 status=None, status_message=None, updated_time=None, use_https=None, vault_id=None):
        # The alert settings. Valid value: INHERITED, which indicates that the backup client sends alert notifications in the same way as the backup vault.
        self.alert_setting = alert_setting  # type: str
        # The ID of the backup client.
        self.client_id = client_id  # type: str
        # The name of the backup client.
        self.client_name = client_name  # type: str
        # The type of the backup client. Valid value:**ECS_AGENT**, which indicates an SAP HANA backup client.
        self.client_type = client_type  # type: str
        # The version number of the backup client.
        self.client_version = client_version  # type: str
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The time when the backup client was created.
        self.created_time = created_time  # type: long
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the ECS instance.
        self.instance_name = instance_name  # type: str
        # The maximum version number of the backup client.
        self.max_version = max_version  # type: str
        # The network type. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: virtual private cloud (VPC)
        self.network_type = network_type  # type: str
        # The status of the backup client. Valid values:
        # 
        # *   **REGISTERED**: The backup client is registered.
        # *   **ACTIVATED**: The backup client is enabled.
        # *   **DEACTIVATED**: The backup client fails to be enabled.
        # *   **INSTALLING**: The backup client is being installed.
        # *   **INSTALL_FAILED**: The backup client fails to be installed.
        # *   **NOT_INSTALLED**: The backup client is not installed.
        # *   **UPGRADING**: The backup client is being upgraded.
        # *   **UPGRADE_FAILED**: The backup client fails to be upgraded.
        # *   **UNINSTALLING**: The backup client is being uninstalled.
        # *   **UNINSTALL_FAILED**: The backup client fails to be uninstalled.
        # *   **STOPPED**: The backup client is out of service.
        # *   **UNKNOWN**: The backup client is disconnected.
        self.status = status  # type: str
        # The status information.
        self.status_message = status_message  # type: str
        # The time when the backup client was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long
        # Indicates whether data is transmitted over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientsResponseBodyClientsClient, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeClientsResponseBodyClients(TeaModel):
    def __init__(self, client=None):
        self.client = client  # type: list[DescribeClientsResponseBodyClientsClient]

    def validate(self):
        if self.client:
            for k in self.client:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClientsResponseBodyClients, self).to_map()
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
                temp_model = DescribeClientsResponseBodyClientsClient()
                self.client.append(temp_model.from_map(k))
        return self


class DescribeClientsResponseBody(TeaModel):
    def __init__(self, clients=None, code=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        # The backup clients.
        self.clients = clients  # type: DescribeClientsResponseBodyClients
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.clients:
            self.clients.validate()

    def to_map(self):
        _map = super(DescribeClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clients is not None:
            result['Clients'] = self.clients.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clients') is not None:
            temp_model = DescribeClientsResponseBodyClients()
            self.clients = temp_model.from_map(m['Clients'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClientsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClientsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, identifier=None, page_number=None, page_size=None):
        # The ID of the cluster.
        self.cluster_id = cluster_id  # type: str
        # The identifier of container cluster.
        self.identifier = identifier  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeContainerClusterResponseBodyClusters(TeaModel):
    def __init__(self, agent_status=None, cluster_id=None, cluster_type=None, description=None, identifier=None,
                 name=None, network_type=None, token=None):
        # The status of the client. Valid values:
        # 
        # *   **MISS**: The client is disconnected.
        # *   **UNKNOWN**: The client is in an unknown state.
        # *   **READY**: The client is ready.
        self.agent_status = agent_status  # type: str
        # The ID of the cluster.
        self.cluster_id = cluster_id  # type: str
        # The type of the cluster. Valid value: ACK, which indicates ACK clusters.
        self.cluster_type = cluster_type  # type: str
        # The description.
        self.description = description  # type: str
        # The identifier of the cluster.
        self.identifier = identifier  # type: str
        # The name of the instance.
        self.name = name  # type: str
        # The network type of the cluster. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: virtual private cloud (VPC)
        self.network_type = network_type  # type: str
        # The token that is used to register the Hybrid Backup Recovery (HBR) client in the cluster.
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerClusterResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.description is not None:
            result['Description'] = self.description
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.name is not None:
            result['Name'] = self.name
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeContainerClusterResponseBody(TeaModel):
    def __init__(self, clusters=None, code=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        # The information of clusters.
        self.clusters = clusters  # type: list[DescribeContainerClusterResponseBodyClusters]
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeContainerClusterResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContainerClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeContainerClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCrossAccountsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCrossAccountsRequest, self).to_map()
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


class DescribeCrossAccountsResponseBodyCrossAccountsCrossAccount(TeaModel):
    def __init__(self, alias=None, created_time=None, cross_account_role_name=None, cross_account_user_id=None,
                 id=None, owner_id=None, updated_time=None):
        self.alias = alias  # type: str
        self.created_time = created_time  # type: long
        self.cross_account_role_name = cross_account_role_name  # type: str
        self.cross_account_user_id = cross_account_user_id  # type: long
        self.id = id  # type: long
        self.owner_id = owner_id  # type: long
        self.updated_time = updated_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCrossAccountsResponseBodyCrossAccountsCrossAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeCrossAccountsResponseBodyCrossAccounts(TeaModel):
    def __init__(self, cross_account=None):
        self.cross_account = cross_account  # type: list[DescribeCrossAccountsResponseBodyCrossAccountsCrossAccount]

    def validate(self):
        if self.cross_account:
            for k in self.cross_account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCrossAccountsResponseBodyCrossAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CrossAccount'] = []
        if self.cross_account is not None:
            for k in self.cross_account:
                result['CrossAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cross_account = []
        if m.get('CrossAccount') is not None:
            for k in m.get('CrossAccount'):
                temp_model = DescribeCrossAccountsResponseBodyCrossAccountsCrossAccount()
                self.cross_account.append(temp_model.from_map(k))
        return self


class DescribeCrossAccountsResponseBody(TeaModel):
    def __init__(self, code=None, cross_accounts=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.code = code  # type: str
        self.cross_accounts = cross_accounts  # type: DescribeCrossAccountsResponseBodyCrossAccounts
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.cross_accounts:
            self.cross_accounts.validate()

    def to_map(self):
        _map = super(DescribeCrossAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cross_accounts is not None:
            result['CrossAccounts'] = self.cross_accounts.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CrossAccounts') is not None:
            temp_model = DescribeCrossAccountsResponseBodyCrossAccounts()
            self.cross_accounts = temp_model.from_map(m['CrossAccounts'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCrossAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCrossAccountsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCrossAccountsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCrossAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaBackupPlansRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, page_number=None, page_size=None,
                 resource_group_id=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaBackupPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan(TeaModel):
    def __init__(self, backup_prefix=None, backup_type=None, cluster_id=None, database_name=None, disabled=None,
                 plan_id=None, plan_name=None, schedule=None, vault_id=None):
        # The backup prefix.
        self.backup_prefix = backup_prefix  # type: str
        # The backup type. Valid values:
        # 
        # *   COMPLETE: full backup
        # *   INCREMENTAL: incremental backup
        # *   DIFFERENTIAL: differential backup
        self.backup_type = backup_type  # type: str
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # Indicates whether the backup plan is disabled. Valid values:
        # 
        # *   true: The backup plan is disabled.
        # *   false: The backup plan is enabled.
        self.disabled = disabled  # type: bool
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The name of the backup plan.
        self.plan_name = plan_name  # type: str
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaBackupPlansResponseBodyHanaBackupPlans(TeaModel):
    def __init__(self, hana_backup_plan=None):
        self.hana_backup_plan = hana_backup_plan  # type: list[DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan]

    def validate(self):
        if self.hana_backup_plan:
            for k in self.hana_backup_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHanaBackupPlansResponseBodyHanaBackupPlans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HanaBackupPlan'] = []
        if self.hana_backup_plan is not None:
            for k in self.hana_backup_plan:
                result['HanaBackupPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hana_backup_plan = []
        if m.get('HanaBackupPlan') is not None:
            for k in m.get('HanaBackupPlan'):
                temp_model = DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan()
                self.hana_backup_plan.append(temp_model.from_map(k))
        return self


class DescribeHanaBackupPlansResponseBody(TeaModel):
    def __init__(self, code=None, hana_backup_plans=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The details of the backup plan.
        self.hana_backup_plans = hana_backup_plans  # type: DescribeHanaBackupPlansResponseBodyHanaBackupPlans
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.hana_backup_plans:
            self.hana_backup_plans.validate()

    def to_map(self):
        _map = super(DescribeHanaBackupPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_backup_plans is not None:
            result['HanaBackupPlans'] = self.hana_backup_plans.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaBackupPlans') is not None:
            temp_model = DescribeHanaBackupPlansResponseBodyHanaBackupPlans()
            self.hana_backup_plans = temp_model.from_map(m['HanaBackupPlans'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaBackupPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHanaBackupPlansResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHanaBackupPlansResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaBackupPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaBackupSettingRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaBackupSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaBackupSettingResponseBodyHanaBackupSetting(TeaModel):
    def __init__(self, catalog_backup_parameter_file=None, catalog_backup_using_backint=None,
                 data_backup_parameter_file=None, database_name=None, enable_auto_log_backup=None, log_backup_parameter_file=None,
                 log_backup_timeout=None, log_backup_using_backint=None):
        # The configuration file for catalog backup.
        self.catalog_backup_parameter_file = catalog_backup_parameter_file  # type: str
        # Indicates whether Backint is used to back up catalogs. Valid values:
        # 
        # *   true: Backint is used to back up catalogs.
        # *   false: Backint is not used to back up catalogs.
        self.catalog_backup_using_backint = catalog_backup_using_backint  # type: bool
        # The configuration file for data backup.
        self.data_backup_parameter_file = data_backup_parameter_file  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # Indicates whether automatic log backup is enabled. Valid values:
        # 
        # *   **true**: Automatic log backup is enabled.
        # *   **false**: Automatic log backup is disabled.
        self.enable_auto_log_backup = enable_auto_log_backup  # type: bool
        # The configuration file for log backup.
        self.log_backup_parameter_file = log_backup_parameter_file  # type: str
        # The interval at which logs are backed up. Unit: seconds.
        self.log_backup_timeout = log_backup_timeout  # type: long
        # Indicates whether Backint is used to back up logs. Valid values:
        # 
        # *   true: Backint is used to back up logs.
        # *   false: Backint is not used to back up logs.
        self.log_backup_using_backint = log_backup_using_backint  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaBackupSettingResponseBodyHanaBackupSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_backup_parameter_file is not None:
            result['CatalogBackupParameterFile'] = self.catalog_backup_parameter_file
        if self.catalog_backup_using_backint is not None:
            result['CatalogBackupUsingBackint'] = self.catalog_backup_using_backint
        if self.data_backup_parameter_file is not None:
            result['DataBackupParameterFile'] = self.data_backup_parameter_file
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.enable_auto_log_backup is not None:
            result['EnableAutoLogBackup'] = self.enable_auto_log_backup
        if self.log_backup_parameter_file is not None:
            result['LogBackupParameterFile'] = self.log_backup_parameter_file
        if self.log_backup_timeout is not None:
            result['LogBackupTimeout'] = self.log_backup_timeout
        if self.log_backup_using_backint is not None:
            result['LogBackupUsingBackint'] = self.log_backup_using_backint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CatalogBackupParameterFile') is not None:
            self.catalog_backup_parameter_file = m.get('CatalogBackupParameterFile')
        if m.get('CatalogBackupUsingBackint') is not None:
            self.catalog_backup_using_backint = m.get('CatalogBackupUsingBackint')
        if m.get('DataBackupParameterFile') is not None:
            self.data_backup_parameter_file = m.get('DataBackupParameterFile')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EnableAutoLogBackup') is not None:
            self.enable_auto_log_backup = m.get('EnableAutoLogBackup')
        if m.get('LogBackupParameterFile') is not None:
            self.log_backup_parameter_file = m.get('LogBackupParameterFile')
        if m.get('LogBackupTimeout') is not None:
            self.log_backup_timeout = m.get('LogBackupTimeout')
        if m.get('LogBackupUsingBackint') is not None:
            self.log_backup_using_backint = m.get('LogBackupUsingBackint')
        return self


class DescribeHanaBackupSettingResponseBody(TeaModel):
    def __init__(self, code=None, hana_backup_setting=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The backup settings.
        self.hana_backup_setting = hana_backup_setting  # type: DescribeHanaBackupSettingResponseBodyHanaBackupSetting
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.hana_backup_setting:
            self.hana_backup_setting.validate()

    def to_map(self):
        _map = super(DescribeHanaBackupSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_backup_setting is not None:
            result['HanaBackupSetting'] = self.hana_backup_setting.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaBackupSetting') is not None:
            temp_model = DescribeHanaBackupSettingResponseBodyHanaBackupSetting()
            self.hana_backup_setting = temp_model.from_map(m['HanaBackupSetting'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHanaBackupSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHanaBackupSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHanaBackupSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaBackupSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaBackupsAsyncRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, include_differential=None, include_incremental=None,
                 include_log=None, log_position=None, mode=None, page_number=None, page_size=None, recovery_point_in_time=None,
                 resource_group_id=None, source=None, source_cluster_id=None, system_copy=None, use_backint=None, vault_id=None,
                 volume_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # Specifies whether to include differential backups in the query results. Valid values:
        # 
        # *   true: includes differential backups.
        # *   false: excludes differential backups.
        self.include_differential = include_differential  # type: bool
        # Specifies whether to include incremental backups in the query results. Valid values:
        # 
        # *   true: includes incremental backups.
        # *   false: excludes incremental backups.
        self.include_incremental = include_incremental  # type: bool
        # Specifies whether to include log backups in the query results. Valid values:
        # 
        # *   true: includes log backups.
        # *   false: excludes log backups.
        self.include_log = include_log  # type: bool
        # The log position to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position  # type: long
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: restores the database to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: restores the database to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: restores the database to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: restores the database to a specified log position.
        self.mode = mode  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The point in time to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_POINT_IN_TIME**. HBR restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time  # type: long
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the source system. This parameter specifies the name of the source database that you want to restore. You must set the parameter in the `<Source database name>@SID` format.
        self.source = source  # type: str
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id  # type: str
        # Specifies whether to restore the database to a different instance. Valid values:
        # 
        # *   true: restores the database to a different instance.
        # *   false: restores the database within the same instance.
        self.system_copy = system_copy  # type: bool
        # Specifies whether Backint is used. Valid values:
        # 
        # *   true: Backint is used.
        # *   false: Backint is not used.
        self.use_backint = use_backint  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str
        # The ID of the volume that you want to restore. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaBackupsAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.include_differential is not None:
            result['IncludeDifferential'] = self.include_differential
        if self.include_incremental is not None:
            result['IncludeIncremental'] = self.include_incremental
        if self.include_log is not None:
            result['IncludeLog'] = self.include_log
        if self.log_position is not None:
            result['LogPosition'] = self.log_position
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id
        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy
        if self.use_backint is not None:
            result['UseBackint'] = self.use_backint
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IncludeDifferential') is not None:
            self.include_differential = m.get('IncludeDifferential')
        if m.get('IncludeIncremental') is not None:
            self.include_incremental = m.get('IncludeIncremental')
        if m.get('IncludeLog') is not None:
            self.include_log = m.get('IncludeLog')
        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')
        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')
        if m.get('UseBackint') is not None:
            self.use_backint = m.get('UseBackint')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        return self


class DescribeHanaBackupsAsyncResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaBackupsAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeHanaBackupsAsyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHanaBackupsAsyncResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHanaBackupsAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaBackupsAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaDatabasesRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None, resource_group_id=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaDatabasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase(TeaModel):
    def __init__(self, active_status=None, database_name=None, detail=None, host=None, service_name=None,
                 sql_port=None):
        # Indicates whether the database is started. Valid values:
        # 
        # *   **YES**: The database is started.
        # *   **NO**: The database is not started.
        self.active_status = active_status  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The detailed information.
        self.detail = detail  # type: str
        # The hostname.
        self.host = host  # type: str
        # The name of the service.
        self.service_name = service_name  # type: str
        # The port number.
        self.sql_port = sql_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_status is not None:
            result['ActiveStatus'] = self.active_status
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.host is not None:
            result['Host'] = self.host
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sql_port is not None:
            result['SqlPort'] = self.sql_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveStatus') is not None:
            self.active_status = m.get('ActiveStatus')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SqlPort') is not None:
            self.sql_port = m.get('SqlPort')
        return self


class DescribeHanaDatabasesResponseBodyHanaDatabases(TeaModel):
    def __init__(self, hana_database=None):
        self.hana_database = hana_database  # type: list[DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase]

    def validate(self):
        if self.hana_database:
            for k in self.hana_database:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHanaDatabasesResponseBodyHanaDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HanaDatabase'] = []
        if self.hana_database is not None:
            for k in self.hana_database:
                result['HanaDatabase'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hana_database = []
        if m.get('HanaDatabase') is not None:
            for k in m.get('HanaDatabase'):
                temp_model = DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase()
                self.hana_database.append(temp_model.from_map(k))
        return self


class DescribeHanaDatabasesResponseBody(TeaModel):
    def __init__(self, code=None, hana_databases=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The information about SAP HANA databases.
        self.hana_databases = hana_databases  # type: DescribeHanaDatabasesResponseBodyHanaDatabases
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.hana_databases:
            self.hana_databases.validate()

    def to_map(self):
        _map = super(DescribeHanaDatabasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_databases is not None:
            result['HanaDatabases'] = self.hana_databases.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaDatabases') is not None:
            temp_model = DescribeHanaDatabasesResponseBodyHanaDatabases()
            self.hana_databases = temp_model.from_map(m['HanaDatabases'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaDatabasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHanaDatabasesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHanaDatabasesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaInstancesRequestTag, self).to_map()
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


class DescribeHanaInstancesRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None, resource_group_id=None, tag=None,
                 vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags of SAP HANA instance.
        self.tag = tag  # type: list[DescribeHanaInstancesRequestTag]
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHanaInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeHanaInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaInstancesResponseBodyHanasHanaTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaInstancesResponseBodyHanasHanaTagsTag, self).to_map()
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


class DescribeHanaInstancesResponseBodyHanasHanaTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeHanaInstancesResponseBodyHanasHanaTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHanaInstancesResponseBodyHanasHanaTags, self).to_map()
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
                temp_model = DescribeHanaInstancesResponseBodyHanasHanaTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeHanaInstancesResponseBodyHanasHana(TeaModel):
    def __init__(self, alert_setting=None, cluster_id=None, hana_name=None, host=None, instance_number=None,
                 resource_group_id=None, status=None, status_message=None, tags=None, use_ssl=None, user_name=None,
                 validate_certificate=None, vault_id=None):
        # The alert settings. Valid value: INHERITED, which indicates that the backup client sends alert notifications in the same way as the backup vault.
        self.alert_setting = alert_setting  # type: str
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the SAP HANA instance.
        self.hana_name = hana_name  # type: str
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host  # type: str
        # The instance number of the SAP HANA system.
        self.instance_number = instance_number  # type: int
        # The ID of resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the SAP HANA instance. Valid values:
        # 
        # *   INITIALIZING: The instance is being initialized.
        # *   INITIALIZED: The instance is registered.
        # *   INVALID_HANA_NODE: The instance is invalid.
        # *   INITIALIZE_FAILED: The client fails to be installed on the instance.
        self.status = status  # type: long
        # The status information.
        self.status_message = status_message  # type: str
        # The tags of the SAP HANA instance.
        self.tags = tags  # type: DescribeHanaInstancesResponseBodyHanasHanaTags
        # Indicates whether the SAP HANA instance is connected over Secure Sockets Layer (SSL). Valid values:
        # 
        # *   true: The SAP HANA instance is connected over SSL.
        # *   false: The SAP HANA instance is not connected over SSL.
        self.use_ssl = use_ssl  # type: bool
        # The username of the SYSTEMDB database.
        self.user_name = user_name  # type: str
        # Indicates whether the SSL certificate of the SAP HANA instance is verified.
        self.validate_certificate = validate_certificate  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeHanaInstancesResponseBodyHanasHana, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.hana_name is not None:
            result['HanaName'] = self.hana_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('Tags') is not None:
            temp_model = DescribeHanaInstancesResponseBodyHanasHanaTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaInstancesResponseBodyHanas(TeaModel):
    def __init__(self, hana=None):
        self.hana = hana  # type: list[DescribeHanaInstancesResponseBodyHanasHana]

    def validate(self):
        if self.hana:
            for k in self.hana:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHanaInstancesResponseBodyHanas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hana'] = []
        if self.hana is not None:
            for k in self.hana:
                result['Hana'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hana = []
        if m.get('Hana') is not None:
            for k in m.get('Hana'):
                temp_model = DescribeHanaInstancesResponseBodyHanasHana()
                self.hana.append(temp_model.from_map(k))
        return self


class DescribeHanaInstancesResponseBody(TeaModel):
    def __init__(self, code=None, hanas=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The information about the SAP HANA instances.
        self.hanas = hanas  # type: DescribeHanaInstancesResponseBodyHanas
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.hanas:
            self.hanas.validate()

    def to_map(self):
        _map = super(DescribeHanaInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hanas is not None:
            result['Hanas'] = self.hanas.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Hanas') is not None:
            temp_model = DescribeHanaInstancesResponseBodyHanas()
            self.hanas = temp_model.from_map(m['Hanas'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHanaInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHanaInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaRestoresRequest(TeaModel):
    def __init__(self, backup_id=None, cluster_id=None, database_name=None, page_number=None, page_size=None,
                 resource_group_id=None, restore_id=None, restore_status=None, vault_id=None):
        # The ID of the backup.
        self.backup_id = backup_id  # type: long
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the restore job.
        self.restore_id = restore_id  # type: str
        # The status of the restore job. Valid values:
        # 
        # *   **RUNNING**: The restore job is running.
        # *   **COMPLETE**: The restore job is completed.
        # *   **PARTIAL_COMPLETE**: The restore job is partially completed.
        # *   **FAILED**: The restore job has failed.
        # *   **CANCELED**: The restore job is canceled.
        # *   **EXPIRED**: The restore job has timed out.
        self.restore_status = restore_status  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaRestoresRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores(TeaModel):
    def __init__(self, backup_id=None, backup_prefix=None, check_access=None, clear_log=None, cluster_id=None,
                 current_phase=None, current_progress=None, database_name=None, database_restore_id=None, end_time=None,
                 log_position=None, max_phase=None, max_progress=None, message=None, mode=None, phase=None, reached_time=None,
                 recovery_point_in_time=None, restore_id=None, source=None, source_cluster_id=None, start_time=None, state=None,
                 status=None, system_copy=None, use_catalog=None, use_delta=None, vault_id=None, volume_id=None):
        # The ID of the backup.
        self.backup_id = backup_id  # type: long
        # The backup prefix.
        self.backup_prefix = backup_prefix  # type: str
        # Indicates whether the differential backup and log backup are validated. Valid values:
        # 
        # *   true: HBR checks whether the required differential backup and log backup are available before the restore job starts. If the differential backup or log backup is unavailable, HBR does not start the restore job.
        # *   false: HBR does not check whether the required differential backup and log backup are available before the restore job starts.
        self.check_access = check_access  # type: bool
        # Indicates whether all log entries are deleted from the log area after the log entries are restored. Valid values: true and false. If the return value is false, all log entries are deleted from the log area after the log entries are restored.
        self.clear_log = clear_log  # type: bool
        # The ID of the SAP HANA instance that is restored.
        self.cluster_id = cluster_id  # type: str
        # The current recovery phase. This value is obtained from SAP HANA.
        self.current_phase = current_phase  # type: int
        # The current progress. This value is obtained from SAP HANA.
        self.current_progress = current_progress  # type: long
        # The name of the database.
        self.database_name = database_name  # type: str
        # The ID of the database recovery.
        self.database_restore_id = database_restore_id  # type: long
        # The time when the restore job ends. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The log position to which the database is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position  # type: long
        # The maximum recovery phase. This value is obtained from SAP HANA.
        self.max_phase = max_phase  # type: int
        # The maximum progress. This value is obtained from SAP HANA.
        self.max_progress = max_progress  # type: long
        # The details of the recovery phase.
        self.message = message  # type: str
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: The database is restored to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: The database is restored to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: The database is restored to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: The database is restored to a specified log position.
        self.mode = mode  # type: str
        # The recovery phase.
        self.phase = phase  # type: str
        # The point in time at which the database is restored.
        self.reached_time = reached_time  # type: long
        # The point in time to which the database is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_POINT_IN_TIME**. HBR restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time  # type: long
        # The ID of the restore job.
        self.restore_id = restore_id  # type: str
        # The name of the source system. This parameter indicates the name of the source database that is restored. Format: `<Source database name>@SID`.
        self.source = source  # type: str
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id  # type: str
        # The time when the restore job starts. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # The recovery status. This value is obtained from SAP HANA.
        self.state = state  # type: str
        # The status of the restore job. Valid values:
        # 
        # *   **RUNNING**: The restore job is running.
        # *   **COMPLETE**: The restore job is completed.
        # *   **PARTIAL_COMPLETE**: The restore job is partially completed.
        # *   **FAILED**: The restore job has failed.
        # *   **CANCELED**: The restore job is canceled.
        # *   **EXPIRED**: The restore job has timed out.
        self.status = status  # type: str
        # Indicates whether the database is restored to a different instance. Valid values:
        # 
        # *   true: The database is restored to a different instance.
        # *   false: The database is restored within the same instance.
        self.system_copy = system_copy  # type: bool
        # Indicates whether a catalog backup is used to restore the database. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_SPECIFIC_BACKUP**. If the return value is false, HBR finds the backup file based on the specified prefix and then restores the backup file.
        self.use_catalog = use_catalog  # type: bool
        # Indicates whether a differential backup or an incremental backup is used to restore the database. Valid values: true and false. If the return value is true, HBR uses a differential backup or an incremental backup to restore the database. If the return value is false, HBR uses a log backup to restore the database.
        self.use_delta = use_delta  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str
        # The ID of the volume that is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupID'] = self.backup_id
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.check_access is not None:
            result['CheckAccess'] = self.check_access
        if self.clear_log is not None:
            result['ClearLog'] = self.clear_log
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.current_phase is not None:
            result['CurrentPhase'] = self.current_phase
        if self.current_progress is not None:
            result['CurrentProgress'] = self.current_progress
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.database_restore_id is not None:
            result['DatabaseRestoreId'] = self.database_restore_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_position is not None:
            result['LogPosition'] = self.log_position
        if self.max_phase is not None:
            result['MaxPhase'] = self.max_phase
        if self.max_progress is not None:
            result['MaxProgress'] = self.max_progress
        if self.message is not None:
            result['Message'] = self.message
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.reached_time is not None:
            result['ReachedTime'] = self.reached_time
        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy
        if self.use_catalog is not None:
            result['UseCatalog'] = self.use_catalog
        if self.use_delta is not None:
            result['UseDelta'] = self.use_delta
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupID') is not None:
            self.backup_id = m.get('BackupID')
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('CheckAccess') is not None:
            self.check_access = m.get('CheckAccess')
        if m.get('ClearLog') is not None:
            self.clear_log = m.get('ClearLog')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CurrentPhase') is not None:
            self.current_phase = m.get('CurrentPhase')
        if m.get('CurrentProgress') is not None:
            self.current_progress = m.get('CurrentProgress')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatabaseRestoreId') is not None:
            self.database_restore_id = m.get('DatabaseRestoreId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')
        if m.get('MaxPhase') is not None:
            self.max_phase = m.get('MaxPhase')
        if m.get('MaxProgress') is not None:
            self.max_progress = m.get('MaxProgress')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ReachedTime') is not None:
            self.reached_time = m.get('ReachedTime')
        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')
        if m.get('UseCatalog') is not None:
            self.use_catalog = m.get('UseCatalog')
        if m.get('UseDelta') is not None:
            self.use_delta = m.get('UseDelta')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        return self


class DescribeHanaRestoresResponseBodyHanaRestore(TeaModel):
    def __init__(self, hana_restores=None):
        self.hana_restores = hana_restores  # type: list[DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores]

    def validate(self):
        if self.hana_restores:
            for k in self.hana_restores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHanaRestoresResponseBodyHanaRestore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HanaRestores'] = []
        if self.hana_restores is not None:
            for k in self.hana_restores:
                result['HanaRestores'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hana_restores = []
        if m.get('HanaRestores') is not None:
            for k in m.get('HanaRestores'):
                temp_model = DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores()
                self.hana_restores.append(temp_model.from_map(k))
        return self


class DescribeHanaRestoresResponseBody(TeaModel):
    def __init__(self, code=None, hana_restore=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The information about restore jobs.
        self.hana_restore = hana_restore  # type: DescribeHanaRestoresResponseBodyHanaRestore
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.hana_restore:
            self.hana_restore.validate()

    def to_map(self):
        _map = super(DescribeHanaRestoresResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hana_restore is not None:
            result['HanaRestore'] = self.hana_restore.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HanaRestore') is not None:
            temp_model = DescribeHanaRestoresResponseBodyHanaRestore()
            self.hana_restore = temp_model.from_map(m['HanaRestore'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHanaRestoresResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHanaRestoresResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHanaRestoresResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaRestoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHanaRetentionSettingRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaRetentionSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaRetentionSettingResponseBody(TeaModel):
    def __init__(self, cluster_id=None, code=None, database_name=None, disabled=None, message=None, request_id=None,
                 retention_days=None, schedule=None, success=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # Indicates whether the backup is permanently retained. Valid values:
        # 
        # *   true: The backup is permanently retained.
        # *   false: The backup is retained for the specified number of days.
        self.disabled = disabled  # type: bool
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of days for which the backup is retained. If the value of the Disabled parameter is false, the backup is retained for the number of days specified by this parameter.
        self.retention_days = retention_days  # type: long
        # The policy to update the retention period. Format: `I|{startTime}|{interval}`, which indicates that the retention period is updated at an interval of {interval} starting from {startTime}.
        # 
        # *   startTime: the time at which the system starts to update the retention period. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system updates the retention period. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHanaRetentionSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.code is not None:
            result['Code'] = self.code
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.success is not None:
            result['Success'] = self.success
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeHanaRetentionSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHanaRetentionSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHanaRetentionSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHanaRetentionSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOtsTableSnapshotsRequestOtsInstances(TeaModel):
    def __init__(self, instance_name=None, table_names=None):
        # The name of the Tablestore instance.
        self.instance_name = instance_name  # type: str
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOtsTableSnapshotsRequestOtsInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class DescribeOtsTableSnapshotsRequest(TeaModel):
    def __init__(self, cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None,
                 end_time=None, limit=None, next_token=None, ots_instances=None, snapshot_ids=None, start_time=None):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The UID of the source account used for cross-account backup.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The end time of the backup. The value must be a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The maximum number of rows that you want the current query to return.
        self.limit = limit  # type: int
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token  # type: str
        # The Tablestore instances that are backed up.
        self.ots_instances = ots_instances  # type: list[DescribeOtsTableSnapshotsRequestOtsInstances]
        # The snapshot IDs.
        self.snapshot_ids = snapshot_ids  # type: list[str]
        # The start time of the backup. The value must be a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        if self.ots_instances:
            for k in self.ots_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOtsTableSnapshotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['OtsInstances'] = []
        if self.ots_instances is not None:
            for k in self.ots_instances:
                result['OtsInstances'].append(k.to_map() if k else None)
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.ots_instances = []
        if m.get('OtsInstances') is not None:
            for k in m.get('OtsInstances'):
                temp_model = DescribeOtsTableSnapshotsRequestOtsInstances()
                self.ots_instances.append(temp_model.from_map(k))
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOtsTableSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(self, actual_bytes=None, backup_type=None, bytes_total=None, complete_time=None, create_time=None,
                 created_time=None, instance_name=None, job_id=None, parent_snapshot_hash=None, range_end=None, range_start=None,
                 retention=None, snapshot_hash=None, snapshot_id=None, source_type=None, start_time=None, status=None,
                 table_name=None, updated_time=None, vault_id=None):
        # The actual data amount of backup snapshots after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes  # type: str
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total  # type: long
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time  # type: long
        # The time when the Tablestore instance was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time  # type: long
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The name of the Tablestore instance.
        self.instance_name = instance_name  # type: str
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash  # type: str
        # The time when the backup job ended. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_end = range_end  # type: long
        # The time when the backup job started. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_start = range_start  # type: long
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention  # type: long
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash  # type: str
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        # *   **OTS_TABLE**: backup snapshots for Tablestore instances
        self.source_type = source_type  # type: str
        # The time when the backup snapshot started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status  # type: str
        # The name of the table in the Tablestore instance.
        self.table_name = table_name  # type: str
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long
        # The ID of the backup vault that stores the backup snapshot.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOtsTableSnapshotsResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash
        if self.range_end is not None:
            result['RangeEnd'] = self.range_end
        if self.range_start is not None:
            result['RangeStart'] = self.range_start
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')
        if m.get('RangeEnd') is not None:
            self.range_end = m.get('RangeEnd')
        if m.get('RangeStart') is not None:
            self.range_start = m.get('RangeStart')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeOtsTableSnapshotsResponseBody(TeaModel):
    def __init__(self, code=None, limit=None, message=None, next_token=None, request_id=None, snapshots=None,
                 success=None):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The number of backup snapshots that are displayed on the current page.
        self.limit = limit  # type: int
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message  # type: str
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The backup snapshots.
        self.snapshots = snapshots  # type: list[DescribeOtsTableSnapshotsResponseBodySnapshots]
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOtsTableSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeOtsTableSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeOtsTableSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOtsTableSnapshotsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOtsTableSnapshotsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOtsTableSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePoliciesV2Request(TeaModel):
    def __init__(self, max_results=None, next_token=None, policy_id=None):
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results  # type: int
        # The token that is used to obtain the next page of backup policies.
        self.next_token = next_token  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePoliciesV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules(TeaModel):
    def __init__(self, advanced_retention_type=None, retention=None, which_snapshot=None):
        # The type of the special retention rule. Valid values:
        # 
        # *   **WEEKLY**: weekly backups.
        # *   **MONTHLY**: monthly backups.
        # *   **YEARLY**: yearly backups.
        self.advanced_retention_type = advanced_retention_type  # type: str
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # Indicates which backup is retained based on the special retention rule. Only the first backup can be retained.
        self.which_snapshot = which_snapshot  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.which_snapshot is not None:
            result['WhichSnapshot'] = self.which_snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('WhichSnapshot') is not None:
            self.which_snapshot = m.get('WhichSnapshot')
        return self


class DescribePoliciesV2ResponseBodyPoliciesRules(TeaModel):
    def __init__(self, archive_days=None, backup_type=None, keep_latest_snapshots=None, replication_region_id=None,
                 retention=None, retention_rules=None, rule_id=None, rule_type=None, schedule=None, vault_id=None):
        self.archive_days = archive_days  # type: long
        # This parameter is returned only if the value of the **RuleType** parameter is **BACKUP**. This parameter indicates the backup type. Only **COMPLETE** may be returned, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # Indicates whether the feature of keeping at least one backup version is enabled. Valid values:
        # 
        # *   **0**: This feature is disabled.
        # *   **1**: This feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # This parameter is returned only if the value of the **RuleType** parameter is **REPLICATION**. This parameter indicates the ID of the destination region.
        self.replication_region_id = replication_region_id  # type: str
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION** or **REPLICATION**.
        # 
        # *   If the value of the **RuleType** parameter is **TRANSITION**, this parameter indicates the retention period of the backup data. Minimum value: 1. Unit: days.
        # *   If the value of the **RuleType** parameter is **REPLICATION**, this parameter indicates the retention period of remote backups. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION**. This parameter indicates the special retention rules.
        self.retention_rules = retention_rules  # type: list[DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules]
        # The rule ID.
        self.rule_id = rule_id  # type: str
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type.
        # 
        # *   **BACKUP**: the backup rule.
        # *   **TRANSITION**: the lifecycle rule.
        # *   **REPLICATION**: the replication rule.
        self.rule_type = rule_type  # type: str
        # This parameter is returned only if the value of the **RuleType** parameter is **BACKUP**. This parameter indicates the scheduling settings for the backups. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is complete. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time when the system starts to run a backup job. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H indicates an interval of one hour. P1D indicates an interval of one day.
        self.schedule = schedule  # type: str
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.retention_rules:
            for k in self.retention_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePoliciesV2ResponseBodyPoliciesRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_days is not None:
            result['ArchiveDays'] = self.archive_days
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.replication_region_id is not None:
            result['ReplicationRegionId'] = self.replication_region_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['RetentionRules'] = []
        if self.retention_rules is not None:
            for k in self.retention_rules:
                result['RetentionRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchiveDays') is not None:
            self.archive_days = m.get('ArchiveDays')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('ReplicationRegionId') is not None:
            self.replication_region_id = m.get('ReplicationRegionId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.retention_rules = []
        if m.get('RetentionRules') is not None:
            for k in m.get('RetentionRules'):
                temp_model = DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribePoliciesV2ResponseBodyPolicies(TeaModel):
    def __init__(self, created_time=None, policy_binding_count=None, policy_description=None, policy_id=None,
                 policy_name=None, rules=None, updated_time=None):
        # The time when the backup policy was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_time = created_time  # type: long
        # The number of data sources that are bound to the backup policy.
        self.policy_binding_count = policy_binding_count  # type: long
        # The description of the backup policy.
        self.policy_description = policy_description  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The name of the backup policy.
        self.policy_name = policy_name  # type: str
        # The rules in the backup policy.
        self.rules = rules  # type: list[DescribePoliciesV2ResponseBodyPoliciesRules]
        # The time when the backup policy was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.updated_time = updated_time  # type: long

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePoliciesV2ResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.policy_binding_count is not None:
            result['PolicyBindingCount'] = self.policy_binding_count
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('PolicyBindingCount') is not None:
            self.policy_binding_count = m.get('PolicyBindingCount')
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribePoliciesV2ResponseBodyPoliciesRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribePoliciesV2ResponseBody(TeaModel):
    def __init__(self, code=None, max_results=None, message=None, next_token=None, policies=None, request_id=None,
                 success=None, total_count=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results  # type: int
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The token that is used to obtain the next page of backup policies.
        self.next_token = next_token  # type: str
        # The backup policies.
        self.policies = policies  # type: list[DescribePoliciesV2ResponseBodyPolicies]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePoliciesV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribePoliciesV2ResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePoliciesV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePoliciesV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePoliciesV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePoliciesV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyBindingsRequestFilters(TeaModel):
    def __init__(self, key=None, operator=None, values=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyBindingsRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribePolicyBindingsRequest(TeaModel):
    def __init__(self, data_source_ids=None, filters=None, max_results=None, next_token=None, policy_id=None,
                 source_type=None):
        self.data_source_ids = data_source_ids  # type: list[str]
        self.filters = filters  # type: list[DescribePolicyBindingsRequestFilters]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.policy_id = policy_id  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribePolicyBindingsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribePolicyBindingsShrinkRequestFilters(TeaModel):
    def __init__(self, key=None, operator=None, values=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyBindingsShrinkRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribePolicyBindingsShrinkRequest(TeaModel):
    def __init__(self, data_source_ids_shrink=None, filters=None, max_results=None, next_token=None, policy_id=None,
                 source_type=None):
        self.data_source_ids_shrink = data_source_ids_shrink  # type: str
        self.filters = filters  # type: list[DescribePolicyBindingsShrinkRequestFilters]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.policy_id = policy_id  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyBindingsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribePolicyBindingsShrinkRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail(TeaModel):
    def __init__(self, fetch_slice_size=None, full_on_increment_fail=None):
        self.fetch_slice_size = fetch_slice_size  # type: long
        self.full_on_increment_fail = full_on_increment_fail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail(TeaModel):
    def __init__(self, client_id=None, cluster_id=None, fetch_slice_size=None, full_on_increment_fail=None):
        # The ID of the HBR client.
        self.client_id = client_id  # type: str
        self.cluster_id = cluster_id  # type: str
        # The size of backup shards (the number of files).
        self.fetch_slice_size = fetch_slice_size  # type: long
        # Indicates whether the system performs full backup if incremental backup fails. Valid values:
        # 
        # *   **true**: The system performs full backup if incremental backup fails.
        # *   **false**: The system does not perform full backup if incremental backup fails.
        self.full_on_increment_fail = full_on_increment_fail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail(TeaModel):
    def __init__(self, adv_policy=None, use_vss=None):
        # Indicates whether an advanced policy is used. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.adv_policy = adv_policy  # type: bool
        # Indicates whether the Volume Shadow Copy Service (VSS) feature is enabled. Valid values:
        # 
        # *   **true**: The feature is enabled.
        # *   **false**: The feature is disabled.
        self.use_vss = use_vss  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adv_policy is not None:
            result['AdvPolicy'] = self.adv_policy
        if self.use_vss is not None:
            result['UseVSS'] = self.use_vss
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvPolicy') is not None:
            self.adv_policy = m.get('AdvPolicy')
        if m.get('UseVSS') is not None:
            self.use_vss = m.get('UseVSS')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail(TeaModel):
    def __init__(self, inventory_cleanup_policy=None, inventory_id=None):
        # Indicates whether the system deletes the inventory lists when a backup is completed. This parameter is valid only when OSS inventories are used. Valid values:
        # 
        # *   **NO_CLEANUP**: Inventory lists are not deleted.
        # *   **DELETE_CURRENT**: The current inventory list is deleted.
        # *   **DELETE_CURRENT_AND_PREVIOUS**: All inventory lists are deleted.
        self.inventory_cleanup_policy = inventory_cleanup_policy  # type: str
        # The name of the OSS inventory. If this parameter is not empty, the OSS inventory is used for performance optimization.
        # 
        # *   If you want to back up more than 100 million OSS objects, we recommend that you use inventory lists to accelerate incremental backup. Storage fees for inventory lists are included into your OSS bills.
        # *   A certain amount of time is required for OSS to generate inventory lists. Before inventory lists are generated, OSS objects may fail to be backed up. In this case, you can back up the OSS objects in the next backup cycle.
        self.inventory_id = inventory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_cleanup_policy is not None:
            result['InventoryCleanupPolicy'] = self.inventory_cleanup_policy
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InventoryCleanupPolicy') is not None:
            self.inventory_cleanup_policy = m.get('InventoryCleanupPolicy')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail(TeaModel):
    def __init__(self, app_consistent=None, destination_kms_key_id=None, disk_id_list=None, enable_fs_freeze=None,
                 enable_writers=None, exclude_disk_id_list=None, post_script_path=None, pre_script_path=None, ram_role_name=None,
                 snapshot_group=None, timeout_in_seconds=None):
        # Indicates whether application consistency is enabled. You can enable application consistency only if all disks are ESSDs.
        self.app_consistent = app_consistent  # type: bool
        self.destination_kms_key_id = destination_kms_key_id  # type: str
        # The IDs of the disks that need to be protected. If all disks need to be protected, this parameter is empty.
        self.disk_id_list = disk_id_list  # type: list[str]
        # This parameter is returned only if **AppConsistent** is set to **true**. This parameter indicates whether Linux fsfreeze is enabled to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        self.enable_fs_freeze = enable_fs_freeze  # type: bool
        # This parameter is returned only if **AppConsistent** is set to **true**. This parameter indicates whether application-consistent snapshots are created. Valid values:
        # 
        # *   true: Application-consistent snapshots are created.
        # *   false: File system-consistent snapshots are created.
        # 
        # Default value: true.
        self.enable_writers = enable_writers  # type: bool
        # The IDs of the disks that do not need to be protected. If DiskIdList is not empty, this parameter is ignored.
        self.exclude_disk_id_list = exclude_disk_id_list  # type: list[str]
        # This parameter is returned only if **AppConsistent** is set to **true**. This parameter indicates the path of the post-thaw scripts that are executed after application-consistent snapshots are created.
        self.post_script_path = post_script_path  # type: str
        # This parameter is returned only if **AppConsistent** is set to **true**. This parameter indicates the path of the pre-freeze scripts that are executed before application-consistent snapshots are created.
        self.pre_script_path = pre_script_path  # type: str
        # This parameter is returned only if **AppConsistent** is set to **true**. This parameter indicates the name of the RAM role that is required to create application-consistent snapshots.
        self.ram_role_name = ram_role_name  # type: str
        # Indicates whether a snapshot-consistent group is created. You can create a snapshot-consistent group only if all disks are enhanced SSDs (ESSDs).
        self.snapshot_group = snapshot_group  # type: bool
        # This parameter is returned only if **AppConsistent** is set to **true**. This parameter indicates the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.timeout_in_seconds = timeout_in_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_consistent is not None:
            result['AppConsistent'] = self.app_consistent
        if self.destination_kms_key_id is not None:
            result['DestinationKmsKeyId'] = self.destination_kms_key_id
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.enable_fs_freeze is not None:
            result['EnableFsFreeze'] = self.enable_fs_freeze
        if self.enable_writers is not None:
            result['EnableWriters'] = self.enable_writers
        if self.exclude_disk_id_list is not None:
            result['ExcludeDiskIdList'] = self.exclude_disk_id_list
        if self.post_script_path is not None:
            result['PostScriptPath'] = self.post_script_path
        if self.pre_script_path is not None:
            result['PreScriptPath'] = self.pre_script_path
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.snapshot_group is not None:
            result['SnapshotGroup'] = self.snapshot_group
        if self.timeout_in_seconds is not None:
            result['TimeoutInSeconds'] = self.timeout_in_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppConsistent') is not None:
            self.app_consistent = m.get('AppConsistent')
        if m.get('DestinationKmsKeyId') is not None:
            self.destination_kms_key_id = m.get('DestinationKmsKeyId')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('EnableFsFreeze') is not None:
            self.enable_fs_freeze = m.get('EnableFsFreeze')
        if m.get('EnableWriters') is not None:
            self.enable_writers = m.get('EnableWriters')
        if m.get('ExcludeDiskIdList') is not None:
            self.exclude_disk_id_list = m.get('ExcludeDiskIdList')
        if m.get('PostScriptPath') is not None:
            self.post_script_path = m.get('PostScriptPath')
        if m.get('PreScriptPath') is not None:
            self.pre_script_path = m.get('PreScriptPath')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SnapshotGroup') is not None:
            self.snapshot_group = m.get('SnapshotGroup')
        if m.get('TimeoutInSeconds') is not None:
            self.timeout_in_seconds = m.get('TimeoutInSeconds')
        return self


class DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions(TeaModel):
    def __init__(self, common_file_system_detail=None, common_nas_detail=None, file_detail=None, oss_detail=None,
                 udm_detail=None):
        self.common_file_system_detail = common_file_system_detail  # type: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail
        # The advanced options for on-premises NAS backup.
        self.common_nas_detail = common_nas_detail  # type: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail
        # The advanced options for file backup.
        self.file_detail = file_detail  # type: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail
        # The advanced options for OSS backup.
        self.oss_detail = oss_detail  # type: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail
        # The advanced options for ECS instance backup.
        self.udm_detail = udm_detail  # type: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail

    def validate(self):
        if self.common_file_system_detail:
            self.common_file_system_detail.validate()
        if self.common_nas_detail:
            self.common_nas_detail.validate()
        if self.file_detail:
            self.file_detail.validate()
        if self.oss_detail:
            self.oss_detail.validate()
        if self.udm_detail:
            self.udm_detail.validate()

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_file_system_detail is not None:
            result['CommonFileSystemDetail'] = self.common_file_system_detail.to_map()
        if self.common_nas_detail is not None:
            result['CommonNasDetail'] = self.common_nas_detail.to_map()
        if self.file_detail is not None:
            result['FileDetail'] = self.file_detail.to_map()
        if self.oss_detail is not None:
            result['OssDetail'] = self.oss_detail.to_map()
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonFileSystemDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m['CommonFileSystemDetail'])
        if m.get('CommonNasDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsCommonNasDetail()
            self.common_nas_detail = temp_model.from_map(m['CommonNasDetail'])
        if m.get('FileDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsFileDetail()
            self.file_detail = temp_model.from_map(m['FileDetail'])
        if m.get('OssDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m['OssDetail'])
        if m.get('UdmDetail') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m['UdmDetail'])
        return self


class DescribePolicyBindingsResponseBodyPolicyBindings(TeaModel):
    def __init__(self, advanced_options=None, created_time=None, cross_account_role_name=None,
                 cross_account_type=None, cross_account_user_id=None, data_source_id=None, disabled=None,
                 policy_binding_description=None, policy_binding_id=None, policy_id=None, source_type=None, updated_time=None):
        # The advanced options.
        self.advanced_options = advanced_options  # type: DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions
        # The time when the backup policy was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Indicates whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The ID of the data source.
        self.data_source_id = data_source_id  # type: str
        # Indicates whether the backup policy is enabled for the data source. Valid values:
        # 
        # *   true: The backup policy is disabled.
        # *   false: The backup policy is enabled.
        self.disabled = disabled  # type: bool
        # The description of the association.
        self.policy_binding_description = policy_binding_description  # type: str
        # The ID of the association.
        self.policy_binding_id = policy_binding_id  # type: str
        # The policy ID.
        self.policy_id = policy_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str
        # The time when the backup policy was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBodyPolicyBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.policy_binding_id is not None:
            result['PolicyBindingId'] = self.policy_binding_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = DescribePolicyBindingsResponseBodyPolicyBindingsAdvancedOptions()
            self.advanced_options = temp_model.from_map(m['AdvancedOptions'])
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('PolicyBindingId') is not None:
            self.policy_binding_id = m.get('PolicyBindingId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribePolicyBindingsResponseBody(TeaModel):
    def __init__(self, code=None, max_results=None, message=None, next_token=None, policy_bindings=None,
                 request_id=None, success=None, total_count=None):
        self.code = code  # type: str
        self.max_results = max_results  # type: int
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        # The association between the backup policy and data sources.
        self.policy_bindings = policy_bindings  # type: list[DescribePolicyBindingsResponseBodyPolicyBindings]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.policy_bindings:
            for k in self.policy_bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyBindingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PolicyBindings'] = []
        if self.policy_bindings is not None:
            for k in self.policy_bindings:
                result['PolicyBindings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policy_bindings = []
        if m.get('PolicyBindings') is not None:
            for k in m.get('PolicyBindings'):
                temp_model = DescribePolicyBindingsResponseBodyPolicyBindings()
                self.policy_bindings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePolicyBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyBindingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyBindingsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecoverableOtsInstancesRequest(TeaModel):
    def __init__(self, cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None):
        # The role name created in the RAM of the original account used for cross-account backup.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # The type of cross-account backup. Supported:
        # * SELF_ACCOUNT: backup of this account
        # * CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type  # type: str
        # The Alibaba Cloud Uid of the original account used to cross accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecoverableOtsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        return self


class DescribeRecoverableOtsInstancesResponseBodyOtsInstances(TeaModel):
    def __init__(self, instance_name=None, table_names=None):
        # The name of the Tablestore instance that can be restored.
        self.instance_name = instance_name  # type: str
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecoverableOtsInstancesResponseBodyOtsInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class DescribeRecoverableOtsInstancesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, ots_instances=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The list of Tablestore instances that can be restored and the tables in the instances.
        self.ots_instances = ots_instances  # type: list[DescribeRecoverableOtsInstancesResponseBodyOtsInstances]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.ots_instances:
            for k in self.ots_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRecoverableOtsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['OtsInstances'] = []
        if self.ots_instances is not None:
            for k in self.ots_instances:
                result['OtsInstances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.ots_instances = []
        if m.get('OtsInstances') is not None:
            for k in m.get('OtsInstances'):
                temp_model = DescribeRecoverableOtsInstancesResponseBodyOtsInstances()
                self.ots_instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRecoverableOtsInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRecoverableOtsInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecoverableOtsInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRecoverableOtsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, need_vault_count=None):
        # Specifies whether to return detailed information. Default value: false.
        self.need_vault_count = need_vault_count  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_vault_count is not None:
            result['NeedVaultCount'] = self.need_vault_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedVaultCount') is not None:
            self.need_vault_count = m.get('NeedVaultCount')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_id=None, vault_count=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The number of repositories in the region.
        self.vault_count = vault_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vault_count is not None:
            result['VaultCount'] = self.vault_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VaultCount') is not None:
            self.vault_count = m.get('VaultCount')
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
    def __init__(self, code=None, message=None, regions=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The list of regions.
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
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


class DescribeRestoreJobs2RequestFilters(TeaModel):
    def __init__(self, key=None, operator=None, values=None):
        # The key in the filter. Valid values:
        # 
        # *   **RegionId**: the region ID
        # *   **PlanId**: the ID of a backup plan
        # *   **JobId**: the ID of a backup job
        # *   **VaultId**: the ID of a backup vault
        # *   **InstanceId**: the ID of an ECS instance
        # *   **Bucket**: the name of an OSS bucket
        # *   **FileSystemId**: the ID of a file system
        # *   **Status**: the status of a backup job
        # *   **CompleteTime**: the end time of a backup job
        self.key = key  # type: str
        # The matching method. Default value: IN. This parameter specifies the operator that you want to use to match a key and a value in the filter. Valid values:
        # 
        # *   **EQUAL**: equal to
        # *   **NOT_EQUAL**: not equal to
        # *   **GREATER_THAN**: greater than
        # *   **GREATER_THAN_OR_EQUAL**: greater than or equal to
        # *   **LESS_THAN**: less than
        # *   **LESS_THAN_OR_EQUAL**: less than or equal to
        # *   **BETWEEN**: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        # *   **IN**: specifies an array as a collection. The results must fall within the collection.
        # 
        # > If you specify the **CompleteTime** parameter as a key to query backup jobs, you cannot use the IN operator to perform a match.
        self.operator = operator  # type: str
        # The values that you want to match in the filter.
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreJobs2RequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeRestoreJobs2Request(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None, restore_type=None):
        # The keys in the filter.
        self.filters = filters  # type: list[DescribeRestoreJobs2RequestFilters]
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS_ROLLBACK**: ECS instances
        self.restore_type = restore_type  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRestoreJobs2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeRestoreJobs2RequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail(TeaModel):
    def __init__(self, batch_channel_count=None, overwrite_existing=None):
        # The number of channels processed by each Tablestore restore job.
        self.batch_channel_count = batch_channel_count  # type: int
        # Indicates whether the existing Tablestore restore job was overwritten.
        self.overwrite_existing = overwrite_existing  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_channel_count is not None:
            result['BatchChannelCount'] = self.batch_channel_count
        if self.overwrite_existing is not None:
            result['OverwriteExisting'] = self.overwrite_existing
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchChannelCount') is not None:
            self.batch_channel_count = m.get('BatchChannelCount')
        if m.get('OverwriteExisting') is not None:
            self.overwrite_existing = m.get('OverwriteExisting')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport(TeaModel):
    def __init__(self, failed_files=None, report_task_status=None, skipped_files=None, success_files=None,
                 total_files=None):
        self.failed_files = failed_files  # type: str
        self.report_task_status = report_task_status  # type: str
        self.skipped_files = skipped_files  # type: str
        self.success_files = success_files  # type: str
        self.total_files = total_files  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_files is not None:
            result['FailedFiles'] = self.failed_files
        if self.report_task_status is not None:
            result['ReportTaskStatus'] = self.report_task_status
        if self.skipped_files is not None:
            result['SkippedFiles'] = self.skipped_files
        if self.success_files is not None:
            result['SuccessFiles'] = self.success_files
        if self.total_files is not None:
            result['TotalFiles'] = self.total_files
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedFiles') is not None:
            self.failed_files = m.get('FailedFiles')
        if m.get('ReportTaskStatus') is not None:
            self.report_task_status = m.get('ReportTaskStatus')
        if m.get('SkippedFiles') is not None:
            self.skipped_files = m.get('SkippedFiles')
        if m.get('SuccessFiles') is not None:
            self.success_files = m.get('SuccessFiles')
        if m.get('TotalFiles') is not None:
            self.total_files = m.get('TotalFiles')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob(TeaModel):
    def __init__(self, actual_bytes=None, actual_items=None, bytes_done=None, bytes_total=None, cluster_id=None,
                 complete_time=None, created_time=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, error_file=None, error_message=None, exclude=None, expire_time=None, failback_detail=None,
                 include=None, items_done=None, items_total=None, metering_bytes_done=None, metering_bytes_total=None,
                 options=None, ots_detail=None, parent_id=None, progress=None, report=None, restore_id=None,
                 restore_type=None, snapshot_hash=None, snapshot_id=None, source_type=None, speed=None, start_time=None,
                 status=None, storage_class=None, target_bucket=None, target_client_id=None, target_create_time=None,
                 target_data_source_id=None, target_file_system_id=None, target_instance_id=None, target_instance_name=None,
                 target_path=None, target_prefix=None, target_table_name=None, target_time=None, udm_detail=None,
                 updated_time=None, vault_id=None):
        # The actual amount of data that is restored after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes  # type: long
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the actual number of objects that are restored by the restore job.
        self.actual_items = actual_items  # type: long
        # The amount of data that was restored. Unit: bytes.
        self.bytes_done = bytes_done  # type: long
        # The total amount of data that is backed up from the data source. Unit: bytes.
        self.bytes_total = bytes_total  # type: long
        # The ID of the client group used for restoration.
        self.cluster_id = cluster_id  # type: str
        # The time when the restore job was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time  # type: long
        # The time when the restore job was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Indicates whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The list of the files that failed to be restored.
        self.error_file = error_file  # type: str
        # The error message that is returned for the restore job.
        self.error_message = error_message  # type: str
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the restore job. The value can be 1 to 255 characters in length.
        self.exclude = exclude  # type: str
        # The time when the restore job expires.
        self.expire_time = expire_time  # type: long
        self.failback_detail = failback_detail  # type: str
        # The paths to the files that are included in the restore job.
        self.include = include  # type: str
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the number of restored objects.
        self.items_done = items_done  # type: long
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the total number of objects in the data source.
        self.items_total = items_total  # type: long
        self.metering_bytes_done = metering_bytes_done  # type: long
        self.metering_bytes_total = metering_bytes_total  # type: long
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates whether Windows Volume Shadow Copy Service (VSS) is used to define a restoration path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot restore data from multiple directories.
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail  # type: DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail
        # The ID of the parent job.
        self.parent_id = parent_id  # type: str
        # The progress of the restore job. For example, 10000 indicates that the progress is 100%.
        self.progress = progress  # type: int
        self.report = report  # type: DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport
        # The ID of the restore job.
        self.restore_id = restore_id  # type: str
        # The type of the restore job.
        self.restore_type = restore_type  # type: str
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash  # type: str
        # The ID of the snapshot used for restoration.
        self.snapshot_id = snapshot_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str
        # The average speed at which data is backed up. Unit: KB/s.
        self.speed = speed  # type: long
        # The time when the restore job starts. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # The status of the restore job. Valid values:
        # 
        # *   **COMPLETE**: The restore job is completed.
        # *   **PARTIAL_COMPLETE**: The restore job is partially completed.
        # *   **FAILED**: The restore job has failed.
        self.status = status  # type: str
        self.storage_class = storage_class  # type: str
        # The name of the destination OSS bucket. This parameter is returned only for OSS buckets.
        self.target_bucket = target_bucket  # type: str
        # The ID of the destination client.
        self.target_client_id = target_client_id  # type: str
        # This parameter is returned only for NAS file systems. This parameter indicates the time when the file system was created.
        self.target_create_time = target_create_time  # type: long
        # The ID of the destination data source.
        self.target_data_source_id = target_data_source_id  # type: str
        # The ID of the destination NAS file system. This parameter is returned only for NAS file systems.
        self.target_file_system_id = target_file_system_id  # type: str
        # The ID of the destination instance for the restore job.
        self.target_instance_id = target_instance_id  # type: str
        # The name of the destination Tablestore instance.
        self.target_instance_name = target_instance_name  # type: str
        # The destination file path of the restore job.
        self.target_path = target_path  # type: str
        # The prefix of the objects that are restored. This parameter is returned only for OSS buckets.
        self.target_prefix = target_prefix  # type: str
        # The name of the destination table in the Tablestore instance.
        self.target_table_name = target_table_name  # type: str
        # The time when the Tablestore instance was backed up. The value is a UNIX timestamp. Unit: seconds.
        self.target_time = target_time  # type: long
        # The details about ECS instance backup.
        self.udm_detail = udm_detail  # type: str
        # The time when the restore job was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.report:
            self.report.validate()

    def to_map(self):
        _map = super(DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.error_file is not None:
            result['ErrorFile'] = self.error_file
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.failback_detail is not None:
            result['FailbackDetail'] = self.failback_detail
        if self.include is not None:
            result['Include'] = self.include
        if self.items_done is not None:
            result['ItemsDone'] = self.items_done
        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total
        if self.metering_bytes_done is not None:
            result['MeteringBytesDone'] = self.metering_bytes_done
        if self.metering_bytes_total is not None:
            result['MeteringBytesTotal'] = self.metering_bytes_total
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.report is not None:
            result['Report'] = self.report.to_map()
        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_client_id is not None:
            result['TargetClientId'] = self.target_client_id
        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time
        if self.target_data_source_id is not None:
            result['TargetDataSourceId'] = self.target_data_source_id
        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        if self.target_time is not None:
            result['TargetTime'] = self.target_time
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('ErrorFile') is not None:
            self.error_file = m.get('ErrorFile')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FailbackDetail') is not None:
            self.failback_detail = m.get('FailbackDetail')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')
        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')
        if m.get('MeteringBytesDone') is not None:
            self.metering_bytes_done = m.get('MeteringBytesDone')
        if m.get('MeteringBytesTotal') is not None:
            self.metering_bytes_total = m.get('MeteringBytesTotal')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Report') is not None:
            temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport()
            self.report = temp_model.from_map(m['Report'])
        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetClientId') is not None:
            self.target_client_id = m.get('TargetClientId')
        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')
        if m.get('TargetDataSourceId') is not None:
            self.target_data_source_id = m.get('TargetDataSourceId')
        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')
        if m.get('UdmDetail') is not None:
            self.udm_detail = m.get('UdmDetail')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeRestoreJobs2ResponseBodyRestoreJobs(TeaModel):
    def __init__(self, restore_job=None):
        self.restore_job = restore_job  # type: list[DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob]

    def validate(self):
        if self.restore_job:
            for k in self.restore_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRestoreJobs2ResponseBodyRestoreJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestoreJob'] = []
        if self.restore_job is not None:
            for k in self.restore_job:
                result['RestoreJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.restore_job = []
        if m.get('RestoreJob') is not None:
            for k in m.get('RestoreJob'):
                temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob()
                self.restore_job.append(temp_model.from_map(k))
        return self


class DescribeRestoreJobs2ResponseBody(TeaModel):
    def __init__(self, code=None, message=None, page_number=None, page_size=None, request_id=None, restore_jobs=None,
                 success=None, total_count=None):
        # The response status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The response message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message  # type: str
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The details about the restore jobs.
        self.restore_jobs = restore_jobs  # type: DescribeRestoreJobs2ResponseBodyRestoreJobs
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.restore_jobs:
            self.restore_jobs.validate()

    def to_map(self):
        _map = super(DescribeRestoreJobs2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_jobs is not None:
            result['RestoreJobs'] = self.restore_jobs.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreJobs') is not None:
            temp_model = DescribeRestoreJobs2ResponseBodyRestoreJobs()
            self.restore_jobs = temp_model.from_map(m['RestoreJobs'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRestoreJobs2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRestoreJobs2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRestoreJobs2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRestoreJobs2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskRequest(TeaModel):
    def __init__(self, resource_group_id=None, task_id=None, token=None):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the job.
        self.task_id = task_id  # type: str
        # The access token.
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(self, code=None, completed_time=None, created_time=None, description=None, message=None, name=None,
                 progress=None, request_id=None, result=None, success=None, updated_time=None):
        # HttpCode
        self.code = code  # type: str
        # The time when the job was completed. This value is a UNIX timestamp. Unit: seconds.
        self.completed_time = completed_time  # type: long
        # The time when the job was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The status of the job. Valid values:
        # 
        # *   **created**: The job is created.
        # *   **expired**: The job expires.
        # *   **completed**: The job is completed.
        # *   **cancelled**: The job is canceled.
        self.description = description  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The name of the job.
        self.name = name  # type: str
        # The progress of the job. Valid values: 0 to 100. Unit: percentage (%). If the job fails, the value -1 is returned.
        self.progress = progress  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the job.
        self.result = result  # type: str
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The time when the job was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUdmSnapshotsRequest(TeaModel):
    def __init__(self, disk_id=None, end_time=None, instance_id=None, job_id=None, snapshot_ids=None,
                 source_type=None, start_time=None, udm_region_id=None):
        # The ID of the disk.
        self.disk_id = disk_id  # type: str
        # The end of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The list of backup snapshots.
        self.snapshot_ids = snapshot_ids  # type: dict[str, any]
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        self.source_type = source_type  # type: str
        # The beginning of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # The ID of the region where the ECS instance resides.
        self.udm_region_id = udm_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUdmSnapshotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        return self


class DescribeUdmSnapshotsShrinkRequest(TeaModel):
    def __init__(self, disk_id=None, end_time=None, instance_id=None, job_id=None, snapshot_ids_shrink=None,
                 source_type=None, start_time=None, udm_region_id=None):
        # The ID of the disk.
        self.disk_id = disk_id  # type: str
        # The end of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The list of backup snapshots.
        self.snapshot_ids_shrink = snapshot_ids_shrink  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        self.source_type = source_type  # type: str
        # The beginning of the time range to query. The value must be a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # The ID of the region where the ECS instance resides.
        self.udm_region_id = udm_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUdmSnapshotsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.snapshot_ids_shrink is not None:
            result['SnapshotIds'] = self.snapshot_ids_shrink
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids_shrink = m.get('SnapshotIds')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')
        return self


class DescribeUdmSnapshotsResponseBodySnapshotsDetail(TeaModel):
    def __init__(self, consistent_level=None, contain_os_disk=None, disk_category=None, disk_dev_name=None,
                 disk_hbr_snapshot_id_with_device_map=None, disk_id_list=None, downgrade_reason=None, host_name=None,
                 instance_id_with_disk_id_list_map=None, instance_name=None, instance_type=None, instant_access=None, native_snapshot_id_list=None,
                 os_disk_id=None, os_name=None, os_name_en=None, os_type=None, performance_level=None, platform=None,
                 snapshot_group_id=None, system_disk=None, vm_name=None):
        # The consistency level.
        self.consistent_level = consistent_level  # type: str
        # Indicates whether the system disk is included.
        self.contain_os_disk = contain_os_disk  # type: bool
        # The type of the source disk.
        self.disk_category = disk_category  # type: str
        # The name of the disk.
        self.disk_dev_name = disk_dev_name  # type: str
        # The mapping between the device and the recovery point ID.
        self.disk_hbr_snapshot_id_with_device_map = disk_hbr_snapshot_id_with_device_map  # type: dict[str, any]
        # The IDs of the disks that are backed up at the recovery point.
        self.disk_id_list = disk_id_list  # type: list[str]
        # The reason for the downgrade.
        self.downgrade_reason = downgrade_reason  # type: str
        # The hostname.
        self.host_name = host_name  # type: str
        # The mapping between the instance ID and the disk ID.
        self.instance_id_with_disk_id_list_map = instance_id_with_disk_id_list_map  # type: dict[str, any]
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The specifications of the source instance.
        self.instance_type = instance_type  # type: str
        # Indicates whether the backup is created by the instant clone feature.
        self.instant_access = instant_access  # type: bool
        # The list of snapshot IDs, corresponding to DiskIdList.
        self.native_snapshot_id_list = native_snapshot_id_list  # type: list[str]
        # The ID of the system disk.
        self.os_disk_id = os_disk_id  # type: str
        # The name of the operating system.
        self.os_name = os_name  # type: str
        # The English name of the operating system.
        self.os_name_en = os_name_en  # type: str
        # The type of the operating system. Valid values: linux and windows.
        self.os_type = os_type  # type: str
        # The performance level of the source disk.
        self.performance_level = performance_level  # type: str
        # The system platform.
        self.platform = platform  # type: str
        # The ID of the snapshot group.
        self.snapshot_group_id = snapshot_group_id  # type: str
        # Indicates whether the disk is a system disk.
        self.system_disk = system_disk  # type: bool
        # The name of the instance.
        self.vm_name = vm_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUdmSnapshotsResponseBodySnapshotsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistent_level is not None:
            result['ConsistentLevel'] = self.consistent_level
        if self.contain_os_disk is not None:
            result['ContainOsDisk'] = self.contain_os_disk
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.disk_dev_name is not None:
            result['DiskDevName'] = self.disk_dev_name
        if self.disk_hbr_snapshot_id_with_device_map is not None:
            result['DiskHbrSnapshotIdWithDeviceMap'] = self.disk_hbr_snapshot_id_with_device_map
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.downgrade_reason is not None:
            result['DowngradeReason'] = self.downgrade_reason
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id_with_disk_id_list_map is not None:
            result['InstanceIdWithDiskIdListMap'] = self.instance_id_with_disk_id_list_map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access
        if self.native_snapshot_id_list is not None:
            result['NativeSnapshotIdList'] = self.native_snapshot_id_list
        if self.os_disk_id is not None:
            result['OsDiskId'] = self.os_disk_id
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.os_name_en is not None:
            result['OsNameEn'] = self.os_name_en
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.snapshot_group_id is not None:
            result['SnapshotGroupId'] = self.snapshot_group_id
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk
        if self.vm_name is not None:
            result['VmName'] = self.vm_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsistentLevel') is not None:
            self.consistent_level = m.get('ConsistentLevel')
        if m.get('ContainOsDisk') is not None:
            self.contain_os_disk = m.get('ContainOsDisk')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DiskDevName') is not None:
            self.disk_dev_name = m.get('DiskDevName')
        if m.get('DiskHbrSnapshotIdWithDeviceMap') is not None:
            self.disk_hbr_snapshot_id_with_device_map = m.get('DiskHbrSnapshotIdWithDeviceMap')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('DowngradeReason') is not None:
            self.downgrade_reason = m.get('DowngradeReason')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceIdWithDiskIdListMap') is not None:
            self.instance_id_with_disk_id_list_map = m.get('InstanceIdWithDiskIdListMap')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')
        if m.get('NativeSnapshotIdList') is not None:
            self.native_snapshot_id_list = m.get('NativeSnapshotIdList')
        if m.get('OsDiskId') is not None:
            self.os_disk_id = m.get('OsDiskId')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('OsNameEn') is not None:
            self.os_name_en = m.get('OsNameEn')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SnapshotGroupId') is not None:
            self.snapshot_group_id = m.get('SnapshotGroupId')
        if m.get('SystemDisk') is not None:
            self.system_disk = m.get('SystemDisk')
        if m.get('VmName') is not None:
            self.vm_name = m.get('VmName')
        return self


class DescribeUdmSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(self, actual_bytes=None, advanced_retention_type=None, backup_type=None, bytes_total=None,
                 complete_time=None, create_time=None, created_time=None, detail=None, disk_id=None, expire_time=None,
                 instance_id=None, job_id=None, native_snapshot_id=None, native_snapshot_info=None, parent_snapshot_hash=None,
                 prefix=None, real_snapshot_time=None, retention=None, snapshot_hash=None, snapshot_id=None,
                 source_type=None, start_time=None, status=None, updated_time=None):
        # The size of the backup snapshot. Unit: bytes.
        self.actual_bytes = actual_bytes  # type: str
        # The special retention type, which is valid only for special backups. Valid values:
        # 
        # *   **WEEKLY**: weekly backups
        # *   **MONTHLY**: monthly backups
        # *   **YEARLY**: yearly backups
        self.advanced_retention_type = advanced_retention_type  # type: str
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total  # type: long
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time  # type: long
        # The time when the backup snapshot was created.
        self.create_time = create_time  # type: long
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The snapshot details.
        self.detail = detail  # type: DescribeUdmSnapshotsResponseBodySnapshotsDetail
        # The ID of the cloud disk or local disk.
        self.disk_id = disk_id  # type: str
        # The expiration time of the backup.
        self.expire_time = expire_time  # type: long
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The ID of the backup snapshot.
        self.native_snapshot_id = native_snapshot_id  # type: str
        # The snapshot information.
        self.native_snapshot_info = native_snapshot_info  # type: str
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash  # type: str
        # The prefix of the backup snapshot.
        self.prefix = prefix  # type: str
        # The timestamp of the backup snapshot. The value is a UNIX timestamp. Unit: seconds.
        self.real_snapshot_time = real_snapshot_time  # type: long
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention  # type: long
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash  # type: str
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        self.source_type = source_type  # type: str
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status  # type: str
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super(DescribeUdmSnapshotsResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.native_snapshot_id is not None:
            result['NativeSnapshotId'] = self.native_snapshot_id
        if self.native_snapshot_info is not None:
            result['NativeSnapshotInfo'] = self.native_snapshot_info
        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.real_snapshot_time is not None:
            result['RealSnapshotTime'] = self.real_snapshot_time
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Detail') is not None:
            temp_model = DescribeUdmSnapshotsResponseBodySnapshotsDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('NativeSnapshotId') is not None:
            self.native_snapshot_id = m.get('NativeSnapshotId')
        if m.get('NativeSnapshotInfo') is not None:
            self.native_snapshot_info = m.get('NativeSnapshotInfo')
        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RealSnapshotTime') is not None:
            self.real_snapshot_time = m.get('RealSnapshotTime')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeUdmSnapshotsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, snapshots=None, success=None, total_count=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details about snapshots.
        self.snapshots = snapshots  # type: list[DescribeUdmSnapshotsResponseBodySnapshots]
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of backup snapshots.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUdmSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeUdmSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUdmSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUdmSnapshotsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUdmSnapshotsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUdmSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVaultReplicationRegionsRequest(TeaModel):
    def __init__(self, token=None, vault_id=None):
        # The access token.
        self.token = token  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultReplicationRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DescribeVaultReplicationRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultReplicationRegionsResponseBodyRegions, self).to_map()
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


class DescribeVaultReplicationRegionsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, regions=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The regions that support cross-region replication.
        self.regions = regions  # type: DescribeVaultReplicationRegionsResponseBodyRegions
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeVaultReplicationRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeVaultReplicationRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeVaultReplicationRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVaultReplicationRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVaultReplicationRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVaultReplicationRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVaultsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultsRequestTag, self).to_map()
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


class DescribeVaultsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, resource_group_id=None, status=None, tag=None,
                 vault_id=None, vault_region_id=None, vault_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tag = tag  # type: list[DescribeVaultsRequestTag]
        self.vault_id = vault_id  # type: str
        self.vault_region_id = vault_region_id  # type: str
        self.vault_type = vault_type  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVaultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_type is not None:
            result['VaultType'] = self.vault_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVaultsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')
        return self


class DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics(TeaModel):
    def __init__(self, common_nas=None, csg=None, ecs_file=None, ecs_hana=None, isilon=None, local_file=None,
                 local_vm=None, my_sql=None, nas=None, oracle=None, oss=None, ots=None, sql_server=None):
        self.common_nas = common_nas  # type: int
        self.csg = csg  # type: int
        self.ecs_file = ecs_file  # type: int
        self.ecs_hana = ecs_hana  # type: int
        self.isilon = isilon  # type: int
        self.local_file = local_file  # type: int
        self.local_vm = local_vm  # type: int
        self.my_sql = my_sql  # type: int
        self.nas = nas  # type: int
        self.oracle = oracle  # type: int
        self.oss = oss  # type: int
        self.ots = ots  # type: int
        self.sql_server = sql_server  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_nas is not None:
            result['CommonNas'] = self.common_nas
        if self.csg is not None:
            result['Csg'] = self.csg
        if self.ecs_file is not None:
            result['EcsFile'] = self.ecs_file
        if self.ecs_hana is not None:
            result['EcsHana'] = self.ecs_hana
        if self.isilon is not None:
            result['Isilon'] = self.isilon
        if self.local_file is not None:
            result['LocalFile'] = self.local_file
        if self.local_vm is not None:
            result['LocalVm'] = self.local_vm
        if self.my_sql is not None:
            result['MySql'] = self.my_sql
        if self.nas is not None:
            result['Nas'] = self.nas
        if self.oracle is not None:
            result['Oracle'] = self.oracle
        if self.oss is not None:
            result['Oss'] = self.oss
        if self.ots is not None:
            result['Ots'] = self.ots
        if self.sql_server is not None:
            result['SqlServer'] = self.sql_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonNas') is not None:
            self.common_nas = m.get('CommonNas')
        if m.get('Csg') is not None:
            self.csg = m.get('Csg')
        if m.get('EcsFile') is not None:
            self.ecs_file = m.get('EcsFile')
        if m.get('EcsHana') is not None:
            self.ecs_hana = m.get('EcsHana')
        if m.get('Isilon') is not None:
            self.isilon = m.get('Isilon')
        if m.get('LocalFile') is not None:
            self.local_file = m.get('LocalFile')
        if m.get('LocalVm') is not None:
            self.local_vm = m.get('LocalVm')
        if m.get('MySql') is not None:
            self.my_sql = m.get('MySql')
        if m.get('Nas') is not None:
            self.nas = m.get('Nas')
        if m.get('Oracle') is not None:
            self.oracle = m.get('Oracle')
        if m.get('Oss') is not None:
            self.oss = m.get('Oss')
        if m.get('Ots') is not None:
            self.ots = m.get('Ots')
        if m.get('SqlServer') is not None:
            self.sql_server = m.get('SqlServer')
        return self


class DescribeVaultsResponseBodyVaultsVaultReplicationProgress(TeaModel):
    def __init__(self, historical_replication_progress=None, new_replication_progress=None):
        self.historical_replication_progress = historical_replication_progress  # type: int
        self.new_replication_progress = new_replication_progress  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaultsVaultReplicationProgress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.historical_replication_progress is not None:
            result['HistoricalReplicationProgress'] = self.historical_replication_progress
        if self.new_replication_progress is not None:
            result['NewReplicationProgress'] = self.new_replication_progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HistoricalReplicationProgress') is not None:
            self.historical_replication_progress = m.get('HistoricalReplicationProgress')
        if m.get('NewReplicationProgress') is not None:
            self.new_replication_progress = m.get('NewReplicationProgress')
        return self


class DescribeVaultsResponseBodyVaultsVaultSourceTypes(TeaModel):
    def __init__(self, source_type=None):
        self.source_type = source_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaultsVaultSourceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeVaultsResponseBodyVaultsVaultTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaultsVaultTagsTag, self).to_map()
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


class DescribeVaultsResponseBodyVaultsVaultTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeVaultsResponseBodyVaultsVaultTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaultsVaultTags, self).to_map()
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
                temp_model = DescribeVaultsResponseBodyVaultsVaultTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeVaultsResponseBodyVaultsVaultTrialInfo(TeaModel):
    def __init__(self, keep_after_trial_expiration=None, trial_expire_time=None, trial_start_time=None,
                 trial_vault_release_time=None):
        self.keep_after_trial_expiration = keep_after_trial_expiration  # type: bool
        self.trial_expire_time = trial_expire_time  # type: long
        self.trial_start_time = trial_start_time  # type: long
        self.trial_vault_release_time = trial_vault_release_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaultsVaultTrialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_after_trial_expiration is not None:
            result['KeepAfterTrialExpiration'] = self.keep_after_trial_expiration
        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time
        if self.trial_start_time is not None:
            result['TrialStartTime'] = self.trial_start_time
        if self.trial_vault_release_time is not None:
            result['TrialVaultReleaseTime'] = self.trial_vault_release_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeepAfterTrialExpiration') is not None:
            self.keep_after_trial_expiration = m.get('KeepAfterTrialExpiration')
        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')
        if m.get('TrialStartTime') is not None:
            self.trial_start_time = m.get('TrialStartTime')
        if m.get('TrialVaultReleaseTime') is not None:
            self.trial_vault_release_time = m.get('TrialVaultReleaseTime')
        return self


class DescribeVaultsResponseBodyVaultsVault(TeaModel):
    def __init__(self, archive_bytes_done=None, archive_storage_size=None, backup_plan_statistics=None,
                 bucket_name=None, bytes_done=None, charge_type=None, charged_storage_size=None, compression_algorithm=None,
                 created_time=None, dedup=None, description=None, encrypt_type=None, index_available=None, index_level=None,
                 index_update_time=None, kms_key_id=None, latest_replication_time=None, redundancy_type=None, replication=None,
                 replication_progress=None, replication_source_region_id=None, replication_source_vault=None,
                 replication_source_vault_id=None, replication_target_region_id=None, resource_group_id=None, retention=None,
                 search_enabled=None, snapshot_count=None, source_types=None, status=None, storage_size=None, tags=None,
                 trial_info=None, updated_time=None, vault_id=None, vault_name=None, vault_region_id=None,
                 vault_status_message=None, vault_storage_class=None, vault_type=None, worm_enabled=None):
        self.archive_bytes_done = archive_bytes_done  # type: long
        self.archive_storage_size = archive_storage_size  # type: long
        self.backup_plan_statistics = backup_plan_statistics  # type: DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics
        self.bucket_name = bucket_name  # type: str
        self.bytes_done = bytes_done  # type: long
        self.charge_type = charge_type  # type: str
        self.charged_storage_size = charged_storage_size  # type: long
        self.compression_algorithm = compression_algorithm  # type: str
        self.created_time = created_time  # type: long
        self.dedup = dedup  # type: bool
        self.description = description  # type: str
        self.encrypt_type = encrypt_type  # type: str
        self.index_available = index_available  # type: bool
        self.index_level = index_level  # type: str
        self.index_update_time = index_update_time  # type: long
        self.kms_key_id = kms_key_id  # type: str
        self.latest_replication_time = latest_replication_time  # type: long
        self.redundancy_type = redundancy_type  # type: str
        self.replication = replication  # type: bool
        self.replication_progress = replication_progress  # type: DescribeVaultsResponseBodyVaultsVaultReplicationProgress
        self.replication_source_region_id = replication_source_region_id  # type: str
        self.replication_source_vault = replication_source_vault  # type: bool
        self.replication_source_vault_id = replication_source_vault_id  # type: str
        self.replication_target_region_id = replication_target_region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.retention = retention  # type: long
        self.search_enabled = search_enabled  # type: bool
        self.snapshot_count = snapshot_count  # type: long
        self.source_types = source_types  # type: DescribeVaultsResponseBodyVaultsVaultSourceTypes
        self.status = status  # type: str
        self.storage_size = storage_size  # type: long
        self.tags = tags  # type: DescribeVaultsResponseBodyVaultsVaultTags
        self.trial_info = trial_info  # type: DescribeVaultsResponseBodyVaultsVaultTrialInfo
        self.updated_time = updated_time  # type: long
        self.vault_id = vault_id  # type: str
        self.vault_name = vault_name  # type: str
        self.vault_region_id = vault_region_id  # type: str
        self.vault_status_message = vault_status_message  # type: str
        self.vault_storage_class = vault_storage_class  # type: str
        self.vault_type = vault_type  # type: str
        self.worm_enabled = worm_enabled  # type: bool

    def validate(self):
        if self.backup_plan_statistics:
            self.backup_plan_statistics.validate()
        if self.replication_progress:
            self.replication_progress.validate()
        if self.source_types:
            self.source_types.validate()
        if self.tags:
            self.tags.validate()
        if self.trial_info:
            self.trial_info.validate()

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaultsVault, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_bytes_done is not None:
            result['ArchiveBytesDone'] = self.archive_bytes_done
        if self.archive_storage_size is not None:
            result['ArchiveStorageSize'] = self.archive_storage_size
        if self.backup_plan_statistics is not None:
            result['BackupPlanStatistics'] = self.backup_plan_statistics.to_map()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.charged_storage_size is not None:
            result['ChargedStorageSize'] = self.charged_storage_size
        if self.compression_algorithm is not None:
            result['CompressionAlgorithm'] = self.compression_algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedup is not None:
            result['Dedup'] = self.dedup
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.index_available is not None:
            result['IndexAvailable'] = self.index_available
        if self.index_level is not None:
            result['IndexLevel'] = self.index_level
        if self.index_update_time is not None:
            result['IndexUpdateTime'] = self.index_update_time
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.latest_replication_time is not None:
            result['LatestReplicationTime'] = self.latest_replication_time
        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type
        if self.replication is not None:
            result['Replication'] = self.replication
        if self.replication_progress is not None:
            result['ReplicationProgress'] = self.replication_progress.to_map()
        if self.replication_source_region_id is not None:
            result['ReplicationSourceRegionId'] = self.replication_source_region_id
        if self.replication_source_vault is not None:
            result['ReplicationSourceVault'] = self.replication_source_vault
        if self.replication_source_vault_id is not None:
            result['ReplicationSourceVaultId'] = self.replication_source_vault_id
        if self.replication_target_region_id is not None:
            result['ReplicationTargetRegionId'] = self.replication_target_region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.search_enabled is not None:
            result['SearchEnabled'] = self.search_enabled
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.source_types is not None:
            result['SourceTypes'] = self.source_types.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.trial_info is not None:
            result['TrialInfo'] = self.trial_info.to_map()
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id
        if self.vault_status_message is not None:
            result['VaultStatusMessage'] = self.vault_status_message
        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class
        if self.vault_type is not None:
            result['VaultType'] = self.vault_type
        if self.worm_enabled is not None:
            result['WormEnabled'] = self.worm_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchiveBytesDone') is not None:
            self.archive_bytes_done = m.get('ArchiveBytesDone')
        if m.get('ArchiveStorageSize') is not None:
            self.archive_storage_size = m.get('ArchiveStorageSize')
        if m.get('BackupPlanStatistics') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics()
            self.backup_plan_statistics = temp_model.from_map(m['BackupPlanStatistics'])
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ChargedStorageSize') is not None:
            self.charged_storage_size = m.get('ChargedStorageSize')
        if m.get('CompressionAlgorithm') is not None:
            self.compression_algorithm = m.get('CompressionAlgorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Dedup') is not None:
            self.dedup = m.get('Dedup')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('IndexAvailable') is not None:
            self.index_available = m.get('IndexAvailable')
        if m.get('IndexLevel') is not None:
            self.index_level = m.get('IndexLevel')
        if m.get('IndexUpdateTime') is not None:
            self.index_update_time = m.get('IndexUpdateTime')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('LatestReplicationTime') is not None:
            self.latest_replication_time = m.get('LatestReplicationTime')
        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')
        if m.get('Replication') is not None:
            self.replication = m.get('Replication')
        if m.get('ReplicationProgress') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultReplicationProgress()
            self.replication_progress = temp_model.from_map(m['ReplicationProgress'])
        if m.get('ReplicationSourceRegionId') is not None:
            self.replication_source_region_id = m.get('ReplicationSourceRegionId')
        if m.get('ReplicationSourceVault') is not None:
            self.replication_source_vault = m.get('ReplicationSourceVault')
        if m.get('ReplicationSourceVaultId') is not None:
            self.replication_source_vault_id = m.get('ReplicationSourceVaultId')
        if m.get('ReplicationTargetRegionId') is not None:
            self.replication_target_region_id = m.get('ReplicationTargetRegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SearchEnabled') is not None:
            self.search_enabled = m.get('SearchEnabled')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('SourceTypes') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultSourceTypes()
            self.source_types = temp_model.from_map(m['SourceTypes'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('Tags') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TrialInfo') is not None:
            temp_model = DescribeVaultsResponseBodyVaultsVaultTrialInfo()
            self.trial_info = temp_model.from_map(m['TrialInfo'])
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')
        if m.get('VaultStatusMessage') is not None:
            self.vault_status_message = m.get('VaultStatusMessage')
        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')
        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')
        if m.get('WormEnabled') is not None:
            self.worm_enabled = m.get('WormEnabled')
        return self


class DescribeVaultsResponseBodyVaults(TeaModel):
    def __init__(self, vault=None):
        self.vault = vault  # type: list[DescribeVaultsResponseBodyVaultsVault]

    def validate(self):
        if self.vault:
            for k in self.vault:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVaultsResponseBodyVaults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vault'] = []
        if self.vault is not None:
            for k in self.vault:
                result['Vault'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vault = []
        if m.get('Vault') is not None:
            for k in m.get('Vault'):
                temp_model = DescribeVaultsResponseBodyVaultsVault()
                self.vault.append(temp_model.from_map(k))
        return self


class DescribeVaultsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, page_number=None, page_size=None, request_id=None, success=None,
                 total_count=None, vaults=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int
        self.vaults = vaults  # type: DescribeVaultsResponseBodyVaults

    def validate(self):
        if self.vaults:
            self.vaults.validate()

    def to_map(self):
        _map = super(DescribeVaultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vaults is not None:
            result['Vaults'] = self.vaults.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Vaults') is not None:
            temp_model = DescribeVaultsResponseBodyVaults()
            self.vaults = temp_model.from_map(m['Vaults'])
        return self


class DescribeVaultsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVaultsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVaultsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVaultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachNasFileSystemRequest(TeaModel):
    def __init__(self, create_time=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, file_system_id=None):
        # The time when the file system was created. The value must be a UNIX timestamp. Unit: seconds.
        self.create_time = create_time  # type: str
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachNasFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DetachNasFileSystemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachNasFileSystemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetachNasFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachNasFileSystemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachNasFileSystemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachNasFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableBackupPlanRequest(TeaModel):
    def __init__(self, plan_id=None, source_type=None, vault_id=None):
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: The system backs up data from Elastic Compute Service (ECS) instances.
        # *   **OSS**: The system backs up data from Object Storage Service (OSS) buckets.
        # *   **NAS**: The system backs up data from Apsara File Storage NAS file systems.
        self.source_type = source_type  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DisableBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: indicates that the request is successful.
        # *   false: indicates that the request fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableHanaBackupPlanRequest(TeaModel):
    def __init__(self, cluster_id=None, plan_id=None, resource_group_id=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableHanaBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class DisableHanaBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableHanaBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableHanaBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableHanaBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableHanaBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableBackupPlanRequest(TeaModel):
    def __init__(self, plan_id=None, source_type=None, vault_id=None):
        # The ID of the backup schedule.
        self.plan_id = plan_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: The system backs up data from Elastic Compute Service (ECS) instances.
        # *   **OSS**: The system backs up data from Object Storage Service (OSS) buckets.
        # *   **NAS**: The system backs up data from Apsara File Storage NAS file systems.
        self.source_type = source_type  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class EnableBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: indicates that the request is successful.
        # *   false: indicates that the request fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHanaBackupPlanRequest(TeaModel):
    def __init__(self, cluster_id=None, plan_id=None, resource_group_id=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableHanaBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class EnableHanaBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableHanaBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableHanaBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableHanaBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableHanaBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteBackupPlanRequest(TeaModel):
    def __init__(self, plan_id=None, rule_id=None, source_type=None, vault_id=None):
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The ID of the backup rule.
        self.rule_id = rule_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        self.source_type = source_type  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class ExecuteBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, job_id=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecutePolicyV2Request(TeaModel):
    def __init__(self, data_source_id=None, policy_id=None, rule_id=None, source_type=None):
        self.data_source_id = data_source_id  # type: str
        self.policy_id = policy_id  # type: str
        self.rule_id = rule_id  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecutePolicyV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ExecutePolicyV2ResponseBody(TeaModel):
    def __init__(self, code=None, job_id=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.job_id = job_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecutePolicyV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecutePolicyV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecutePolicyV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecutePolicyV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecutePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateRamPolicyRequest(TeaModel):
    def __init__(self, action_type=None, require_base_policy=None, resource_group_id=None, vault_id=None):
        # The type of the policy that you want to generate. Valid values:
        # 
        # *   custom: custom policy
        # *   system: system policy
        self.action_type = action_type  # type: str
        # Specifies whether to generate the policy based on an existing instance-specific rule. Valid values:
        # 
        # *   true
        # *   false
        self.require_base_policy = require_base_policy  # type: bool
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateRamPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.require_base_policy is not None:
            result['RequireBasePolicy'] = self.require_base_policy
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('RequireBasePolicy') is not None:
            self.require_base_policy = m.get('RequireBasePolicy')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class GenerateRamPolicyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, policy_document=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The content of the policy.
        self.policy_document = policy_document  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateRamPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateRamPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateRamPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateRamPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateRamPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTempFileDownloadLinkRequest(TeaModel):
    def __init__(self, temp_file_key=None):
        # The key that is used to download a file.
        self.temp_file_key = temp_file_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTempFileDownloadLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temp_file_key is not None:
            result['TempFileKey'] = self.temp_file_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TempFileKey') is not None:
            self.temp_file_key = m.get('TempFileKey')
        return self


class GetTempFileDownloadLinkResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, url=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success  # type: bool
        # The download URL of the file.
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTempFileDownloadLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetTempFileDownloadLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTempFileDownloadLinkResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTempFileDownloadLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTempFileDownloadLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallBackupClientsRequest(TeaModel):
    def __init__(self, cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None,
                 instance_ids=None):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The IDs of the ECS instances. You can specify up to 20 IDs.
        self.instance_ids = instance_ids  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallBackupClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class InstallBackupClientsShrinkRequest(TeaModel):
    def __init__(self, cross_account_role_name=None, cross_account_type=None, cross_account_user_id=None,
                 instance_ids_shrink=None):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The IDs of the ECS instances. You can specify up to 20 IDs.
        self.instance_ids_shrink = instance_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallBackupClientsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class InstallBackupClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(self, error_code=None, instance_id=None, valid_instance=None):
        # The error code that is returned. Valid values:
        # 
        # *   If the value is empty, the call is successful.
        # *   **InstanceNotExists**: The ECS instance does not exist.
        # *   **InstanceNotRunning**: The ECS instance is not running.
        # *   **CloudAssistNotRunningOnInstance**: Cloud Assistant is unavailable.
        self.error_code = error_code  # type: str
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether an HBR client can be installed on the ECS instance. Valid values:
        # 
        # *   true: An HBR client can be installed on the ECS instance.
        # *   false: An HBR client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallBackupClientsResponseBodyInstanceStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class InstallBackupClientsResponseBody(TeaModel):
    def __init__(self, code=None, instance_statuses=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The status of the ECS instance.
        self.instance_statuses = instance_statuses  # type: list[InstallBackupClientsResponseBodyInstanceStatuses]
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        if self.instance_statuses:
            for k in self.instance_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InstallBackupClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k in self.instance_statuses:
                result['InstanceStatuses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k in m.get('InstanceStatuses'):
                temp_model = InstallBackupClientsResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class InstallBackupClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InstallBackupClientsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallBackupClientsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InstallBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenHbrServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenHbrServiceResponseBody, self).to_map()
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


class OpenHbrServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenHbrServiceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenHbrServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenHbrServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchHistoricalSnapshotsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, order=None, query=None, sort_by=None, source_type=None):
        # The maximum number of rows that you want the current query to return. To query only the number of matched rows without the need to return specific data, you can set the Limit parameter to `0`. Then, the operation returns only the number of matched rows.
        self.limit = limit  # type: int
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        # The query conditions. Example:
        # 
        #     [
        #       {
        #         "field": "VaultId",
        #         "value": "v-0003rf9m*****qx5",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "InstanceId",
        #         "value": "i-bp1i20zq2*****e9368m",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "PlanId",
        #         "value": "plan-0005vk*****gkd1iu4f",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "CompleteTime",
        #         "value": 1626769913,
        #         "operation": "GREATER_THAN_OR_EQUAL"
        #       }
        #     ]
        # 
        # *   The following fields are supported:
        # 
        #     *   VaultId: specifies the ID of the backup vault. This field is required.
        #     *   InstanceId: specifies the ID of the ECS instance. If the SourceType parameter is set to ECS_FILE, this field is required.
        #     *   Bucket: specifies the ID of the OSS bucket. If the SourceType parameter is set to OSS, this field is required.
        #     *   FileSystemId: specifies the ID of the NAS file system. If the SourceType parameter is set to NAS, this field is required.
        #     *   CreateTime: specifies the time when the NAS file system was created. If the SourceType parameter is set to NAS, this field is required.
        #     *   CompleteTime: specifies the time when the backup snapshot was completed.
        #     *   PlanId: the ID of a backup plan.
        # 
        # *   The following operations are supported:
        # 
        #     *   MATCH_TERM: exact match.
        #     *   GREATER_THAN: greater than.
        #     *   GREATER_THAN_OR_EQUAL: greater than or equal to.
        #     *   LESS_THAN: less than.
        #     *   LESS_THAN_OR_EQUAL: less than or equal to.
        #     *   BETWEEN: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        #     *   IN: specifies an array as a collection. The results must fall within the collection.
        #     *   NOT_IN: specifies an array as a collection. The results cannot fall within the collection.
        self.query = query  # type: list[any]
        self.sort_by = sort_by  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchHistoricalSnapshotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.query is not None:
            result['Query'] = self.query
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SearchHistoricalSnapshotsShrinkRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, order=None, query_shrink=None, sort_by=None, source_type=None):
        # The maximum number of rows that you want the current query to return. To query only the number of matched rows without the need to return specific data, you can set the Limit parameter to `0`. Then, the operation returns only the number of matched rows.
        self.limit = limit  # type: int
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        # The query conditions. Example:
        # 
        #     [
        #       {
        #         "field": "VaultId",
        #         "value": "v-0003rf9m*****qx5",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "InstanceId",
        #         "value": "i-bp1i20zq2*****e9368m",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "PlanId",
        #         "value": "plan-0005vk*****gkd1iu4f",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "CompleteTime",
        #         "value": 1626769913,
        #         "operation": "GREATER_THAN_OR_EQUAL"
        #       }
        #     ]
        # 
        # *   The following fields are supported:
        # 
        #     *   VaultId: specifies the ID of the backup vault. This field is required.
        #     *   InstanceId: specifies the ID of the ECS instance. If the SourceType parameter is set to ECS_FILE, this field is required.
        #     *   Bucket: specifies the ID of the OSS bucket. If the SourceType parameter is set to OSS, this field is required.
        #     *   FileSystemId: specifies the ID of the NAS file system. If the SourceType parameter is set to NAS, this field is required.
        #     *   CreateTime: specifies the time when the NAS file system was created. If the SourceType parameter is set to NAS, this field is required.
        #     *   CompleteTime: specifies the time when the backup snapshot was completed.
        #     *   PlanId: the ID of a backup plan.
        # 
        # *   The following operations are supported:
        # 
        #     *   MATCH_TERM: exact match.
        #     *   GREATER_THAN: greater than.
        #     *   GREATER_THAN_OR_EQUAL: greater than or equal to.
        #     *   LESS_THAN: less than.
        #     *   LESS_THAN_OR_EQUAL: less than or equal to.
        #     *   BETWEEN: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        #     *   IN: specifies an array as a collection. The results must fall within the collection.
        #     *   NOT_IN: specifies an array as a collection. The results cannot fall within the collection.
        self.query_shrink = query_shrink  # type: str
        self.sort_by = sort_by  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchHistoricalSnapshotsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths(TeaModel):
    def __init__(self, path=None):
        self.path = path  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot(TeaModel):
    def __init__(self, actual_bytes=None, actual_items=None, archive_time=None, backup_type=None, bucket=None,
                 bytes_done=None, bytes_total=None, client_id=None, complete_time=None, create_time=None, created_time=None,
                 error_file=None, exclude=None, expire_time=None, file_system_id=None, include=None, instance_id=None,
                 instance_name=None, items_done=None, items_total=None, job_id=None, parent_snapshot_hash=None, path=None,
                 paths=None, prefix=None, range_end=None, range_start=None, retention=None, snapshot_hash=None,
                 snapshot_id=None, source_parent_snapshot_hash=None, source_snapshot_hash=None, source_type=None,
                 start_time=None, status=None, storage_class=None, table_name=None, updated_time=None, use_common_nas=None,
                 vault_id=None):
        # The actual data amount of backup snapshots after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes  # type: long
        # The actual number of backup snapshots.
        # 
        # >  This parameter is available only for file backup.
        self.actual_items = actual_items  # type: long
        self.archive_time = archive_time  # type: long
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the name of the OSS bucket.
        self.bucket = bucket  # type: str
        # The actual amount of data that is generated by incremental backups. Unit: bytes.
        self.bytes_done = bytes_done  # type: long
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total  # type: long
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the HBR client.
        self.client_id = client_id  # type: str
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time  # type: long
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the time when the file system was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time  # type: long
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time  # type: long
        # The files that record the information about backup failures, including the information about partially completed backups.
        self.error_file = error_file  # type: str
        self.exclude = exclude  # type: str
        # The time when the snapshot expired. The value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time  # type: long
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id  # type: str
        self.include = include  # type: str
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the Tablestore instance.
        self.instance_name = instance_name  # type: str
        # The number of objects that are backed up.
        # 
        # >  This parameter is available only for file backup.
        self.items_done = items_done  # type: long
        # The total number of objects in the data source.
        # 
        # >  This parameter is available only for file backup.
        self.items_total = items_total  # type: long
        # The ID of the backup job.
        self.job_id = job_id  # type: str
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash  # type: str
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the path to the files that are backed up.
        self.path = path  # type: str
        # The source paths.
        self.paths = paths  # type: SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the prefix of objects that are backed up.
        self.prefix = prefix  # type: str
        # The time when the backup job ended. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_end = range_end  # type: long
        # The time when the backup job started. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_start = range_start  # type: long
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention  # type: long
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash  # type: str
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id  # type: str
        self.source_parent_snapshot_hash = source_parent_snapshot_hash  # type: str
        self.source_snapshot_hash = source_snapshot_hash  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for ECS files
        # *   **OSS**: backup snapshots for OSS buckets
        # *   **NAS**: backup snapshots for NAS file systems
        self.source_type = source_type  # type: str
        # The time when the backup snapshot started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status  # type: str
        self.storage_class = storage_class  # type: str
        # The name of a table in the Tablestore instance.
        self.table_name = table_name  # type: str
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time  # type: long
        self.use_common_nas = use_common_nas  # type: bool
        # The ID of the backup vault that stores the backup snapshot.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.paths:
            self.paths.validate()

    def to_map(self):
        _map = super(SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items
        if self.archive_time is not None:
            result['ArchiveTime'] = self.archive_time
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.error_file is not None:
            result['ErrorFile'] = self.error_file
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.include is not None:
            result['Include'] = self.include
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.items_done is not None:
            result['ItemsDone'] = self.items_done
        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash
        if self.path is not None:
            result['Path'] = self.path
        if self.paths is not None:
            result['Paths'] = self.paths.to_map()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.range_end is not None:
            result['RangeEnd'] = self.range_end
        if self.range_start is not None:
            result['RangeStart'] = self.range_start
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.source_parent_snapshot_hash is not None:
            result['SourceParentSnapshotHash'] = self.source_parent_snapshot_hash
        if self.source_snapshot_hash is not None:
            result['SourceSnapshotHash'] = self.source_snapshot_hash
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.use_common_nas is not None:
            result['UseCommonNas'] = self.use_common_nas
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')
        if m.get('ArchiveTime') is not None:
            self.archive_time = m.get('ArchiveTime')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ErrorFile') is not None:
            self.error_file = m.get('ErrorFile')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')
        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Paths') is not None:
            temp_model = SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths()
            self.paths = temp_model.from_map(m['Paths'])
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RangeEnd') is not None:
            self.range_end = m.get('RangeEnd')
        if m.get('RangeStart') is not None:
            self.range_start = m.get('RangeStart')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SourceParentSnapshotHash') is not None:
            self.source_parent_snapshot_hash = m.get('SourceParentSnapshotHash')
        if m.get('SourceSnapshotHash') is not None:
            self.source_snapshot_hash = m.get('SourceSnapshotHash')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UseCommonNas') is not None:
            self.use_common_nas = m.get('UseCommonNas')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class SearchHistoricalSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot]

    def validate(self):
        if self.snapshot:
            for k in self.snapshot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchHistoricalSnapshotsResponseBodySnapshots, self).to_map()
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
                temp_model = SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k))
        return self


class SearchHistoricalSnapshotsResponseBody(TeaModel):
    def __init__(self, code=None, limit=None, message=None, next_token=None, request_id=None, snapshots=None,
                 success=None, total_count=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The number of historical backup snapshots that are displayed on the current page.
        self.limit = limit  # type: int
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The historical backup snapshots.
        self.snapshots = snapshots  # type: SearchHistoricalSnapshotsResponseBodySnapshots
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The total number of returned backup snapshots that meet the specified conditions.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super(SearchHistoricalSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshots') is not None:
            temp_model = SearchHistoricalSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchHistoricalSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchHistoricalSnapshotsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchHistoricalSnapshotsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchHistoricalSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartHanaDatabaseAsyncRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartHanaDatabaseAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class StartHanaDatabaseAsyncResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the job that is used to initialize the backup vault. You can call the DescribeTask operation to query the status of the job.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartHanaDatabaseAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartHanaDatabaseAsyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartHanaDatabaseAsyncResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartHanaDatabaseAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartHanaDatabaseAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopHanaDatabaseAsyncRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopHanaDatabaseAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class StopHanaDatabaseAsyncResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopHanaDatabaseAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopHanaDatabaseAsyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopHanaDatabaseAsyncResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopHanaDatabaseAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopHanaDatabaseAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallBackupClientsRequest(TeaModel):
    def __init__(self, client_ids=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, instance_ids=None):
        # The ID of the backup client. The sum of the number of backup client IDs and the number of ECS instance IDs cannot exceed 20. Otherwise, an error occurs.
        self.client_ids = client_ids  # type: dict[str, any]
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The ID of the ECS instance. You can specify up to 20 IDs.
        self.instance_ids = instance_ids  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallBackupClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class UninstallBackupClientsShrinkRequest(TeaModel):
    def __init__(self, client_ids_shrink=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, instance_ids_shrink=None):
        # The ID of the backup client. The sum of the number of backup client IDs and the number of ECS instance IDs cannot exceed 20. Otherwise, an error occurs.
        self.client_ids_shrink = client_ids_shrink  # type: str
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up and restored within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up and restored within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up and restored across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up and restore data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The ID of the ECS instance. You can specify up to 20 IDs.
        self.instance_ids_shrink = instance_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallBackupClientsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class UninstallBackupClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(self, error_code=None, instance_id=None, valid_instance=None):
        # The error code. Valid values:
        # 
        # *   If the value is empty, the request is successful.
        # *   **InstanceNotExists**: The ECS instance does not exist.
        # *   **InstanceNotRunning**: The ECS instance is not running.
        # *   **CloudAssistNotRunningOnInstance**: Cloud Assistant is unavailable.
        self.error_code = error_code  # type: str
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether a backup client can be installed on the ECS instance.
        # 
        # *   true: A backup client can be installed on the ECS instance.
        # *   false: A backup client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallBackupClientsResponseBodyInstanceStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class UninstallBackupClientsResponseBody(TeaModel):
    def __init__(self, code=None, instance_statuses=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The status of the ECS instance.
        self.instance_statuses = instance_statuses  # type: list[UninstallBackupClientsResponseBodyInstanceStatuses]
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        if self.instance_statuses:
            for k in self.instance_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UninstallBackupClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k in self.instance_statuses:
                result['InstanceStatuses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k in m.get('InstanceStatuses'):
                temp_model = UninstallBackupClientsResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UninstallBackupClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UninstallBackupClientsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallBackupClientsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UninstallBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallClientRequest(TeaModel):
    def __init__(self, client_id=None, resource_group_id=None, vault_id=None):
        # The ID of the HBR client.
        self.client_id = client_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UninstallClientResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallClientResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UninstallClientResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UninstallClientResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallClientResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UninstallClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBackupPlanRequestRule(TeaModel):
    def __init__(self, backup_type=None, destination_region_id=None, destination_retention=None, disabled=None,
                 do_copy=None, retention=None, rule_name=None, schedule=None):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # The ID of the region where the remote backup vault resides.
        self.destination_region_id = destination_region_id  # type: str
        # The retention period of the backup data. Unit: days.
        self.destination_retention = destination_retention  # type: long
        # Specifies whether to disable the policy.
        self.disabled = disabled  # type: bool
        # Specifies whether to enable remote replication.
        self.do_copy = do_copy  # type: bool
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # The name of the backup policy.
        self.rule_name = rule_name  # type: str
        # The backup policy. Format: I|{startTime}|{interval}. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, I|1631685600|P1D specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds. interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBackupPlanRequestRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateBackupPlanRequest(TeaModel):
    def __init__(self, change_list_path=None, detail=None, exclude=None, include=None, keep_latest_snapshots=None,
                 options=None, ots_detail=None, path=None, plan_id=None, plan_name=None, prefix=None, retention=None,
                 rule=None, schedule=None, source_type=None, speed_limit=None, update_paths=None, vault_id=None):
        # The configurations of the incremental file synchronization. This parameter is required for data synchronization only.
        self.change_list_path = change_list_path  # type: str
        # The details about ECS instance backup. The value is a JSON string.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are enhanced SSDs (ESSDs).
        # *   appConsistent: specifies whether to enable application consistency. If you set this parameter to true, you must also specify the preScriptPath and postScriptPath parameters.
        # *   preScriptPath: the path to the pre-freeze scripts.
        # *   postScriptPath: the path to the post-thaw scripts.
        self.detail = detail  # type: dict[str, any]
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value must be 1 to 255 characters in length.
        self.include = include  # type: str
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a source path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail  # type: OtsDetail
        # The source paths.
        self.path = path  # type: list[str]
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The name of the backup plan.
        self.plan_name = plan_name  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to back up. After a prefix is specified, only objects whose names start with the prefix are backed up.
        self.prefix = prefix  # type: str
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # The rule of the backup plan.
        self.rule = rule  # type: list[UpdateBackupPlanRequestRule]
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the `{startTime}` parameter and the subsequent backup jobs at an interval that is specified in the `{interval}` parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the throttling rules. To ensure business continuity, you can limit the bandwidth that is used for file backup during peak hours. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit  # type: str
        # Specifies whether to update the source path if the backup source is empty. Valid values:
        # 
        # *   true: The system replaces the original source path with the specified source path.
        # *   false: The system does not update the original source path. The system backs up data based on the source path that you specified when you created the backup plan.
        self.update_paths = update_paths  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.update_paths is not None:
            result['UpdatePaths'] = self.update_paths
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            temp_model = OtsDetail()
            self.ots_detail = temp_model.from_map(m['OtsDetail'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = UpdateBackupPlanRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UpdatePaths') is not None:
            self.update_paths = m.get('UpdatePaths')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateBackupPlanShrinkRequestRule(TeaModel):
    def __init__(self, backup_type=None, destination_region_id=None, destination_retention=None, disabled=None,
                 do_copy=None, retention=None, rule_name=None, schedule=None):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # The ID of the region where the remote backup vault resides.
        self.destination_region_id = destination_region_id  # type: str
        # The retention period of the backup data. Unit: days.
        self.destination_retention = destination_retention  # type: long
        # Specifies whether to disable the policy.
        self.disabled = disabled  # type: bool
        # Specifies whether to enable remote replication.
        self.do_copy = do_copy  # type: bool
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # The name of the backup policy.
        self.rule_name = rule_name  # type: str
        # The backup policy. Format: I|{startTime}|{interval}. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, I|1631685600|P1D specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds. interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBackupPlanShrinkRequestRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateBackupPlanShrinkRequest(TeaModel):
    def __init__(self, change_list_path=None, detail_shrink=None, exclude=None, include=None,
                 keep_latest_snapshots=None, options=None, ots_detail_shrink=None, path=None, plan_id=None, plan_name=None, prefix=None,
                 retention=None, rule=None, schedule=None, source_type=None, speed_limit=None, update_paths=None,
                 vault_id=None):
        # The configurations of the incremental file synchronization. This parameter is required for data synchronization only.
        self.change_list_path = change_list_path  # type: str
        # The details about ECS instance backup. The value is a JSON string.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are enhanced SSDs (ESSDs).
        # *   appConsistent: specifies whether to enable application consistency. If you set this parameter to true, you must also specify the preScriptPath and postScriptPath parameters.
        # *   preScriptPath: the path to the pre-freeze scripts.
        # *   postScriptPath: the path to the post-thaw scripts.
        self.detail_shrink = detail_shrink  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value must be 1 to 255 characters in length.
        self.include = include  # type: str
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a source path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options  # type: str
        # The details about the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink  # type: str
        # The source paths.
        self.path = path  # type: list[str]
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The name of the backup plan.
        self.plan_name = plan_name  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to back up. After a prefix is specified, only objects whose names start with the prefix are backed up.
        self.prefix = prefix  # type: str
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # The rule of the backup plan.
        self.rule = rule  # type: list[UpdateBackupPlanShrinkRequestRule]
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the `{startTime}` parameter and the subsequent backup jobs at an interval that is specified in the `{interval}` parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type  # type: str
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the throttling rules. To ensure business continuity, you can limit the bandwidth that is used for file backup during peak hours. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit  # type: str
        # Specifies whether to update the source path if the backup source is empty. Valid values:
        # 
        # *   true: The system replaces the original source path with the specified source path.
        # *   false: The system does not update the original source path. The system backs up data based on the source path that you specified when you created the backup plan.
        self.update_paths = update_paths  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateBackupPlanShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path
        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.include is not None:
            result['Include'] = self.include
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.options is not None:
            result['Options'] = self.options
        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink
        if self.path is not None:
            result['Path'] = self.path
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.retention is not None:
            result['Retention'] = self.retention
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.update_paths is not None:
            result['UpdatePaths'] = self.update_paths
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')
        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Include') is not None:
            self.include = m.get('Include')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = UpdateBackupPlanShrinkRequestRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('UpdatePaths') is not None:
            self.update_paths = m.get('UpdatePaths')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClientSettingsRequest(TeaModel):
    def __init__(self, alert_on_partial_complete=None, client_id=None, data_network_type=None,
                 data_proxy_setting=None, max_cpu_core=None, max_memory=None, max_worker=None, proxy_host=None, proxy_password=None,
                 proxy_port=None, proxy_user=None, resource_group_id=None, use_https=None, vault_id=None):
        # Specifies whether to generate alert for partially completed jobs. This parameter is valid only for on-premises file backup and ECS file backup.
        self.alert_on_partial_complete = alert_on_partial_complete  # type: bool
        # The ID of the HBR client.
        self.client_id = client_id  # type: str
        # The type of the endpoint on the data plane. Valid values:
        # 
        # *   **PUBLIC**: Internet
        # *   **VPC**: virtual private cloud (VPC)
        # *   **CLASSIC**: classic network
        self.data_network_type = data_network_type  # type: str
        # The proxy configuration on the data plane. Valid values:
        # 
        # *   **DISABLE**: No proxy is used.
        # *   **USE_CONTROL_PROXY** (default): The configuration is the same as that on the control plane.
        # *   **CUSTOM**: The configuration is customized (HTTP).
        self.data_proxy_setting = data_proxy_setting  # type: str
        # The number of CPU cores used by a single backup job. The value 0 indicates that the number is unlimited.
        self.max_cpu_core = max_cpu_core  # type: int
        # The maximum memory that can be used by the client. Unit: bytes. Only V2.13.0 and later are supported.
        self.max_memory = max_memory  # type: long
        # The number of concurrent backup jobs. The value 0 indicates that the number is unlimited.
        self.max_worker = max_worker  # type: int
        # The custom host IP address of the proxy server on the data plane.
        self.proxy_host = proxy_host  # type: str
        # The custom password of the proxy server on the data plane.
        self.proxy_password = proxy_password  # type: str
        # The custom host port of the proxy server on the data plane.
        self.proxy_port = proxy_port  # type: int
        # The custom username of the proxy server on the data plane.
        self.proxy_user = proxy_user  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # Specifies whether to transmit the data on the data plane over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https  # type: bool
        # The ID of the backup vault. This parameter is required for the old HBR client.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClientSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_on_partial_complete is not None:
            result['AlertOnPartialComplete'] = self.alert_on_partial_complete
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.data_network_type is not None:
            result['DataNetworkType'] = self.data_network_type
        if self.data_proxy_setting is not None:
            result['DataProxySetting'] = self.data_proxy_setting
        if self.max_cpu_core is not None:
            result['MaxCpuCore'] = self.max_cpu_core
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.max_worker is not None:
            result['MaxWorker'] = self.max_worker
        if self.proxy_host is not None:
            result['ProxyHost'] = self.proxy_host
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_port is not None:
            result['ProxyPort'] = self.proxy_port
        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.use_https is not None:
            result['UseHttps'] = self.use_https
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertOnPartialComplete') is not None:
            self.alert_on_partial_complete = m.get('AlertOnPartialComplete')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DataNetworkType') is not None:
            self.data_network_type = m.get('DataNetworkType')
        if m.get('DataProxySetting') is not None:
            self.data_proxy_setting = m.get('DataProxySetting')
        if m.get('MaxCpuCore') is not None:
            self.max_cpu_core = m.get('MaxCpuCore')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MaxWorker') is not None:
            self.max_worker = m.get('MaxWorker')
        if m.get('ProxyHost') is not None:
            self.proxy_host = m.get('ProxyHost')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')
        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateClientSettingsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClientSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClientSettingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateClientSettingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClientSettingsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateClientSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContainerClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, description=None, name=None, network_type=None, renew_token=None):
        self.cluster_id = cluster_id  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.network_type = network_type  # type: str
        self.renew_token = renew_token  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.renew_token is not None:
            result['RenewToken'] = self.renew_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RenewToken') is not None:
            self.renew_token = m.get('RenewToken')
        return self


class UpdateContainerClusterResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, token=None, token_updated=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.token = token  # type: str
        self.token_updated = token_updated  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        if self.token_updated is not None:
            result['TokenUpdated'] = self.token_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenUpdated') is not None:
            self.token_updated = m.get('TokenUpdated')
        return self


class UpdateContainerClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateContainerClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateContainerClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateContainerClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaBackupPlanRequest(TeaModel):
    def __init__(self, backup_prefix=None, cluster_id=None, plan_id=None, plan_name=None, resource_group_id=None,
                 schedule=None, vault_id=None):
        # The backup prefix.
        self.backup_prefix = backup_prefix  # type: str
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the backup plan.
        self.plan_id = plan_id  # type: str
        # The name of the backup plan.
        self.plan_name = plan_name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of 1 hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaBackupPlanResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHanaBackupPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHanaBackupPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaBackupSettingRequest(TeaModel):
    def __init__(self, catalog_backup_parameter_file=None, catalog_backup_using_backint=None, cluster_id=None,
                 data_backup_parameter_file=None, database_name=None, enable_auto_log_backup=None, log_backup_parameter_file=None,
                 log_backup_timeout=None, log_backup_using_backint=None, vault_id=None):
        # The configuration file for catalog backup.
        self.catalog_backup_parameter_file = catalog_backup_parameter_file  # type: str
        # Specifies whether to use Backint to back up catalogs. Valid values:
        # 
        # *   true: Backint is used to back up catalogs.
        # *   false: Backint is not used to back up catalogs.
        self.catalog_backup_using_backint = catalog_backup_using_backint  # type: bool
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The configuration file for data backup.
        self.data_backup_parameter_file = data_backup_parameter_file  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # Specifies whether to enable automatic log backup. Valid values:
        # 
        # *   **true**: enables automatic log backup.
        # *   **false**: disables automatic log backup.
        self.enable_auto_log_backup = enable_auto_log_backup  # type: bool
        # The configuration file for log backup.
        self.log_backup_parameter_file = log_backup_parameter_file  # type: str
        # The interval at which logs are backed up. Unit: seconds.
        self.log_backup_timeout = log_backup_timeout  # type: long
        # Specifies whether to use Backint to back up logs. Valid values:
        # 
        # *   true: Backint is used to back up logs.
        # *   false: Backint is not used to back up logs.
        self.log_backup_using_backint = log_backup_using_backint  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaBackupSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_backup_parameter_file is not None:
            result['CatalogBackupParameterFile'] = self.catalog_backup_parameter_file
        if self.catalog_backup_using_backint is not None:
            result['CatalogBackupUsingBackint'] = self.catalog_backup_using_backint
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_backup_parameter_file is not None:
            result['DataBackupParameterFile'] = self.data_backup_parameter_file
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.enable_auto_log_backup is not None:
            result['EnableAutoLogBackup'] = self.enable_auto_log_backup
        if self.log_backup_parameter_file is not None:
            result['LogBackupParameterFile'] = self.log_backup_parameter_file
        if self.log_backup_timeout is not None:
            result['LogBackupTimeout'] = self.log_backup_timeout
        if self.log_backup_using_backint is not None:
            result['LogBackupUsingBackint'] = self.log_backup_using_backint
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CatalogBackupParameterFile') is not None:
            self.catalog_backup_parameter_file = m.get('CatalogBackupParameterFile')
        if m.get('CatalogBackupUsingBackint') is not None:
            self.catalog_backup_using_backint = m.get('CatalogBackupUsingBackint')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataBackupParameterFile') is not None:
            self.data_backup_parameter_file = m.get('DataBackupParameterFile')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EnableAutoLogBackup') is not None:
            self.enable_auto_log_backup = m.get('EnableAutoLogBackup')
        if m.get('LogBackupParameterFile') is not None:
            self.log_backup_parameter_file = m.get('LogBackupParameterFile')
        if m.get('LogBackupTimeout') is not None:
            self.log_backup_timeout = m.get('LogBackupTimeout')
        if m.get('LogBackupUsingBackint') is not None:
            self.log_backup_using_backint = m.get('LogBackupUsingBackint')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaBackupSettingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaBackupSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaBackupSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHanaBackupSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHanaBackupSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaBackupSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaInstanceRequest(TeaModel):
    def __init__(self, alert_setting=None, cluster_id=None, hana_name=None, host=None, instance_number=None,
                 password=None, resource_group_id=None, use_ssl=None, user_name=None, validate_certificate=None,
                 vault_id=None):
        # The alert settings. Valid value: INHERITED, which indicates that the backup client sends alert notifications in the same way as the backup vault.
        self.alert_setting = alert_setting  # type: str
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the SAP HANA instance.
        self.hana_name = hana_name  # type: str
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host  # type: str
        # The instance number of the SAP HANA system.
        self.instance_number = instance_number  # type: int
        # The password that is used to connect with the SAP HANA database.
        self.password = password  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # Specifies whether to connect with the SAP HANA database over Secure Sockets Layer (SSL). Valid values:
        # 
        # *   true: The SAP HANA database is connected over SSL.
        # *   false: The SAP HANA database is not connected over SSL.
        self.use_ssl = use_ssl  # type: bool
        # The username of the SYSTEMDB database.
        self.user_name = user_name  # type: str
        # Specifies whether to verify the SSL certificate of the SAP HANA database. Valid values:
        # 
        # *   true: The SSL certificate of the SAP HANA instance is verified.
        # *   false: The SSL certificate of the SAP HANA instance is not verified.
        self.validate_certificate = validate_certificate  # type: bool
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.hana_name is not None:
            result['HanaName'] = self.hana_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call was successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHanaInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHanaInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHanaRetentionSettingRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, disabled=None, retention_days=None, schedule=None,
                 vault_id=None):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # Specifies whether to permanently retain the backup. Valid values:
        # 
        # *   true: The backup is permanently retained.
        # *   false: The backup is retained for the specified number of days.
        self.disabled = disabled  # type: bool
        # The number of days for which the backup is retained. If you set the Disabled parameter to false, the backup is retained for the number of days specified by this parameter.
        self.retention_days = retention_days  # type: long
        # The policy to update the retention period. Format: `I|{startTime}|{interval}`. The retention period is updated at an interval of {interval} starting from {startTime}.
        # 
        # *   startTime: the time at which the system starts to update the retention period. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system updates the retention period. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of 1 hour and P1D specifies an interval of one day.
        self.schedule = schedule  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaRetentionSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpdateHanaRetentionSettingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHanaRetentionSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateHanaRetentionSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHanaRetentionSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHanaRetentionSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHanaRetentionSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyBindingRequestAdvancedOptionsCommonFileSystemDetail(TeaModel):
    def __init__(self, fetch_slice_size=None, full_on_increment_fail=None):
        self.fetch_slice_size = fetch_slice_size  # type: long
        self.full_on_increment_fail = full_on_increment_fail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyBindingRequestAdvancedOptionsCommonFileSystemDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_slice_size is not None:
            result['FetchSliceSize'] = self.fetch_slice_size
        if self.full_on_increment_fail is not None:
            result['FullOnIncrementFail'] = self.full_on_increment_fail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchSliceSize') is not None:
            self.fetch_slice_size = m.get('FetchSliceSize')
        if m.get('FullOnIncrementFail') is not None:
            self.full_on_increment_fail = m.get('FullOnIncrementFail')
        return self


class UpdatePolicyBindingRequestAdvancedOptionsOssDetail(TeaModel):
    def __init__(self, inventory_cleanup_policy=None, inventory_id=None):
        # Specifies whether the system deletes the inventory lists after a backup is complete. This parameter is available only when OSS inventory lists are used. Valid values:
        # 
        # *   **NO_CLEANUP**: Does not delete inventory lists.
        # *   **DELETE_CURRENT**: Deletes the current inventory list.
        # *   **DELETE_CURRENT_AND_PREVIOUS**: Deletes all inventory lists.
        self.inventory_cleanup_policy = inventory_cleanup_policy  # type: str
        # The name of the OSS inventory list. The OSS inventory list specified for this parameter is used for performance optimization.
        # 
        # *   If you want to back up more than 100 million OSS objects, we recommend that you use inventory lists to accelerate incremental backup. Storage fees for inventory lists are included in your OSS bills.
        # *   An extended period of time is required for OSS to generate inventory lists. Before inventory lists are generated, OSS objects may fail to be backed up. In this case, you can back up the OSS objects in the next backup cycle.
        self.inventory_id = inventory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyBindingRequestAdvancedOptionsOssDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory_cleanup_policy is not None:
            result['InventoryCleanupPolicy'] = self.inventory_cleanup_policy
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InventoryCleanupPolicy') is not None:
            self.inventory_cleanup_policy = m.get('InventoryCleanupPolicy')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        return self


class UpdatePolicyBindingRequestAdvancedOptionsUdmDetail(TeaModel):
    def __init__(self, app_consistent=None, disk_id_list=None, enable_fs_freeze=None, enable_writers=None,
                 exclude_disk_id_list=None, post_script_path=None, pre_script_path=None, ram_role_name=None, snapshot_group=None,
                 timeout_in_seconds=None):
        # Specifies whether to enable application consistency. You can enable application consistency only if all disks are ESSDs.
        self.app_consistent = app_consistent  # type: bool
        # The IDs of the disks that require protection. This parameter is not required if all disks require protection.
        self.disk_id_list = disk_id_list  # type: list[str]
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies whether to enable Linux fsfreeze to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        self.enable_fs_freeze = enable_fs_freeze  # type: bool
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies whether to create application-consistent snapshots. Valid values:
        # 
        # *   true: creates application-consistent snapshots.
        # *   false: creates file system-consistent snapshots.
        # 
        # Default value: true.
        self.enable_writers = enable_writers  # type: bool
        # The IDs of the disks that require no protection. This parameter is not required if the DiskIdList parameter is specified.
        self.exclude_disk_id_list = exclude_disk_id_list  # type: list[str]
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the path of the post-thaw scripts that are executed after application-consistent snapshots are created.
        self.post_script_path = post_script_path  # type: str
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the path of the pre-freeze scripts that are executed before application-consistent snapshots are created.
        self.pre_script_path = pre_script_path  # type: str
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the name of the Resource Access Management (RAM) role that is required to create application-consistent snapshots.
        self.ram_role_name = ram_role_name  # type: str
        # Specifies whether to create a snapshot-consistent group. You can create a snapshot-consistent group only if all disks are enhanced SSDs (ESSDs).
        self.snapshot_group = snapshot_group  # type: bool
        # This parameter is required only if the **AppConsistent** parameter is set to **true**. This parameter specifies the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.timeout_in_seconds = timeout_in_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyBindingRequestAdvancedOptionsUdmDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_consistent is not None:
            result['AppConsistent'] = self.app_consistent
        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list
        if self.enable_fs_freeze is not None:
            result['EnableFsFreeze'] = self.enable_fs_freeze
        if self.enable_writers is not None:
            result['EnableWriters'] = self.enable_writers
        if self.exclude_disk_id_list is not None:
            result['ExcludeDiskIdList'] = self.exclude_disk_id_list
        if self.post_script_path is not None:
            result['PostScriptPath'] = self.post_script_path
        if self.pre_script_path is not None:
            result['PreScriptPath'] = self.pre_script_path
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.snapshot_group is not None:
            result['SnapshotGroup'] = self.snapshot_group
        if self.timeout_in_seconds is not None:
            result['TimeoutInSeconds'] = self.timeout_in_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppConsistent') is not None:
            self.app_consistent = m.get('AppConsistent')
        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')
        if m.get('EnableFsFreeze') is not None:
            self.enable_fs_freeze = m.get('EnableFsFreeze')
        if m.get('EnableWriters') is not None:
            self.enable_writers = m.get('EnableWriters')
        if m.get('ExcludeDiskIdList') is not None:
            self.exclude_disk_id_list = m.get('ExcludeDiskIdList')
        if m.get('PostScriptPath') is not None:
            self.post_script_path = m.get('PostScriptPath')
        if m.get('PreScriptPath') is not None:
            self.pre_script_path = m.get('PreScriptPath')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SnapshotGroup') is not None:
            self.snapshot_group = m.get('SnapshotGroup')
        if m.get('TimeoutInSeconds') is not None:
            self.timeout_in_seconds = m.get('TimeoutInSeconds')
        return self


class UpdatePolicyBindingRequestAdvancedOptions(TeaModel):
    def __init__(self, common_file_system_detail=None, oss_detail=None, udm_detail=None):
        self.common_file_system_detail = common_file_system_detail  # type: UpdatePolicyBindingRequestAdvancedOptionsCommonFileSystemDetail
        # The details of the Object Storage Service (OSS) backup.
        self.oss_detail = oss_detail  # type: UpdatePolicyBindingRequestAdvancedOptionsOssDetail
        # The backup details of the Elastic Compute Service (ECS) instance.
        self.udm_detail = udm_detail  # type: UpdatePolicyBindingRequestAdvancedOptionsUdmDetail

    def validate(self):
        if self.common_file_system_detail:
            self.common_file_system_detail.validate()
        if self.oss_detail:
            self.oss_detail.validate()
        if self.udm_detail:
            self.udm_detail.validate()

    def to_map(self):
        _map = super(UpdatePolicyBindingRequestAdvancedOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_file_system_detail is not None:
            result['CommonFileSystemDetail'] = self.common_file_system_detail.to_map()
        if self.oss_detail is not None:
            result['OssDetail'] = self.oss_detail.to_map()
        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonFileSystemDetail') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptionsCommonFileSystemDetail()
            self.common_file_system_detail = temp_model.from_map(m['CommonFileSystemDetail'])
        if m.get('OssDetail') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptionsOssDetail()
            self.oss_detail = temp_model.from_map(m['OssDetail'])
        if m.get('UdmDetail') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptionsUdmDetail()
            self.udm_detail = temp_model.from_map(m['UdmDetail'])
        return self


class UpdatePolicyBindingRequest(TeaModel):
    def __init__(self, advanced_options=None, data_source_id=None, disabled=None, policy_binding_description=None,
                 policy_id=None, source_type=None):
        # The advanced options.
        self.advanced_options = advanced_options  # type: UpdatePolicyBindingRequestAdvancedOptions
        # The ID of the data source.
        self.data_source_id = data_source_id  # type: str
        # Specifies whether to disable the backup policy for the data source.
        # 
        # *   true: disables the backup policy for the data source
        # *   false: enables the backup policy for the data source
        self.disabled = disabled  # type: bool
        # The description of the association.
        self.policy_binding_description = policy_binding_description  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type  # type: str

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()

    def to_map(self):
        _map = super(UpdatePolicyBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            temp_model = UpdatePolicyBindingRequestAdvancedOptions()
            self.advanced_options = temp_model.from_map(m['AdvancedOptions'])
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class UpdatePolicyBindingShrinkRequest(TeaModel):
    def __init__(self, advanced_options_shrink=None, data_source_id=None, disabled=None,
                 policy_binding_description=None, policy_id=None, source_type=None):
        # The advanced options.
        self.advanced_options_shrink = advanced_options_shrink  # type: str
        # The ID of the data source.
        self.data_source_id = data_source_id  # type: str
        # Specifies whether to disable the backup policy for the data source.
        # 
        # *   true: disables the backup policy for the data source
        # *   false: enables the backup policy for the data source
        self.disabled = disabled  # type: bool
        # The description of the association.
        self.policy_binding_description = policy_binding_description  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyBindingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_options_shrink is not None:
            result['AdvancedOptions'] = self.advanced_options_shrink
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.policy_binding_description is not None:
            result['PolicyBindingDescription'] = self.policy_binding_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedOptions') is not None:
            self.advanced_options_shrink = m.get('AdvancedOptions')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('PolicyBindingDescription') is not None:
            self.policy_binding_description = m.get('PolicyBindingDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class UpdatePolicyBindingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyBindingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePolicyBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePolicyBindingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePolicyBindingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePolicyBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyV2RequestRulesRetentionRules(TeaModel):
    def __init__(self, advanced_retention_type=None, retention=None, which_snapshot=None):
        # The type of the special retention rule. Valid values:
        # 
        # *   **WEEKLY**: weekly backups
        # *   **MONTHLY**: monthly backups
        # *   **YEARLY**: yearly backups
        self.advanced_retention_type = advanced_retention_type  # type: str
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # Specifies which backup is retained based on the special retention rule. Only the first backup can be retained.
        self.which_snapshot = which_snapshot  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyV2RequestRulesRetentionRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.which_snapshot is not None:
            result['WhichSnapshot'] = self.which_snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('WhichSnapshot') is not None:
            self.which_snapshot = m.get('WhichSnapshot')
        return self


class UpdatePolicyV2RequestRules(TeaModel):
    def __init__(self, archive_days=None, backup_type=None, cold_archive_days=None, keep_latest_snapshots=None,
                 replication_region_id=None, retention=None, retention_rules=None, rule_id=None, rule_type=None, schedule=None):
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION**. This parameter specifies the time when data is dumped from a backup vault to an archive vault. Unit: days.
        self.archive_days = archive_days  # type: long
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type  # type: str
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION**. This parameter specifies the time when data is dumped from a backup vault to a cold archive vault. Unit: days.
        self.cold_archive_days = cold_archive_days  # type: long
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots  # type: long
        # This parameter is required only if the **RuleType** parameter is set to **REPLICATION**. This parameter specifies the ID of the destination region.
        self.replication_region_id = replication_region_id  # type: str
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION** or **REPLICATION**.
        # 
        # *   If the **RuleType** parameter is set to **TRANSITION**, this parameter specifies the retention period of the backup data. Minimum value: 1. Unit: days.
        # *   If the **RuleType** parameter is set to **REPLICATION**, this parameter specifies the retention period of remote backups. Minimum value: 1. Unit: days.
        self.retention = retention  # type: long
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION**. This parameter specifies the special retention rules.
        self.retention_rules = retention_rules  # type: list[UpdatePolicyV2RequestRulesRetentionRules]
        # The rule ID.
        self.rule_id = rule_id  # type: str
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type.
        # 
        # *   **BACKUP**: backup rule
        # *   **TRANSITION**: lifecycle rule
        # *   **REPLICATION**: replication rule
        self.rule_type = rule_type  # type: str
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup schedule settings. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is complete. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule  # type: str

    def validate(self):
        if self.retention_rules:
            for k in self.retention_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePolicyV2RequestRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_days is not None:
            result['ArchiveDays'] = self.archive_days
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cold_archive_days is not None:
            result['ColdArchiveDays'] = self.cold_archive_days
        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots
        if self.replication_region_id is not None:
            result['ReplicationRegionId'] = self.replication_region_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['RetentionRules'] = []
        if self.retention_rules is not None:
            for k in self.retention_rules:
                result['RetentionRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchiveDays') is not None:
            self.archive_days = m.get('ArchiveDays')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ColdArchiveDays') is not None:
            self.cold_archive_days = m.get('ColdArchiveDays')
        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')
        if m.get('ReplicationRegionId') is not None:
            self.replication_region_id = m.get('ReplicationRegionId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.retention_rules = []
        if m.get('RetentionRules') is not None:
            for k in m.get('RetentionRules'):
                temp_model = UpdatePolicyV2RequestRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdatePolicyV2Request(TeaModel):
    def __init__(self, policy_description=None, policy_id=None, policy_name=None, rules=None):
        # The description of the backup policy.
        self.policy_description = policy_description  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The name of the backup policy.
        self.policy_name = policy_name  # type: str
        # The rules in the backup policy.
        self.rules = rules  # type: list[UpdatePolicyV2RequestRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePolicyV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = UpdatePolicyV2RequestRules()
                self.rules.append(temp_model.from_map(k))
        return self


class UpdatePolicyV2ShrinkRequest(TeaModel):
    def __init__(self, policy_description=None, policy_id=None, policy_name=None, rules_shrink=None):
        # The description of the backup policy.
        self.policy_description = policy_description  # type: str
        # The ID of the backup policy.
        self.policy_id = policy_id  # type: str
        # The name of the backup policy.
        self.policy_name = policy_name  # type: str
        # The rules in the backup policy.
        self.rules_shrink = rules_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyV2ShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')
        return self


class UpdatePolicyV2ResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePolicyV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePolicyV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePolicyV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePolicyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVaultRequest(TeaModel):
    def __init__(self, description=None, resource_group_id=None, vault_id=None, vault_name=None):
        self.description = description  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.vault_id = vault_id  # type: str
        self.vault_name = vault_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVaultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        if self.vault_name is not None:
            result['VaultName'] = self.vault_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')
        return self


class UpdateVaultResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVaultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateVaultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVaultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVaultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateVaultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeBackupClientsRequest(TeaModel):
    def __init__(self, client_ids=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, instance_ids=None):
        # The ID of the HBR client. The sum of the number of HBR client IDs and the number of ECS instance IDs cannot exceed 100.
        self.client_ids = client_ids  # type: dict[str, any]
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The IDs of the ECS instances. The sum of the number of HBR client IDs and the number of ECS instance IDs cannot exceed 100.
        self.instance_ids = instance_ids  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeBackupClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class UpgradeBackupClientsShrinkRequest(TeaModel):
    def __init__(self, client_ids_shrink=None, cross_account_role_name=None, cross_account_type=None,
                 cross_account_user_id=None, instance_ids_shrink=None):
        # The ID of the HBR client. The sum of the number of HBR client IDs and the number of ECS instance IDs cannot exceed 100.
        self.client_ids_shrink = client_ids_shrink  # type: str
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name  # type: str
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type  # type: str
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id  # type: long
        # The IDs of the ECS instances. The sum of the number of HBR client IDs and the number of ECS instance IDs cannot exceed 100.
        self.instance_ids_shrink = instance_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeBackupClientsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name
        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type
        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')
        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')
        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class UpgradeBackupClientsResponseBodyInstanceStatuses(TeaModel):
    def __init__(self, error_code=None, instance_id=None, valid_instance=None):
        # The error code that is returned. Valid values:
        # 
        # *   If the value is empty, the call is successful.
        # *   **InstanceNotExists**: The ECS instance does not exist.
        # *   **InstanceNotRunning**: The ECS instance is not running.
        # *   **CloudAssistNotRunningOnInstance**: Cloud Assistant is unavailable.
        self.error_code = error_code  # type: str
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether an HBR client can be installed on the ECS instance. Valid values:
        # 
        # *   true: An HBR client can be installed on the ECS instance.
        # *   false: An HBR client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeBackupClientsResponseBodyInstanceStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')
        return self


class UpgradeBackupClientsResponseBody(TeaModel):
    def __init__(self, code=None, instance_statuses=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The status of the ECS instance. If the status of an ECS instance cannot meet the requirements to install an HBR client and the value of the InstanceIds parameter is greater than 1, an error message is returned based on the value of this parameter.
        self.instance_statuses = instance_statuses  # type: list[UpgradeBackupClientsResponseBodyInstanceStatuses]
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of an asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        if self.instance_statuses:
            for k in self.instance_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpgradeBackupClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k in self.instance_statuses:
                result['InstanceStatuses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k in m.get('InstanceStatuses'):
                temp_model = UpgradeBackupClientsResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeBackupClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeBackupClientsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeBackupClientsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeBackupClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClientRequest(TeaModel):
    def __init__(self, client_id=None, resource_group_id=None, vault_id=None):
        # The ID of the backup client.
        self.client_id = client_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the backup vault.
        self.vault_id = vault_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vault_id is not None:
            result['VaultId'] = self.vault_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')
        return self


class UpgradeClientResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, task_id=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: str
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success  # type: bool
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClientResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeClientResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeClientResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeClientResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


