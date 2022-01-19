# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateClusterPublicConnectionRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateClusterPublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AllocateClusterPublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateClusterPublicConnectionResponseBody, self).to_map()
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


class AllocateClusterPublicConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AllocateClusterPublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocateClusterPublicConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AllocateClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckClickhouseToRDSRequest(TeaModel):
    def __init__(self, ck_password=None, ck_user_name=None, clickhouse_port=None, db_cluster_id=None,
                 owner_account=None, owner_id=None, rds_id=None, rds_password=None, rds_port=None, rds_user_name=None,
                 rds_vpc_id=None, resource_owner_account=None, resource_owner_id=None):
        self.ck_password = ck_password  # type: str
        self.ck_user_name = ck_user_name  # type: str
        self.clickhouse_port = clickhouse_port  # type: long
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.rds_id = rds_id  # type: str
        self.rds_password = rds_password  # type: str
        self.rds_port = rds_port  # type: long
        self.rds_user_name = rds_user_name  # type: str
        self.rds_vpc_id = rds_vpc_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckClickhouseToRDSRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ck_password is not None:
            result['CkPassword'] = self.ck_password
        if self.ck_user_name is not None:
            result['CkUserName'] = self.ck_user_name
        if self.clickhouse_port is not None:
            result['ClickhousePort'] = self.clickhouse_port
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password
        if self.rds_port is not None:
            result['RdsPort'] = self.rds_port
        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name
        if self.rds_vpc_id is not None:
            result['RdsVpcId'] = self.rds_vpc_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CkPassword') is not None:
            self.ck_password = m.get('CkPassword')
        if m.get('CkUserName') is not None:
            self.ck_user_name = m.get('CkUserName')
        if m.get('ClickhousePort') is not None:
            self.clickhouse_port = m.get('ClickhousePort')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')
        if m.get('RdsPort') is not None:
            self.rds_port = m.get('RdsPort')
        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')
        if m.get('RdsVpcId') is not None:
            self.rds_vpc_id = m.get('RdsVpcId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckClickhouseToRDSResponseBody(TeaModel):
    def __init__(self, error_code=None, request_id=None, status=None):
        self.error_code = error_code  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckClickhouseToRDSResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckClickhouseToRDSResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckClickhouseToRDSResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckClickhouseToRDSResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckClickhouseToRDSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMonitorAlertRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMonitorAlertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckMonitorAlertResponseBody(TeaModel):
    def __init__(self, parameter=None, request_id=None, state=None):
        self.parameter = parameter  # type: str
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMonitorAlertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameter') is not None:
            self.parameter = m.get('Parameter')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class CheckMonitorAlertResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckMonitorAlertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckMonitorAlertResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckMonitorAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckScaleOutBalancedRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckScaleOutBalancedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckScaleOutBalancedResponseBodyTableDetailsTableDetail(TeaModel):
    def __init__(self, cluster=None, database=None, detail=None, table_name=None):
        self.cluster = cluster  # type: str
        self.database = database  # type: str
        self.detail = detail  # type: int
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckScaleOutBalancedResponseBodyTableDetailsTableDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster
        if self.database is not None:
            result['Database'] = self.database
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class CheckScaleOutBalancedResponseBodyTableDetails(TeaModel):
    def __init__(self, table_detail=None):
        self.table_detail = table_detail  # type: list[CheckScaleOutBalancedResponseBodyTableDetailsTableDetail]

    def validate(self):
        if self.table_detail:
            for k in self.table_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckScaleOutBalancedResponseBodyTableDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TableDetail'] = []
        if self.table_detail is not None:
            for k in self.table_detail:
                result['TableDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table_detail = []
        if m.get('TableDetail') is not None:
            for k in m.get('TableDetail'):
                temp_model = CheckScaleOutBalancedResponseBodyTableDetailsTableDetail()
                self.table_detail.append(temp_model.from_map(k))
        return self


class CheckScaleOutBalancedResponseBody(TeaModel):
    def __init__(self, check_code=None, page_number=None, page_size=None, request_id=None, table_details=None,
                 time_duration=None, total_count=None):
        self.check_code = check_code  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.table_details = table_details  # type: CheckScaleOutBalancedResponseBodyTableDetails
        self.time_duration = time_duration  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.table_details:
            self.table_details.validate()

    def to_map(self):
        _map = super(CheckScaleOutBalancedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_code is not None:
            result['CheckCode'] = self.check_code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.table_details is not None:
            result['TableDetails'] = self.table_details.to_map()
        if self.time_duration is not None:
            result['TimeDuration'] = self.time_duration
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckCode') is not None:
            self.check_code = m.get('CheckCode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TableDetails') is not None:
            temp_model = CheckScaleOutBalancedResponseBodyTableDetails()
            self.table_details = temp_model.from_map(m['TableDetails'])
        if m.get('TimeDuration') is not None:
            self.time_duration = m.get('TimeDuration')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CheckScaleOutBalancedResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckScaleOutBalancedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckScaleOutBalancedResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckScaleOutBalancedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, has_service_linked_role=None, request_id=None):
        self.has_service_linked_role = has_service_linked_role  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_service_linked_role is not None:
            result['HasServiceLinkedRole'] = self.has_service_linked_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckServiceLinkedRoleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckVersionTransferRequest(TeaModel):
    def __init__(self, check_account=None, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None, source_account=None,
                 source_password=None, target_account=None, target_db_cluster_id=None, target_password=None):
        self.check_account = check_account  # type: bool
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.source_account = source_account  # type: str
        self.source_password = source_password  # type: str
        self.target_account = target_account  # type: str
        self.target_db_cluster_id = target_db_cluster_id  # type: str
        self.target_password = target_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVersionTransferRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_account is not None:
            result['CheckAccount'] = self.check_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_account is not None:
            result['SourceAccount'] = self.source_account
        if self.source_password is not None:
            result['SourcePassword'] = self.source_password
        if self.target_account is not None:
            result['TargetAccount'] = self.target_account
        if self.target_db_cluster_id is not None:
            result['TargetDbClusterId'] = self.target_db_cluster_id
        if self.target_password is not None:
            result['TargetPassword'] = self.target_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckAccount') is not None:
            self.check_account = m.get('CheckAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceAccount') is not None:
            self.source_account = m.get('SourceAccount')
        if m.get('SourcePassword') is not None:
            self.source_password = m.get('SourcePassword')
        if m.get('TargetAccount') is not None:
            self.target_account = m.get('TargetAccount')
        if m.get('TargetDbClusterId') is not None:
            self.target_db_cluster_id = m.get('TargetDbClusterId')
        if m.get('TargetPassword') is not None:
            self.target_password = m.get('TargetPassword')
        return self


class CheckVersionTransferResponseBodyCheckAccess(TeaModel):
    def __init__(self, err_code=None, err_message=None):
        self.err_code = err_code  # type: long
        self.err_message = err_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVersionTransferResponseBodyCheckAccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class CheckVersionTransferResponseBodyCheckCode(TeaModel):
    def __init__(self, err_code=None, err_message=None):
        self.err_code = err_code  # type: long
        self.err_message = err_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVersionTransferResponseBodyCheckCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class CheckVersionTransferResponseBodyCheckStatus(TeaModel):
    def __init__(self, err_code=None, err_message=None):
        self.err_code = err_code  # type: long
        self.err_message = err_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVersionTransferResponseBodyCheckStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class CheckVersionTransferResponseBody(TeaModel):
    def __init__(self, check_access=None, check_category=None, check_code=None, check_connection=None,
                 check_status=None, check_storage=None, request_id=None, time_duration=None, total_count=None):
        self.check_access = check_access  # type: CheckVersionTransferResponseBodyCheckAccess
        self.check_category = check_category  # type: bool
        self.check_code = check_code  # type: CheckVersionTransferResponseBodyCheckCode
        self.check_connection = check_connection  # type: bool
        self.check_status = check_status  # type: CheckVersionTransferResponseBodyCheckStatus
        self.check_storage = check_storage  # type: bool
        self.request_id = request_id  # type: str
        self.time_duration = time_duration  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.check_access:
            self.check_access.validate()
        if self.check_code:
            self.check_code.validate()
        if self.check_status:
            self.check_status.validate()

    def to_map(self):
        _map = super(CheckVersionTransferResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_access is not None:
            result['CheckAccess'] = self.check_access.to_map()
        if self.check_category is not None:
            result['CheckCategory'] = self.check_category
        if self.check_code is not None:
            result['CheckCode'] = self.check_code.to_map()
        if self.check_connection is not None:
            result['CheckConnection'] = self.check_connection
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status.to_map()
        if self.check_storage is not None:
            result['CheckStorage'] = self.check_storage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_duration is not None:
            result['TimeDuration'] = self.time_duration
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckAccess') is not None:
            temp_model = CheckVersionTransferResponseBodyCheckAccess()
            self.check_access = temp_model.from_map(m['CheckAccess'])
        if m.get('CheckCategory') is not None:
            self.check_category = m.get('CheckCategory')
        if m.get('CheckCode') is not None:
            temp_model = CheckVersionTransferResponseBodyCheckCode()
            self.check_code = temp_model.from_map(m['CheckCode'])
        if m.get('CheckConnection') is not None:
            self.check_connection = m.get('CheckConnection')
        if m.get('CheckStatus') is not None:
            temp_model = CheckVersionTransferResponseBodyCheckStatus()
            self.check_status = temp_model.from_map(m['CheckStatus'])
        if m.get('CheckStorage') is not None:
            self.check_storage = m.get('CheckStorage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeDuration') is not None:
            self.time_duration = m.get('TimeDuration')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CheckVersionTransferResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckVersionTransferResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckVersionTransferResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckVersionTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, dbcluster_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountResponseBody, self).to_map()
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


class CreateAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountAndAuthorityRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, allow_databases=None,
                 allow_dictionaries=None, dbcluster_id=None, ddl_authority=None, dml_authority=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, total_databases=None,
                 total_dictionaries=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.allow_databases = allow_databases  # type: str
        self.allow_dictionaries = allow_dictionaries  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.ddl_authority = ddl_authority  # type: bool
        self.dml_authority = dml_authority  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.total_databases = total_databases  # type: str
        self.total_dictionaries = total_dictionaries  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountAndAuthorityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases
        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority
        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.total_databases is not None:
            result['TotalDatabases'] = self.total_databases
        if self.total_dictionaries is not None:
            result['TotalDictionaries'] = self.total_dictionaries
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')
        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')
        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TotalDatabases') is not None:
            self.total_databases = m.get('TotalDatabases')
        if m.get('TotalDictionaries') is not None:
            self.total_dictionaries = m.get('TotalDictionaries')
        return self


class CreateAccountAndAuthorityResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountAndAuthorityResponseBody, self).to_map()
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


class CreateAccountAndAuthorityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAccountAndAuthorityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccountAndAuthorityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAccountAndAuthorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPolicyRequest(TeaModel):
    def __init__(self, backup_retention_period=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 preferred_backup_period=None, preferred_backup_time=None, resource_owner_account=None, resource_owner_id=None):
        self.backup_retention_period = backup_retention_period  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPolicyResponseBody, self).to_map()
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


class CreateBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBackupPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_category=None, dbcluster_class=None,
                 dbcluster_description=None, dbcluster_network_type=None, dbcluster_version=None, dbnode_group_count=None,
                 dbnode_storage=None, db_node_storage_type=None, encryption_key=None, encryption_type=None, owner_account=None,
                 owner_id=None, pay_type=None, period=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, used_time=None, vpcid=None, v_switch_id=None, zone_id=None):
        self.client_token = client_token  # type: str
        self.dbcluster_category = dbcluster_category  # type: str
        self.dbcluster_class = dbcluster_class  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_network_type = dbcluster_network_type  # type: str
        self.dbcluster_version = dbcluster_version  # type: str
        self.dbnode_group_count = dbnode_group_count  # type: str
        self.dbnode_storage = dbnode_storage  # type: str
        self.db_node_storage_type = db_node_storage_type  # type: str
        self.encryption_key = encryption_key  # type: str
        self.encryption_type = encryption_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.used_time = used_time  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version
        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.db_node_storage_type is not None:
            result['DbNodeStorageType'] = self.db_node_storage_type
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')
        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DbNodeStorageType') is not None:
            self.db_node_storage_type = m.get('DbNodeStorageType')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, order_id=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMonitorDataReportRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMonitorDataReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateMonitorDataReportResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMonitorDataReportResponseBody, self).to_map()
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


class CreateMonitorDataReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateMonitorDataReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMonitorDataReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMonitorDataReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOSSStorageRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOSSStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateOSSStorageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOSSStorageResponseBody, self).to_map()
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


class CreateOSSStorageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOSSStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOSSStorageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOSSStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePortsForClickHouseRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, port_type=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.port_type = port_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePortsForClickHouseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port_type is not None:
            result['PortType'] = self.port_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreatePortsForClickHouseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePortsForClickHouseResponseBody, self).to_map()
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


class CreatePortsForClickHouseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePortsForClickHouseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePortsForClickHouseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePortsForClickHouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRDSToClickhouseDbRequest(TeaModel):
    def __init__(self, ck_password=None, ck_user_name=None, clickhouse_port=None, db_cluster_id=None,
                 limit_upper=None, owner_account=None, owner_id=None, rds_id=None, rds_password=None, rds_port=None,
                 rds_user_name=None, rds_vpc_id=None, resource_owner_account=None, resource_owner_id=None, skip_unsupported=None,
                 syn_db_tables=None):
        self.ck_password = ck_password  # type: str
        self.ck_user_name = ck_user_name  # type: str
        self.clickhouse_port = clickhouse_port  # type: long
        self.db_cluster_id = db_cluster_id  # type: str
        self.limit_upper = limit_upper  # type: long
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.rds_id = rds_id  # type: str
        self.rds_password = rds_password  # type: str
        self.rds_port = rds_port  # type: long
        self.rds_user_name = rds_user_name  # type: str
        self.rds_vpc_id = rds_vpc_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.skip_unsupported = skip_unsupported  # type: bool
        self.syn_db_tables = syn_db_tables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRDSToClickhouseDbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ck_password is not None:
            result['CkPassword'] = self.ck_password
        if self.ck_user_name is not None:
            result['CkUserName'] = self.ck_user_name
        if self.clickhouse_port is not None:
            result['ClickhousePort'] = self.clickhouse_port
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.limit_upper is not None:
            result['LimitUpper'] = self.limit_upper
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password
        if self.rds_port is not None:
            result['RdsPort'] = self.rds_port
        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name
        if self.rds_vpc_id is not None:
            result['RdsVpcId'] = self.rds_vpc_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.skip_unsupported is not None:
            result['SkipUnsupported'] = self.skip_unsupported
        if self.syn_db_tables is not None:
            result['SynDbTables'] = self.syn_db_tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CkPassword') is not None:
            self.ck_password = m.get('CkPassword')
        if m.get('CkUserName') is not None:
            self.ck_user_name = m.get('CkUserName')
        if m.get('ClickhousePort') is not None:
            self.clickhouse_port = m.get('ClickhousePort')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('LimitUpper') is not None:
            self.limit_upper = m.get('LimitUpper')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')
        if m.get('RdsPort') is not None:
            self.rds_port = m.get('RdsPort')
        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')
        if m.get('RdsVpcId') is not None:
            self.rds_vpc_id = m.get('RdsVpcId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SkipUnsupported') is not None:
            self.skip_unsupported = m.get('SkipUnsupported')
        if m.get('SynDbTables') is not None:
            self.syn_db_tables = m.get('SynDbTables')
        return self


class CreateRDSToClickhouseDbResponseBody(TeaModel):
    def __init__(self, error_msg=None, repeated_dbs=None, request_id=None, status=None):
        self.error_msg = error_msg  # type: str
        self.repeated_dbs = repeated_dbs  # type: list[str]
        self.request_id = request_id  # type: str
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRDSToClickhouseDbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.repeated_dbs is not None:
            result['RepeatedDbs'] = self.repeated_dbs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RepeatedDbs') is not None:
            self.repeated_dbs = m.get('RepeatedDbs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRDSToClickhouseDbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRDSToClickhouseDbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRDSToClickhouseDbResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRDSToClickhouseDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountResponseBody, self).to_map()
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


class DeleteAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterResponseBody, self).to_map()
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


class DeleteDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLorneTaskRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLorneTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteLorneTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLorneTaskResponseBody, self).to_map()
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


class DeleteLorneTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteLorneTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLorneTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLorneTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSyndbRequest(TeaModel):
    def __init__(self, db_cluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, syn_db=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.syn_db = syn_db  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSyndbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.syn_db is not None:
            result['SynDb'] = self.syn_db
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SynDb') is not None:
            self.syn_db = m.get('SynDb')
        return self


class DeleteSyndbResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, status=None):
        self.error_code = error_code  # type: long
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSyndbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteSyndbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSyndbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSyndbResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSyndbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountAuthorityRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountAuthorityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAccountAuthorityResponseBody(TeaModel):
    def __init__(self, account_name=None, allow_databases=None, allow_dictionaries=None, ddl_authority=None,
                 dml_authority=None, request_id=None, total_databases=None, total_dictionaries=None):
        self.account_name = account_name  # type: str
        self.allow_databases = allow_databases  # type: list[str]
        self.allow_dictionaries = allow_dictionaries  # type: list[str]
        self.ddl_authority = ddl_authority  # type: bool
        self.dml_authority = dml_authority  # type: str
        self.request_id = request_id  # type: str
        self.total_databases = total_databases  # type: list[str]
        self.total_dictionaries = total_dictionaries  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountAuthorityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases
        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries
        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority
        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_databases is not None:
            result['TotalDatabases'] = self.total_databases
        if self.total_dictionaries is not None:
            result['TotalDictionaries'] = self.total_dictionaries
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')
        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')
        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')
        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalDatabases') is not None:
            self.total_databases = m.get('TotalDatabases')
        if m.get('TotalDictionaries') is not None:
            self.total_dictionaries = m.get('TotalDictionaries')
        return self


class DescribeAccountAuthorityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAccountAuthorityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccountAuthorityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAccountAuthorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_status=None, account_type=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_status = account_status  # type: str
        self.account_type = account_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccountsAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
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
    def __init__(self, accounts=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.accounts = accounts  # type: DescribeAccountsResponseBodyAccounts
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

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
        if m.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllDataSourceRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAllDataSourceResponseBodyColumnsColumn(TeaModel):
    def __init__(self, auto_increment_column=None, column_name=None, dbcluster_id=None, primary_key=None,
                 schema_name=None, table_name=None, type=None):
        self.auto_increment_column = auto_increment_column  # type: bool
        self.column_name = column_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.primary_key = primary_key  # type: bool
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourceResponseBodyColumnsColumn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAllDataSourceResponseBodyColumns(TeaModel):
    def __init__(self, column=None):
        self.column = column  # type: list[DescribeAllDataSourceResponseBodyColumnsColumn]

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourceResponseBodyColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = DescribeAllDataSourceResponseBodyColumnsColumn()
                self.column.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBodySchemasSchema(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.schema_name = schema_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourceResponseBodySchemasSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeAllDataSourceResponseBodySchemas(TeaModel):
    def __init__(self, schema=None):
        self.schema = schema  # type: list[DescribeAllDataSourceResponseBodySchemasSchema]

    def validate(self):
        if self.schema:
            for k in self.schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourceResponseBodySchemas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Schema'] = []
        if self.schema is not None:
            for k in self.schema:
                result['Schema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k in m.get('Schema'):
                temp_model = DescribeAllDataSourceResponseBodySchemasSchema()
                self.schema.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBodyTablesTable(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourceResponseBodyTablesTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAllDataSourceResponseBodyTables(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[DescribeAllDataSourceResponseBodyTablesTable]

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourceResponseBodyTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeAllDataSourceResponseBodyTablesTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBody(TeaModel):
    def __init__(self, columns=None, request_id=None, schemas=None, tables=None):
        self.columns = columns  # type: DescribeAllDataSourceResponseBodyColumns
        self.request_id = request_id  # type: str
        self.schemas = schemas  # type: DescribeAllDataSourceResponseBodySchemas
        self.tables = tables  # type: DescribeAllDataSourceResponseBodyTables

    def validate(self):
        if self.columns:
            self.columns.validate()
        if self.schemas:
            self.schemas.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schemas is not None:
            result['Schemas'] = self.schemas.to_map()
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Columns') is not None:
            temp_model = DescribeAllDataSourceResponseBodyColumns()
            self.columns = temp_model.from_map(m['Columns'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schemas') is not None:
            temp_model = DescribeAllDataSourceResponseBodySchemas()
            self.schemas = temp_model.from_map(m['Schemas'])
        if m.get('Tables') is not None:
            temp_model = DescribeAllDataSourceResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        return self


class DescribeAllDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAllDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAllDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllDataSourcesRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAllDataSourcesResponseBodyColumnsColumn(TeaModel):
    def __init__(self, auto_increment_column=None, column_name=None, dbcluster_id=None, primary_key=None,
                 schema_name=None, table_name=None, type=None):
        self.auto_increment_column = auto_increment_column  # type: bool
        self.column_name = column_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.primary_key = primary_key  # type: bool
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponseBodyColumnsColumn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAllDataSourcesResponseBodyColumns(TeaModel):
    def __init__(self, column=None):
        self.column = column  # type: list[DescribeAllDataSourcesResponseBodyColumnsColumn]

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponseBodyColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = DescribeAllDataSourcesResponseBodyColumnsColumn()
                self.column.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourcesResponseBodySchemasSchema(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.schema_name = schema_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponseBodySchemasSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeAllDataSourcesResponseBodySchemas(TeaModel):
    def __init__(self, schema=None):
        self.schema = schema  # type: list[DescribeAllDataSourcesResponseBodySchemasSchema]

    def validate(self):
        if self.schema:
            for k in self.schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponseBodySchemas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Schema'] = []
        if self.schema is not None:
            for k in self.schema:
                result['Schema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k in m.get('Schema'):
                temp_model = DescribeAllDataSourcesResponseBodySchemasSchema()
                self.schema.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourcesResponseBodyTablesTable(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponseBodyTablesTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAllDataSourcesResponseBodyTables(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[DescribeAllDataSourcesResponseBodyTablesTable]

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponseBodyTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeAllDataSourcesResponseBodyTablesTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourcesResponseBody(TeaModel):
    def __init__(self, columns=None, request_id=None, schemas=None, tables=None):
        self.columns = columns  # type: DescribeAllDataSourcesResponseBodyColumns
        self.request_id = request_id  # type: str
        self.schemas = schemas  # type: DescribeAllDataSourcesResponseBodySchemas
        self.tables = tables  # type: DescribeAllDataSourcesResponseBodyTables

    def validate(self):
        if self.columns:
            self.columns.validate()
        if self.schemas:
            self.schemas.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schemas is not None:
            result['Schemas'] = self.schemas.to_map()
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Columns') is not None:
            temp_model = DescribeAllDataSourcesResponseBodyColumns()
            self.columns = temp_model.from_map(m['Columns'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schemas') is not None:
            temp_model = DescribeAllDataSourcesResponseBodySchemas()
            self.schemas = temp_model.from_map(m['Schemas'])
        if m.get('Tables') is not None:
            temp_model = DescribeAllDataSourcesResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        return self


class DescribeAllDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAllDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAllDataSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAllDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, accept_language=None, charge_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, zone_id=None):
        self.accept_language = accept_language  # type: str
        self.charge_type = charge_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutorNodeCount(TeaModel):
    def __init__(self, max_count=None, min_count=None, step=None):
        self.max_count = max_count  # type: str
        self.min_count = min_count  # type: str
        self.step = step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutorNodeCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutor(TeaModel):
    def __init__(self, node_count=None):
        self.node_count = node_count  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutorNodeCount

    def validate(self):
        if self.node_count:
            self.node_count.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutorNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorList(TeaModel):
    def __init__(self, supported_executor=None):
        self.supported_executor = supported_executor  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutor]

    def validate(self):
        if self.supported_executor:
            for k in self.supported_executor:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedExecutor'] = []
        if self.supported_executor is not None:
            for k in self.supported_executor:
                result['SupportedExecutor'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_executor = []
        if m.get('SupportedExecutor') is not None:
            for k in m.get('SupportedExecutor'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorListSupportedExecutor()
                self.supported_executor.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountNodeCount(TeaModel):
    def __init__(self, max_count=None, min_count=None, step=None):
        self.max_count = max_count  # type: str
        self.min_count = min_count  # type: str
        self.step = step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountNodeCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountStorageSize(TeaModel):
    def __init__(self, storage_size=None):
        self.storage_size = storage_size  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountStorageSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCount(TeaModel):
    def __init__(self, node_count=None, storage_size=None):
        self.node_count = node_count  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountNodeCount
        self.storage_size = storage_size  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountStorageSize

    def validate(self):
        if self.node_count:
            self.node_count.validate()
        if self.storage_size:
            self.storage_size.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        if m.get('StorageSize') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCountStorageSize()
            self.storage_size = temp_model.from_map(m['StorageSize'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountList(TeaModel):
    def __init__(self, supported_node_count=None):
        self.supported_node_count = supported_node_count  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCount]

    def validate(self):
        if self.supported_node_count:
            for k in self.supported_node_count:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedNodeCount'] = []
        if self.supported_node_count is not None:
            for k in self.supported_node_count:
                result['SupportedNodeCount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_node_count = []
        if m.get('SupportedNodeCount') is not None:
            for k in m.get('SupportedNodeCount'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountListSupportedNodeCount()
                self.supported_node_count.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass(TeaModel):
    def __init__(self, instance_class=None, supported_executor_list=None, supported_node_count_list=None,
                 tips=None):
        self.instance_class = instance_class  # type: str
        self.supported_executor_list = supported_executor_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorList
        self.supported_node_count_list = supported_node_count_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountList
        self.tips = tips  # type: str

    def validate(self):
        if self.supported_executor_list:
            self.supported_executor_list.validate()
        if self.supported_node_count_list:
            self.supported_node_count_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.supported_executor_list is not None:
            result['SupportedExecutorList'] = self.supported_executor_list.to_map()
        if self.supported_node_count_list is not None:
            result['SupportedNodeCountList'] = self.supported_node_count_list.to_map()
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('SupportedExecutorList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedExecutorList()
            self.supported_executor_list = temp_model.from_map(m['SupportedExecutorList'])
        if m.get('SupportedNodeCountList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedNodeCountList()
            self.supported_node_count_list = temp_model.from_map(m['SupportedNodeCountList'])
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList(TeaModel):
    def __init__(self, supported_instance_class=None):
        self.supported_instance_class = supported_instance_class  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass]

    def validate(self):
        if self.supported_instance_class:
            for k in self.supported_instance_class:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedInstanceClass'] = []
        if self.supported_instance_class is not None:
            for k in self.supported_instance_class:
                result['SupportedInstanceClass'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_instance_class = []
        if m.get('SupportedInstanceClass') is not None:
            for k in m.get('SupportedInstanceClass'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass()
                self.supported_instance_class.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial(TeaModel):
    def __init__(self, serial=None, supported_instance_class_list=None):
        self.serial = serial  # type: str
        self.supported_instance_class_list = supported_instance_class_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList

    def validate(self):
        if self.supported_instance_class_list:
            self.supported_instance_class_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial is not None:
            result['Serial'] = self.serial
        if self.supported_instance_class_list is not None:
            result['SupportedInstanceClassList'] = self.supported_instance_class_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')
        if m.get('SupportedInstanceClassList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList()
            self.supported_instance_class_list = temp_model.from_map(m['SupportedInstanceClassList'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList(TeaModel):
    def __init__(self, supported_serial=None):
        self.supported_serial = supported_serial  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial]

    def validate(self):
        if self.supported_serial:
            for k in self.supported_serial:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedSerial'] = []
        if self.supported_serial is not None:
            for k in self.supported_serial:
                result['SupportedSerial'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_serial = []
        if m.get('SupportedSerial') is not None:
            for k in m.get('SupportedSerial'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial()
                self.supported_serial.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone(TeaModel):
    def __init__(self, supported_serial_list=None, zone_id=None):
        self.supported_serial_list = supported_serial_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.supported_serial_list:
            self.supported_serial_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_serial_list is not None:
            result['SupportedSerialList'] = self.supported_serial_list.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedSerialList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList()
            self.supported_serial_list = temp_model.from_map(m['SupportedSerialList'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneList(TeaModel):
    def __init__(self, available_zone=None):
        self.available_zone = available_zone  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone]

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k in m.get('AvailableZone'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(self, available_zone_list=None, region_id=None, request_id=None):
        self.available_zone_list = available_zone_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneList
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zone_list:
            self.available_zone_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zone_list is not None:
            result['AvailableZoneList'] = self.available_zone_list.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZoneList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneList()
            self.available_zone_list = temp_model.from_map(m['AvailableZoneList'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAvailableResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, backup_retention_period=None, preferred_backup_period=None, preferred_backup_time=None,
                 request_id=None, switch=None):
        self.backup_retention_period = backup_retention_period  # type: int
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.request_id = request_id  # type: str
        self.switch = switch  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.switch is not None:
            result['Switch'] = self.switch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, dbcluster_id=None, end_time=None, owner_account=None, owner_id=None,
                 page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.backup_id = backup_id  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupsResponseBodyItems(TeaModel):
    def __init__(self, backup_end_time=None, backup_id=None, backup_method=None, backup_set_info=None,
                 backup_size=None, backup_start_time=None, backup_status=None, backup_type=None, dbcluster_id=None):
        self.backup_end_time = backup_end_time  # type: str
        self.backup_id = backup_id  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_set_info = backup_set_info  # type: str
        self.backup_size = backup_size  # type: int
        self.backup_start_time = backup_start_time  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_type = backup_type  # type: str
        self.dbcluster_id = dbcluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_set_info is not None:
            result['BackupSetInfo'] = self.backup_set_info
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupSetInfo') is not None:
            self.backup_set_info = m.get('BackupSetInfo')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.items = items  # type: list[DescribeBackupsResponseBodyItems]
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
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
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColumnsRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColumnsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsResponseBodyItemsColumn(TeaModel):
    def __init__(self, auto_increment_column=None, column_name=None, dbcluster_id=None, primary_key=None,
                 schema_name=None, table_name=None, type=None):
        self.auto_increment_column = auto_increment_column  # type: bool
        self.column_name = column_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.primary_key = primary_key  # type: bool
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColumnsResponseBodyItemsColumn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeColumnsResponseBodyItems(TeaModel):
    def __init__(self, column=None):
        self.column = column  # type: list[DescribeColumnsResponseBodyItemsColumn]

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeColumnsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = DescribeColumnsResponseBodyItemsColumn()
                self.column.append(temp_model.from_map(k))
        return self


class DescribeColumnsResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeColumnsResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeColumnsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeColumnsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeColumnsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeColumnsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeColumnsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAccessWhiteListRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteListIPArray(TeaModel):
    def __init__(self, dbcluster_iparray_attribute=None, dbcluster_iparray_name=None, security_iplist=None):
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute  # type: str
        self.dbcluster_iparray_name = dbcluster_iparray_name  # type: str
        self.security_iplist = security_iplist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteListIPArray, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteList(TeaModel):
    def __init__(self, iparray=None):
        self.iparray = iparray  # type: list[DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteListIPArray]

    def validate(self):
        if self.iparray:
            for k in self.iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IPArray'] = []
        if self.iparray is not None:
            for k in self.iparray:
                result['IPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.iparray = []
        if m.get('IPArray') is not None:
            for k in m.get('IPArray'):
                temp_model = DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteListIPArray()
                self.iparray.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(self, dbcluster_access_white_list=None, request_id=None):
        self.dbcluster_access_white_list = dbcluster_access_white_list  # type: DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbcluster_access_white_list:
            self.dbcluster_access_white_list.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_access_white_list is not None:
            result['DBClusterAccessWhiteList'] = self.dbcluster_access_white_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterAccessWhiteList') is not None:
            temp_model = DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteList()
            self.dbcluster_access_white_list = temp_model.from_map(m['DBClusterAccessWhiteList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAccessWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterAccessWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhiteListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAttributeRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterAttributeResponseBodyDBClusterScaleOutStatus(TeaModel):
    def __init__(self, progress=None, ratio=None):
        self.progress = progress  # type: str
        self.ratio = ratio  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBodyDBClusterScaleOutStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        return self


class DescribeDBClusterAttributeResponseBodyDBClusterTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBodyDBClusterTagsTag, self).to_map()
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


class DescribeDBClusterAttributeResponseBodyDBClusterTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBClusterAttributeResponseBodyDBClusterTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBodyDBClusterTags, self).to_map()
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
                temp_model = DescribeDBClusterAttributeResponseBodyDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAttributeResponseBodyDBCluster(TeaModel):
    def __init__(self, ali_uid=None, bid=None, category=None, commodity_code=None, connection_string=None,
                 control_version=None, create_time=None, dbcluster_description=None, dbcluster_id=None,
                 dbcluster_network_type=None, dbcluster_status=None, dbcluster_type=None, dbnode_class=None, dbnode_count=None,
                 dbnode_storage=None, encryption_key=None, encryption_type=None, engine=None, engine_version=None,
                 expire_time=None, is_expired=None, lock_mode=None, lock_reason=None, maintain_time=None, pay_type=None,
                 port=None, public_connection_string=None, public_port=None, region_id=None, scale_out_status=None,
                 storage_type=None, support_backup=None, support_https_port=None, support_mysql_port=None, tags=None,
                 v_switch_id=None, vpc_cloud_instance_id=None, vpc_id=None, zone_id=None):
        self.ali_uid = ali_uid  # type: str
        self.bid = bid  # type: str
        self.category = category  # type: str
        self.commodity_code = commodity_code  # type: str
        self.connection_string = connection_string  # type: str
        self.control_version = control_version  # type: str
        self.create_time = create_time  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbcluster_network_type = dbcluster_network_type  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.dbcluster_type = dbcluster_type  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_count = dbnode_count  # type: long
        self.dbnode_storage = dbnode_storage  # type: long
        self.encryption_key = encryption_key  # type: str
        self.encryption_type = encryption_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.expire_time = expire_time  # type: str
        self.is_expired = is_expired  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.maintain_time = maintain_time  # type: str
        self.pay_type = pay_type  # type: str
        self.port = port  # type: int
        self.public_connection_string = public_connection_string  # type: str
        self.public_port = public_port  # type: str
        self.region_id = region_id  # type: str
        self.scale_out_status = scale_out_status  # type: DescribeDBClusterAttributeResponseBodyDBClusterScaleOutStatus
        self.storage_type = storage_type  # type: str
        self.support_backup = support_backup  # type: int
        self.support_https_port = support_https_port  # type: bool
        self.support_mysql_port = support_mysql_port  # type: bool
        self.tags = tags  # type: DescribeDBClusterAttributeResponseBodyDBClusterTags
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.scale_out_status:
            self.scale_out_status.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBodyDBCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.category is not None:
            result['Category'] = self.category
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.control_version is not None:
            result['ControlVersion'] = self.control_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.public_port is not None:
            result['PublicPort'] = self.public_port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_out_status is not None:
            result['ScaleOutStatus'] = self.scale_out_status.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.support_backup is not None:
            result['SupportBackup'] = self.support_backup
        if self.support_https_port is not None:
            result['SupportHttpsPort'] = self.support_https_port
        if self.support_mysql_port is not None:
            result['SupportMysqlPort'] = self.support_mysql_port
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ControlVersion') is not None:
            self.control_version = m.get('ControlVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('PublicPort') is not None:
            self.public_port = m.get('PublicPort')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleOutStatus') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyDBClusterScaleOutStatus()
            self.scale_out_status = temp_model.from_map(m['ScaleOutStatus'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SupportBackup') is not None:
            self.support_backup = m.get('SupportBackup')
        if m.get('SupportHttpsPort') is not None:
            self.support_https_port = m.get('SupportHttpsPort')
        if m.get('SupportMysqlPort') is not None:
            self.support_mysql_port = m.get('SupportMysqlPort')
        if m.get('Tags') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyDBClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClusterAttributeResponseBody(TeaModel):
    def __init__(self, dbcluster=None, request_id=None):
        self.dbcluster = dbcluster  # type: DescribeDBClusterAttributeResponseBodyDBCluster
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbcluster:
            self.dbcluster.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster is not None:
            result['DBCluster'] = self.dbcluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBCluster') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyDBCluster()
            self.dbcluster = temp_model.from_map(m['DBCluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterConfigRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterConfigResponseBody(TeaModel):
    def __init__(self, config=None, request_id=None):
        self.config = config  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterNetInfoItemsRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterNetInfoItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterNetInfoItemsResponseBodyNetInfoItemsNetInfoItem(TeaModel):
    def __init__(self, connection_string=None, http_port=None, ipaddress=None, jdbc_port=None, net_type=None,
                 v_switch_id=None, vpc_id=None):
        self.connection_string = connection_string  # type: str
        self.http_port = http_port  # type: str
        self.ipaddress = ipaddress  # type: str
        self.jdbc_port = jdbc_port  # type: str
        self.net_type = net_type  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterNetInfoItemsResponseBodyNetInfoItemsNetInfoItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.jdbc_port is not None:
            result['JdbcPort'] = self.jdbc_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('JdbcPort') is not None:
            self.jdbc_port = m.get('JdbcPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDBClusterNetInfoItemsResponseBodyNetInfoItems(TeaModel):
    def __init__(self, net_info_item=None):
        self.net_info_item = net_info_item  # type: list[DescribeDBClusterNetInfoItemsResponseBodyNetInfoItemsNetInfoItem]

    def validate(self):
        if self.net_info_item:
            for k in self.net_info_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterNetInfoItemsResponseBodyNetInfoItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetInfoItem'] = []
        if self.net_info_item is not None:
            for k in self.net_info_item:
                result['NetInfoItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.net_info_item = []
        if m.get('NetInfoItem') is not None:
            for k in m.get('NetInfoItem'):
                temp_model = DescribeDBClusterNetInfoItemsResponseBodyNetInfoItemsNetInfoItem()
                self.net_info_item.append(temp_model.from_map(k))
        return self


class DescribeDBClusterNetInfoItemsResponseBody(TeaModel):
    def __init__(self, cluster_network_type=None, net_info_items=None, request_id=None):
        self.cluster_network_type = cluster_network_type  # type: str
        self.net_info_items = net_info_items  # type: DescribeDBClusterNetInfoItemsResponseBodyNetInfoItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        _map = super(DescribeDBClusterNetInfoItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('NetInfoItems') is not None:
            temp_model = DescribeDBClusterNetInfoItemsResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m['NetInfoItems'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterNetInfoItemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterNetInfoItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterNetInfoItemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterNetInfoItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, key=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformancesSeriesValues(TeaModel):
    def __init__(self, point=None):
        self.point = point  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformancesSeriesValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformancesSeries(TeaModel):
    def __init__(self, name=None, values=None):
        self.name = name  # type: str
        self.values = values  # type: list[DescribeDBClusterPerformanceResponseBodyPerformancesSeriesValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformancesSeries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformancesSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBodyPerformances(TeaModel):
    def __init__(self, key=None, name=None, series=None, unit=None):
        self.key = key  # type: str
        self.name = name  # type: str
        self.series = series  # type: list[DescribeDBClusterPerformanceResponseBodyPerformancesSeries]
        self.unit = unit  # type: str

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, performances=None, request_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.performances = performances  # type: list[DescribeDBClusterPerformanceResponseBodyPerformances]
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClustersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersRequestTag, self).to_map()
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


class DescribeDBClustersRequest(TeaModel):
    def __init__(self, control_version=None, dbcluster_description=None, dbcluster_ids=None, dbcluster_status=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, tag=None):
        self.control_version = control_version  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_ids = dbcluster_ids  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag = tag  # type: list[DescribeDBClustersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_version is not None:
            result['ControlVersion'] = self.control_version
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlVersion') is not None:
            self.control_version = m.get('ControlVersion')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyDBClustersDBClusterScaleOutStatus(TeaModel):
    def __init__(self, progress=None, ratio=None):
        self.progress = progress  # type: str
        self.ratio = ratio  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyDBClustersDBClusterScaleOutStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        return self


class DescribeDBClustersResponseBodyDBClustersDBClusterTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyDBClustersDBClusterTagsTag, self).to_map()
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


class DescribeDBClustersResponseBodyDBClustersDBClusterTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBClustersResponseBodyDBClustersDBClusterTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyDBClustersDBClusterTags, self).to_map()
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
                temp_model = DescribeDBClustersResponseBodyDBClustersDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyDBClustersDBCluster(TeaModel):
    def __init__(self, ali_uid=None, bid=None, category=None, commodity_code=None, connection_string=None,
                 control_version=None, create_time=None, dbcluster_description=None, dbcluster_id=None,
                 dbcluster_network_type=None, dbcluster_status=None, dbnode_class=None, dbnode_count=None, dbnode_storage=None,
                 expire_time=None, is_expired=None, lock_mode=None, lock_reason=None, pay_type=None, port=None, region_id=None,
                 scale_out_status=None, storage_type=None, tags=None, v_switch_id=None, vpc_cloud_instance_id=None, vpc_id=None,
                 zone_id=None):
        self.ali_uid = ali_uid  # type: str
        self.bid = bid  # type: str
        self.category = category  # type: str
        self.commodity_code = commodity_code  # type: str
        self.connection_string = connection_string  # type: str
        self.control_version = control_version  # type: str
        self.create_time = create_time  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbcluster_network_type = dbcluster_network_type  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_count = dbnode_count  # type: long
        self.dbnode_storage = dbnode_storage  # type: long
        self.expire_time = expire_time  # type: str
        self.is_expired = is_expired  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.pay_type = pay_type  # type: str
        self.port = port  # type: int
        self.region_id = region_id  # type: str
        self.scale_out_status = scale_out_status  # type: DescribeDBClustersResponseBodyDBClustersDBClusterScaleOutStatus
        self.storage_type = storage_type  # type: str
        self.tags = tags  # type: DescribeDBClustersResponseBodyDBClustersDBClusterTags
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.scale_out_status:
            self.scale_out_status.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyDBClustersDBCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.category is not None:
            result['Category'] = self.category
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.control_version is not None:
            result['ControlVersion'] = self.control_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_out_status is not None:
            result['ScaleOutStatus'] = self.scale_out_status.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ControlVersion') is not None:
            self.control_version = m.get('ControlVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleOutStatus') is not None:
            temp_model = DescribeDBClustersResponseBodyDBClustersDBClusterScaleOutStatus()
            self.scale_out_status = temp_model.from_map(m['ScaleOutStatus'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBClustersResponseBodyDBClustersDBClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClustersResponseBodyDBClusters(TeaModel):
    def __init__(self, dbcluster=None):
        self.dbcluster = dbcluster  # type: list[DescribeDBClustersResponseBodyDBClustersDBCluster]

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyDBClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClustersResponseBodyDBClustersDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBody(TeaModel):
    def __init__(self, dbclusters=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.dbclusters = dbclusters  # type: DescribeDBClustersResponseBodyDBClusters
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dbclusters:
            self.dbclusters.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbclusters is not None:
            result['DBClusters'] = self.dbclusters.to_map()
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
        if m.get('DBClusters') is not None:
            temp_model = DescribeDBClustersResponseBodyDBClusters()
            self.dbclusters = temp_model.from_map(m['DBClusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBConfigRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBConfigResponseBody(TeaModel):
    def __init__(self, config=None, request_id=None):
        self.config = config  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogHubAttributeRequest(TeaModel):
    def __init__(self, dbcluster_id=None, deliver_name=None, log_store_name=None, owner_account=None, owner_id=None,
                 project_name=None, region_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.deliver_name = deliver_name  # type: str
        self.log_store_name = log_store_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogHubAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.deliver_name is not None:
            result['DeliverName'] = self.deliver_name
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DeliverName') is not None:
            self.deliver_name = m.get('DeliverName')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStoresLogHubStore(TeaModel):
    def __init__(self, field_key=None, log_key=None, type=None):
        self.field_key = field_key  # type: str
        self.log_key = log_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStoresLogHubStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.log_key is not None:
            result['LogKey'] = self.log_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('LogKey') is not None:
            self.log_key = m.get('LogKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStores(TeaModel):
    def __init__(self, log_hub_store=None):
        self.log_hub_store = log_hub_store  # type: list[DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStoresLogHubStore]

    def validate(self):
        if self.log_hub_store:
            for k in self.log_hub_store:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStores, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogHubStore'] = []
        if self.log_hub_store is not None:
            for k in self.log_hub_store:
                result['LogHubStore'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_hub_store = []
        if m.get('LogHubStore') is not None:
            for k in m.get('LogHubStore'):
                temp_model = DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStoresLogHubStore()
                self.log_hub_store.append(temp_model.from_map(k))
        return self


class DescribeLogHubAttributeResponseBodyLoghubInfo(TeaModel):
    def __init__(self, dbcluster_id=None, dbtype=None, deliver_name=None, deliver_time=None, description=None,
                 domain_url=None, filter_dirty_data=None, id=None, log_hub_stores=None, log_store_name=None, password=None,
                 project_name=None, region_id=None, schema_name=None, table_name=None, user_name=None, zone_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbtype = dbtype  # type: str
        self.deliver_name = deliver_name  # type: str
        self.deliver_time = deliver_time  # type: str
        self.description = description  # type: str
        self.domain_url = domain_url  # type: str
        self.filter_dirty_data = filter_dirty_data  # type: str
        self.id = id  # type: str
        self.log_hub_stores = log_hub_stores  # type: DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStores
        self.log_store_name = log_store_name  # type: str
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.user_name = user_name  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.log_hub_stores:
            self.log_hub_stores.validate()

    def to_map(self):
        _map = super(DescribeLogHubAttributeResponseBodyLoghubInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.deliver_name is not None:
            result['DeliverName'] = self.deliver_name
        if self.deliver_time is not None:
            result['DeliverTime'] = self.deliver_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_url is not None:
            result['DomainUrl'] = self.domain_url
        if self.filter_dirty_data is not None:
            result['FilterDirtyData'] = self.filter_dirty_data
        if self.id is not None:
            result['Id'] = self.id
        if self.log_hub_stores is not None:
            result['LogHubStores'] = self.log_hub_stores.to_map()
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DeliverName') is not None:
            self.deliver_name = m.get('DeliverName')
        if m.get('DeliverTime') is not None:
            self.deliver_time = m.get('DeliverTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainUrl') is not None:
            self.domain_url = m.get('DomainUrl')
        if m.get('FilterDirtyData') is not None:
            self.filter_dirty_data = m.get('FilterDirtyData')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogHubStores') is not None:
            temp_model = DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStores()
            self.log_hub_stores = temp_model.from_map(m['LogHubStores'])
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeLogHubAttributeResponseBody(TeaModel):
    def __init__(self, loghub_info=None, request_id=None):
        self.loghub_info = loghub_info  # type: DescribeLogHubAttributeResponseBodyLoghubInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.loghub_info:
            self.loghub_info.validate()

    def to_map(self):
        _map = super(DescribeLogHubAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loghub_info is not None:
            result['LoghubInfo'] = self.loghub_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoghubInfo') is not None:
            temp_model = DescribeLogHubAttributeResponseBodyLoghubInfo()
            self.loghub_info = temp_model.from_map(m['LoghubInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogHubAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLogHubAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogHubAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLogHubAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreKeysRequest(TeaModel):
    def __init__(self, log_store_name=None, owner_account=None, owner_id=None, project_name=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.log_store_name = log_store_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeLogStoreKeysResponseBodyLogStoreKeys(TeaModel):
    def __init__(self, log_store_key=None):
        self.log_store_key = log_store_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreKeysResponseBodyLogStoreKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store_key is not None:
            result['LogStoreKey'] = self.log_store_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogStoreKey') is not None:
            self.log_store_key = m.get('LogStoreKey')
        return self


class DescribeLogStoreKeysResponseBody(TeaModel):
    def __init__(self, log_store_keys=None, request_id=None):
        self.log_store_keys = log_store_keys  # type: DescribeLogStoreKeysResponseBodyLogStoreKeys
        self.request_id = request_id  # type: str

    def validate(self):
        if self.log_store_keys:
            self.log_store_keys.validate()

    def to_map(self):
        _map = super(DescribeLogStoreKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store_keys is not None:
            result['LogStoreKeys'] = self.log_store_keys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogStoreKeys') is not None:
            temp_model = DescribeLogStoreKeysResponseBodyLogStoreKeys()
            self.log_store_keys = temp_model.from_map(m['LogStoreKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogStoreKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLogStoreKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogStoreKeysResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLogStoreKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoghubDetailRequest(TeaModel):
    def __init__(self, export_name=None, owner_account=None, owner_id=None, project_name=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.export_name = export_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLoghubDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_name is not None:
            result['ExportName'] = self.export_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExportName') is not None:
            self.export_name = m.get('ExportName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeLoghubDetailResponseBodyLoghubInfoLogHubStoresLogHubStore(TeaModel):
    def __init__(self, field_key=None, log_key=None, type=None):
        self.field_key = field_key  # type: str
        self.log_key = log_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLoghubDetailResponseBodyLoghubInfoLogHubStoresLogHubStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.log_key is not None:
            result['LogKey'] = self.log_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('LogKey') is not None:
            self.log_key = m.get('LogKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeLoghubDetailResponseBodyLoghubInfoLogHubStores(TeaModel):
    def __init__(self, log_hub_store=None):
        self.log_hub_store = log_hub_store  # type: list[DescribeLoghubDetailResponseBodyLoghubInfoLogHubStoresLogHubStore]

    def validate(self):
        if self.log_hub_store:
            for k in self.log_hub_store:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLoghubDetailResponseBodyLoghubInfoLogHubStores, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogHubStore'] = []
        if self.log_hub_store is not None:
            for k in self.log_hub_store:
                result['LogHubStore'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_hub_store = []
        if m.get('LogHubStore') is not None:
            for k in m.get('LogHubStore'):
                temp_model = DescribeLoghubDetailResponseBodyLoghubInfoLogHubStoresLogHubStore()
                self.log_hub_store.append(temp_model.from_map(k))
        return self


class DescribeLoghubDetailResponseBodyLoghubInfo(TeaModel):
    def __init__(self, access_key=None, access_secret=None, dbcluster_id=None, dbtype=None, deliver_name=None,
                 deliver_time=None, description=None, domain_url=None, filter_dirty_data=None, log_hub_stores=None,
                 log_store_name=None, password=None, project_name=None, region_id=None, schema_name=None, table_name=None,
                 user_name=None, zone_id=None):
        self.access_key = access_key  # type: str
        self.access_secret = access_secret  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbtype = dbtype  # type: str
        self.deliver_name = deliver_name  # type: str
        self.deliver_time = deliver_time  # type: str
        self.description = description  # type: str
        self.domain_url = domain_url  # type: str
        self.filter_dirty_data = filter_dirty_data  # type: bool
        self.log_hub_stores = log_hub_stores  # type: DescribeLoghubDetailResponseBodyLoghubInfoLogHubStores
        self.log_store_name = log_store_name  # type: str
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.user_name = user_name  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.log_hub_stores:
            self.log_hub_stores.validate()

    def to_map(self):
        _map = super(DescribeLoghubDetailResponseBodyLoghubInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.deliver_name is not None:
            result['DeliverName'] = self.deliver_name
        if self.deliver_time is not None:
            result['DeliverTime'] = self.deliver_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_url is not None:
            result['DomainUrl'] = self.domain_url
        if self.filter_dirty_data is not None:
            result['FilterDirtyData'] = self.filter_dirty_data
        if self.log_hub_stores is not None:
            result['LogHubStores'] = self.log_hub_stores.to_map()
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DeliverName') is not None:
            self.deliver_name = m.get('DeliverName')
        if m.get('DeliverTime') is not None:
            self.deliver_time = m.get('DeliverTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainUrl') is not None:
            self.domain_url = m.get('DomainUrl')
        if m.get('FilterDirtyData') is not None:
            self.filter_dirty_data = m.get('FilterDirtyData')
        if m.get('LogHubStores') is not None:
            temp_model = DescribeLoghubDetailResponseBodyLoghubInfoLogHubStores()
            self.log_hub_stores = temp_model.from_map(m['LogHubStores'])
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeLoghubDetailResponseBody(TeaModel):
    def __init__(self, loghub_info=None, request_id=None):
        self.loghub_info = loghub_info  # type: DescribeLoghubDetailResponseBodyLoghubInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.loghub_info:
            self.loghub_info.validate()

    def to_map(self):
        _map = super(DescribeLoghubDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loghub_info is not None:
            result['LoghubInfo'] = self.loghub_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoghubInfo') is not None:
            temp_model = DescribeLoghubDetailResponseBodyLoghubInfo()
            self.loghub_info = temp_model.from_map(m['LoghubInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLoghubDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLoghubDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLoghubDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoghubDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLorneLogRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None, start_time=None,
                 task_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeLorneLogResponseBodyData(TeaModel):
    def __init__(self, code=None, count=None, end_time=None, message=None, start_time=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.end_time = end_time  # type: str
        self.message = message  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeLorneLogResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[DescribeLorneLogResponseBodyData]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLorneLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeLorneLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLorneLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLorneLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLorneLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLorneLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLorneTasksRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeLorneTasksResponseBodyTaskDetails(TeaModel):
    def __init__(self, checkpoint=None, column_mapper=None, create_time=None, description=None, id=None,
                 message=None, name=None, sink_instance=None, sink_region=None, sink_schema=None, sink_table=None,
                 sink_type=None, sink_user=None, sink_vpc_id=None, source_project=None, source_region=None, source_topic=None,
                 source_type=None, state=None, strict=None):
        self.checkpoint = checkpoint  # type: str
        self.column_mapper = column_mapper  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.sink_instance = sink_instance  # type: str
        self.sink_region = sink_region  # type: str
        self.sink_schema = sink_schema  # type: str
        self.sink_table = sink_table  # type: str
        self.sink_type = sink_type  # type: str
        self.sink_user = sink_user  # type: str
        self.sink_vpc_id = sink_vpc_id  # type: str
        self.source_project = source_project  # type: str
        self.source_region = source_region  # type: str
        self.source_topic = source_topic  # type: str
        self.source_type = source_type  # type: str
        self.state = state  # type: str
        self.strict = strict  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneTasksResponseBodyTaskDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.column_mapper is not None:
            result['ColumnMapper'] = self.column_mapper
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.sink_instance is not None:
            result['SinkInstance'] = self.sink_instance
        if self.sink_region is not None:
            result['SinkRegion'] = self.sink_region
        if self.sink_schema is not None:
            result['SinkSchema'] = self.sink_schema
        if self.sink_table is not None:
            result['SinkTable'] = self.sink_table
        if self.sink_type is not None:
            result['SinkType'] = self.sink_type
        if self.sink_user is not None:
            result['SinkUser'] = self.sink_user
        if self.sink_vpc_id is not None:
            result['SinkVpcId'] = self.sink_vpc_id
        if self.source_project is not None:
            result['SourceProject'] = self.source_project
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.source_topic is not None:
            result['SourceTopic'] = self.source_topic
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.state is not None:
            result['State'] = self.state
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ColumnMapper') is not None:
            self.column_mapper = m.get('ColumnMapper')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SinkInstance') is not None:
            self.sink_instance = m.get('SinkInstance')
        if m.get('SinkRegion') is not None:
            self.sink_region = m.get('SinkRegion')
        if m.get('SinkSchema') is not None:
            self.sink_schema = m.get('SinkSchema')
        if m.get('SinkTable') is not None:
            self.sink_table = m.get('SinkTable')
        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')
        if m.get('SinkUser') is not None:
            self.sink_user = m.get('SinkUser')
        if m.get('SinkVpcId') is not None:
            self.sink_vpc_id = m.get('SinkVpcId')
        if m.get('SourceProject') is not None:
            self.source_project = m.get('SourceProject')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('SourceTopic') is not None:
            self.source_topic = m.get('SourceTopic')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class DescribeLorneTasksResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, task_details=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.task_details = task_details  # type: list[DescribeLorneTasksResponseBodyTaskDetails]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.task_details:
            for k in self.task_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLorneTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskDetails'] = []
        if self.task_details is not None:
            for k in self.task_details:
                result['TaskDetails'].append(k.to_map() if k else None)
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
        self.task_details = []
        if m.get('TaskDetails') is not None:
            for k in m.get('TaskDetails'):
                temp_model = DescribeLorneTasksResponseBodyTaskDetails()
                self.task_details.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLorneTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLorneTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLorneTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLorneTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLorneTasksMCountRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, metric_name=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, start_time=None, task_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.metric_name = metric_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneTasksMCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeLorneTasksMCountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: float
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneTasksMCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLorneTasksMCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLorneTasksMCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLorneTasksMCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLorneTasksMCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLorneTasksMetricsRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, metric_name=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, start_time=None, task_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.metric_name = metric_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneTasksMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeLorneTasksMetricsResponseBodyData(TeaModel):
    def __init__(self, columns=None, name=None, task_id=None, values=None):
        self.columns = columns  # type: list[str]
        self.name = name  # type: str
        self.task_id = task_id  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLorneTasksMetricsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns
        if self.name is not None:
            result['Name'] = self.name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeLorneTasksMetricsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeLorneTasksMetricsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeLorneTasksMetricsResponseBody, self).to_map()
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
            temp_model = DescribeLorneTasksMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLorneTasksMetricsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLorneTasksMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLorneTasksMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLorneTasksMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOSSStorageRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOSSStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeOSSStorageResponseBody(TeaModel):
    def __init__(self, cold_storage=None, policy=None, request_id=None, state=None, storage_usage=None):
        self.cold_storage = cold_storage  # type: bool
        self.policy = policy  # type: str
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.storage_usage = storage_usage  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOSSStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.storage_usage is not None:
            result['StorageUsage'] = self.storage_usage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StorageUsage') is not None:
            self.storage_usage = m.get('StorageUsage')
        return self


class DescribeOSSStorageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeOSSStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOSSStorageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOSSStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessListRequest(TeaModel):
    def __init__(self, dbcluster_id=None, initial_query_id=None, initial_user=None, keyword=None, order=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, query_duration_ms=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.initial_query_id = initial_query_id  # type: str
        self.initial_user = initial_user  # type: str
        self.keyword = keyword  # type: str
        self.order = order  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_duration_ms = query_duration_ms  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProcessListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeProcessListResponseBodyProcessListDataResultSet(TeaModel):
    def __init__(self, initial_address=None, initial_query_id=None, initial_user=None, query=None,
                 query_duration_ms=None, query_start_time=None):
        self.initial_address = initial_address  # type: str
        self.initial_query_id = initial_query_id  # type: str
        self.initial_user = initial_user  # type: str
        self.query = query  # type: str
        self.query_duration_ms = query_duration_ms  # type: str
        self.query_start_time = query_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProcessListResponseBodyProcessListDataResultSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.query is not None:
            result['Query'] = self.query
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        return self


class DescribeProcessListResponseBodyProcessListData(TeaModel):
    def __init__(self, result_set=None):
        self.result_set = result_set  # type: list[DescribeProcessListResponseBodyProcessListDataResultSet]

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProcessListResponseBodyProcessListData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeProcessListResponseBodyProcessListDataResultSet()
                self.result_set.append(temp_model.from_map(k))
        return self


class DescribeProcessListResponseBodyProcessListStatistics(TeaModel):
    def __init__(self, bytes_read=None, elapsed_time=None, rows_read=None):
        self.bytes_read = bytes_read  # type: int
        self.elapsed_time = elapsed_time  # type: float
        self.rows_read = rows_read  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProcessListResponseBodyProcessListStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_read is not None:
            result['BytesRead'] = self.bytes_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.rows_read is not None:
            result['RowsRead'] = self.rows_read
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BytesRead') is not None:
            self.bytes_read = m.get('BytesRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('RowsRead') is not None:
            self.rows_read = m.get('RowsRead')
        return self


class DescribeProcessListResponseBodyProcessListTableSchemaResultSet(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProcessListResponseBodyProcessListTableSchemaResultSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeProcessListResponseBodyProcessListTableSchema(TeaModel):
    def __init__(self, result_set=None):
        self.result_set = result_set  # type: list[DescribeProcessListResponseBodyProcessListTableSchemaResultSet]

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProcessListResponseBodyProcessListTableSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeProcessListResponseBodyProcessListTableSchemaResultSet()
                self.result_set.append(temp_model.from_map(k))
        return self


class DescribeProcessListResponseBodyProcessList(TeaModel):
    def __init__(self, data=None, rows=None, rows_before_limit_at_least=None, statistics=None, table_schema=None):
        self.data = data  # type: DescribeProcessListResponseBodyProcessListData
        self.rows = rows  # type: str
        self.rows_before_limit_at_least = rows_before_limit_at_least  # type: str
        self.statistics = statistics  # type: DescribeProcessListResponseBodyProcessListStatistics
        self.table_schema = table_schema  # type: DescribeProcessListResponseBodyProcessListTableSchema

    def validate(self):
        if self.data:
            self.data.validate()
        if self.statistics:
            self.statistics.validate()
        if self.table_schema:
            self.table_schema.validate()

    def to_map(self):
        _map = super(DescribeProcessListResponseBodyProcessList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.rows_before_limit_at_least is not None:
            result['RowsBeforeLimitAtLeast'] = self.rows_before_limit_at_least
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeProcessListResponseBodyProcessListData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('RowsBeforeLimitAtLeast') is not None:
            self.rows_before_limit_at_least = m.get('RowsBeforeLimitAtLeast')
        if m.get('Statistics') is not None:
            temp_model = DescribeProcessListResponseBodyProcessListStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        if m.get('TableSchema') is not None:
            temp_model = DescribeProcessListResponseBodyProcessListTableSchema()
            self.table_schema = temp_model.from_map(m['TableSchema'])
        return self


class DescribeProcessListResponseBody(TeaModel):
    def __init__(self, process_list=None, request_id=None):
        self.process_list = process_list  # type: DescribeProcessListResponseBodyProcessList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.process_list:
            self.process_list.validate()

    def to_map(self):
        _map = super(DescribeProcessListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process_list is not None:
            result['ProcessList'] = self.process_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProcessList') is not None:
            temp_model = DescribeProcessListResponseBodyProcessList()
            self.process_list = temp_model.from_map(m['ProcessList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProcessListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProcessListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProcessListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeProcessListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRDSTablesRequest(TeaModel):
    def __init__(self, db_cluster_id=None, owner_account=None, owner_id=None, rds_id=None, rds_password=None,
                 rds_port=None, rds_user_name=None, resource_owner_account=None, resource_owner_id=None, schema=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.rds_id = rds_id  # type: str
        self.rds_password = rds_password  # type: str
        self.rds_port = rds_port  # type: long
        self.rds_user_name = rds_user_name  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.schema = schema  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRDSTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password
        if self.rds_port is not None:
            result['RdsPort'] = self.rds_port
        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')
        if m.get('RdsPort') is not None:
            self.rds_port = m.get('RdsPort')
        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class DescribeRDSTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, tables=None):
        self.request_id = request_id  # type: str
        self.tables = tables  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRDSTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class DescribeRDSTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRDSTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRDSTablesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRDSTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRDSVpcRequest(TeaModel):
    def __init__(self, db_cluster_id=None, owner_account=None, owner_id=None, rds_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.rds_id = rds_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRDSVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRDSVpcResponseBody(TeaModel):
    def __init__(self, request_id=None, vpc_id=None):
        self.request_id = request_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRDSVpcResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeRDSVpcResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRDSVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRDSVpcResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRDSVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRDSschemasRequest(TeaModel):
    def __init__(self, db_cluster_id=None, owner_account=None, owner_id=None, rds_id=None, rds_password=None,
                 rds_port=None, rds_user_name=None, resource_owner_account=None, resource_owner_id=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.rds_id = rds_id  # type: str
        self.rds_password = rds_password  # type: str
        self.rds_port = rds_port  # type: long
        self.rds_user_name = rds_user_name  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRDSschemasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password
        if self.rds_port is not None:
            result['RdsPort'] = self.rds_port
        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')
        if m.get('RdsPort') is not None:
            self.rds_port = m.get('RdsPort')
        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRDSschemasResponseBody(TeaModel):
    def __init__(self, request_id=None, schemas=None):
        self.request_id = request_id  # type: str
        self.schemas = schemas  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRDSschemasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schemas is not None:
            result['Schemas'] = self.schemas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schemas') is not None:
            self.schemas = m.get('Schemas')
        return self


class DescribeRDSschemasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRDSschemasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRDSschemasResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRDSschemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(self, vpc_enabled=None, zone_id=None):
        self.vpc_enabled = vpc_enabled  # type: bool
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionZonesZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
    def __init__(self, region_id=None, zones=None):
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class DescribeSchemasRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSchemasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSchemasResponseBodyItemsSchema(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.schema_name = schema_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSchemasResponseBodyItemsSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeSchemasResponseBodyItems(TeaModel):
    def __init__(self, schema=None):
        self.schema = schema  # type: list[DescribeSchemasResponseBodyItemsSchema]

    def validate(self):
        if self.schema:
            for k in self.schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSchemasResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Schema'] = []
        if self.schema is not None:
            for k in self.schema:
                result['Schema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k in m.get('Schema'):
                temp_model = DescribeSchemasResponseBodyItemsSchema()
                self.schema.append(temp_model.from_map(k))
        return self


class DescribeSchemasResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeSchemasResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeSchemasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeSchemasResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSchemasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSchemasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSchemasResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, query_duration_ms=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_duration_ms = query_duration_ms  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogRecordsResponseBodySlowLogRecordsDataResultSet(TeaModel):
    def __init__(self, initial_address=None, initial_query_id=None, initial_user=None, memory_usage=None,
                 query=None, query_duration_ms=None, query_start_time=None, read_bytes=None, read_rows=None,
                 result_bytes=None, type=None):
        self.initial_address = initial_address  # type: str
        self.initial_query_id = initial_query_id  # type: str
        self.initial_user = initial_user  # type: str
        self.memory_usage = memory_usage  # type: str
        self.query = query  # type: str
        self.query_duration_ms = query_duration_ms  # type: str
        self.query_start_time = query_start_time  # type: str
        self.read_bytes = read_bytes  # type: str
        self.read_rows = read_rows  # type: str
        self.result_bytes = result_bytes  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodySlowLogRecordsDataResultSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage
        if self.query is not None:
            result['Query'] = self.query
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes
        if self.read_rows is not None:
            result['ReadRows'] = self.read_rows
        if self.result_bytes is not None:
            result['ResultBytes'] = self.result_bytes
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')
        if m.get('ReadRows') is not None:
            self.read_rows = m.get('ReadRows')
        if m.get('ResultBytes') is not None:
            self.result_bytes = m.get('ResultBytes')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSlowLogRecordsResponseBodySlowLogRecordsData(TeaModel):
    def __init__(self, result_set=None):
        self.result_set = result_set  # type: list[DescribeSlowLogRecordsResponseBodySlowLogRecordsDataResultSet]

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodySlowLogRecordsData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeSlowLogRecordsResponseBodySlowLogRecordsDataResultSet()
                self.result_set.append(temp_model.from_map(k))
        return self


class DescribeSlowLogRecordsResponseBodySlowLogRecordsStatistics(TeaModel):
    def __init__(self, bytes_read=None, elapsed_time=None, rows_read=None):
        self.bytes_read = bytes_read  # type: int
        self.elapsed_time = elapsed_time  # type: float
        self.rows_read = rows_read  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodySlowLogRecordsStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_read is not None:
            result['BytesRead'] = self.bytes_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.rows_read is not None:
            result['RowsRead'] = self.rows_read
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BytesRead') is not None:
            self.bytes_read = m.get('BytesRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('RowsRead') is not None:
            self.rows_read = m.get('RowsRead')
        return self


class DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchemaResultSet(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchemaResultSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchema(TeaModel):
    def __init__(self, result_set=None):
        self.result_set = result_set  # type: list[DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchemaResultSet]

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchemaResultSet()
                self.result_set.append(temp_model.from_map(k))
        return self


class DescribeSlowLogRecordsResponseBodySlowLogRecords(TeaModel):
    def __init__(self, data=None, rows=None, rows_before_limit_at_least=None, statistics=None, table_schema=None):
        self.data = data  # type: DescribeSlowLogRecordsResponseBodySlowLogRecordsData
        self.rows = rows  # type: str
        self.rows_before_limit_at_least = rows_before_limit_at_least  # type: str
        self.statistics = statistics  # type: DescribeSlowLogRecordsResponseBodySlowLogRecordsStatistics
        self.table_schema = table_schema  # type: DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchema

    def validate(self):
        if self.data:
            self.data.validate()
        if self.statistics:
            self.statistics.validate()
        if self.table_schema:
            self.table_schema.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodySlowLogRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.rows_before_limit_at_least is not None:
            result['RowsBeforeLimitAtLeast'] = self.rows_before_limit_at_least
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodySlowLogRecordsData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('RowsBeforeLimitAtLeast') is not None:
            self.rows_before_limit_at_least = m.get('RowsBeforeLimitAtLeast')
        if m.get('Statistics') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodySlowLogRecordsStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        if m.get('TableSchema') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchema()
            self.table_schema = temp_model.from_map(m['TableSchema'])
        return self


class DescribeSlowLogRecordsResponseBody(TeaModel):
    def __init__(self, request_id=None, slow_log_records=None):
        self.request_id = request_id  # type: str
        self.slow_log_records = slow_log_records  # type: DescribeSlowLogRecordsResponseBodySlowLogRecords

    def validate(self):
        if self.slow_log_records:
            self.slow_log_records.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slow_log_records is not None:
            result['SlowLogRecords'] = self.slow_log_records.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlowLogRecords') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodySlowLogRecords()
            self.slow_log_records = temp_model.from_map(m['SlowLogRecords'])
        return self


class DescribeSlowLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSlowLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSlowLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogTrendRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, owner_account=None, owner_id=None, query_duration_ms=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.query_duration_ms = query_duration_ms  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogTrendResponseBodySlowLogTrendDataResultSet(TeaModel):
    def __init__(self, avg_query_duration_ms=None, count=None, max_query_duration_ms=None,
                 min_query_duration_ms=None, query_start_time=None):
        self.avg_query_duration_ms = avg_query_duration_ms  # type: str
        self.count = count  # type: str
        self.max_query_duration_ms = max_query_duration_ms  # type: str
        self.min_query_duration_ms = min_query_duration_ms  # type: str
        self.query_start_time = query_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponseBodySlowLogTrendDataResultSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_query_duration_ms is not None:
            result['AvgQueryDurationMs'] = self.avg_query_duration_ms
        if self.count is not None:
            result['Count'] = self.count
        if self.max_query_duration_ms is not None:
            result['MaxQueryDurationMs'] = self.max_query_duration_ms
        if self.min_query_duration_ms is not None:
            result['MinQueryDurationMs'] = self.min_query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgQueryDurationMs') is not None:
            self.avg_query_duration_ms = m.get('AvgQueryDurationMs')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('MaxQueryDurationMs') is not None:
            self.max_query_duration_ms = m.get('MaxQueryDurationMs')
        if m.get('MinQueryDurationMs') is not None:
            self.min_query_duration_ms = m.get('MinQueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        return self


class DescribeSlowLogTrendResponseBodySlowLogTrendData(TeaModel):
    def __init__(self, result_set=None):
        self.result_set = result_set  # type: list[DescribeSlowLogTrendResponseBodySlowLogTrendDataResultSet]

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponseBodySlowLogTrendData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeSlowLogTrendResponseBodySlowLogTrendDataResultSet()
                self.result_set.append(temp_model.from_map(k))
        return self


class DescribeSlowLogTrendResponseBodySlowLogTrendStatistics(TeaModel):
    def __init__(self, bytes_read=None, elapsed_time=None, rows_read=None):
        self.bytes_read = bytes_read  # type: int
        self.elapsed_time = elapsed_time  # type: float
        self.rows_read = rows_read  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponseBodySlowLogTrendStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_read is not None:
            result['BytesRead'] = self.bytes_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.rows_read is not None:
            result['RowsRead'] = self.rows_read
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BytesRead') is not None:
            self.bytes_read = m.get('BytesRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('RowsRead') is not None:
            self.rows_read = m.get('RowsRead')
        return self


class DescribeSlowLogTrendResponseBodySlowLogTrendTableSchemaResultSet(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponseBodySlowLogTrendTableSchemaResultSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSlowLogTrendResponseBodySlowLogTrendTableSchema(TeaModel):
    def __init__(self, result_set=None):
        self.result_set = result_set  # type: list[DescribeSlowLogTrendResponseBodySlowLogTrendTableSchemaResultSet]

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponseBodySlowLogTrendTableSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeSlowLogTrendResponseBodySlowLogTrendTableSchemaResultSet()
                self.result_set.append(temp_model.from_map(k))
        return self


class DescribeSlowLogTrendResponseBodySlowLogTrend(TeaModel):
    def __init__(self, data=None, rows=None, rows_before_limit_at_least=None, statistics=None, table_schema=None):
        self.data = data  # type: DescribeSlowLogTrendResponseBodySlowLogTrendData
        self.rows = rows  # type: str
        self.rows_before_limit_at_least = rows_before_limit_at_least  # type: str
        self.statistics = statistics  # type: DescribeSlowLogTrendResponseBodySlowLogTrendStatistics
        self.table_schema = table_schema  # type: DescribeSlowLogTrendResponseBodySlowLogTrendTableSchema

    def validate(self):
        if self.data:
            self.data.validate()
        if self.statistics:
            self.statistics.validate()
        if self.table_schema:
            self.table_schema.validate()

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponseBodySlowLogTrend, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.rows_before_limit_at_least is not None:
            result['RowsBeforeLimitAtLeast'] = self.rows_before_limit_at_least
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSlowLogTrendResponseBodySlowLogTrendData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('RowsBeforeLimitAtLeast') is not None:
            self.rows_before_limit_at_least = m.get('RowsBeforeLimitAtLeast')
        if m.get('Statistics') is not None:
            temp_model = DescribeSlowLogTrendResponseBodySlowLogTrendStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        if m.get('TableSchema') is not None:
            temp_model = DescribeSlowLogTrendResponseBodySlowLogTrendTableSchema()
            self.table_schema = temp_model.from_map(m['TableSchema'])
        return self


class DescribeSlowLogTrendResponseBody(TeaModel):
    def __init__(self, request_id=None, slow_log_trend=None):
        self.request_id = request_id  # type: str
        self.slow_log_trend = slow_log_trend  # type: DescribeSlowLogTrendResponseBodySlowLogTrend

    def validate(self):
        if self.slow_log_trend:
            self.slow_log_trend.validate()

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slow_log_trend is not None:
            result['SlowLogTrend'] = self.slow_log_trend.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlowLogTrend') is not None:
            temp_model = DescribeSlowLogTrendResponseBodySlowLogTrend()
            self.slow_log_trend = temp_model.from_map(m['SlowLogTrend'])
        return self


class DescribeSlowLogTrendResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSlowLogTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlowLogTrendResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSlowLogTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynDbTablesRequest(TeaModel):
    def __init__(self, db_cluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, syn_db=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.syn_db = syn_db  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynDbTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.syn_db is not None:
            result['SynDb'] = self.syn_db
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SynDb') is not None:
            self.syn_db = m.get('SynDb')
        return self


class DescribeSynDbTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, tables=None):
        self.request_id = request_id  # type: str
        self.tables = tables  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynDbTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class DescribeSynDbTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSynDbTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSynDbTablesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSynDbTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynDbsRequest(TeaModel):
    def __init__(self, db_cluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynDbsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSynDbsResponseBodySynDbs(TeaModel):
    def __init__(self, error_msg=None, rds_id=None, rds_password=None, rds_user_name=None, syn_db=None,
                 syn_status=None):
        self.error_msg = error_msg  # type: str
        self.rds_id = rds_id  # type: str
        self.rds_password = rds_password  # type: str
        self.rds_user_name = rds_user_name  # type: str
        self.syn_db = syn_db  # type: str
        self.syn_status = syn_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynDbsResponseBodySynDbs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password
        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name
        if self.syn_db is not None:
            result['SynDb'] = self.syn_db
        if self.syn_status is not None:
            result['SynStatus'] = self.syn_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')
        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')
        if m.get('SynDb') is not None:
            self.syn_db = m.get('SynDb')
        if m.get('SynStatus') is not None:
            self.syn_status = m.get('SynStatus')
        return self


class DescribeSynDbsResponseBody(TeaModel):
    def __init__(self, request_id=None, syn_dbs=None):
        self.request_id = request_id  # type: str
        self.syn_dbs = syn_dbs  # type: list[DescribeSynDbsResponseBodySynDbs]

    def validate(self):
        if self.syn_dbs:
            for k in self.syn_dbs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynDbsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SynDbs'] = []
        if self.syn_dbs is not None:
            for k in self.syn_dbs:
                result['SynDbs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.syn_dbs = []
        if m.get('SynDbs') is not None:
            for k in m.get('SynDbs'):
                temp_model = DescribeSynDbsResponseBodySynDbs()
                self.syn_dbs.append(temp_model.from_map(k))
        return self


class DescribeSynDbsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSynDbsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSynDbsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSynDbsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTablesRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTablesResponseBodyItemsTable(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None, table_name=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTablesResponseBodyItemsTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTablesResponseBodyItems(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[DescribeTablesResponseBodyItemsTable]

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTablesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeTablesResponseBodyItemsTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeTablesResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeTablesResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeTablesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTablesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTransferHistoryRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTransferHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeTransferHistoryResponseBodyHistoryDetailsHistoryDetail(TeaModel):
    def __init__(self, progress=None, source_dbcluster=None, status=None, target_dbcluster=None):
        self.progress = progress  # type: str
        self.source_dbcluster = source_dbcluster  # type: str
        self.status = status  # type: str
        self.target_dbcluster = target_dbcluster  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTransferHistoryResponseBodyHistoryDetailsHistoryDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.source_dbcluster is not None:
            result['SourceDBCluster'] = self.source_dbcluster
        if self.status is not None:
            result['Status'] = self.status
        if self.target_dbcluster is not None:
            result['TargetDBCluster'] = self.target_dbcluster
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('SourceDBCluster') is not None:
            self.source_dbcluster = m.get('SourceDBCluster')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetDBCluster') is not None:
            self.target_dbcluster = m.get('TargetDBCluster')
        return self


class DescribeTransferHistoryResponseBodyHistoryDetails(TeaModel):
    def __init__(self, history_detail=None):
        self.history_detail = history_detail  # type: list[DescribeTransferHistoryResponseBodyHistoryDetailsHistoryDetail]

    def validate(self):
        if self.history_detail:
            for k in self.history_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTransferHistoryResponseBodyHistoryDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HistoryDetail'] = []
        if self.history_detail is not None:
            for k in self.history_detail:
                result['HistoryDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.history_detail = []
        if m.get('HistoryDetail') is not None:
            for k in m.get('HistoryDetail'):
                temp_model = DescribeTransferHistoryResponseBodyHistoryDetailsHistoryDetail()
                self.history_detail.append(temp_model.from_map(k))
        return self


class DescribeTransferHistoryResponseBody(TeaModel):
    def __init__(self, history_details=None, request_id=None):
        self.history_details = history_details  # type: DescribeTransferHistoryResponseBodyHistoryDetails
        self.request_id = request_id  # type: str

    def validate(self):
        if self.history_details:
            self.history_details.validate()

    def to_map(self):
        _map = super(DescribeTransferHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_details is not None:
            result['HistoryDetails'] = self.history_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HistoryDetails') is not None:
            temp_model = DescribeTransferHistoryResponseBodyHistoryDetails()
            self.history_details = temp_model.from_map(m['HistoryDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTransferHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTransferHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTransferHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTransferHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillProcessRequest(TeaModel):
    def __init__(self, dbcluster_id=None, initial_query_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.initial_query_id = initial_query_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillProcessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class KillProcessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillProcessResponseBody, self).to_map()
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


class KillProcessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: KillProcessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(KillProcessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = KillProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountAuthorityRequest(TeaModel):
    def __init__(self, account_name=None, allow_databases=None, allow_dictionaries=None, dbcluster_id=None,
                 ddl_authority=None, dml_authority=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, total_databases=None, total_dictionaries=None):
        self.account_name = account_name  # type: str
        self.allow_databases = allow_databases  # type: str
        self.allow_dictionaries = allow_dictionaries  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.ddl_authority = ddl_authority  # type: bool
        self.dml_authority = dml_authority  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.total_databases = total_databases  # type: str
        self.total_dictionaries = total_dictionaries  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountAuthorityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases
        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority
        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.total_databases is not None:
            result['TotalDatabases'] = self.total_databases
        if self.total_dictionaries is not None:
            result['TotalDictionaries'] = self.total_dictionaries
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')
        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')
        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TotalDatabases') is not None:
            self.total_databases = m.get('TotalDatabases')
        if m.get('TotalDictionaries') is not None:
            self.total_dictionaries = m.get('TotalDictionaries')
        return self


class ModifyAccountAuthorityResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountAuthorityResponseBody, self).to_map()
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


class ModifyAccountAuthorityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAccountAuthorityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccountAuthorityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAccountAuthorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, dbcluster_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountDescriptionResponseBody, self).to_map()
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


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAccountDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccountDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, backup_retention_period=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 preferred_backup_period=None, preferred_backup_time=None, resource_owner_account=None, resource_owner_id=None):
        self.backup_retention_period = backup_retention_period  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyResponseBody, self).to_map()
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


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBackupPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterRequest(TeaModel):
    def __init__(self, dbcluster_class=None, dbcluster_id=None, dbnode_group_count=None, dbnode_storage=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_class = dbcluster_class  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_group_count = dbnode_group_count  # type: str
        self.dbnode_storage = dbnode_storage  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterResponseBodyDBCluster(TeaModel):
    def __init__(self, db_cluster_id=None, order_id=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterResponseBodyDBCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['dbClusterId'] = self.db_cluster_id
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dbClusterId') is not None:
            self.db_cluster_id = m.get('dbClusterId')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ModifyDBClusterResponseBody(TeaModel):
    def __init__(self, dbcluster=None, request_id=None):
        self.dbcluster = dbcluster  # type: ModifyDBClusterResponseBodyDBCluster
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbcluster:
            self.dbcluster.validate()

    def to_map(self):
        _map = super(ModifyDBClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster is not None:
            result['DBCluster'] = self.dbcluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBCluster') is not None:
            temp_model = ModifyDBClusterResponseBodyDBCluster()
            self.dbcluster = temp_model.from_map(m['DBCluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterAccessWhiteListRequest(TeaModel):
    def __init__(self, dbcluster_iparray_attribute=None, dbcluster_iparray_name=None, dbcluster_id=None,
                 modify_mode=None, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_ips=None):
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute  # type: str
        self.dbcluster_iparray_name = dbcluster_iparray_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.modify_mode = modify_mode  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterAccessWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifyDBClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterAccessWhiteListResponseBody, self).to_map()
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


class ModifyDBClusterAccessWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterAccessWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterAccessWhiteListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterConfigRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, user_config=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class ModifyDBClusterConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterConfigResponseBody, self).to_map()
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


class ModifyDBClusterConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBClusterConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterDescriptionRequest(TeaModel):
    def __init__(self, dbcluster_description=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterDescriptionResponseBody, self).to_map()
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


class ModifyDBClusterDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBClusterDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterMaintainTimeRequest(TeaModel):
    def __init__(self, dbcluster_id=None, maintain_time=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.maintain_time = maintain_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMaintainTimeResponseBody, self).to_map()
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


class ModifyDBClusterMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterMaintainTimeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBClusterMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBConfigRequest(TeaModel):
    def __init__(self, config=None, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.config = config  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBConfigResponseBody, self).to_map()
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


class ModifyDBConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRDSToClickhouseDbRequest(TeaModel):
    def __init__(self, ck_password=None, ck_user_name=None, clickhouse_port=None, db_cluster_id=None,
                 limit_upper=None, owner_account=None, owner_id=None, rds_id=None, rds_password=None, rds_port=None,
                 rds_syn_db=None, rds_syn_tables=None, rds_user_name=None, rds_vpc_id=None, resource_owner_account=None,
                 resource_owner_id=None, skip_unsupported=None):
        self.ck_password = ck_password  # type: str
        self.ck_user_name = ck_user_name  # type: str
        self.clickhouse_port = clickhouse_port  # type: long
        self.db_cluster_id = db_cluster_id  # type: str
        self.limit_upper = limit_upper  # type: long
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.rds_id = rds_id  # type: str
        self.rds_password = rds_password  # type: str
        self.rds_port = rds_port  # type: long
        self.rds_syn_db = rds_syn_db  # type: str
        self.rds_syn_tables = rds_syn_tables  # type: str
        self.rds_user_name = rds_user_name  # type: str
        self.rds_vpc_id = rds_vpc_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.skip_unsupported = skip_unsupported  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRDSToClickhouseDbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ck_password is not None:
            result['CkPassword'] = self.ck_password
        if self.ck_user_name is not None:
            result['CkUserName'] = self.ck_user_name
        if self.clickhouse_port is not None:
            result['ClickhousePort'] = self.clickhouse_port
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.limit_upper is not None:
            result['LimitUpper'] = self.limit_upper
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password
        if self.rds_port is not None:
            result['RdsPort'] = self.rds_port
        if self.rds_syn_db is not None:
            result['RdsSynDb'] = self.rds_syn_db
        if self.rds_syn_tables is not None:
            result['RdsSynTables'] = self.rds_syn_tables
        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name
        if self.rds_vpc_id is not None:
            result['RdsVpcId'] = self.rds_vpc_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.skip_unsupported is not None:
            result['SkipUnsupported'] = self.skip_unsupported
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CkPassword') is not None:
            self.ck_password = m.get('CkPassword')
        if m.get('CkUserName') is not None:
            self.ck_user_name = m.get('CkUserName')
        if m.get('ClickhousePort') is not None:
            self.clickhouse_port = m.get('ClickhousePort')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('LimitUpper') is not None:
            self.limit_upper = m.get('LimitUpper')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')
        if m.get('RdsPort') is not None:
            self.rds_port = m.get('RdsPort')
        if m.get('RdsSynDb') is not None:
            self.rds_syn_db = m.get('RdsSynDb')
        if m.get('RdsSynTables') is not None:
            self.rds_syn_tables = m.get('RdsSynTables')
        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')
        if m.get('RdsVpcId') is not None:
            self.rds_vpc_id = m.get('RdsVpcId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SkipUnsupported') is not None:
            self.skip_unsupported = m.get('SkipUnsupported')
        return self


class ModifyRDSToClickhouseDbResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, status=None):
        self.error_code = error_code  # type: long
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRDSToClickhouseDbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyRDSToClickhouseDbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyRDSToClickhouseDbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRDSToClickhouseDbResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRDSToClickhouseDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateLogHubRequestLogHubStores(TeaModel):
    def __init__(self, field_key=None, log_key=None, type=None):
        self.field_key = field_key  # type: str
        self.log_key = log_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateLogHubRequestLogHubStores, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.log_key is not None:
            result['LogKey'] = self.log_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('LogKey') is not None:
            self.log_key = m.get('LogKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OperateLogHubRequest(TeaModel):
    def __init__(self, access_key=None, access_secret=None, create=None, dbcluster_id=None, deliver_name=None,
                 deliver_time=None, description=None, domain_url=None, filter_dirty_data=None, log_hub_stores=None,
                 log_store_name=None, owner_account=None, owner_id=None, password=None, project_name=None,
                 resource_owner_account=None, resource_owner_id=None, schema_name=None, table_name=None, task_id=None, use_lorne=None,
                 user_name=None):
        self.access_key = access_key  # type: str
        self.access_secret = access_secret  # type: str
        self.create = create  # type: bool
        self.dbcluster_id = dbcluster_id  # type: str
        self.deliver_name = deliver_name  # type: str
        self.deliver_time = deliver_time  # type: str
        self.description = description  # type: str
        self.domain_url = domain_url  # type: str
        self.filter_dirty_data = filter_dirty_data  # type: bool
        self.log_hub_stores = log_hub_stores  # type: list[OperateLogHubRequestLogHubStores]
        self.log_store_name = log_store_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.task_id = task_id  # type: str
        self.use_lorne = use_lorne  # type: bool
        self.user_name = user_name  # type: str

    def validate(self):
        if self.log_hub_stores:
            for k in self.log_hub_stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OperateLogHubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.create is not None:
            result['Create'] = self.create
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.deliver_name is not None:
            result['DeliverName'] = self.deliver_name
        if self.deliver_time is not None:
            result['DeliverTime'] = self.deliver_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_url is not None:
            result['DomainUrl'] = self.domain_url
        if self.filter_dirty_data is not None:
            result['FilterDirtyData'] = self.filter_dirty_data
        result['LogHubStores'] = []
        if self.log_hub_stores is not None:
            for k in self.log_hub_stores:
                result['LogHubStores'].append(k.to_map() if k else None)
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.use_lorne is not None:
            result['UseLorne'] = self.use_lorne
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DeliverName') is not None:
            self.deliver_name = m.get('DeliverName')
        if m.get('DeliverTime') is not None:
            self.deliver_time = m.get('DeliverTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainUrl') is not None:
            self.domain_url = m.get('DomainUrl')
        if m.get('FilterDirtyData') is not None:
            self.filter_dirty_data = m.get('FilterDirtyData')
        self.log_hub_stores = []
        if m.get('LogHubStores') is not None:
            for k in m.get('LogHubStores'):
                temp_model = OperateLogHubRequestLogHubStores()
                self.log_hub_stores.append(temp_model.from_map(k))
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UseLorne') is not None:
            self.use_lorne = m.get('UseLorne')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class OperateLogHubResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateLogHubResponseBody, self).to_map()
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


class OperateLogHubResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OperateLogHubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateLogHubResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperateLogHubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateLorneTaskStatusRequest(TeaModel):
    def __init__(self, dbcluster_id=None, lorne_status=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.lorne_status = lorne_status  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateLorneTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.lorne_status is not None:
            result['LorneStatus'] = self.lorne_status
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('LorneStatus') is not None:
            self.lorne_status = m.get('LorneStatus')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OperateLorneTaskStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateLorneTaskStatusResponseBody, self).to_map()
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


class OperateLorneTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OperateLorneTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateLorneTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperateLorneTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterPublicConnectionRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseClusterPublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReleaseClusterPublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseClusterPublicConnectionResponseBody, self).to_map()
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


class ReleaseClusterPublicConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseClusterPublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseClusterPublicConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, dbcluster_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountPasswordResponseBody, self).to_map()
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


class ResetAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetAccountPasswordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBody, self).to_map()
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


class RestartInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRDSTablesRequest(TeaModel):
    def __init__(self, db_cluster_id=None, owner_account=None, owner_id=None, rds_id=None, rds_password=None,
                 rds_port=None, rds_user_name=None, resource_owner_account=None, resource_owner_id=None, table_name=None):
        self.db_cluster_id = db_cluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.rds_id = rds_id  # type: str
        self.rds_password = rds_password  # type: str
        self.rds_port = rds_port  # type: long
        self.rds_user_name = rds_user_name  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchRDSTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rds_id is not None:
            result['RdsId'] = self.rds_id
        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password
        if self.rds_port is not None:
            result['RdsPort'] = self.rds_port
        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')
        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')
        if m.get('RdsPort') is not None:
            self.rds_port = m.get('RdsPort')
        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class SearchRDSTablesResponseBodySchemas(TeaModel):
    def __init__(self, db_name=None, tables=None):
        self.db_name = db_name  # type: str
        self.tables = tables  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchRDSTablesResponseBodySchemas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class SearchRDSTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, schemas=None):
        self.request_id = request_id  # type: str
        self.schemas = schemas  # type: list[SearchRDSTablesResponseBodySchemas]

    def validate(self):
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchRDSTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['Schemas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schemas = []
        if m.get('Schemas') is not None:
            for k in m.get('Schemas'):
                temp_model = SearchRDSTablesResponseBodySchemas()
                self.schemas.append(temp_model.from_map(k))
        return self


class SearchRDSTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SearchRDSTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchRDSTablesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchRDSTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferVersionRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, source_account=None,
                 source_password=None, target_account=None, target_db_cluster_id=None, target_password=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.source_account = source_account  # type: str
        self.source_password = source_password  # type: str
        self.target_account = target_account  # type: str
        self.target_db_cluster_id = target_db_cluster_id  # type: str
        self.target_password = target_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_account is not None:
            result['SourceAccount'] = self.source_account
        if self.source_password is not None:
            result['SourcePassword'] = self.source_password
        if self.target_account is not None:
            result['TargetAccount'] = self.target_account
        if self.target_db_cluster_id is not None:
            result['TargetDbClusterId'] = self.target_db_cluster_id
        if self.target_password is not None:
            result['TargetPassword'] = self.target_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceAccount') is not None:
            self.source_account = m.get('SourceAccount')
        if m.get('SourcePassword') is not None:
            self.source_password = m.get('SourcePassword')
        if m.get('TargetAccount') is not None:
            self.target_account = m.get('TargetAccount')
        if m.get('TargetDbClusterId') is not None:
            self.target_db_cluster_id = m.get('TargetDbClusterId')
        if m.get('TargetPassword') is not None:
            self.target_password = m.get('TargetPassword')
        return self


class TransferVersionResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_name=None, request_id=None, task_id=None):
        self.dbinstance_id = dbinstance_id  # type: int
        self.dbinstance_name = dbinstance_name  # type: long
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TransferVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TransferVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TransferVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


