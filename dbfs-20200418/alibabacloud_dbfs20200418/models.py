# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateConstantsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, constants_data=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.constants_data = constants_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConstantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class CreateConstantsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, page_size=None, total_count=None, page_number=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConstantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class CreateConstantsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateConstantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConstantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDbfsRequest(TeaModel):
    def __init__(self, fs_id=None, region_id=None):
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDbfsRequest, self).to_map()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConstantsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, constants_data=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.constants_data = constants_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConstantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class DeleteConstantsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, page_size=None, total_count=None, page_number=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConstantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DeleteConstantsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteConstantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConstantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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


class ResizeDbfsRequest(TeaModel):
    def __init__(self, region_id=None, fs_id=None, new_size_g=None):
        self.region_id = region_id  # type: str
        self.fs_id = fs_id  # type: str
        self.new_size_g = new_size_g  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.new_size_g is not None:
            result['NewSizeG'] = self.new_size_g
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('NewSizeG') is not None:
            self.new_size_g = m.get('NewSizeG')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResizeDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResizeDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishUpgradeTaskRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, batch_strategy_list=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.batch_strategy_list = batch_strategy_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishUpgradeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.batch_strategy_list is not None:
            result['BatchStrategyList'] = self.batch_strategy_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BatchStrategyList') is not None:
            self.batch_strategy_list = m.get('BatchStrategyList')
        return self


class PublishUpgradeTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishUpgradeTaskResponseBody, self).to_map()
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


class PublishUpgradeTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PublishUpgradeTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishUpgradeTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishUpgradeTaskResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagValuesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, snapshot_id=None, force=None):
        self.region_id = region_id  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDbfsRequest(TeaModel):
    def __init__(self, fs_id=None, ecsinstance_id=None, region_id=None):
        self.fs_id = fs_id  # type: str
        self.ecsinstance_id = ecsinstance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUpgradeRecordRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, batch_strategy_list=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.batch_strategy_list = batch_strategy_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUpgradeRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.batch_strategy_list is not None:
            result['BatchStrategyList'] = self.batch_strategy_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BatchStrategyList') is not None:
            self.batch_strategy_list = m.get('BatchStrategyList')
        return self


class GenerateUpgradeRecordResponseBodyRecords(TeaModel):
    def __init__(self, id=None, batch_strategy_no=None, account_id=None, dbfs_id=None, ecs_id=None, task_id=None,
                 region_id=None, zone_id=None, state=None, current_version=None, target_version=None, upgrade_start_time=None,
                 upgrade_end_time=None, task_execution_counts=None, task_error_reason=None, create_time=None, update_time=None):
        self.id = id  # type: long
        self.batch_strategy_no = batch_strategy_no  # type: str
        self.account_id = account_id  # type: str
        self.dbfs_id = dbfs_id  # type: str
        self.ecs_id = ecs_id  # type: str
        self.task_id = task_id  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str
        self.state = state  # type: str
        self.current_version = current_version  # type: str
        self.target_version = target_version  # type: str
        self.upgrade_start_time = upgrade_start_time  # type: long
        self.upgrade_end_time = upgrade_end_time  # type: long
        self.task_execution_counts = task_execution_counts  # type: int
        self.task_error_reason = task_error_reason  # type: str
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUpgradeRecordResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.batch_strategy_no is not None:
            result['BatchStrategyNo'] = self.batch_strategy_no
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.state is not None:
            result['State'] = self.state
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.upgrade_start_time is not None:
            result['UpgradeStartTime'] = self.upgrade_start_time
        if self.upgrade_end_time is not None:
            result['UpgradeEndTime'] = self.upgrade_end_time
        if self.task_execution_counts is not None:
            result['TaskExecutionCounts'] = self.task_execution_counts
        if self.task_error_reason is not None:
            result['TaskErrorReason'] = self.task_error_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BatchStrategyNo') is not None:
            self.batch_strategy_no = m.get('BatchStrategyNo')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('UpgradeStartTime') is not None:
            self.upgrade_start_time = m.get('UpgradeStartTime')
        if m.get('UpgradeEndTime') is not None:
            self.upgrade_end_time = m.get('UpgradeEndTime')
        if m.get('TaskExecutionCounts') is not None:
            self.task_execution_counts = m.get('TaskExecutionCounts')
        if m.get('TaskErrorReason') is not None:
            self.task_error_reason = m.get('TaskErrorReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GenerateUpgradeRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, records=None):
        self.request_id = request_id  # type: str
        self.records = records  # type: list[GenerateUpgradeRecordResponseBodyRecords]

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateUpgradeRecordResponseBody, self).to_map()
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
                temp_model = GenerateUpgradeRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GenerateUpgradeRecordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateUpgradeRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUpgradeRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateUpgradeRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDbfsRequest(TeaModel):
    def __init__(self, region_id=None, fs_id=None, snapshot_id=None):
        self.region_id = region_id  # type: str
        self.fs_id = fs_id  # type: str
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetDbfsResponseBody, self).to_map()
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


class ResetDbfsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetDbfsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDbfsRequest(TeaModel):
    def __init__(self, region_id=None, fs_id=None):
        self.region_id = region_id  # type: str
        self.fs_id = fs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        return self


class GetDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(self, tag_value=None, id=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.id = id  # type: int
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDbfsResponseBodyDBFSInfoTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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


class GetDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(self, status=None, pay_type=None, fs_id=None, tags=None, size_g=None, ecs_list=None, region_id=None,
                 dbfscluster_id=None, description=None, zone_id=None, fs_name=None, category=None, created_time=None,
                 attach_node_number=None, kmskey_id=None, encryption=None, performance_level=None, used_scene=None,
                 last_mount_time=None, last_umount_time=None, enable_raid=None, raid_strip=None, ebs_list=None):
        self.status = status  # type: str
        self.pay_type = pay_type  # type: str
        self.fs_id = fs_id  # type: str
        self.tags = tags  # type: list[GetDbfsResponseBodyDBFSInfoTags]
        self.size_g = size_g  # type: int
        self.ecs_list = ecs_list  # type: list[GetDbfsResponseBodyDBFSInfoEcsList]
        self.region_id = region_id  # type: str
        self.dbfscluster_id = dbfscluster_id  # type: str
        self.description = description  # type: str
        self.zone_id = zone_id  # type: str
        self.fs_name = fs_name  # type: str
        self.category = category  # type: str
        self.created_time = created_time  # type: str
        self.attach_node_number = attach_node_number  # type: int
        self.kmskey_id = kmskey_id  # type: str
        self.encryption = encryption  # type: bool
        self.performance_level = performance_level  # type: str
        self.used_scene = used_scene  # type: str
        self.last_mount_time = last_mount_time  # type: str
        self.last_umount_time = last_umount_time  # type: str
        self.enable_raid = enable_raid  # type: bool
        self.raid_strip = raid_strip  # type: int
        self.ebs_list = ebs_list  # type: list[GetDbfsResponseBodyDBFSInfoEbsList]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDbfsResponseBodyDBFSInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        return self


class GetDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None, dbfsinfo=None):
        self.request_id = request_id  # type: str
        self.dbfsinfo = dbfsinfo  # type: GetDbfsResponseBodyDBFSInfo

    def validate(self):
        if self.dbfsinfo:
            self.dbfsinfo.validate()

    def to_map(self):
        _map = super(GetDbfsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbfsinfo is not None:
            result['DBFSInfo'] = self.dbfsinfo.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBFSInfo') is not None:
            temp_model = GetDbfsResponseBodyDBFSInfo()
            self.dbfsinfo = temp_model.from_map(m['DBFSInfo'])
        return self


class GetDbfsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DbfsRecordRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, data=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DbfsRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DbfsRecordResponseBodyRecords(TeaModel):
    def __init__(self, id=None, batch_strategy_no=None, account_id=None, dbfs_id=None, ecs_id=None, task_id=None,
                 region_id=None, zone_id=None, state=None, current_version=None, target_version=None, upgrade_start_time=None,
                 upgrade_end_time=None, task_execution_counts=None, task_error_reason=None, create_time=None, update_time=None,
                 is_del=None):
        self.id = id  # type: long
        self.batch_strategy_no = batch_strategy_no  # type: str
        self.account_id = account_id  # type: str
        self.dbfs_id = dbfs_id  # type: str
        self.ecs_id = ecs_id  # type: str
        self.task_id = task_id  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str
        self.state = state  # type: str
        self.current_version = current_version  # type: str
        self.target_version = target_version  # type: str
        self.upgrade_start_time = upgrade_start_time  # type: long
        self.upgrade_end_time = upgrade_end_time  # type: long
        self.task_execution_counts = task_execution_counts  # type: int
        self.task_error_reason = task_error_reason  # type: str
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long
        self.is_del = is_del  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DbfsRecordResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.batch_strategy_no is not None:
            result['BatchStrategyNo'] = self.batch_strategy_no
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.state is not None:
            result['State'] = self.state
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        if self.upgrade_start_time is not None:
            result['UpgradeStartTime'] = self.upgrade_start_time
        if self.upgrade_end_time is not None:
            result['UpgradeEndTime'] = self.upgrade_end_time
        if self.task_execution_counts is not None:
            result['TaskExecutionCounts'] = self.task_execution_counts
        if self.task_error_reason is not None:
            result['TaskErrorReason'] = self.task_error_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.is_del is not None:
            result['IsDel'] = self.is_del
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BatchStrategyNo') is not None:
            self.batch_strategy_no = m.get('BatchStrategyNo')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        if m.get('UpgradeStartTime') is not None:
            self.upgrade_start_time = m.get('UpgradeStartTime')
        if m.get('UpgradeEndTime') is not None:
            self.upgrade_end_time = m.get('UpgradeEndTime')
        if m.get('TaskExecutionCounts') is not None:
            self.task_execution_counts = m.get('TaskExecutionCounts')
        if m.get('TaskErrorReason') is not None:
            self.task_error_reason = m.get('TaskErrorReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IsDel') is not None:
            self.is_del = m.get('IsDel')
        return self


class DbfsRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, records=None, page_no=None, page_size=None, total=None):
        self.request_id = request_id  # type: str
        self.records = records  # type: list[DbfsRecordResponseBodyRecords]
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DbfsRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DbfsRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DbfsRecordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DbfsRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DbfsRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DbfsRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopUpgradeTaskRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, batch_strategy_list=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.batch_strategy_list = batch_strategy_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopUpgradeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.batch_strategy_list is not None:
            result['BatchStrategyList'] = self.batch_strategy_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BatchStrategyList') is not None:
            self.batch_strategy_list = m.get('BatchStrategyList')
        return self


class StopUpgradeTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopUpgradeTaskResponseBody, self).to_map()
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


class StopUpgradeTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopUpgradeTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopUpgradeTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopUpgradeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDbfsRequest(TeaModel):
    def __init__(self, region_id=None, fs_name=None, category=None, size_g=None, zone_id=None, client_token=None,
                 snapshot_id=None, delete_snapshot=None, performance_level=None, enable_raid=None,
                 raid_stripe_unit_number=None, kmskey_id=None, encryption=None, used_scene=None, instance_type=None):
        self.region_id = region_id  # type: str
        self.fs_name = fs_name  # type: str
        self.category = category  # type: str
        self.size_g = size_g  # type: int
        self.zone_id = zone_id  # type: str
        self.client_token = client_token  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.delete_snapshot = delete_snapshot  # type: bool
        self.performance_level = performance_level  # type: str
        self.enable_raid = enable_raid  # type: bool
        self.raid_stripe_unit_number = raid_stripe_unit_number  # type: int
        self.kmskey_id = kmskey_id  # type: str
        self.encryption = encryption  # type: bool
        self.used_scene = used_scene  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.category is not None:
            result['Category'] = self.category
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.delete_snapshot is not None:
            result['DeleteSnapshot'] = self.delete_snapshot
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.raid_stripe_unit_number is not None:
            result['RaidStripeUnitNumber'] = self.raid_stripe_unit_number
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('DeleteSnapshot') is not None:
            self.delete_snapshot = m.get('DeleteSnapshot')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('RaidStripeUnitNumber') is not None:
            self.raid_stripe_unit_number = m.get('RaidStripeUnitNumber')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None, fs_id=None):
        self.request_id = request_id  # type: str
        self.fs_id = fs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDbfsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        return self


class CreateDbfsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskRequest(TeaModel):
    def __init__(self, region_id=None, task_ids=None, task_progress=None):
        self.region_id = region_id  # type: str
        self.task_ids = task_ids  # type: str
        self.task_progress = task_progress  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')
        return self


class UpdateTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskResponseBody, self).to_map()
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


class UpdateTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagsBatchRequest(TeaModel):
    def __init__(self, region_id=None, dbfs_list=None, tags=None):
        self.region_id = region_id  # type: str
        self.dbfs_list = dbfs_list  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagsBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTagsBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTagsBatchResponseBody()
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
    def __init__(self, account_id=None, request_id=None, dbfs_linked_role=None, region_id=None):
        self.account_id = account_id  # type: str
        self.request_id = request_id  # type: str
        self.dbfs_linked_role = dbfs_linked_role  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbfs_linked_role is not None:
            result['DbfsLinkedRole'] = self.dbfs_linked_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DbfsLinkedRole') is not None:
            self.dbfs_linked_role = m.get('DbfsLinkedRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConstantsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, constants_data=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.constants_data = constants_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConstantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class UpdateConstantsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, page_size=None, total_count=None, page_number=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConstantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class UpdateConstantsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateConstantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConstantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertSynchronizConstantsRequest(TeaModel):
    def __init__(self, region_id=None, access_data=None, endpoint_data=None, master_data=None,
                 product_code_data=None, osversion_data=None, zone_data=None, region_data=None, page_number=None, page_size=None):
        self.region_id = region_id  # type: str
        self.access_data = access_data  # type: str
        self.endpoint_data = endpoint_data  # type: str
        self.master_data = master_data  # type: str
        self.product_code_data = product_code_data  # type: str
        self.osversion_data = osversion_data  # type: str
        self.zone_data = zone_data  # type: str
        self.region_data = region_data  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertSynchronizConstantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.access_data is not None:
            result['AccessData'] = self.access_data
        if self.endpoint_data is not None:
            result['EndpointData'] = self.endpoint_data
        if self.master_data is not None:
            result['MasterData'] = self.master_data
        if self.product_code_data is not None:
            result['ProductCodeData'] = self.product_code_data
        if self.osversion_data is not None:
            result['OsversionData'] = self.osversion_data
        if self.zone_data is not None:
            result['ZoneData'] = self.zone_data
        if self.region_data is not None:
            result['RegionData'] = self.region_data
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AccessData') is not None:
            self.access_data = m.get('AccessData')
        if m.get('EndpointData') is not None:
            self.endpoint_data = m.get('EndpointData')
        if m.get('MasterData') is not None:
            self.master_data = m.get('MasterData')
        if m.get('ProductCodeData') is not None:
            self.product_code_data = m.get('ProductCodeData')
        if m.get('OsversionData') is not None:
            self.osversion_data = m.get('OsversionData')
        if m.get('ZoneData') is not None:
            self.zone_data = m.get('ZoneData')
        if m.get('RegionData') is not None:
            self.region_data = m.get('RegionData')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class InsertSynchronizConstantsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, page_size=None, total_count=None, page_number=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertSynchronizConstantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class InsertSynchronizConstantsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertSynchronizConstantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertSynchronizConstantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InsertSynchronizConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDbfsRequest(TeaModel):
    def __init__(self, ecsinstance_id=None, server_url=None, fs_id=None, region_id=None, attach_mode=None,
                 attach_point=None):
        self.ecsinstance_id = ecsinstance_id  # type: str
        self.server_url = server_url  # type: str
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str
        self.attach_mode = attach_mode  # type: str
        self.attach_point = attach_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.attach_mode is not None:
            result['AttachMode'] = self.attach_mode
        if self.attach_point is not None:
            result['AttachPoint'] = self.attach_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AttachMode') is not None:
            self.attach_mode = m.get('AttachMode')
        if m.get('AttachPoint') is not None:
            self.attach_point = m.get('AttachPoint')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, sort_key=None, sort_type=None,
                 filter_key=None, filter_value=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_key = sort_key  # type: str
        self.sort_type = sort_type  # type: str
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        return self


class ListTaskResponseBodyTasks(TeaModel):
    def __init__(self, task_error_reason=None, task_name=None, priority=None, next_execution_time=None,
                 completion_time=None, task_type=None, task_status=None, task_status_code=None, task_execution_counts=None,
                 client_token=None, task_adder=None, task_progress_description=None, created_time=None, task_runner=None,
                 task_progress=None, task_owner=None, id=None, max_retry=None):
        self.task_error_reason = task_error_reason  # type: str
        self.task_name = task_name  # type: str
        self.priority = priority  # type: str
        self.next_execution_time = next_execution_time  # type: str
        self.completion_time = completion_time  # type: str
        self.task_type = task_type  # type: str
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_execution_counts = task_execution_counts  # type: int
        self.client_token = client_token  # type: str
        self.task_adder = task_adder  # type: str
        self.task_progress_description = task_progress_description  # type: str
        self.created_time = created_time  # type: str
        self.task_runner = task_runner  # type: str
        self.task_progress = task_progress  # type: int
        self.task_owner = task_owner  # type: str
        self.id = id  # type: int
        self.max_retry = max_retry  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_error_reason is not None:
            result['TaskErrorReason'] = self.task_error_reason
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.next_execution_time is not None:
            result['NextExecutionTime'] = self.next_execution_time
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_execution_counts is not None:
            result['TaskExecutionCounts'] = self.task_execution_counts
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_adder is not None:
            result['TaskAdder'] = self.task_adder
        if self.task_progress_description is not None:
            result['TaskProgressDescription'] = self.task_progress_description
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.task_runner is not None:
            result['TaskRunner'] = self.task_runner
        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress
        if self.task_owner is not None:
            result['TaskOwner'] = self.task_owner
        if self.id is not None:
            result['Id'] = self.id
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskErrorReason') is not None:
            self.task_error_reason = m.get('TaskErrorReason')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('NextExecutionTime') is not None:
            self.next_execution_time = m.get('NextExecutionTime')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskExecutionCounts') is not None:
            self.task_execution_counts = m.get('TaskExecutionCounts')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskAdder') is not None:
            self.task_adder = m.get('TaskAdder')
        if m.get('TaskProgressDescription') is not None:
            self.task_progress_description = m.get('TaskProgressDescription')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('TaskRunner') is not None:
            self.task_runner = m.get('TaskRunner')
        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')
        if m.get('TaskOwner') is not None:
            self.task_owner = m.get('TaskOwner')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        return self


class ListTaskResponseBody(TeaModel):
    def __init__(self, total_count=None, tasks=None, page_size=None, request_id=None, page_number=None):
        self.total_count = total_count  # type: int
        self.tasks = tasks  # type: list[ListTaskResponseBodyTasks]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, sort_key=None, sort_type=None,
                 filter_key=None, filter_value=None, tags=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_key = sort_key  # type: str
        self.sort_type = sort_type  # type: str
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(self, tag_value=None, id=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.id = id  # type: long
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsResponseBodyDBFSInfoTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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


class ListDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(self, status=None, encryption=None, pay_type=None, fs_id=None, tags=None, size_g=None, ecs_list=None,
                 ebs_list=None, region_id=None, dbfscluster_id=None, zone_id=None, fs_name=None, category=None,
                 created_time=None, attach_node_number=None, kmskey_id=None, performance_level=None, used_scene=None,
                 last_mount_time=None, last_umount_time=None, enable_raid=None, raid_strip=None):
        self.status = status  # type: str
        self.encryption = encryption  # type: bool
        self.pay_type = pay_type  # type: str
        self.fs_id = fs_id  # type: str
        self.tags = tags  # type: list[ListDbfsResponseBodyDBFSInfoTags]
        self.size_g = size_g  # type: int
        self.ecs_list = ecs_list  # type: list[ListDbfsResponseBodyDBFSInfoEcsList]
        self.ebs_list = ebs_list  # type: list[ListDbfsResponseBodyDBFSInfoEbsList]
        self.region_id = region_id  # type: str
        self.dbfscluster_id = dbfscluster_id  # type: str
        self.zone_id = zone_id  # type: str
        self.fs_name = fs_name  # type: str
        self.category = category  # type: str
        self.created_time = created_time  # type: str
        self.attach_node_number = attach_node_number  # type: int
        self.kmskey_id = kmskey_id  # type: str
        self.performance_level = performance_level  # type: str
        self.used_scene = used_scene  # type: str
        self.last_mount_time = last_mount_time  # type: str
        self.last_umount_time = last_umount_time  # type: str
        self.enable_raid = enable_raid  # type: bool
        self.raid_strip = raid_strip  # type: int

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDbfsResponseBodyDBFSInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        return self


class ListDbfsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, dbfsinfo=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.dbfsinfo = dbfsinfo  # type: list[ListDbfsResponseBodyDBFSInfo]

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['DBFSInfo'] = []
        if self.dbfsinfo is not None:
            for k in self.dbfsinfo:
                result['DBFSInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.dbfsinfo = []
        if m.get('DBFSInfo') is not None:
            for k in m.get('DBFSInfo'):
                temp_model = ListDbfsResponseBodyDBFSInfo()
                self.dbfsinfo.append(temp_model.from_map(k))
        return self


class ListDbfsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTagsBatchRequest(TeaModel):
    def __init__(self, region_id=None, dbfs_list=None, tags=None, client_token=None):
        self.region_id = region_id  # type: str
        self.dbfs_list = dbfs_list  # type: str
        self.tags = tags  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTagsBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddTagsBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddTagsBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagDbfsRequest(TeaModel):
    def __init__(self, region_id=None, dbfs_id=None, tags=None):
        self.region_id = region_id  # type: str
        self.dbfs_id = dbfs_id  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSynchronizConstantsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSynchronizConstantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetSynchronizConstantsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, page_size=None, total_count=None, page_number=None,
                 region_data=None, zone_data=None, osversion_data=None, product_code_data=None, master_data=None,
                 endpoint_data=None, access_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_number = page_number  # type: long
        self.region_data = region_data  # type: str
        self.zone_data = zone_data  # type: str
        self.osversion_data = osversion_data  # type: str
        self.product_code_data = product_code_data  # type: str
        self.master_data = master_data  # type: str
        self.endpoint_data = endpoint_data  # type: str
        self.access_data = access_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSynchronizConstantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.region_data is not None:
            result['RegionData'] = self.region_data
        if self.zone_data is not None:
            result['ZoneData'] = self.zone_data
        if self.osversion_data is not None:
            result['OsversionData'] = self.osversion_data
        if self.product_code_data is not None:
            result['ProductCodeData'] = self.product_code_data
        if self.master_data is not None:
            result['MasterData'] = self.master_data
        if self.endpoint_data is not None:
            result['EndpointData'] = self.endpoint_data
        if self.access_data is not None:
            result['AccessData'] = self.access_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RegionData') is not None:
            self.region_data = m.get('RegionData')
        if m.get('ZoneData') is not None:
            self.zone_data = m.get('ZoneData')
        if m.get('OsversionData') is not None:
            self.osversion_data = m.get('OsversionData')
        if m.get('ProductCodeData') is not None:
            self.product_code_data = m.get('ProductCodeData')
        if m.get('MasterData') is not None:
            self.master_data = m.get('MasterData')
        if m.get('EndpointData') is not None:
            self.endpoint_data = m.get('EndpointData')
        if m.get('AccessData') is not None:
            self.access_data = m.get('AccessData')
        return self


class GetSynchronizConstantsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSynchronizConstantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSynchronizConstantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSynchronizConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpreateConstantsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, constants_data=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.constants_data = constants_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpreateConstantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class OpreateConstantsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, region_data=None, zone_data=None, osversion_data=None,
                 page_size=None, total_count=None, page_number=None, product_code_data=None, master_data=None,
                 endpoint_data=None, access_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.region_data = region_data  # type: str
        self.zone_data = zone_data  # type: str
        self.osversion_data = osversion_data  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_number = page_number  # type: long
        self.product_code_data = product_code_data  # type: str
        self.master_data = master_data  # type: str
        self.endpoint_data = endpoint_data  # type: str
        self.access_data = access_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpreateConstantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.region_data is not None:
            result['RegionData'] = self.region_data
        if self.zone_data is not None:
            result['ZoneData'] = self.zone_data
        if self.osversion_data is not None:
            result['OsversionData'] = self.osversion_data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.product_code_data is not None:
            result['ProductCodeData'] = self.product_code_data
        if self.master_data is not None:
            result['MasterData'] = self.master_data
        if self.endpoint_data is not None:
            result['EndpointData'] = self.endpoint_data
        if self.access_data is not None:
            result['AccessData'] = self.access_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RegionData') is not None:
            self.region_data = m.get('RegionData')
        if m.get('ZoneData') is not None:
            self.zone_data = m.get('ZoneData')
        if m.get('OsversionData') is not None:
            self.osversion_data = m.get('OsversionData')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ProductCodeData') is not None:
            self.product_code_data = m.get('ProductCodeData')
        if m.get('MasterData') is not None:
            self.master_data = m.get('MasterData')
        if m.get('EndpointData') is not None:
            self.endpoint_data = m.get('EndpointData')
        if m.get('AccessData') is not None:
            self.access_data = m.get('AccessData')
        return self


class OpreateConstantsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpreateConstantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpreateConstantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpreateConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDbfsRequest(TeaModel):
    def __init__(self, fs_name=None, fs_id=None, region_id=None):
        self.fs_name = fs_name  # type: str
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenameDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenameDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenameDbfsResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConstantsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, constants_data=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.constants_data = constants_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConstantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.constants_data is not None:
            result['ConstantsData'] = self.constants_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConstantsData') is not None:
            self.constants_data = m.get('ConstantsData')
        return self


class ListConstantsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, page_size=None, total_count=None, page_number=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConstantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListConstantsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConstantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConstantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConstantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, sort_key=None, sort_type=None,
                 filter_key=None, filter_value=None, fs_id=None, status=None, snapshot_name=None, snapshot_type=None,
                 snapshot_ids=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_key = sort_key  # type: str
        self.sort_type = sort_type  # type: str
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.fs_id = fs_id  # type: str
        self.status = status  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.snapshot_type = snapshot_type  # type: str
        self.snapshot_ids = snapshot_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.status is not None:
            result['Status'] = self.status
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        return self


class ListSnapshotResponseBodySnapshots(TeaModel):
    def __init__(self, status=None, creation_time=None, progress=None, source_fs_size=None, retention_days=None,
                 remain_time=None, last_modified_time=None, snapshot_type=None, snapshot_name=None, description=None,
                 source_fs_id=None, snapshot_id=None, category=None):
        self.status = status  # type: str
        self.creation_time = creation_time  # type: str
        self.progress = progress  # type: str
        self.source_fs_size = source_fs_size  # type: int
        self.retention_days = retention_days  # type: int
        self.remain_time = remain_time  # type: int
        self.last_modified_time = last_modified_time  # type: str
        self.snapshot_type = snapshot_type  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.description = description  # type: str
        self.source_fs_id = source_fs_id  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.category = category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.source_fs_size is not None:
            result['SourceFsSize'] = self.source_fs_size
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.source_fs_id is not None:
            result['SourceFsId'] = self.source_fs_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('SourceFsSize') is not None:
            self.source_fs_size = m.get('SourceFsSize')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceFsId') is not None:
            self.source_fs_id = m.get('SourceFsId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ListSnapshotResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, snapshots=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.snapshots = snapshots  # type: list[ListSnapshotResponseBodySnapshots]

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListSnapshotResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        return self


class ListSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbfsSpecificationsRequest(TeaModel):
    def __init__(self, region_id=None, ecs_instance_type=None, category=None):
        self.region_id = region_id  # type: str
        self.ecs_instance_type = ecs_instance_type  # type: str
        self.category = category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDbfsSpecificationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class DescribeDbfsSpecificationsResponseBody(TeaModel):
    def __init__(self, request_id=None, supported_ecs_instance_type_family=None, max_dbfs_number_per_ecs=None):
        self.request_id = request_id  # type: str
        self.supported_ecs_instance_type_family = supported_ecs_instance_type_family  # type: list[str]
        self.max_dbfs_number_per_ecs = max_dbfs_number_per_ecs  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDbfsSpecificationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supported_ecs_instance_type_family is not None:
            result['SupportedEcsInstanceTypeFamily'] = self.supported_ecs_instance_type_family
        if self.max_dbfs_number_per_ecs is not None:
            result['MaxDbfsNumberPerEcs'] = self.max_dbfs_number_per_ecs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportedEcsInstanceTypeFamily') is not None:
            self.supported_ecs_instance_type_family = m.get('SupportedEcsInstanceTypeFamily')
        if m.get('MaxDbfsNumberPerEcs') is not None:
            self.max_dbfs_number_per_ecs = m.get('MaxDbfsNumberPerEcs')
        return self


class DescribeDbfsSpecificationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDbfsSpecificationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDbfsSpecificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, fs_id=None, snapshot_name=None, description=None, retention_days=None,
                 client_token=None):
        self.region_id = region_id  # type: str
        self.fs_id = fs_id  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.description = description  # type: str
        self.retention_days = retention_days  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(self, snapshot_id=None, request_id=None):
        self.snapshot_id = snapshot_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


