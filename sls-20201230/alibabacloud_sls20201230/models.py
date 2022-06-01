# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ConsumerGroup(TeaModel):
    def __init__(self, name=None, order=None, timeout=None):
        # consumerGroup
        self.name = name  # type: str
        # order
        self.order = order  # type: bool
        # timeout
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConsumerGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class EncryptConf(TeaModel):
    def __init__(self, enable=None, encrypt_type=None, user_cmk_info=None):
        # enable
        self.enable = enable  # type: bool
        # encrypt_type
        self.encrypt_type = encrypt_type  # type: str
        self.user_cmk_info = user_cmk_info  # type: EncryptUserCmkConf

    def validate(self):
        if self.user_cmk_info:
            self.user_cmk_info.validate()

    def to_map(self):
        _map = super(EncryptConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.encrypt_type is not None:
            result['encrypt_type'] = self.encrypt_type
        if self.user_cmk_info is not None:
            result['user_cmk_info'] = self.user_cmk_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('encrypt_type') is not None:
            self.encrypt_type = m.get('encrypt_type')
        if m.get('user_cmk_info') is not None:
            temp_model = EncryptUserCmkConf()
            self.user_cmk_info = temp_model.from_map(m['user_cmk_info'])
        return self


class EncryptUserCmkConf(TeaModel):
    def __init__(self, arn=None, cmk_key_id=None, region_id=None):
        # arn
        self.arn = arn  # type: str
        # cmk_key_id
        self.cmk_key_id = cmk_key_id  # type: str
        # region_id
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptUserCmkConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.cmk_key_id is not None:
            result['cmk_key_id'] = self.cmk_key_id
        if self.region_id is not None:
            result['region_id'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('cmk_key_id') is not None:
            self.cmk_key_id = m.get('cmk_key_id')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        return self


class SavedSearch(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        # displayName
        self.display_name = display_name  # type: str
        # logstore
        self.logstore = logstore  # type: str
        # savedsearchName
        self.savedsearch_name = savedsearch_name  # type: str
        # searchQuery
        self.search_query = search_query  # type: str
        # topic
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SavedSearch, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class Logstore(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, create_time=None, enable_tracking=None, encrypt_conf=None,
                 hot_ttl=None, last_modify_time=None, logstore_name=None, max_split_shard=None, shard_count=None,
                 telemetry_type=None, ttl=None):
        # append client ip and receive time
        self.append_meta = append_meta  # type: bool
        # auto spilt shard
        self.auto_split = auto_split  # type: bool
        # create time
        self.create_time = create_time  # type: int
        # enable web tracking
        self.enable_tracking = enable_tracking  # type: bool
        # Encrypt configuration
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        # hot ttl
        self.hot_ttl = hot_ttl  # type: int
        # last modify time
        self.last_modify_time = last_modify_time  # type: int
        # logstore name
        self.logstore_name = logstore_name  # type: str
        # max split shard
        self.max_split_shard = max_split_shard  # type: int
        # shard count
        self.shard_count = shard_count  # type: int
        # telemetryType
        self.telemetry_type = telemetry_type  # type: str
        # ttl
        self.ttl = ttl  # type: int

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super(Logstore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class Project(TeaModel):
    def __init__(self, create_time=None, description=None, last_modify_time=None, owner=None, project_name=None,
                 region=None, status=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 最后更新时间
        self.last_modify_time = last_modify_time  # type: str
        # owner
        self.owner = owner  # type: str
        # Project名称
        self.project_name = project_name  # type: str
        # 所在区域
        self.region = region  # type: str
        # 状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Project, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.owner is not None:
            result['owner'] = self.owner
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class Shard(TeaModel):
    def __init__(self, create_time=None, exclusive_end_key=None, inclusive_begin_key=None, shard_id=None,
                 status=None):
        # createTime
        self.create_time = create_time  # type: int
        # exclusiveEndKey
        self.exclusive_end_key = exclusive_end_key  # type: str
        # inclusiveBeginKey
        self.inclusive_begin_key = inclusive_begin_key  # type: str
        # shard id
        self.shard_id = shard_id  # type: int
        # status
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Shard, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.exclusive_end_key is not None:
            result['exclusiveEndKey'] = self.exclusive_end_key
        if self.inclusive_begin_key is not None:
            result['inclusiveBeginKey'] = self.inclusive_begin_key
        if self.shard_id is not None:
            result['shardId'] = self.shard_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('exclusiveEndKey') is not None:
            self.exclusive_end_key = m.get('exclusiveEndKey')
        if m.get('inclusiveBeginKey') is not None:
            self.inclusive_begin_key = m.get('inclusiveBeginKey')
        if m.get('shardId') is not None:
            self.shard_id = m.get('shardId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(self, consumer_group=None, order=None, timeout=None):
        self.consumer_group = consumer_group  # type: str
        self.order = order  # type: bool
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['consumerGroup'] = self.consumer_group
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consumerGroup') is not None:
            self.consumer_group = m.get('consumerGroup')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateLogStoreRequest(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, enable_tracking=None, encrypt_conf=None, hot_ttl=None,
                 logstore_name=None, max_split_shard=None, shard_count=None, telemetry_type=None, ttl=None):
        self.append_meta = append_meta  # type: bool
        self.auto_split = auto_split  # type: bool
        self.enable_tracking = enable_tracking  # type: bool
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        self.hot_ttl = hot_ttl  # type: int
        self.logstore_name = logstore_name  # type: str
        self.max_split_shard = max_split_shard  # type: int
        self.shard_count = shard_count  # type: int
        self.telemetry_type = telemetry_type  # type: str
        self.ttl = ttl  # type: int

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super(CreateLogStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class CreateLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateLogStoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, description=None, project_name=None):
        self.description = description  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateSavedSearchRequest(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        self.display_name = display_name  # type: str
        self.logstore = logstore  # type: str
        self.savedsearch_name = savedsearch_name  # type: str
        self.search_query = search_query  # type: str
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSavedSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class CreateSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateSavedSearchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteSavedSearchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Logstore

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogStoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Logstore()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Project

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SavedSearch

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSavedSearchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SavedSearch()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[ConsumerGroup]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ConsumerGroup()
                self.body.append(temp_model.from_map(k))
        return self


class ListLogStoresRequest(TeaModel):
    def __init__(self, logstore_name=None, offset=None, size=None, telemetry_type=None):
        self.logstore_name = logstore_name  # type: str
        self.offset = offset  # type: int
        self.size = size  # type: int
        self.telemetry_type = telemetry_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogStoresRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        return self


class ListLogStoresResponseBody(TeaModel):
    def __init__(self, logstores=None, total=None):
        self.logstores = logstores  # type: list[str]
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogStoresResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstores is not None:
            result['logstores'] = self.logstores
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstores') is not None:
            self.logstores = m.get('logstores')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListLogStoresResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLogStoresResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogStoresResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLogStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(self, offset=None, project_name=None, size=None):
        self.offset = offset  # type: int
        self.project_name = project_name  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(self, count=None, projects=None, total=None):
        self.count = count  # type: long
        self.projects = projects  # type: list[Project]
        self.total = total  # type: long

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = Project()
                self.projects.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSavedSearchRequest(TeaModel):
    def __init__(self, offset=None, size=None):
        self.offset = offset  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSavedSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListSavedSearchResponseBody(TeaModel):
    def __init__(self, count=None, savedsearch_items=None, total=None):
        self.count = count  # type: int
        self.savedsearch_items = savedsearch_items  # type: list[SavedSearch]
        self.total = total  # type: int

    def validate(self):
        if self.savedsearch_items:
            for k in self.savedsearch_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSavedSearchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['savedsearchItems'] = []
        if self.savedsearch_items is not None:
            for k in self.savedsearch_items:
                result['savedsearchItems'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.savedsearch_items = []
        if m.get('savedsearchItems') is not None:
            for k in m.get('savedsearchItems'):
                temp_model = SavedSearch()
                self.savedsearch_items.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSavedSearchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSavedSearchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSavedSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConsumerGroupRequest(TeaModel):
    def __init__(self, order=None, timeout=None):
        self.order = order  # type: bool
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateLogStoreRequest(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, enable_tracking=None, encrypt_conf=None, hot_ttl=None,
                 logstore_name=None, max_split_shard=None, shard_count=None, telemetry_type=None, ttl=None):
        self.append_meta = append_meta  # type: bool
        self.auto_split = auto_split  # type: bool
        self.enable_tracking = enable_tracking  # type: bool
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        self.hot_ttl = hot_ttl  # type: int
        self.logstore_name = logstore_name  # type: str
        self.max_split_shard = max_split_shard  # type: int
        self.shard_count = shard_count  # type: int
        self.telemetry_type = telemetry_type  # type: str
        self.ttl = ttl  # type: int

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super(UpdateLogStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class UpdateLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateLogStoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, description=None):
        # Project description
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


