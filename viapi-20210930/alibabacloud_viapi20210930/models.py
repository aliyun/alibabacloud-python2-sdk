# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AiStoreUserTask(TeaModel):
    def __init__(self, id=None, gmt_create=None, gmt_modified=None, region=None, region_desc=None, name=None,
                 product=None, product_desc=None, api_name=None, api_desc=None, version=None, param_info=None,
                 bucket_name=None, bucket_key_prefix=None, remark=None, receive_config=None, status=None, enable_time=None,
                 disable_time=None):
        # ID
        self.id = id  # type: long
        # 创建时间
        self.gmt_create = gmt_create  # type: str
        # 修改时间
        self.gmt_modified = gmt_modified  # type: str
        # 地域
        self.region = region  # type: str
        # 地域描述
        self.region_desc = region_desc  # type: str
        # 任务名称
        self.name = name  # type: str
        # 产品名称
        self.product = product  # type: str
        # 产品描述
        self.product_desc = product_desc  # type: str
        # API名称
        self.api_name = api_name  # type: str
        # API描述
        self.api_desc = api_desc  # type: str
        # API版本
        self.version = version  # type: str
        # 参数信息
        self.param_info = param_info  # type: str
        # bucket名称
        self.bucket_name = bucket_name  # type: str
        # bucketKey前缀
        self.bucket_key_prefix = bucket_key_prefix  # type: str
        # 备注
        self.remark = remark  # type: str
        # 接收消息配置
        self.receive_config = receive_config  # type: str
        # 状态
        self.status = status  # type: str
        # 启用时间
        self.enable_time = enable_time  # type: str
        # 停用时间
        self.disable_time = disable_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreUserTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.region is not None:
            result['Region'] = self.region
        if self.region_desc is not None:
            result['RegionDesc'] = self.region_desc
        if self.name is not None:
            result['Name'] = self.name
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_desc is not None:
            result['ApiDesc'] = self.api_desc
        if self.version is not None:
            result['Version'] = self.version
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.status is not None:
            result['Status'] = self.status
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.disable_time is not None:
            result['DisableTime'] = self.disable_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionDesc') is not None:
            self.region_desc = m.get('RegionDesc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiDesc') is not None:
            self.api_desc = m.get('ApiDesc')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('DisableTime') is not None:
            self.disable_time = m.get('DisableTime')
        return self


class AiStoreReceiveConfigEventBridge(TeaModel):
    def __init__(self, event_bus=None, event_rule=None):
        # 事件总线
        self.event_bus = event_bus  # type: str
        # 事件规则
        self.event_rule = event_rule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreReceiveConfigEventBridge, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus is not None:
            result['EventBus'] = self.event_bus
        if self.event_rule is not None:
            result['EventRule'] = self.event_rule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBus') is not None:
            self.event_bus = m.get('EventBus')
        if m.get('EventRule') is not None:
            self.event_rule = m.get('EventRule')
        return self


class AiStoreReceiveConfigMns(TeaModel):
    def __init__(self, queue=None):
        # 消息队列
        self.queue = queue  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreReceiveConfigMns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue is not None:
            result['Queue'] = self.queue
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        return self


class AiStoreReceiveConfig(TeaModel):
    def __init__(self, event_bridge=None, mns=None):
        # 事件总线
        self.event_bridge = event_bridge  # type: AiStoreReceiveConfigEventBridge
        # MNS消息
        self.mns = mns  # type: AiStoreReceiveConfigMns

    def validate(self):
        if self.event_bridge:
            self.event_bridge.validate()
        if self.mns:
            self.mns.validate()

    def to_map(self):
        _map = super(AiStoreReceiveConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bridge is not None:
            result['EventBridge'] = self.event_bridge.to_map()
        if self.mns is not None:
            result['Mns'] = self.mns.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBridge') is not None:
            temp_model = AiStoreReceiveConfigEventBridge()
            self.event_bridge = temp_model.from_map(m['EventBridge'])
        if m.get('Mns') is not None:
            temp_model = AiStoreReceiveConfigMns()
            self.mns = temp_model.from_map(m['Mns'])
        return self


class AiStoreApiNode(TeaModel):
    def __init__(self, product=None, product_desc=None, apis=None):
        # 产品名称
        self.product = product  # type: str
        # 产品描述
        self.product_desc = product_desc  # type: str
        # API列表
        self.apis = apis  # type: list[AiStoreUserTask]

    def validate(self):
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AiStoreApiNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        result['Apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['Apis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        self.apis = []
        if m.get('Apis') is not None:
            for k in m.get('Apis'):
                temp_model = AiStoreUserTask()
                self.apis.append(temp_model.from_map(k))
        return self


class GetAiStoreUserTaskRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAiStoreUserTaskRequest, self).to_map()
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


class GetAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: AiStoreUserTask

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAiStoreUserTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskResponse, self).to_map()
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
            temp_model = GetAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreUserTaskPageRequest(TeaModel):
    def __init__(self, product=None, api_name=None, status=None, page_no=None, page_size=None, name=None,
                 bucket_name=None):
        self.product = product  # type: str
        self.api_name = api_name  # type: str
        self.status = status  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.name = name  # type: str
        self.bucket_name = bucket_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAiStoreUserTaskPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class QueryAiStoreUserTaskPageResponseBodyData(TeaModel):
    def __init__(self, task_list=None, total_count=None):
        self.task_list = task_list  # type: list[AiStoreUserTask]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAiStoreUserTaskPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = AiStoreUserTask()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryAiStoreUserTaskPageResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryAiStoreUserTaskPageResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryAiStoreUserTaskPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryAiStoreUserTaskPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryAiStoreUserTaskPageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAiStoreUserTaskPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAiStoreUserTaskPageResponse, self).to_map()
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
            temp_model = QueryAiStoreUserTaskPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: list[AiStoreUserTask]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAiStoreRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreUserTask()
                self.data.append(temp_model.from_map(k))
        return self


class QueryAiStoreRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAiStoreRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAiStoreRegionsResponse, self).to_map()
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
            temp_model = QueryAiStoreRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAiStoreBucketsRequest(TeaModel):
    def __init__(self, product=None, api_name=None):
        self.product = product  # type: str
        self.api_name = api_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAiStoreBucketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        return self


class ListAiStoreBucketsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAiStoreBucketsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListAiStoreBucketsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAiStoreBucketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAiStoreBucketsResponse, self).to_map()
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
            temp_model = ListAiStoreBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiStoreUserTaskByNameRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAiStoreUserTaskByNameRequest, self).to_map()
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


class GetAiStoreUserTaskByNameResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: AiStoreUserTask

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskByNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAiStoreUserTaskByNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAiStoreUserTaskByNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskByNameResponse, self).to_map()
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
            temp_model = GetAiStoreUserTaskByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAiStoreUserTaskRequest(TeaModel):
    def __init__(self, product=None, api_name=None, bucket_name=None, bucket_key_prefix=None, name=None,
                 param_info=None, remark=None, receive_config=None, status=None, id=None):
        self.product = product  # type: str
        self.api_name = api_name  # type: str
        self.bucket_name = bucket_name  # type: str
        self.bucket_key_prefix = bucket_key_prefix  # type: str
        self.name = name  # type: str
        self.param_info = param_info  # type: str
        self.remark = remark  # type: str
        self.receive_config = receive_config  # type: str
        self.status = status  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAiStoreUserTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.status is not None:
            result['Status'] = self.status
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAiStoreUserTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAiStoreUserTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAiStoreUserTaskResponse, self).to_map()
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
            temp_model = UpdateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAiStoreUserTaskRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAiStoreUserTaskRequest, self).to_map()
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


class DisableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAiStoreUserTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DisableAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableAiStoreUserTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableAiStoreUserTaskResponse, self).to_map()
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
            temp_model = DisableAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreApiTreeResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: list[AiStoreApiNode]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAiStoreApiTreeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreApiNode()
                self.data.append(temp_model.from_map(k))
        return self


class QueryAiStoreApiTreeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAiStoreApiTreeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAiStoreApiTreeResponse, self).to_map()
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
            temp_model = QueryAiStoreApiTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAiStoreUserTaskRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAiStoreUserTaskRequest, self).to_map()
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


class DeleteAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAiStoreUserTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAiStoreUserTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAiStoreUserTaskResponse, self).to_map()
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
            temp_model = DeleteAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreUserTaskRequest(TeaModel):
    def __init__(self, product=None, api_name=None, bucket_name=None, bucket_key_prefix=None, name=None,
                 param_info=None, remark=None, receive_config=None, status=None):
        self.product = product  # type: str
        self.api_name = api_name  # type: str
        self.bucket_name = bucket_name  # type: str
        self.bucket_key_prefix = bucket_key_prefix  # type: str
        self.name = name  # type: str
        self.param_info = param_info  # type: str
        self.remark = remark  # type: str
        self.receive_config = receive_config  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreUserTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreUserTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAiStoreUserTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAiStoreUserTaskResponse, self).to_map()
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
            temp_model = CreateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreReceiveConfigRequest(TeaModel):
    def __init__(self, product=None, api_name=None):
        self.product = product  # type: str
        self.api_name = api_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreReceiveConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        return self


class CreateAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: AiStoreReceiveConfig

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateAiStoreReceiveConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateAiStoreReceiveConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAiStoreReceiveConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAiStoreReceiveConfigResponse, self).to_map()
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
            temp_model = CreateAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiStoreReceiveConfigRequest(TeaModel):
    def __init__(self, product=None, api_name=None):
        self.product = product  # type: str
        self.api_name = api_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAiStoreReceiveConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        return self


class GetAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: AiStoreReceiveConfig

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAiStoreReceiveConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAiStoreReceiveConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAiStoreReceiveConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAiStoreReceiveConfigResponse, self).to_map()
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
            temp_model = GetAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAiStoreUserTaskRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAiStoreUserTaskRequest, self).to_map()
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


class EnableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAiStoreUserTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class EnableAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableAiStoreUserTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableAiStoreUserTaskResponse, self).to_map()
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
            temp_model = EnableAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreBucketRequest(TeaModel):
    def __init__(self, bucket_name=None):
        self.bucket_name = bucket_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreBucketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class CreateAiStoreBucketResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreBucketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateAiStoreBucketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAiStoreBucketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAiStoreBucketResponse, self).to_map()
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
            temp_model = CreateAiStoreBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(self, role_arn=None, service_name=None, spiregion_id=None, deletion_task_id=None, account_id=None):
        self.role_arn = role_arn  # type: str
        self.service_name = service_name  # type: str
        self.spiregion_id = spiregion_id  # type: str
        self.deletion_task_id = deletion_task_id  # type: str
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages(TeaModel):
    def __init__(self, region=None, resources=None):
        self.region = region  # type: str
        self.resources = resources  # type: list[bytes]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CheckServiceLinkedRoleForDeletingResponseBody(TeaModel):
    def __init__(self, request_id=None, deletable=None, role_usages=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.deletable = deletable  # type: bool
        self.role_usages = role_usages  # type: list[CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages]

    def validate(self):
        if self.role_usages:
            for k in self.role_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeletingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckServiceLinkedRoleForDeletingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingResponse, self).to_map()
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
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


