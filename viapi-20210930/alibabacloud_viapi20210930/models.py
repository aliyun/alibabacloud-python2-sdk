# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AiStoreApiNode(TeaModel):
    def __init__(self, apis=None, product=None, product_desc=None):
        self.apis = apis  # type: list[AiStoreUserTask]
        self.product = product  # type: str
        self.product_desc = product_desc  # type: str

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
        result['Apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['Apis'].append(k.to_map() if k else None)
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apis = []
        if m.get('Apis') is not None:
            for k in m.get('Apis'):
                temp_model = AiStoreUserTask()
                self.apis.append(temp_model.from_map(k))
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        return self


class AiStoreReceiveConfigDingTalk(TeaModel):
    def __init__(self, address=None, secret=None):
        self.address = address  # type: str
        self.secret = secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreReceiveConfigDingTalk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.secret is not None:
            result['Secret'] = self.secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        return self


class AiStoreReceiveConfigEventBridge(TeaModel):
    def __init__(self, event_bus=None, event_rule=None):
        self.event_bus = event_bus  # type: str
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


class AiStoreReceiveConfigHttp(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreReceiveConfigHttp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class AiStoreReceiveConfigHttps(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreReceiveConfigHttps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class AiStoreReceiveConfigMns(TeaModel):
    def __init__(self, queue=None):
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


class AiStoreReceiveConfigRocketMQ(TeaModel):
    def __init__(self, instance_id=None, topic_name=None):
        self.instance_id = instance_id  # type: str
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreReceiveConfigRocketMQ, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class AiStoreReceiveConfig(TeaModel):
    def __init__(self, custom=None, ding_talk=None, event_bridge=None, http=None, https=None, mns=None,
                 rocket_mq=None):
        self.custom = custom  # type: str
        self.ding_talk = ding_talk  # type: AiStoreReceiveConfigDingTalk
        self.event_bridge = event_bridge  # type: AiStoreReceiveConfigEventBridge
        self.http = http  # type: AiStoreReceiveConfigHttp
        self.https = https  # type: AiStoreReceiveConfigHttps
        self.mns = mns  # type: AiStoreReceiveConfigMns
        self.rocket_mq = rocket_mq  # type: AiStoreReceiveConfigRocketMQ

    def validate(self):
        if self.ding_talk:
            self.ding_talk.validate()
        if self.event_bridge:
            self.event_bridge.validate()
        if self.http:
            self.http.validate()
        if self.https:
            self.https.validate()
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        _map = super(AiStoreReceiveConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom is not None:
            result['Custom'] = self.custom
        if self.ding_talk is not None:
            result['DingTalk'] = self.ding_talk.to_map()
        if self.event_bridge is not None:
            result['EventBridge'] = self.event_bridge.to_map()
        if self.http is not None:
            result['Http'] = self.http.to_map()
        if self.https is not None:
            result['Https'] = self.https.to_map()
        if self.mns is not None:
            result['Mns'] = self.mns.to_map()
        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Custom') is not None:
            self.custom = m.get('Custom')
        if m.get('DingTalk') is not None:
            temp_model = AiStoreReceiveConfigDingTalk()
            self.ding_talk = temp_model.from_map(m['DingTalk'])
        if m.get('EventBridge') is not None:
            temp_model = AiStoreReceiveConfigEventBridge()
            self.event_bridge = temp_model.from_map(m['EventBridge'])
        if m.get('Http') is not None:
            temp_model = AiStoreReceiveConfigHttp()
            self.http = temp_model.from_map(m['Http'])
        if m.get('Https') is not None:
            temp_model = AiStoreReceiveConfigHttps()
            self.https = temp_model.from_map(m['Https'])
        if m.get('Mns') is not None:
            temp_model = AiStoreReceiveConfigMns()
            self.mns = temp_model.from_map(m['Mns'])
        if m.get('RocketMQ') is not None:
            temp_model = AiStoreReceiveConfigRocketMQ()
            self.rocket_mq = temp_model.from_map(m['RocketMQ'])
        return self


class AiStoreTemplate(TeaModel):
    def __init__(self, template_context=None, template_variable=None):
        self.template_context = template_context  # type: str
        self.template_variable = template_variable  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_context is not None:
            result['TemplateContext'] = self.template_context
        if self.template_variable is not None:
            result['TemplateVariable'] = self.template_variable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateContext') is not None:
            self.template_context = m.get('TemplateContext')
        if m.get('TemplateVariable') is not None:
            self.template_variable = m.get('TemplateVariable')
        return self


class AiStoreUserTask(TeaModel):
    def __init__(self, api_desc=None, api_name=None, bucket_key_prefix=None, bucket_name=None, disable_time=None,
                 enable_time=None, gmt_create=None, gmt_modified=None, id=None, name=None, param_info=None, product=None,
                 product_desc=None, receive_config=None, region=None, region_desc=None, remark=None, status=None,
                 task_version=None, version=None):
        self.api_desc = api_desc  # type: str
        self.api_name = api_name  # type: str
        self.bucket_key_prefix = bucket_key_prefix  # type: str
        self.bucket_name = bucket_name  # type: str
        self.disable_time = disable_time  # type: str
        self.enable_time = enable_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.param_info = param_info  # type: str
        self.product = product  # type: str
        self.product_desc = product_desc  # type: str
        self.receive_config = receive_config  # type: str
        self.region = region  # type: str
        self.region_desc = region_desc  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: str
        self.task_version = task_version  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AiStoreUserTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_desc is not None:
            result['ApiDesc'] = self.api_desc
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.disable_time is not None:
            result['DisableTime'] = self.disable_time
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.region is not None:
            result['Region'] = self.region
        if self.region_desc is not None:
            result['RegionDesc'] = self.region_desc
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDesc') is not None:
            self.api_desc = m.get('ApiDesc')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DisableTime') is not None:
            self.disable_time = m.get('DisableTime')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionDesc') is not None:
            self.region_desc = m.get('RegionDesc')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(self, account_id=None, deletion_task_id=None, role_arn=None, spiregion_id=None, service_name=None):
        self.account_id = account_id  # type: str
        self.deletion_task_id = deletion_task_id  # type: str
        self.role_arn = role_arn  # type: str
        self.spiregion_id = spiregion_id  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
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
    def __init__(self, deletable=None, request_id=None, role_usages=None):
        self.deletable = deletable  # type: bool
        self.request_id = request_id  # type: str
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
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeletingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckServiceLinkedRoleForDeletingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
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
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreBucketResponseBody, self).to_map()
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


class CreateAiStoreBucketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAiStoreBucketResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAiStoreBucketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAiStoreBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreReceiveConfigRequest(TeaModel):
    def __init__(self, api_name=None, product=None):
        self.api_name = api_name  # type: str
        self.product = product  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreReceiveConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AiStoreReceiveConfig
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateAiStoreReceiveConfigResponseBody, self).to_map()
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
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAiStoreReceiveConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAiStoreReceiveConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAiStoreReceiveConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreUserTaskRequest(TeaModel):
    def __init__(self, api_name=None, bucket_key_prefix=None, bucket_name=None, create_config=None, name=None,
                 param_info=None, product=None, receive_config=None, remark=None, status=None):
        self.api_name = api_name  # type: str
        self.bucket_key_prefix = bucket_key_prefix  # type: str
        self.bucket_name = bucket_name  # type: str
        self.create_config = create_config  # type: str
        self.name = name  # type: str
        self.param_info = param_info  # type: str
        self.product = product  # type: str
        self.receive_config = receive_config  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreUserTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.create_config is not None:
            result['CreateConfig'] = self.create_config
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.product is not None:
            result['Product'] = self.product
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CreateConfig') is not None:
            self.create_config = m.get('CreateConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAiStoreUserTaskResponseBody, self).to_map()
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


class CreateAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAiStoreUserTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAiStoreUserTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAiStoreUserTaskRequest(TeaModel):
    def __init__(self, aistore_version=None, id=None):
        self.aistore_version = aistore_version  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAiStoreUserTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aistore_version is not None:
            result['AistoreVersion'] = self.aistore_version
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AistoreVersion') is not None:
            self.aistore_version = m.get('AistoreVersion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAiStoreUserTaskResponseBody, self).to_map()
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


class DeleteAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAiStoreUserTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAiStoreUserTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAiStoreUserTaskRequest(TeaModel):
    def __init__(self, aistore_version=None, id=None):
        self.aistore_version = aistore_version  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAiStoreUserTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aistore_version is not None:
            result['AistoreVersion'] = self.aistore_version
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AistoreVersion') is not None:
            self.aistore_version = m.get('AistoreVersion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DisableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAiStoreUserTaskResponseBody, self).to_map()
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


class DisableAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableAiStoreUserTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableAiStoreUserTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAiStoreUserTaskRequest(TeaModel):
    def __init__(self, aistore_version=None, id=None):
        self.aistore_version = aistore_version  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAiStoreUserTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aistore_version is not None:
            result['AistoreVersion'] = self.aistore_version
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AistoreVersion') is not None:
            self.aistore_version = m.get('AistoreVersion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class EnableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAiStoreUserTaskResponseBody, self).to_map()
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


class EnableAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableAiStoreUserTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableAiStoreUserTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiStoreReceiveConfigRequest(TeaModel):
    def __init__(self, api_name=None, product=None):
        self.api_name = api_name  # type: str
        self.product = product  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAiStoreReceiveConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class GetAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AiStoreReceiveConfig
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAiStoreReceiveConfigResponseBody, self).to_map()
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
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAiStoreReceiveConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAiStoreReceiveConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAiStoreReceiveConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
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
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AiStoreUserTask
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskResponseBody, self).to_map()
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
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAiStoreUserTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAiStoreUserTaskResponseBody()
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
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AiStoreUserTask
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskByNameResponseBody, self).to_map()
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
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAiStoreUserTaskByNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAiStoreUserTaskByNameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAiStoreUserTaskByNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAiStoreUserTaskByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAiStoreBucketsRequest(TeaModel):
    def __init__(self, api_name=None, product=None):
        self.api_name = api_name  # type: str
        self.product = product  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAiStoreBucketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class ListAiStoreBucketsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAiStoreBucketsResponseBody, self).to_map()
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


class ListAiStoreBucketsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAiStoreBucketsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAiStoreBucketsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAiStoreBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreApiTreeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[AiStoreApiNode]
        self.request_id = request_id  # type: str

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreApiNode()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAiStoreApiTreeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAiStoreApiTreeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAiStoreApiTreeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAiStoreApiTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreRegionsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[AiStoreUserTask]
        self.request_id = request_id  # type: str

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreUserTask()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAiStoreRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAiStoreRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAiStoreRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAiStoreRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreUserTaskPageRequest(TeaModel):
    def __init__(self, api_name=None, bucket_name=None, name=None, page_no=None, page_size=None, product=None,
                 status=None):
        self.api_name = api_name  # type: str
        self.bucket_name = bucket_name  # type: str
        self.name = name  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.product = product  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAiStoreUserTaskPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryAiStoreUserTaskPageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryAiStoreUserTaskPageResponseBody, self).to_map()
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
            temp_model = QueryAiStoreUserTaskPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAiStoreUserTaskPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAiStoreUserTaskPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAiStoreUserTaskPageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAiStoreUserTaskPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAiStoreUserTaskRequest(TeaModel):
    def __init__(self, api_name=None, bucket_key_prefix=None, bucket_name=None, id=None, name=None, param_info=None,
                 product=None, receive_config=None, remark=None, status=None):
        self.api_name = api_name  # type: str
        self.bucket_key_prefix = bucket_key_prefix  # type: str
        self.bucket_name = bucket_name  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.param_info = param_info  # type: str
        self.product = product  # type: str
        self.receive_config = receive_config  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAiStoreUserTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.product is not None:
            result['Product'] = self.product
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAiStoreUserTaskResponseBody, self).to_map()
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


class UpdateAiStoreUserTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAiStoreUserTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAiStoreUserTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


