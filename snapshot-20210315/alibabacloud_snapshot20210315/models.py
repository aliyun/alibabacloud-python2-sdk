# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetSnapshotInfoRequest(TeaModel):
    def __init__(self, client_token=None, snapshot_id=None, show_detail=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        # 待读取数据的快照名称
        self.snapshot_id = snapshot_id  # type: str
        # 是否返回详细信息，详细信息需要更多查询时间，默认为 False
        self.show_detail = show_detail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')
        return self


class GetSnapshotInfoResponseBody(TeaModel):
    def __init__(self, volume_size=None, block_size=None, block_count=None, valid_block_count=None, status=None,
                 create_time=None, encrypted=None):
        # 快照大小，单位 GB，最小 1GB
        self.volume_size = volume_size  # type: long
        # 快照数据快大小，单位 Bytes
        self.block_size = block_size  # type: long
        # 快照数据块总数量，包含空数据块
        self.block_count = block_count  # type: long
        # 快照中非空数据块总数量，仅在 ShowDetail 为 True 时返回
        self.valid_block_count = valid_block_count  # type: long
        # 快照状态。    "SNAPSHOT_INVALID",     "SNAPSHOT_PENDING",     "SNAPSHOT_COMMITTED",     "SNAPSHOT_DELETED"
        self.status = status  # type: str
        # 快照创建时间戳
        self.create_time = create_time  # type: long
        # 快照是否为加密快照
        self.encrypted = encrypted  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.volume_size is not None:
            result['VolumeSize'] = self.volume_size
        if self.block_size is not None:
            result['BlockSize'] = self.block_size
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.valid_block_count is not None:
            result['ValidBlockCount'] = self.valid_block_count
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VolumeSize') is not None:
            self.volume_size = m.get('VolumeSize')
        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('ValidBlockCount') is not None:
            self.valid_block_count = m.get('ValidBlockCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        return self


class GetSnapshotInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSnapshotInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSnapshotInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSnapshotInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSnapshotBlockRequest(TeaModel):
    def __init__(self, client_token=None, block_index=None, block_token=None, snapshot_id=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        # 待读取的数据块索引，从零开始。从 ListChangedBlocks 或者 ListSnapshotBlocks 返回。最大为快照数据块数量减一
        self.block_index = block_index  # type: long
        # 待读取的数据块Token，从 ListChangedBlocks 或者 ListSnapshotBlocks 返回，最大长度 256 字节
        self.block_token = block_token  # type: str
        # 待读取数据的快照名称，最大 256 字节
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotBlockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.block_index is not None:
            result['BlockIndex'] = self.block_index
        if self.block_token is not None:
            result['BlockToken'] = self.block_token
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BlockIndex') is not None:
            self.block_index = m.get('BlockIndex')
        if m.get('BlockToken') is not None:
            self.block_token = m.get('BlockToken')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class GetSnapshotBlockResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: READABLE

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(GetSnapshotBlockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ListSnapshotBlocksRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, client_token=None, snapshot_id=None,
                 starting_block_index=None):
        # 标记当前开始读取的位置，置空表示从 StartingBlockIndex 指定 Block 开始，最大长度 256 字节
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量，最小 100， 最大 10000， 默认为 100
        self.max_results = max_results  # type: long
        # 幂等参数
        self.client_token = client_token  # type: str
        # 待列出数据块的快照名称，最大 256 字节
        self.snapshot_id = snapshot_id  # type: str
        # 列出快照中数据块起始索引值，从零开始，最大值为快照数据块总数减一。NextToken 不为空时忽略此参数
        self.starting_block_index = starting_block_index  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotBlocksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.starting_block_index is not None:
            result['StartingBlockIndex'] = self.starting_block_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('StartingBlockIndex') is not None:
            self.starting_block_index = m.get('StartingBlockIndex')
        return self


class ListSnapshotBlocksResponseBodyBlocks(TeaModel):
    def __init__(self, block_index=None, block_token=None):
        # 数据块的索引值，从零开始
        self.block_index = block_index  # type: long
        # 数据块的 Token，用于后续的数据读取。最大长度 256 字节
        self.block_token = block_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotBlocksResponseBodyBlocks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_index is not None:
            result['BlockIndex'] = self.block_index
        if self.block_token is not None:
            result['BlockToken'] = self.block_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockIndex') is not None:
            self.block_index = m.get('BlockIndex')
        if m.get('BlockToken') is not None:
            self.block_token = m.get('BlockToken')
        return self


class ListSnapshotBlocksResponseBody(TeaModel):
    def __init__(self, next_token=None, blocks=None, expiry_time=None, volume_size=None, block_size=None,
                 block_count=None, total_block_count=None):
        # 返回下一个有效数据块 token，为空时代表无其他有效数据块，最大  256 字节
        self.next_token = next_token  # type: str
        # 快照有效数据块信息列表，不包含空数据块
        self.blocks = blocks  # type: list[ListSnapshotBlocksResponseBodyBlocks]
        # BlockToken 过期 UTC 时间戳, 单位微秒
        self.expiry_time = expiry_time  # type: long
        # 快照大小，单位 GB，最小 1GB
        self.volume_size = volume_size  # type: long
        # 数据块大小，单位 Byte
        self.block_size = block_size  # type: long
        # 本次查询中快照有效数据块数量
        self.block_count = block_count  # type: long
        # 快照有效数据块总数量
        self.total_block_count = total_block_count  # type: long

    def validate(self):
        if self.blocks:
            for k in self.blocks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSnapshotBlocksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Blocks'] = []
        if self.blocks is not None:
            for k in self.blocks:
                result['Blocks'].append(k.to_map() if k else None)
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.volume_size is not None:
            result['VolumeSize'] = self.volume_size
        if self.block_size is not None:
            result['BlockSize'] = self.block_size
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.total_block_count is not None:
            result['TotalBlockCount'] = self.total_block_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.blocks = []
        if m.get('Blocks') is not None:
            for k in m.get('Blocks'):
                temp_model = ListSnapshotBlocksResponseBodyBlocks()
                self.blocks.append(temp_model.from_map(k))
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('VolumeSize') is not None:
            self.volume_size = m.get('VolumeSize')
        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('TotalBlockCount') is not None:
            self.total_block_count = m.get('TotalBlockCount')
        return self


class ListSnapshotBlocksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSnapshotBlocksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSnapshotBlocksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSnapshotBlocksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChangedBlocksRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, client_token=None, first_snapshot_id=None,
                 second_snapshot_id=None, starting_block_index=None):
        # 标记开始比较差异的位置，为空时代表从 StartingBlockIndex 指定数据块开始比较， 最大长度 256 字节
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量，最小 100，最大 10000
        self.max_results = max_results  # type: long
        # 幂等参数
        self.client_token = client_token  # type: str
        # 待比较的第一个快照名称，最大 256 字节
        self.first_snapshot_id = first_snapshot_id  # type: str
        # 待比较的第二个快照名称，最大 256 字节
        self.second_snapshot_id = second_snapshot_id  # type: str
        # 两个快照比较的起始数据块 index，从零开始，最大值为第二快照的数据块总数量减一。当 NextToken 不为空时忽略该参数
        self.starting_block_index = starting_block_index  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChangedBlocksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.first_snapshot_id is not None:
            result['FirstSnapshotId'] = self.first_snapshot_id
        if self.second_snapshot_id is not None:
            result['SecondSnapshotId'] = self.second_snapshot_id
        if self.starting_block_index is not None:
            result['StartingBlockIndex'] = self.starting_block_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FirstSnapshotId') is not None:
            self.first_snapshot_id = m.get('FirstSnapshotId')
        if m.get('SecondSnapshotId') is not None:
            self.second_snapshot_id = m.get('SecondSnapshotId')
        if m.get('StartingBlockIndex') is not None:
            self.starting_block_index = m.get('StartingBlockIndex')
        return self


class ListChangedBlocksResponseBodyChangedBlocks(TeaModel):
    def __init__(self, block_index=None, first_block_token=None, second_block_token=None):
        # 数据块的索引值，从零开始
        self.block_index = block_index  # type: long
        # FirstSnapshotId 中数据块的 Token，用于后续的数据读取，第一个快照未变化时可省略。最大长度 256 字节
        self.first_block_token = first_block_token  # type: str
        # SecondBlockToken指定的快照中相对于 FirstBlockIndex 变化的数据块 Token，用于后续读取数据。最大长度 256 字节
        self.second_block_token = second_block_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChangedBlocksResponseBodyChangedBlocks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_index is not None:
            result['BlockIndex'] = self.block_index
        if self.first_block_token is not None:
            result['FirstBlockToken'] = self.first_block_token
        if self.second_block_token is not None:
            result['SecondBlockToken'] = self.second_block_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockIndex') is not None:
            self.block_index = m.get('BlockIndex')
        if m.get('FirstBlockToken') is not None:
            self.first_block_token = m.get('FirstBlockToken')
        if m.get('SecondBlockToken') is not None:
            self.second_block_token = m.get('SecondBlockToken')
        return self


class ListChangedBlocksResponseBody(TeaModel):
    def __init__(self, next_token=None, changed_blocks=None, expiry_time=None, volume_size=None, block_size=None,
                 block_count=None, total_block_count=None):
        # 下一个待比较的数据块 BlockToken，为空时代表无其他待比较数据块，最大长度 256 字节
        self.next_token = next_token  # type: str
        # 两个快照差异的数据块列表
        self.changed_blocks = changed_blocks  # type: list[ListChangedBlocksResponseBodyChangedBlocks]
        # 差异数据块 token 过期 UTC 时间戳， 单位微秒
        self.expiry_time = expiry_time  # type: long
        # 第二个快照大小，单位 GB，最小 1GB
        self.volume_size = volume_size  # type: long
        # 数据块大小，单位 Byte
        self.block_size = block_size  # type: long
        # 本次查询中变化数据块数量
        self.block_count = block_count  # type: long
        # 第二个快照相对于第一个快照差异数据快总数
        self.total_block_count = total_block_count  # type: long

    def validate(self):
        if self.changed_blocks:
            for k in self.changed_blocks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChangedBlocksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ChangedBlocks'] = []
        if self.changed_blocks is not None:
            for k in self.changed_blocks:
                result['ChangedBlocks'].append(k.to_map() if k else None)
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.volume_size is not None:
            result['VolumeSize'] = self.volume_size
        if self.block_size is not None:
            result['BlockSize'] = self.block_size
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.total_block_count is not None:
            result['TotalBlockCount'] = self.total_block_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.changed_blocks = []
        if m.get('ChangedBlocks') is not None:
            for k in m.get('ChangedBlocks'):
                temp_model = ListChangedBlocksResponseBodyChangedBlocks()
                self.changed_blocks.append(temp_model.from_map(k))
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('VolumeSize') is not None:
            self.volume_size = m.get('VolumeSize')
        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('TotalBlockCount') is not None:
            self.total_block_count = m.get('TotalBlockCount')
        return self


class ListChangedBlocksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListChangedBlocksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChangedBlocksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListChangedBlocksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


