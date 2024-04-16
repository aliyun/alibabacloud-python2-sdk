# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApplyForStreamAccessTokenRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyForStreamAccessTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ApplyForStreamAccessTokenResponseBody(TeaModel):
    def __init__(self, access_token=None, channel_id=None, request_id=None, stream_secret=None):
        self.access_token = access_token  # type: str
        self.channel_id = channel_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.stream_secret = stream_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyForStreamAccessTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stream_secret is not None:
            result['StreamSecret'] = self.stream_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StreamSecret') is not None:
            self.stream_secret = m.get('StreamSecret')
        return self


class ApplyForStreamAccessTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyForStreamAccessTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyForStreamAccessTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyForStreamAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, perspective=None, recommend_num=None, session_id=None,
                 utterance=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.perspective = perspective  # type: list[str]
        self.recommend_num = recommend_num  # type: long
        self.session_id = session_id  # type: str
        self.utterance = utterance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class AssociateShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, perspective_shrink=None, recommend_num=None,
                 session_id=None, utterance=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.perspective_shrink = perspective_shrink  # type: str
        self.recommend_num = recommend_num  # type: long
        self.session_id = session_id  # type: str
        self.utterance = utterance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perspective_shrink is not None:
            result['Perspective'] = self.perspective_shrink
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class AssociateResponseBodyAssociate(TeaModel):
    def __init__(self, meta=None, title=None):
        self.meta = meta  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateResponseBodyAssociate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AssociateResponseBody(TeaModel):
    def __init__(self, associate=None, message_id=None, request_id=None, session_id=None):
        self.associate = associate  # type: list[AssociateResponseBodyAssociate]
        self.message_id = message_id  # type: str
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        if self.associate:
            for k in self.associate:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Associate'] = []
        if self.associate is not None:
            for k in self.associate:
                result['Associate'].append(k.to_map() if k else None)
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = AssociateResponseBodyAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AssociateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeginSessionRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeginSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class BeginSessionResponseBody(TeaModel):
    def __init__(self, asr_max_end_silence=None, interruptible=None, request_id=None, silence_reply_timeout=None,
                 welcome_message=None):
        self.asr_max_end_silence = asr_max_end_silence  # type: int
        self.interruptible = interruptible  # type: bool
        self.request_id = request_id  # type: str
        # 静默超时时间
        self.silence_reply_timeout = silence_reply_timeout  # type: int
        self.welcome_message = welcome_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeginSessionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_max_end_silence is not None:
            result['AsrMaxEndSilence'] = self.asr_max_end_silence
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.silence_reply_timeout is not None:
            result['SilenceReplyTimeout'] = self.silence_reply_timeout
        if self.welcome_message is not None:
            result['WelcomeMessage'] = self.welcome_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsrMaxEndSilence') is not None:
            self.asr_max_end_silence = m.get('AsrMaxEndSilence')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilenceReplyTimeout') is not None:
            self.silence_reply_timeout = m.get('SilenceReplyTimeout')
        if m.get('WelcomeMessage') is not None:
            self.welcome_message = m.get('WelcomeMessage')
        return self


class BeginSessionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BeginSessionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BeginSessionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BeginSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelInstancePublishTaskRequest(TeaModel):
    def __init__(self, agent_key=None, id=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelInstancePublishTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CancelInstancePublishTaskResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, error=None, id=None, modify_time=None, request_id=None,
                 response=None, status=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.id = id  # type: long
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.response = response  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelInstancePublishTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CancelInstancePublishTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelInstancePublishTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelInstancePublishTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPublishTaskRequest(TeaModel):
    def __init__(self, agent_key=None, id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPublishTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CancelPublishTaskResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, error=None, id=None, modify_time=None, request_id=None,
                 response=None, status=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.id = id  # type: long
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.response = response  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPublishTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CancelPublishTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelPublishTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelPublishTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelPublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_name=None, knowledge_id=None, perspective=None,
                 sand_box=None, sender_id=None, sender_nick=None, session_id=None, utterance=None, vendor_param=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_name = intent_name  # type: str
        self.knowledge_id = knowledge_id  # type: str
        self.perspective = perspective  # type: list[str]
        self.sand_box = sand_box  # type: bool
        self.sender_id = sender_id  # type: str
        self.sender_nick = sender_nick  # type: str
        self.session_id = session_id  # type: str
        self.utterance = utterance  # type: str
        self.vendor_param = vendor_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.sand_box is not None:
            result['SandBox'] = self.sand_box
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        return self


class ChatShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_name=None, knowledge_id=None,
                 perspective_shrink=None, sand_box=None, sender_id=None, sender_nick=None, session_id=None, utterance=None,
                 vendor_param=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_name = intent_name  # type: str
        self.knowledge_id = knowledge_id  # type: str
        self.perspective_shrink = perspective_shrink  # type: str
        self.sand_box = sand_box  # type: bool
        self.sender_id = sender_id  # type: str
        self.sender_nick = sender_nick  # type: str
        self.session_id = session_id  # type: str
        self.utterance = utterance  # type: str
        self.vendor_param = vendor_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective_shrink is not None:
            result['Perspective'] = self.perspective_shrink
        if self.sand_box is not None:
            result['SandBox'] = self.sand_box
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')
        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        return self


class ChatResponseBodyMessagesKnowledgeRelatedKnowledges(TeaModel):
    def __init__(self, knowledge_id=None, title=None):
        self.knowledge_id = knowledge_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatResponseBodyMessagesKnowledgeRelatedKnowledges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesKnowledge(TeaModel):
    def __init__(self, answer_source=None, category=None, content=None, content_type=None, hit_statement=None,
                 id=None, related_knowledges=None, score=None, summary=None, title=None):
        self.answer_source = answer_source  # type: str
        self.category = category  # type: str
        self.content = content  # type: str
        self.content_type = content_type  # type: str
        self.hit_statement = hit_statement  # type: str
        self.id = id  # type: str
        self.related_knowledges = related_knowledges  # type: list[ChatResponseBodyMessagesKnowledgeRelatedKnowledges]
        self.score = score  # type: float
        self.summary = summary  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.related_knowledges:
            for k in self.related_knowledges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatResponseBodyMessagesKnowledge, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.id is not None:
            result['Id'] = self.id
        result['RelatedKnowledges'] = []
        if self.related_knowledges is not None:
            for k in self.related_knowledges:
                result['RelatedKnowledges'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.related_knowledges = []
        if m.get('RelatedKnowledges') is not None:
            for k in m.get('RelatedKnowledges'):
                temp_model = ChatResponseBodyMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesRecommends(TeaModel):
    def __init__(self, answer_source=None, knowledge_id=None, score=None, title=None):
        self.answer_source = answer_source  # type: str
        self.knowledge_id = knowledge_id  # type: str
        self.score = score  # type: float
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatResponseBodyMessagesRecommends, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.score is not None:
            result['Score'] = self.score
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesTextSlots(TeaModel):
    def __init__(self, hit=None, name=None, origin=None, value=None):
        self.hit = hit  # type: bool
        self.name = name  # type: str
        self.origin = origin  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatResponseBodyMessagesTextSlots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit is not None:
            result['Hit'] = self.hit
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hit') is not None:
            self.hit = m.get('Hit')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ChatResponseBodyMessagesText(TeaModel):
    def __init__(self, answer_source=None, article_title=None, commands=None, content=None, content_type=None,
                 dialog_name=None, ext=None, external_flags=None, hit_statement=None, intent_name=None, meta_data=None,
                 node_id=None, node_name=None, response_type=None, score=None, slots=None, user_defined_chat_title=None):
        self.answer_source = answer_source  # type: str
        self.article_title = article_title  # type: str
        self.commands = commands  # type: dict[str, any]
        self.content = content  # type: str
        self.content_type = content_type  # type: str
        self.dialog_name = dialog_name  # type: str
        self.ext = ext  # type: dict[str, any]
        self.external_flags = external_flags  # type: dict[str, any]
        self.hit_statement = hit_statement  # type: str
        self.intent_name = intent_name  # type: str
        self.meta_data = meta_data  # type: str
        self.node_id = node_id  # type: str
        self.node_name = node_name  # type: str
        self.response_type = response_type  # type: str
        self.score = score  # type: float
        self.slots = slots  # type: list[ChatResponseBodyMessagesTextSlots]
        self.user_defined_chat_title = user_defined_chat_title  # type: str

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatResponseBodyMessagesText, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.article_title is not None:
            result['ArticleTitle'] = self.article_title
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.external_flags is not None:
            result['ExternalFlags'] = self.external_flags
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.response_type is not None:
            result['ResponseType'] = self.response_type
        if self.score is not None:
            result['Score'] = self.score
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        if self.user_defined_chat_title is not None:
            result['UserDefinedChatTitle'] = self.user_defined_chat_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('ArticleTitle') is not None:
            self.article_title = m.get('ArticleTitle')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('ExternalFlags') is not None:
            self.external_flags = m.get('ExternalFlags')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ResponseType') is not None:
            self.response_type = m.get('ResponseType')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = ChatResponseBodyMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        return self


class ChatResponseBodyMessages(TeaModel):
    def __init__(self, answer_source=None, answer_type=None, knowledge=None, recommends=None, text=None, title=None,
                 voice_title=None):
        self.answer_source = answer_source  # type: str
        self.answer_type = answer_type  # type: str
        self.knowledge = knowledge  # type: ChatResponseBodyMessagesKnowledge
        self.recommends = recommends  # type: list[ChatResponseBodyMessagesRecommends]
        self.text = text  # type: ChatResponseBodyMessagesText
        self.title = title  # type: str
        self.voice_title = voice_title  # type: str

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()
        if self.recommends:
            for k in self.recommends:
                if k:
                    k.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super(ChatResponseBodyMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        result['Recommends'] = []
        if self.recommends is not None:
            for k in self.recommends:
                result['Recommends'].append(k.to_map() if k else None)
        if self.text is not None:
            result['Text'] = self.text.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.voice_title is not None:
            result['VoiceTitle'] = self.voice_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Knowledge') is not None:
            temp_model = ChatResponseBodyMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = ChatResponseBodyMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            temp_model = ChatResponseBodyMessagesText()
            self.text = temp_model.from_map(m['Text'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VoiceTitle') is not None:
            self.voice_title = m.get('VoiceTitle')
        return self


class ChatResponseBody(TeaModel):
    def __init__(self, message_id=None, messages=None, query_seg_list=None, request_id=None, session_id=None):
        self.message_id = message_id  # type: str
        self.messages = messages  # type: list[ChatResponseBodyMessages]
        self.query_seg_list = query_seg_list  # type: list[str]
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.query_seg_list is not None:
            result['QuerySegList'] = self.query_seg_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('QuerySegList') is not None:
            self.query_seg_list = m.get('QuerySegList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ChatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinueInstancePublishTaskRequest(TeaModel):
    def __init__(self, agent_key=None, id=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueInstancePublishTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ContinueInstancePublishTaskResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, error=None, errors=None, id=None, modify_time=None,
                 request_id=None, response=None, status=None, warnings=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.errors = errors  # type: dict[str, any]
        self.id = id  # type: long
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.response = response  # type: str
        self.status = status  # type: str
        self.warnings = warnings  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueInstancePublishTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.warnings is not None:
            result['Warnings'] = self.warnings
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')
        return self


class ContinueInstancePublishTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ContinueInstancePublishTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContinueInstancePublishTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ContinueInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, biz_code=None, knowledge_type=None, name=None, parent_category_id=None):
        self.agent_key = agent_key  # type: str
        self.biz_code = biz_code  # type: str
        self.knowledge_type = knowledge_type  # type: int
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class CreateCategoryResponseBodyCategory(TeaModel):
    def __init__(self, biz_code=None, category_id=None, name=None, parent_category_id=None, status=None):
        self.biz_code = biz_code  # type: str
        self.category_id = category_id  # type: long
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCategoryResponseBodyCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateCategoryResponseBody(TeaModel):
    def __init__(self, category=None, request_id=None):
        self.category = category  # type: CreateCategoryResponseBodyCategory
        self.request_id = request_id  # type: str

    def validate(self):
        if self.category:
            self.category.validate()

    def to_map(self):
        _map = super(CreateCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = CreateCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m['Category'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCategoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, conn_question_id=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.conn_question_id = conn_question_id  # type: long
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class CreateConnQuestionResponseBody(TeaModel):
    def __init__(self, outline_id=None, request_id=None):
        self.outline_id = outline_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnQuestionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConnQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConnQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConnQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDSEntityRequest(TeaModel):
    def __init__(self, agent_key=None, entity_name=None, entity_type=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDSEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDSEntityResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDSEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDSEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDSEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDSEntityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDSEntityValueRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, entity_id=None, instance_id=None, synonyms=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.entity_id = entity_id  # type: long
        self.instance_id = instance_id  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDSEntityValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class CreateDSEntityValueShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, entity_id=None, instance_id=None, synonyms_shrink=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.entity_id = entity_id  # type: long
        self.instance_id = instance_id  # type: str
        self.synonyms_shrink = synonyms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDSEntityValueShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms_shrink is not None:
            result['Synonyms'] = self.synonyms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms_shrink = m.get('Synonyms')
        return self


class CreateDSEntityValueResponseBody(TeaModel):
    def __init__(self, entity_value_id=None, request_id=None):
        self.entity_value_id = entity_value_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDSEntityValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDSEntityValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDSEntityValueResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDSEntityValueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDocRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None, config=None, content=None, end_date=None, meta=None,
                 start_date=None, title=None):
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long
        self.config = config  # type: str
        self.content = content  # type: str
        self.end_date = end_date  # type: str
        self.meta = meta  # type: str
        self.start_date = start_date  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.content is not None:
            result['Content'] = self.content
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateDocResponseBody(TeaModel):
    def __init__(self, knowledge_id=None, request_id=None):
        self.knowledge_id = knowledge_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDocResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFaqRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None, end_date=None, solution_content=None, solution_type=None,
                 start_date=None, title=None):
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long
        self.end_date = end_date  # type: str
        self.solution_content = solution_content  # type: str
        self.solution_type = solution_type  # type: int
        self.start_date = start_date  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFaqRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.solution_content is not None:
            result['SolutionContent'] = self.solution_content
        if self.solution_type is not None:
            result['SolutionType'] = self.solution_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('SolutionContent') is not None:
            self.solution_content = m.get('SolutionContent')
        if m.get('SolutionType') is not None:
            self.solution_type = m.get('SolutionType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateFaqResponseBody(TeaModel):
    def __init__(self, knowledge_id=None, request_id=None):
        self.knowledge_id = knowledge_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFaqResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFaqResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFaqResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFaqResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, agent_key=None, introduction=None, language_code=None, name=None, robot_type=None):
        self.agent_key = agent_key  # type: str
        self.introduction = introduction  # type: str
        self.language_code = language_code  # type: str
        self.name = name  # type: str
        self.robot_type = robot_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstancePublishTaskRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstancePublishTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstancePublishTaskResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, error=None, id=None, modify_time=None, request_id=None,
                 response=None, status=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.id = id  # type: long
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.response = response  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstancePublishTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateInstancePublishTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstancePublishTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstancePublishTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentRequestIntentDefinitionSlotInfos(TeaModel):
    def __init__(self, array=None, encrypt=None, interactive=None, name=None, slot_id=None, value=None):
        self.array = array  # type: bool
        self.encrypt = encrypt  # type: bool
        self.interactive = interactive  # type: bool
        self.name = name  # type: str
        self.slot_id = slot_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentRequestIntentDefinitionSlotInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateIntentRequestIntentDefinition(TeaModel):
    def __init__(self, alias_name=None, intent_name=None, slot_infos=None):
        self.alias_name = alias_name  # type: str
        self.intent_name = intent_name  # type: str
        self.slot_infos = slot_infos  # type: list[CreateIntentRequestIntentDefinitionSlotInfos]

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateIntentRequestIntentDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = CreateIntentRequestIntentDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class CreateIntentRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_definition=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_definition = intent_definition  # type: CreateIntentRequestIntentDefinition

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super(CreateIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            temp_model = CreateIntentRequestIntentDefinition()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        return self


class CreateIntentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_definition_shrink=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_definition_shrink = intent_definition_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        return self


class CreateIntentResponseBody(TeaModel):
    def __init__(self, intent_id=None, request_id=None):
        self.intent_id = intent_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIntentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIntentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLgfRequestLgfDefinition(TeaModel):
    def __init__(self, intent_id=None, rule_text=None):
        self.intent_id = intent_id  # type: long
        self.rule_text = rule_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLgfRequestLgfDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.rule_text is not None:
            result['RuleText'] = self.rule_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')
        return self


class CreateLgfRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, lgf_definition=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.lgf_definition = lgf_definition  # type: CreateLgfRequestLgfDefinition

    def validate(self):
        if self.lgf_definition:
            self.lgf_definition.validate()

    def to_map(self):
        _map = super(CreateLgfRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition is not None:
            result['LgfDefinition'] = self.lgf_definition.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            temp_model = CreateLgfRequestLgfDefinition()
            self.lgf_definition = temp_model.from_map(m['LgfDefinition'])
        return self


class CreateLgfShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, lgf_definition_shrink=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.lgf_definition_shrink = lgf_definition_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLgfShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition_shrink is not None:
            result['LgfDefinition'] = self.lgf_definition_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            self.lgf_definition_shrink = m.get('LgfDefinition')
        return self


class CreateLgfResponseBody(TeaModel):
    def __init__(self, lgf_id=None, request_id=None):
        # LGF ID
        self.lgf_id = lgf_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLgfResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLgfResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLgfResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLgfResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, description=None, name=None):
        self.agent_key = agent_key  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePerspectiveResponseBody(TeaModel):
    def __init__(self, perspective_id=None, request_id=None):
        self.perspective_id = perspective_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePerspectiveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePerspectiveResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePerspectiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublishTaskRequest(TeaModel):
    def __init__(self, agent_key=None, biz_type=None, data_id_list=None):
        self.agent_key = agent_key  # type: str
        self.biz_type = biz_type  # type: str
        self.data_id_list = data_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePublishTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data_id_list is not None:
            result['DataIdList'] = self.data_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DataIdList') is not None:
            self.data_id_list = m.get('DataIdList')
        return self


class CreatePublishTaskShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, biz_type=None, data_id_list_shrink=None):
        self.agent_key = agent_key  # type: str
        self.biz_type = biz_type  # type: str
        self.data_id_list_shrink = data_id_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePublishTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data_id_list_shrink is not None:
            result['DataIdList'] = self.data_id_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DataIdList') is not None:
            self.data_id_list_shrink = m.get('DataIdList')
        return self


class CreatePublishTaskResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, error=None, id=None, modify_time=None, request_id=None,
                 response=None, status=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.id = id  # type: long
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.response = response  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePublishTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreatePublishTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePublishTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePublishTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None, title=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSimQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateSimQuestionResponseBody(TeaModel):
    def __init__(self, request_id=None, sim_question_id=None):
        self.request_id = request_id  # type: str
        self.sim_question_id = sim_question_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSimQuestionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        return self


class CreateSimQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSimQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSimQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSolutionRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, content_type=None, knowledge_id=None, perspective_codes=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.content_type = content_type  # type: int
        self.knowledge_id = knowledge_id  # type: long
        self.perspective_codes = perspective_codes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        return self


class CreateSolutionResponseBody(TeaModel):
    def __init__(self, request_id=None, solution_id=None):
        self.request_id = request_id  # type: str
        self.solution_id = solution_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSolutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class CreateSolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSolutionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSolutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserSayRequestUserSayDefinitionSlotInfos(TeaModel):
    def __init__(self, end_index=None, slot_id=None, start_index=None):
        self.end_index = end_index  # type: int
        self.slot_id = slot_id  # type: str
        self.start_index = start_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserSayRequestUserSayDefinitionSlotInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        return self


class CreateUserSayRequestUserSayDefinition(TeaModel):
    def __init__(self, content=None, intent_id=None, slot_infos=None):
        self.content = content  # type: str
        self.intent_id = intent_id  # type: long
        self.slot_infos = slot_infos  # type: list[CreateUserSayRequestUserSayDefinitionSlotInfos]

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateUserSayRequestUserSayDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = CreateUserSayRequestUserSayDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class CreateUserSayRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, user_say_definition=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.user_say_definition = user_say_definition  # type: CreateUserSayRequestUserSayDefinition

    def validate(self):
        if self.user_say_definition:
            self.user_say_definition.validate()

    def to_map(self):
        _map = super(CreateUserSayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition is not None:
            result['UserSayDefinition'] = self.user_say_definition.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            temp_model = CreateUserSayRequestUserSayDefinition()
            self.user_say_definition = temp_model.from_map(m['UserSayDefinition'])
        return self


class CreateUserSayShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, user_say_definition_shrink=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.user_say_definition_shrink = user_say_definition_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserSayShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition_shrink is not None:
            result['UserSayDefinition'] = self.user_say_definition_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            self.user_say_definition_shrink = m.get('UserSayDefinition')
        return self


class CreateUserSayResponseBody(TeaModel):
    def __init__(self, request_id=None, user_say_id=None):
        self.request_id = request_id  # type: str
        self.user_say_id = user_say_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserSayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class CreateUserSayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserSayResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserSayResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None):
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DeleteCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCategoryResponseBody, self).to_map()
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


class DeleteCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCategoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, outline_id=None):
        self.agent_key = agent_key  # type: str
        self.outline_id = outline_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        return self


class DeleteConnQuestionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnQuestionResponseBody, self).to_map()
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


class DeleteConnQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteConnQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConnQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDSEntityRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDSEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDSEntityResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDSEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDSEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDSEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDSEntityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDSEntityValueRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, entity_value_id=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_value_id = entity_value_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDSEntityValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDSEntityValueResponseBody(TeaModel):
    def __init__(self, entity_value_id=None, request_id=None):
        self.entity_value_id = entity_value_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDSEntityValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDSEntityValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDSEntityValueResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDSEntityValueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDocRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DeleteDocResponseBody(TeaModel):
    def __init__(self, knowledge_id=None, request_id=None):
        self.knowledge_id = knowledge_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDocResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaqRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaqRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DeleteFaqResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaqResponseBody, self).to_map()
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


class DeleteFaqResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFaqResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFaqResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, create_user_id=None, create_user_name=None, error=None,
                 id=None, request_id=None, response=None, status=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: long
        self.create_user_name = create_user_name  # type: str
        self.error = error  # type: str
        self.id = id  # type: long
        self.request_id = request_id  # type: str
        self.response = response  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntentRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_id = intent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponseBody(TeaModel):
    def __init__(self, intent_id=None, request_id=None):
        self.intent_id = intent_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIntentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIntentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIntentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLgfRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_id=None, lgf_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_id = intent_id  # type: long
        # lgf Id
        self.lgf_id = lgf_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLgfRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        return self


class DeleteLgfResponseBody(TeaModel):
    def __init__(self, lgf_id=None, request_id=None):
        # LGF ID
        self.lgf_id = lgf_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLgfResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLgfResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLgfResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLgfResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, perspective_id=None):
        self.agent_key = agent_key  # type: str
        self.perspective_id = perspective_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DeletePerspectiveResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePerspectiveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeletePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePerspectiveResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePerspectiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSimQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, sim_question_id=None):
        self.agent_key = agent_key  # type: str
        self.sim_question_id = sim_question_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSimQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        return self


class DeleteSimQuestionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSimQuestionResponseBody, self).to_map()
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


class DeleteSimQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSimQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSimQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSolutionRequest(TeaModel):
    def __init__(self, agent_key=None, solution_id=None):
        self.agent_key = agent_key  # type: str
        self.solution_id = solution_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class DeleteSolutionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSolutionResponseBody, self).to_map()
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


class DeleteSolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSolutionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSolutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserSayRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_id=None, user_say_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_id = intent_id  # type: long
        self.user_say_id = user_say_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserSayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class DeleteUserSayResponseBody(TeaModel):
    def __init__(self, request_id=None, user_say_id=None):
        self.request_id = request_id  # type: str
        self.user_say_id = user_say_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserSayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class DeleteUserSayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserSayResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserSayResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None):
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DescribeCategoryResponseBodyCategory(TeaModel):
    def __init__(self, biz_code=None, category_id=None, name=None, parent_category_id=None, status=None):
        self.biz_code = biz_code  # type: str
        self.category_id = category_id  # type: long
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryResponseBodyCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCategoryResponseBody(TeaModel):
    def __init__(self, category=None, request_id=None):
        self.category = category  # type: DescribeCategoryResponseBodyCategory
        self.request_id = request_id  # type: str

    def validate(self):
        if self.category:
            self.category.validate()

    def to_map(self):
        _map = super(DescribeCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = DescribeCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m['Category'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCategoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDSEntityRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDSEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDSEntityResponseBody(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, entity_id=None,
                 entity_name=None, entity_type=None, modify_time=None, modify_user_id=None, modify_user_name=None,
                 request_id=None, sys_entity_code=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.request_id = request_id  # type: str
        self.sys_entity_code = sys_entity_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDSEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sys_entity_code is not None:
            result['SysEntityCode'] = self.sys_entity_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SysEntityCode') is not None:
            self.sys_entity_code = m.get('SysEntityCode')
        return self


class DescribeDSEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDSEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDSEntityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDocRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None, show_detail=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.show_detail = show_detail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')
        return self


class DescribeDocResponseBodyDocInfoDocParas(TeaModel):
    def __init__(self, para_level=None, para_no=None, para_text=None, para_type=None):
        self.para_level = para_level  # type: int
        self.para_no = para_no  # type: int
        self.para_text = para_text  # type: str
        self.para_type = para_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDocResponseBodyDocInfoDocParas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.para_level is not None:
            result['ParaLevel'] = self.para_level
        if self.para_no is not None:
            result['ParaNo'] = self.para_no
        if self.para_text is not None:
            result['ParaText'] = self.para_text
        if self.para_type is not None:
            result['ParaType'] = self.para_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParaLevel') is not None:
            self.para_level = m.get('ParaLevel')
        if m.get('ParaNo') is not None:
            self.para_no = m.get('ParaNo')
        if m.get('ParaText') is not None:
            self.para_text = m.get('ParaText')
        if m.get('ParaType') is not None:
            self.para_type = m.get('ParaType')
        return self


class DescribeDocResponseBodyDocInfo(TeaModel):
    def __init__(self, doc_paras=None):
        self.doc_paras = doc_paras  # type: list[DescribeDocResponseBodyDocInfoDocParas]

    def validate(self):
        if self.doc_paras:
            for k in self.doc_paras:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDocResponseBodyDocInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocParas'] = []
        if self.doc_paras is not None:
            for k in self.doc_paras:
                result['DocParas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.doc_paras = []
        if m.get('DocParas') is not None:
            for k in m.get('DocParas'):
                temp_model = DescribeDocResponseBodyDocInfoDocParas()
                self.doc_paras.append(temp_model.from_map(k))
        return self


class DescribeDocResponseBody(TeaModel):
    def __init__(self, biz_code=None, category_id=None, config=None, create_time=None, create_user_id=None,
                 create_user_name=None, doc_info=None, doc_name=None, effect_status=None, end_date=None, knowledge_id=None, meta=None,
                 modify_time=None, modify_user_id=None, modify_user_name=None, process_can_retry=None, process_message=None,
                 process_status=None, request_id=None, start_date=None, status=None, title=None, url=None):
        self.biz_code = biz_code  # type: str
        self.category_id = category_id  # type: long
        self.config = config  # type: str
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: long
        self.create_user_name = create_user_name  # type: str
        self.doc_info = doc_info  # type: DescribeDocResponseBodyDocInfo
        self.doc_name = doc_name  # type: str
        self.effect_status = effect_status  # type: int
        self.end_date = end_date  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.meta = meta  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: long
        self.modify_user_name = modify_user_name  # type: str
        self.process_can_retry = process_can_retry  # type: bool
        self.process_message = process_message  # type: str
        self.process_status = process_status  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.start_date = start_date  # type: str
        self.status = status  # type: int
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.doc_info:
            self.doc_info.validate()

    def to_map(self):
        _map = super(DescribeDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.doc_info is not None:
            result['DocInfo'] = self.doc_info.to_map()
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.process_can_retry is not None:
            result['ProcessCanRetry'] = self.process_can_retry
        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DocInfo') is not None:
            temp_model = DescribeDocResponseBodyDocInfo()
            self.doc_info = temp_model.from_map(m['DocInfo'])
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('ProcessCanRetry') is not None:
            self.process_can_retry = m.get('ProcessCanRetry')
        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDocResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaqRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaqRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DescribeFaqResponseBodyOutlines(TeaModel):
    def __init__(self, conn_question_id=None, create_time=None, modify_time=None, outline_id=None, title=None):
        self.conn_question_id = conn_question_id  # type: long
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.outline_id = outline_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaqResponseBodyOutlines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeFaqResponseBodySimQuestions(TeaModel):
    def __init__(self, create_time=None, modify_time=None, sim_question_id=None, title=None):
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.sim_question_id = sim_question_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaqResponseBodySimQuestions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeFaqResponseBodySolutions(TeaModel):
    def __init__(self, content=None, content_type=None, create_time=None, modify_time=None, perspective_codes=None,
                 plain_text=None, solution_id=None):
        self.content = content  # type: str
        self.content_type = content_type  # type: int
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.perspective_codes = perspective_codes  # type: list[str]
        self.plain_text = plain_text  # type: str
        self.solution_id = solution_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaqResponseBodySolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class DescribeFaqResponseBody(TeaModel):
    def __init__(self, category_id=None, create_time=None, create_user_name=None, effect_status=None, end_date=None,
                 knowledge_id=None, modify_time=None, modify_user_name=None, outlines=None, request_id=None, sim_questions=None,
                 solutions=None, start_date=None, status=None, title=None):
        self.category_id = category_id  # type: long
        self.create_time = create_time  # type: str
        self.create_user_name = create_user_name  # type: str
        self.effect_status = effect_status  # type: int
        self.end_date = end_date  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.modify_time = modify_time  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.outlines = outlines  # type: list[DescribeFaqResponseBodyOutlines]
        self.request_id = request_id  # type: str
        self.sim_questions = sim_questions  # type: list[DescribeFaqResponseBodySimQuestions]
        self.solutions = solutions  # type: list[DescribeFaqResponseBodySolutions]
        self.start_date = start_date  # type: str
        self.status = status  # type: int
        self.title = title  # type: str

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaqResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = DescribeFaqResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = DescribeFaqResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = DescribeFaqResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeFaqResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFaqResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaqResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceResponseBodyCategories(TeaModel):
    def __init__(self, category_id=None, name=None, parent_category_id=None):
        self.category_id = category_id  # type: long
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, avatar=None, categories=None, create_time=None, edit_status=None, instance_id=None,
                 introduction=None, language_code=None, name=None, request_id=None, robot_type=None, time_zone=None):
        self.avatar = avatar  # type: str
        self.categories = categories  # type: list[DescribeInstanceResponseBodyCategories]
        self.create_time = create_time  # type: str
        self.edit_status = edit_status  # type: str
        self.instance_id = instance_id  # type: str
        self.introduction = introduction  # type: str
        self.language_code = language_code  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.robot_type = robot_type  # type: str
        self.time_zone = time_zone  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.edit_status is not None:
            result['EditStatus'] = self.edit_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = DescribeInstanceResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EditStatus') is not None:
            self.edit_status = m.get('EditStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIntentRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_id = intent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DescribeIntentResponseBodySlotInfos(TeaModel):
    def __init__(self, array=None, encrypt=None, interactive=None, name=None, slot_id=None, value=None):
        self.array = array  # type: bool
        self.encrypt = encrypt  # type: bool
        self.interactive = interactive  # type: bool
        self.name = name  # type: str
        self.slot_id = slot_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIntentResponseBodySlotInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIntentResponseBody(TeaModel):
    def __init__(self, alias_name=None, create_time=None, create_user_id=None, create_user_name=None,
                 intent_id=None, intent_name=None, modify_time=None, modify_user_id=None, modify_user_name=None,
                 request_id=None, slot_infos=None):
        self.alias_name = alias_name  # type: str
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.intent_id = intent_id  # type: long
        self.intent_name = intent_name  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.request_id = request_id  # type: str
        self.slot_infos = slot_infos  # type: list[DescribeIntentResponseBodySlotInfos]

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = DescribeIntentResponseBodySlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class DescribeIntentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIntentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIntentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, perspective_id=None):
        self.agent_key = agent_key  # type: str
        self.perspective_id = perspective_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DescribePerspectiveResponseBody(TeaModel):
    def __init__(self, create_time=None, modify_time=None, name=None, perspective_code=None, perspective_id=None,
                 request_id=None, self_define=None, status=None):
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.name = name  # type: str
        self.perspective_code = perspective_code  # type: str
        self.perspective_id = perspective_id  # type: str
        self.request_id = request_id  # type: str
        self.self_define = self_define  # type: bool
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePerspectiveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePerspectiveResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePerspectiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackRequest(TeaModel):
    def __init__(self, agent_key=None, feedback=None, feedback_content=None, instance_id=None, message_id=None,
                 session_id=None):
        self.agent_key = agent_key  # type: str
        self.feedback = feedback  # type: str
        self.feedback_content = feedback_content  # type: str
        self.instance_id = instance_id  # type: str
        self.message_id = message_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeedbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.feedback_content is not None:
            result['FeedbackContent'] = self.feedback_content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('FeedbackContent') is not None:
            self.feedback_content = m.get('FeedbackContent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FeedbackResponseBody(TeaModel):
    def __init__(self, feedback=None, message_id=None, request_id=None):
        self.feedback = feedback  # type: str
        self.message_id = message_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeedbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FeedbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FeedbackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FeedbackResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUserAccessTokenRequest(TeaModel):
    def __init__(self, agent_key=None, email=None, expire_time=None, extra_info=None, foreign_id=None, nick=None,
                 telephone=None):
        self.agent_key = agent_key  # type: str
        self.email = email  # type: str
        self.expire_time = expire_time  # type: int
        self.extra_info = extra_info  # type: str
        self.foreign_id = foreign_id  # type: str
        self.nick = nick  # type: str
        self.telephone = telephone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUserAccessTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.email is not None:
            result['Email'] = self.email
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.foreign_id is not None:
            result['ForeignId'] = self.foreign_id
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('ForeignId') is not None:
            self.foreign_id = m.get('ForeignId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class GenerateUserAccessTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUserAccessTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateUserAccessTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateUserAccessTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUserAccessTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateUserAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentInfoRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAgentInfoResponseBodyData(TeaModel):
    def __init__(self, agent_key=None, agent_name=None):
        self.agent_key = agent_key  # type: str
        self.agent_name = agent_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        return self


class GetAgentInfoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: GetAgentInfoResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAgentInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAgentInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAgentInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(self, agent_key=None, task_id=None):
        self.agent_key = agent_key  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAsyncResultResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, status=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAsyncResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstancePublishTaskStateRequest(TeaModel):
    def __init__(self, agent_key=None, id=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstancePublishTaskStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstancePublishTaskStateResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, error=None, errors=None, id=None, modify_time=None,
                 request_id=None, response=None, status=None, warnings=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.errors = errors  # type: dict[str, any]
        self.id = id  # type: long
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.response = response  # type: str
        self.status = status  # type: str
        self.warnings = warnings  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstancePublishTaskStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.warnings is not None:
            result['Warnings'] = self.warnings
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')
        return self


class GetInstancePublishTaskStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstancePublishTaskStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstancePublishTaskStateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstancePublishTaskStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublishTaskStateRequest(TeaModel):
    def __init__(self, agent_key=None, id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublishTaskStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetPublishTaskStateResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, create_time=None, error=None, errors=None, id=None, modify_time=None,
                 request_id=None, response=None, status=None, warnings=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.errors = errors  # type: dict[str, any]
        self.id = id  # type: long
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.response = response  # type: str
        self.status = status  # type: str
        self.warnings = warnings  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublishTaskStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.warnings is not None:
            result['Warnings'] = self.warnings
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')
        return self


class GetPublishTaskStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPublishTaskStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPublishTaskStateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPublishTaskStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitIMConnectRequest(TeaModel):
    def __init__(self, agent_key=None, from_=None, user_access_token=None):
        self.agent_key = agent_key  # type: str
        self.from_ = from_  # type: str
        self.user_access_token = user_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitIMConnectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.from_ is not None:
            result['From'] = self.from_
        if self.user_access_token is not None:
            result['UserAccessToken'] = self.user_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('UserAccessToken') is not None:
            self.user_access_token = m.get('UserAccessToken')
        return self


class InitIMConnectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitIMConnectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InitIMConnectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitIMConnectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitIMConnectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitIMConnectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkInstanceCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, category_ids=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.category_ids = category_ids  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LinkInstanceCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class LinkInstanceCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LinkInstanceCategoryResponseBody, self).to_map()
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


class LinkInstanceCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LinkInstanceCategoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LinkInstanceCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LinkInstanceCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentRequest(TeaModel):
    def __init__(self, agent_name=None, goods_codes=None, page_number=None, page_size=None, product_code=None):
        self.agent_name = agent_name  # type: str
        self.goods_codes = goods_codes  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAgentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.goods_codes is not None:
            result['GoodsCodes'] = self.goods_codes
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('GoodsCodes') is not None:
            self.goods_codes = m.get('GoodsCodes')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListAgentResponseBodyData(TeaModel):
    def __init__(self, agent_id=None, agent_key=None, agent_name=None, default_agent=None, instance_infos=None):
        self.agent_id = agent_id  # type: long
        self.agent_key = agent_key  # type: str
        self.agent_name = agent_name  # type: str
        self.default_agent = default_agent  # type: bool
        self.instance_infos = instance_infos  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAgentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.default_agent is not None:
            result['DefaultAgent'] = self.default_agent
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('DefaultAgent') is not None:
            self.default_agent = m.get('DefaultAgent')
        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')
        return self


class ListAgentResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListAgentResponseBodyData]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAgentResponseBody, self).to_map()
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
                temp_model = ListAgentResponseBodyData()
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


class ListAgentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAgentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAgentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_type=None, parent_category_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_type = knowledge_type  # type: int
        self.parent_category_id = parent_category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class ListCategoryResponseBodyCategories(TeaModel):
    def __init__(self, biz_code=None, category_id=None, name=None, parent_category_id=None, status=None):
        self.biz_code = biz_code  # type: str
        self.category_id = category_id  # type: long
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCategoryResponseBodyCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCategoryResponseBody(TeaModel):
    def __init__(self, categories=None, request_id=None):
        self.categories = categories  # type: list[ListCategoryResponseBodyCategories]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = ListCategoryResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCategoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class ListConnQuestionResponseBodyOutlines(TeaModel):
    def __init__(self, conn_question_id=None, create_time=None, modify_time=None, outline_id=None, title=None):
        self.conn_question_id = conn_question_id  # type: long
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.outline_id = outline_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnQuestionResponseBodyOutlines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListConnQuestionResponseBody(TeaModel):
    def __init__(self, outlines=None, request_id=None):
        self.outlines = outlines  # type: list[ListConnQuestionResponseBodyOutlines]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnQuestionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListConnQuestionResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConnQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConnQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDSEntityRequest(TeaModel):
    def __init__(self, agent_key=None, entity_type=None, instance_id=None, keyword=None, page_number=None,
                 page_size=None):
        self.agent_key = agent_key  # type: str
        self.entity_type = entity_type  # type: str
        self.instance_id = instance_id  # type: str
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDSEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDSEntityResponseBodyEntities(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, entity_id=None,
                 entity_name=None, entity_type=None, modify_time=None, modify_user_id=None, modify_user_name=None,
                 sys_entity_code=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.sys_entity_code = sys_entity_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDSEntityResponseBodyEntities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.sys_entity_code is not None:
            result['SysEntityCode'] = self.sys_entity_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('SysEntityCode') is not None:
            self.sys_entity_code = m.get('SysEntityCode')
        return self


class ListDSEntityResponseBody(TeaModel):
    def __init__(self, entities=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.entities = entities  # type: list[ListDSEntityResponseBodyEntities]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDSEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
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
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListDSEntityResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDSEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDSEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDSEntityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDSEntityValueRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, entity_value_id=None, instance_id=None, keyword=None,
                 page_number=None, page_size=None):
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_value_id = entity_value_id  # type: long
        self.instance_id = instance_id  # type: str
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDSEntityValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDSEntityValueResponseBodyEntityValues(TeaModel):
    def __init__(self, content=None, create_time=None, entity_id=None, entity_value_id=None, modify_time=None,
                 synonyms=None):
        self.content = content  # type: str
        self.create_time = create_time  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_value_id = entity_value_id  # type: long
        self.modify_time = modify_time  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDSEntityValueResponseBodyEntityValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class ListDSEntityValueResponseBody(TeaModel):
    def __init__(self, entity_values=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.entity_values = entity_values  # type: list[ListDSEntityValueResponseBodyEntityValues]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.entity_values:
            for k in self.entity_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDSEntityValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityValues'] = []
        if self.entity_values is not None:
            for k in self.entity_values:
                result['EntityValues'].append(k.to_map() if k else None)
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
        self.entity_values = []
        if m.get('EntityValues') is not None:
            for k in m.get('EntityValues'):
                temp_model = ListDSEntityValueResponseBodyEntityValues()
                self.entity_values.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDSEntityValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDSEntityValueResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDSEntityValueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(self, agent_key=None, name=None, page_number=None, page_size=None, robot_type=None):
        self.agent_key = agent_key  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.robot_type = robot_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class ListInstanceResponseBodyInstances(TeaModel):
    def __init__(self, avatar=None, create_time=None, instance_id=None, introduction=None, language_code=None,
                 name=None, robot_type=None):
        self.avatar = avatar  # type: str
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.introduction = introduction  # type: str
        self.language_code = language_code  # type: str
        self.name = name  # type: str
        self.robot_type = robot_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.instances = instances  # type: list[ListInstanceResponseBodyInstances]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
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
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntentRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_name=None, page_number=None, page_size=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_name = intent_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIntentResponseBodyIntentsSlotInfos(TeaModel):
    def __init__(self, array=None, encrypt=None, interactive=None, name=None, slot_id=None, value=None):
        self.array = array  # type: bool
        self.encrypt = encrypt  # type: bool
        self.interactive = interactive  # type: bool
        self.name = name  # type: str
        self.slot_id = slot_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntentResponseBodyIntentsSlotInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListIntentResponseBodyIntents(TeaModel):
    def __init__(self, alias_name=None, create_time=None, create_user_id=None, create_user_name=None,
                 intent_id=None, intent_name=None, modify_time=None, modify_user_id=None, modify_user_name=None,
                 slot_infos=None):
        self.alias_name = alias_name  # type: str
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.intent_id = intent_id  # type: long
        self.intent_name = intent_name  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.slot_infos = slot_infos  # type: list[ListIntentResponseBodyIntentsSlotInfos]

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIntentResponseBodyIntents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = ListIntentResponseBodyIntentsSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class ListIntentResponseBody(TeaModel):
    def __init__(self, intents=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.intents = intents  # type: list[ListIntentResponseBodyIntents]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.intents:
            for k in self.intents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intents'] = []
        if self.intents is not None:
            for k in self.intents:
                result['Intents'].append(k.to_map() if k else None)
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
        self.intents = []
        if m.get('Intents') is not None:
            for k in m.get('Intents'):
                temp_model = ListIntentResponseBodyIntents()
                self.intents.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIntentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIntentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIntentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLgfRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_id=None, lgf_text=None, page_number=None,
                 page_size=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_id = intent_id  # type: long
        self.lgf_text = lgf_text  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLgfRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.lgf_text is not None:
            result['LgfText'] = self.lgf_text
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('LgfText') is not None:
            self.lgf_text = m.get('LgfText')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLgfResponseBodyLgfs(TeaModel):
    def __init__(self, create_time=None, intent_id=None, lgf_id=None, modify_time=None, rule_text=None):
        self.create_time = create_time  # type: str
        self.intent_id = intent_id  # type: long
        # LGF ID
        self.lgf_id = lgf_id  # type: long
        self.modify_time = modify_time  # type: str
        self.rule_text = rule_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLgfResponseBodyLgfs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.rule_text is not None:
            result['RuleText'] = self.rule_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')
        return self


class ListLgfResponseBody(TeaModel):
    def __init__(self, lgfs=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.lgfs = lgfs  # type: list[ListLgfResponseBodyLgfs]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.lgfs:
            for k in self.lgfs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLgfResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Lgfs'] = []
        if self.lgfs is not None:
            for k in self.lgfs:
                result['Lgfs'].append(k.to_map() if k else None)
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
        self.lgfs = []
        if m.get('Lgfs') is not None:
            for k in m.get('Lgfs'):
                temp_model = ListLgfResponseBodyLgfs()
                self.lgfs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLgfResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLgfResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLgfResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSaasInfoRequest(TeaModel):
    def __init__(self, agent_key=None, saas_group_codes=None, saas_name=None):
        self.agent_key = agent_key  # type: str
        self.saas_group_codes = saas_group_codes  # type: str
        self.saas_name = saas_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSaasInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.saas_group_codes is not None:
            result['SaasGroupCodes'] = self.saas_group_codes
        if self.saas_name is not None:
            result['SaasName'] = self.saas_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SaasGroupCodes') is not None:
            self.saas_group_codes = m.get('SaasGroupCodes')
        if m.get('SaasName') is not None:
            self.saas_name = m.get('SaasName')
        return self


class ListSaasInfoResponseBodyData(TeaModel):
    def __init__(self, code=None, en_name=None, name=None, service_url=None, url=None):
        self.code = code  # type: str
        self.en_name = en_name  # type: str
        self.name = name  # type: str
        self.service_url = service_url  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSaasInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.name is not None:
            result['Name'] = self.name
        if self.service_url is not None:
            result['ServiceUrl'] = self.service_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceUrl') is not None:
            self.service_url = m.get('ServiceUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListSaasInfoResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, saas_token=None):
        self.data = data  # type: list[ListSaasInfoResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str
        self.saas_token = saas_token  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSaasInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.saas_token is not None:
            result['SaasToken'] = self.saas_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSaasInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SaasToken') is not None:
            self.saas_token = m.get('SaasToken')
        return self


class ListSaasInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSaasInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSaasInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSaasInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSaasPermissionGroupInfosRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSaasPermissionGroupInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ListSaasPermissionGroupInfosResponseBodyDataPgInfos(TeaModel):
    def __init__(self, pg_code=None, pg_en_name=None, pg_name=None):
        self.pg_code = pg_code  # type: str
        self.pg_en_name = pg_en_name  # type: str
        self.pg_name = pg_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSaasPermissionGroupInfosResponseBodyDataPgInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pg_code is not None:
            result['PgCode'] = self.pg_code
        if self.pg_en_name is not None:
            result['PgEnName'] = self.pg_en_name
        if self.pg_name is not None:
            result['PgName'] = self.pg_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PgCode') is not None:
            self.pg_code = m.get('PgCode')
        if m.get('PgEnName') is not None:
            self.pg_en_name = m.get('PgEnName')
        if m.get('PgName') is not None:
            self.pg_name = m.get('PgName')
        return self


class ListSaasPermissionGroupInfosResponseBodyData(TeaModel):
    def __init__(self, en_name=None, name=None, pg_infos=None, saas_code=None):
        self.en_name = en_name  # type: str
        self.name = name  # type: str
        self.pg_infos = pg_infos  # type: list[ListSaasPermissionGroupInfosResponseBodyDataPgInfos]
        self.saas_code = saas_code  # type: str

    def validate(self):
        if self.pg_infos:
            for k in self.pg_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSaasPermissionGroupInfosResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.name is not None:
            result['Name'] = self.name
        result['PgInfos'] = []
        if self.pg_infos is not None:
            for k in self.pg_infos:
                result['PgInfos'].append(k.to_map() if k else None)
        if self.saas_code is not None:
            result['SaasCode'] = self.saas_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.pg_infos = []
        if m.get('PgInfos') is not None:
            for k in m.get('PgInfos'):
                temp_model = ListSaasPermissionGroupInfosResponseBodyDataPgInfos()
                self.pg_infos.append(temp_model.from_map(k))
        if m.get('SaasCode') is not None:
            self.saas_code = m.get('SaasCode')
        return self


class ListSaasPermissionGroupInfosResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListSaasPermissionGroupInfosResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSaasPermissionGroupInfosResponseBody, self).to_map()
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
                temp_model = ListSaasPermissionGroupInfosResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSaasPermissionGroupInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSaasPermissionGroupInfosResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSaasPermissionGroupInfosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSaasPermissionGroupInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSimQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSimQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class ListSimQuestionResponseBodySimQuestions(TeaModel):
    def __init__(self, create_time=None, modify_time=None, sim_question_id=None, title=None):
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.sim_question_id = sim_question_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSimQuestionResponseBodySimQuestions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListSimQuestionResponseBody(TeaModel):
    def __init__(self, request_id=None, sim_questions=None):
        self.request_id = request_id  # type: str
        self.sim_questions = sim_questions  # type: list[ListSimQuestionResponseBodySimQuestions]

    def validate(self):
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSimQuestionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = ListSimQuestionResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        return self


class ListSimQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSimQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSimQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSolutionRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class ListSolutionResponseBodySolutions(TeaModel):
    def __init__(self, content=None, content_type=None, create_time=None, modify_time=None, perspective_codes=None,
                 plain_text=None, solution_id=None):
        self.content = content  # type: str
        self.content_type = content_type  # type: int
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.perspective_codes = perspective_codes  # type: list[str]
        self.plain_text = plain_text  # type: str
        self.solution_id = solution_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSolutionResponseBodySolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class ListSolutionResponseBody(TeaModel):
    def __init__(self, request_id=None, solutions=None):
        self.request_id = request_id  # type: str
        self.solutions = solutions  # type: list[ListSolutionResponseBodySolutions]

    def validate(self):
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSolutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = ListSolutionResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        return self


class ListSolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSolutionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSolutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserSayRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, instance_id=None, intent_id=None, page_number=None,
                 page_size=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_id = intent_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserSayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserSayResponseBodyUserSaysSlotInfos(TeaModel):
    def __init__(self, end_index=None, slot_id=None, start_index=None):
        self.end_index = end_index  # type: int
        self.slot_id = slot_id  # type: str
        self.start_index = start_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserSayResponseBodyUserSaysSlotInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        return self


class ListUserSayResponseBodyUserSays(TeaModel):
    def __init__(self, content=None, create_time=None, intent_id=None, modify_time=None, slot_infos=None,
                 user_say_id=None):
        self.content = content  # type: str
        self.create_time = create_time  # type: str
        self.intent_id = intent_id  # type: long
        self.modify_time = modify_time  # type: str
        self.slot_infos = slot_infos  # type: list[ListUserSayResponseBodyUserSaysSlotInfos]
        self.user_say_id = user_say_id  # type: long

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserSayResponseBodyUserSays, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = ListUserSayResponseBodyUserSaysSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class ListUserSayResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, user_says=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.user_says = user_says  # type: list[ListUserSayResponseBodyUserSays]

    def validate(self):
        if self.user_says:
            for k in self.user_says:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserSayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserSays'] = []
        if self.user_says is not None:
            for k in self.user_says:
                result['UserSays'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_says = []
        if m.get('UserSays') is not None:
            for k in m.get('UserSays'):
                temp_model = ListUserSayResponseBodyUserSays()
                self.user_says.append(temp_model.from_map(k))
        return self


class ListUserSayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserSayResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserSayResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NluRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, utterance=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.utterance = utterance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NluRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class NluResponseBodyMessagesDialogHubNluInfoGlobalDictList(TeaModel):
    def __init__(self, standard_word=None, word=None):
        self.standard_word = standard_word  # type: str
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NluResponseBodyMessagesDialogHubNluInfoGlobalDictList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.standard_word is not None:
            result['StandardWord'] = self.standard_word
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StandardWord') is not None:
            self.standard_word = m.get('StandardWord')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList(TeaModel):
    def __init__(self, standard_word=None, word=None):
        self.standard_word = standard_word  # type: str
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.standard_word is not None:
            result['StandardWord'] = self.standard_word
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StandardWord') is not None:
            self.standard_word = m.get('StandardWord')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class NluResponseBodyMessagesDialogHubNluInfo(TeaModel):
    def __init__(self, global_dict_list=None, global_sensitive_word_list=None):
        self.global_dict_list = global_dict_list  # type: list[NluResponseBodyMessagesDialogHubNluInfoGlobalDictList]
        self.global_sensitive_word_list = global_sensitive_word_list  # type: list[NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList]

    def validate(self):
        if self.global_dict_list:
            for k in self.global_dict_list:
                if k:
                    k.validate()
        if self.global_sensitive_word_list:
            for k in self.global_sensitive_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NluResponseBodyMessagesDialogHubNluInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GlobalDictList'] = []
        if self.global_dict_list is not None:
            for k in self.global_dict_list:
                result['GlobalDictList'].append(k.to_map() if k else None)
        result['GlobalSensitiveWordList'] = []
        if self.global_sensitive_word_list is not None:
            for k in self.global_sensitive_word_list:
                result['GlobalSensitiveWordList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.global_dict_list = []
        if m.get('GlobalDictList') is not None:
            for k in m.get('GlobalDictList'):
                temp_model = NluResponseBodyMessagesDialogHubNluInfoGlobalDictList()
                self.global_dict_list.append(temp_model.from_map(k))
        self.global_sensitive_word_list = []
        if m.get('GlobalSensitiveWordList') is not None:
            for k in m.get('GlobalSensitiveWordList'):
                temp_model = NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList()
                self.global_sensitive_word_list.append(temp_model.from_map(k))
        return self


class NluResponseBodyMessagesDsNluInfoEntityList(TeaModel):
    def __init__(self, name=None, origin=None, type=None, value=None):
        self.name = name  # type: str
        self.origin = origin  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NluResponseBodyMessagesDsNluInfoEntityList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class NluResponseBodyMessagesDsNluInfoIntentListSlotList(TeaModel):
    def __init__(self, name=None, origin=None, type=None, value=None):
        self.name = name  # type: str
        self.origin = origin  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NluResponseBodyMessagesDsNluInfoIntentListSlotList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class NluResponseBodyMessagesDsNluInfoIntentList(TeaModel):
    def __init__(self, intent_id=None, match_detail=None, match_type=None, name=None, score=None, slot_list=None):
        self.intent_id = intent_id  # type: long
        self.match_detail = match_detail  # type: str
        self.match_type = match_type  # type: str
        self.name = name  # type: str
        self.score = score  # type: float
        self.slot_list = slot_list  # type: list[NluResponseBodyMessagesDsNluInfoIntentListSlotList]

    def validate(self):
        if self.slot_list:
            for k in self.slot_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NluResponseBodyMessagesDsNluInfoIntentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        result['SlotList'] = []
        if self.slot_list is not None:
            for k in self.slot_list:
                result['SlotList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.slot_list = []
        if m.get('SlotList') is not None:
            for k in m.get('SlotList'):
                temp_model = NluResponseBodyMessagesDsNluInfoIntentListSlotList()
                self.slot_list.append(temp_model.from_map(k))
        return self


class NluResponseBodyMessagesDsNluInfo(TeaModel):
    def __init__(self, entity_list=None, intent_list=None):
        self.entity_list = entity_list  # type: list[NluResponseBodyMessagesDsNluInfoEntityList]
        self.intent_list = intent_list  # type: list[NluResponseBodyMessagesDsNluInfoIntentList]

    def validate(self):
        if self.entity_list:
            for k in self.entity_list:
                if k:
                    k.validate()
        if self.intent_list:
            for k in self.intent_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NluResponseBodyMessagesDsNluInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityList'] = []
        if self.entity_list is not None:
            for k in self.entity_list:
                result['EntityList'].append(k.to_map() if k else None)
        result['IntentList'] = []
        if self.intent_list is not None:
            for k in self.intent_list:
                result['IntentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entity_list = []
        if m.get('EntityList') is not None:
            for k in m.get('EntityList'):
                temp_model = NluResponseBodyMessagesDsNluInfoEntityList()
                self.entity_list.append(temp_model.from_map(k))
        self.intent_list = []
        if m.get('IntentList') is not None:
            for k in m.get('IntentList'):
                temp_model = NluResponseBodyMessagesDsNluInfoIntentList()
                self.intent_list.append(temp_model.from_map(k))
        return self


class NluResponseBodyMessages(TeaModel):
    def __init__(self, dialog_hub_nlu_info=None, ds_nlu_info=None):
        self.dialog_hub_nlu_info = dialog_hub_nlu_info  # type: NluResponseBodyMessagesDialogHubNluInfo
        self.ds_nlu_info = ds_nlu_info  # type: NluResponseBodyMessagesDsNluInfo

    def validate(self):
        if self.dialog_hub_nlu_info:
            self.dialog_hub_nlu_info.validate()
        if self.ds_nlu_info:
            self.ds_nlu_info.validate()

    def to_map(self):
        _map = super(NluResponseBodyMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_hub_nlu_info is not None:
            result['DialogHubNluInfo'] = self.dialog_hub_nlu_info.to_map()
        if self.ds_nlu_info is not None:
            result['DsNluInfo'] = self.ds_nlu_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DialogHubNluInfo') is not None:
            temp_model = NluResponseBodyMessagesDialogHubNluInfo()
            self.dialog_hub_nlu_info = temp_model.from_map(m['DialogHubNluInfo'])
        if m.get('DsNluInfo') is not None:
            temp_model = NluResponseBodyMessagesDsNluInfo()
            self.ds_nlu_info = temp_model.from_map(m['DsNluInfo'])
        return self


class NluResponseBody(TeaModel):
    def __init__(self, message_id=None, messages=None, request_id=None):
        self.message_id = message_id  # type: str
        self.messages = messages  # type: list[NluResponseBodyMessages]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NluResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = NluResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NluResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NluResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NluResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = NluResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPerspectivesRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPerspectivesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class QueryPerspectivesResponseBodyPerspectives(TeaModel):
    def __init__(self, create_time=None, modify_time=None, name=None, perspective_code=None, perspective_id=None,
                 self_define=None, status=None):
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.name = name  # type: str
        self.perspective_code = perspective_code  # type: str
        self.perspective_id = perspective_id  # type: str
        self.self_define = self_define  # type: bool
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPerspectivesResponseBodyPerspectives, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPerspectivesResponseBody(TeaModel):
    def __init__(self, perspectives=None, request_id=None):
        self.perspectives = perspectives  # type: list[QueryPerspectivesResponseBodyPerspectives]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.perspectives:
            for k in self.perspectives:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPerspectivesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Perspectives'] = []
        if self.perspectives is not None:
            for k in self.perspectives:
                result['Perspectives'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.perspectives = []
        if m.get('Perspectives') is not None:
            for k in m.get('Perspectives'):
                temp_model = QueryPerspectivesResponseBodyPerspectives()
                self.perspectives.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPerspectivesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPerspectivesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPerspectivesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPerspectivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryDocRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class RetryDocResponseBody(TeaModel):
    def __init__(self, knowledge_id=None, request_id=None):
        self.knowledge_id = knowledge_id  # type: long
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetryDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RetryDocResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RetryDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RetryDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDocRequest(TeaModel):
    def __init__(self, agent_key=None, category_ids=None, create_time_begin=None, create_time_end=None,
                 create_user_name=None, end_time_begin=None, end_time_end=None, keyword=None, modify_time_begin=None,
                 modify_time_end=None, modify_user_name=None, page_number=None, page_size=None, process_status=None,
                 search_scope=None, start_time_begin=None, start_time_end=None, status=None):
        self.agent_key = agent_key  # type: str
        self.category_ids = category_ids  # type: list[long]
        self.create_time_begin = create_time_begin  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_user_name = create_user_name  # type: str
        self.end_time_begin = end_time_begin  # type: str
        self.end_time_end = end_time_end  # type: str
        self.keyword = keyword  # type: str
        self.modify_time_begin = modify_time_begin  # type: str
        self.modify_time_end = modify_time_end  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.process_status = process_status  # type: int
        self.search_scope = search_scope  # type: int
        self.start_time_begin = start_time_begin  # type: str
        self.start_time_end = start_time_end  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchDocShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, category_ids_shrink=None, create_time_begin=None, create_time_end=None,
                 create_user_name=None, end_time_begin=None, end_time_end=None, keyword=None, modify_time_begin=None,
                 modify_time_end=None, modify_user_name=None, page_number=None, page_size=None, process_status=None,
                 search_scope=None, start_time_begin=None, start_time_end=None, status=None):
        self.agent_key = agent_key  # type: str
        self.category_ids_shrink = category_ids_shrink  # type: str
        self.create_time_begin = create_time_begin  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_user_name = create_user_name  # type: str
        self.end_time_begin = end_time_begin  # type: str
        self.end_time_end = end_time_end  # type: str
        self.keyword = keyword  # type: str
        self.modify_time_begin = modify_time_begin  # type: str
        self.modify_time_end = modify_time_end  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.process_status = process_status  # type: int
        self.search_scope = search_scope  # type: int
        self.start_time_begin = start_time_begin  # type: str
        self.start_time_end = start_time_end  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchDocShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchDocResponseBodyDocHits(TeaModel):
    def __init__(self, biz_code=None, category_id=None, config=None, create_time=None, create_user_id=None,
                 create_user_name=None, doc_name=None, effect_status=None, end_date=None, knowledge_id=None, meta=None,
                 modify_time=None, modify_user_id=None, modify_user_name=None, process_can_retry=None, process_message=None,
                 process_status=None, start_date=None, status=None, url=None):
        self.biz_code = biz_code  # type: str
        self.category_id = category_id  # type: long
        self.config = config  # type: str
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: long
        self.create_user_name = create_user_name  # type: str
        self.doc_name = doc_name  # type: str
        self.effect_status = effect_status  # type: int
        self.end_date = end_date  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.meta = meta  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: long
        self.modify_user_name = modify_user_name  # type: str
        self.process_can_retry = process_can_retry  # type: bool
        self.process_message = process_message  # type: str
        self.process_status = process_status  # type: int
        self.start_date = start_date  # type: str
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchDocResponseBodyDocHits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.process_can_retry is not None:
            result['ProcessCanRetry'] = self.process_can_retry
        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('ProcessCanRetry') is not None:
            self.process_can_retry = m.get('ProcessCanRetry')
        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SearchDocResponseBody(TeaModel):
    def __init__(self, doc_hits=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.doc_hits = doc_hits  # type: list[SearchDocResponseBodyDocHits]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.doc_hits:
            for k in self.doc_hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocHits'] = []
        if self.doc_hits is not None:
            for k in self.doc_hits:
                result['DocHits'].append(k.to_map() if k else None)
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
        self.doc_hits = []
        if m.get('DocHits') is not None:
            for k in m.get('DocHits'):
                temp_model = SearchDocResponseBodyDocHits()
                self.doc_hits.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchDocResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFaqRequest(TeaModel):
    def __init__(self, agent_key=None, category_ids=None, create_time_begin=None, create_time_end=None,
                 create_user_name=None, end_time_begin=None, end_time_end=None, keyword=None, modify_time_begin=None,
                 modify_time_end=None, modify_user_name=None, page_number=None, page_size=None, search_scope=None,
                 start_time_begin=None, start_time_end=None, status=None):
        self.agent_key = agent_key  # type: str
        self.category_ids = category_ids  # type: list[long]
        self.create_time_begin = create_time_begin  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_user_name = create_user_name  # type: str
        self.end_time_begin = end_time_begin  # type: str
        self.end_time_end = end_time_end  # type: str
        self.keyword = keyword  # type: str
        self.modify_time_begin = modify_time_begin  # type: str
        self.modify_time_end = modify_time_end  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.search_scope = search_scope  # type: int
        self.start_time_begin = start_time_begin  # type: str
        self.start_time_end = start_time_end  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchFaqRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchFaqShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, category_ids_shrink=None, create_time_begin=None, create_time_end=None,
                 create_user_name=None, end_time_begin=None, end_time_end=None, keyword=None, modify_time_begin=None,
                 modify_time_end=None, modify_user_name=None, page_number=None, page_size=None, search_scope=None,
                 start_time_begin=None, start_time_end=None, status=None):
        self.agent_key = agent_key  # type: str
        self.category_ids_shrink = category_ids_shrink  # type: str
        self.create_time_begin = create_time_begin  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_user_name = create_user_name  # type: str
        self.end_time_begin = end_time_begin  # type: str
        self.end_time_end = end_time_end  # type: str
        self.keyword = keyword  # type: str
        self.modify_time_begin = modify_time_begin  # type: str
        self.modify_time_end = modify_time_end  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.search_scope = search_scope  # type: int
        self.start_time_begin = start_time_begin  # type: str
        self.start_time_end = start_time_end  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchFaqShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchFaqResponseBodyFaqHits(TeaModel):
    def __init__(self, category_id=None, create_time=None, create_user_id=None, create_user_name=None,
                 effect_status=None, hit_similar_titles=None, hit_solutions=None, knowledge_id=None, modify_time=None,
                 modify_user_id=None, modify_user_name=None, status=None, title=None):
        self.category_id = category_id  # type: long
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: long
        self.create_user_name = create_user_name  # type: str
        self.effect_status = effect_status  # type: int
        self.hit_similar_titles = hit_similar_titles  # type: list[str]
        self.hit_solutions = hit_solutions  # type: list[str]
        self.knowledge_id = knowledge_id  # type: long
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: long
        self.modify_user_name = modify_user_name  # type: str
        self.status = status  # type: int
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchFaqResponseBodyFaqHits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.hit_similar_titles is not None:
            result['HitSimilarTitles'] = self.hit_similar_titles
        if self.hit_solutions is not None:
            result['HitSolutions'] = self.hit_solutions
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('HitSimilarTitles') is not None:
            self.hit_similar_titles = m.get('HitSimilarTitles')
        if m.get('HitSolutions') is not None:
            self.hit_solutions = m.get('HitSolutions')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchFaqResponseBody(TeaModel):
    def __init__(self, faq_hits=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.faq_hits = faq_hits  # type: list[SearchFaqResponseBodyFaqHits]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.faq_hits:
            for k in self.faq_hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchFaqResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaqHits'] = []
        if self.faq_hits is not None:
            for k in self.faq_hits:
                result['FaqHits'].append(k.to_map() if k else None)
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
        self.faq_hits = []
        if m.get('FaqHits') is not None:
            for k in m.get('FaqHits'):
                temp_model = SearchFaqResponseBodyFaqHits()
                self.faq_hits.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchFaqResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchFaqResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchFaqResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, biz_code=None, category_id=None, name=None):
        self.agent_key = agent_key  # type: str
        self.biz_code = biz_code  # type: str
        self.category_id = category_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCategoryResponseBody, self).to_map()
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


class UpdateCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCategoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, conn_question_id=None, outline_id=None):
        self.agent_key = agent_key  # type: str
        self.conn_question_id = conn_question_id  # type: long
        self.outline_id = outline_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        return self


class UpdateConnQuestionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnQuestionResponseBody, self).to_map()
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


class UpdateConnQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConnQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConnQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDSEntityRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, entity_name=None, entity_type=None, instance_id=None):
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDSEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDSEntityResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDSEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDSEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDSEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDSEntityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDSEntityValueRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, entity_id=None, entity_value_id=None, instance_id=None,
                 synonyms=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_value_id = entity_value_id  # type: long
        self.instance_id = instance_id  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDSEntityValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class UpdateDSEntityValueShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, entity_id=None, entity_value_id=None, instance_id=None,
                 synonyms_shrink=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_value_id = entity_value_id  # type: long
        self.instance_id = instance_id  # type: str
        self.synonyms_shrink = synonyms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDSEntityValueShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms_shrink is not None:
            result['Synonyms'] = self.synonyms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms_shrink = m.get('Synonyms')
        return self


class UpdateDSEntityValueResponseBody(TeaModel):
    def __init__(self, entity_value_id=None, request_id=None):
        self.entity_value_id = entity_value_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDSEntityValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDSEntityValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDSEntityValueResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDSEntityValueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDocRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None, config=None, content=None, doc_name=None, end_date=None,
                 knowledge_id=None, meta=None, start_date=None, title=None):
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long
        self.config = config  # type: str
        self.content = content  # type: str
        self.doc_name = doc_name  # type: str
        self.end_date = end_date  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.meta = meta  # type: str
        self.start_date = start_date  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateDocResponseBody(TeaModel):
    def __init__(self, knowledge_id=None, request_id=None):
        self.knowledge_id = knowledge_id  # type: long
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDocResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaqRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None, end_date=None, knowledge_id=None, start_date=None,
                 title=None):
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long
        self.end_date = end_date  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.start_date = start_date  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaqRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateFaqResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaqResponseBody, self).to_map()
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


class UpdateFaqResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFaqResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFaqResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, introduction=None, name=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.introduction = introduction  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
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


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntentRequestIntentDefinitionSlotInfos(TeaModel):
    def __init__(self, array=None, encrypt=None, interactive=None, name=None, slot_id=None, value=None):
        self.array = array  # type: bool
        self.encrypt = encrypt  # type: bool
        self.interactive = interactive  # type: bool
        self.name = name  # type: str
        self.slot_id = slot_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntentRequestIntentDefinitionSlotInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateIntentRequestIntentDefinition(TeaModel):
    def __init__(self, alias_name=None, intent_name=None, slot_infos=None):
        self.alias_name = alias_name  # type: str
        self.intent_name = intent_name  # type: str
        self.slot_infos = slot_infos  # type: list[UpdateIntentRequestIntentDefinitionSlotInfos]

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateIntentRequestIntentDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = UpdateIntentRequestIntentDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class UpdateIntentRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_definition=None, intent_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_definition = intent_definition  # type: UpdateIntentRequestIntentDefinition
        self.intent_id = intent_id  # type: long

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super(UpdateIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            temp_model = UpdateIntentRequestIntentDefinition()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, intent_definition_shrink=None, intent_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.intent_definition_shrink = intent_definition_shrink  # type: str
        self.intent_id = intent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponseBody(TeaModel):
    def __init__(self, intent_id=None, request_id=None):
        self.intent_id = intent_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIntentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateIntentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIntentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLgfRequestLgfDefinition(TeaModel):
    def __init__(self, intent_id=None, rule_text=None):
        self.intent_id = intent_id  # type: long
        self.rule_text = rule_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLgfRequestLgfDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.rule_text is not None:
            result['RuleText'] = self.rule_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')
        return self


class UpdateLgfRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, lgf_definition=None, lgf_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.lgf_definition = lgf_definition  # type: UpdateLgfRequestLgfDefinition
        # LGF ID
        self.lgf_id = lgf_id  # type: long

    def validate(self):
        if self.lgf_definition:
            self.lgf_definition.validate()

    def to_map(self):
        _map = super(UpdateLgfRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition is not None:
            result['LgfDefinition'] = self.lgf_definition.to_map()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            temp_model = UpdateLgfRequestLgfDefinition()
            self.lgf_definition = temp_model.from_map(m['LgfDefinition'])
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        return self


class UpdateLgfShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, lgf_definition_shrink=None, lgf_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.lgf_definition_shrink = lgf_definition_shrink  # type: str
        # LGF ID
        self.lgf_id = lgf_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLgfShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition_shrink is not None:
            result['LgfDefinition'] = self.lgf_definition_shrink
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            self.lgf_definition_shrink = m.get('LgfDefinition')
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        return self


class UpdateLgfResponseBody(TeaModel):
    def __init__(self, lgf_id=None, request_id=None):
        self.lgf_id = lgf_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLgfResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLgfResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLgfResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLgfResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, name=None, perspective_id=None):
        self.agent_key = agent_key  # type: str
        self.name = name  # type: str
        self.perspective_id = perspective_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class UpdatePerspectiveResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePerspectiveResponseBody, self).to_map()
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


class UpdatePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePerspectiveResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePerspectiveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSimQuestionRequest(TeaModel):
    def __init__(self, agent_key=None, sim_question_id=None, title=None):
        self.agent_key = agent_key  # type: str
        self.sim_question_id = sim_question_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSimQuestionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateSimQuestionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSimQuestionResponseBody, self).to_map()
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


class UpdateSimQuestionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSimQuestionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSimQuestionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSolutionRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, content_type=None, perspective_codes=None, solution_id=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.content_type = content_type  # type: int
        self.perspective_codes = perspective_codes  # type: list[str]
        self.solution_id = solution_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class UpdateSolutionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSolutionResponseBody, self).to_map()
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


class UpdateSolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSolutionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSolutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserSayRequestUserSayDefinitionSlotInfos(TeaModel):
    def __init__(self, end_index=None, slot_id=None, start_index=None):
        self.end_index = end_index  # type: int
        self.slot_id = slot_id  # type: str
        self.start_index = start_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserSayRequestUserSayDefinitionSlotInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        return self


class UpdateUserSayRequestUserSayDefinition(TeaModel):
    def __init__(self, content=None, intent_id=None, slot_infos=None):
        self.content = content  # type: str
        self.intent_id = intent_id  # type: long
        self.slot_infos = slot_infos  # type: list[UpdateUserSayRequestUserSayDefinitionSlotInfos]

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserSayRequestUserSayDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = UpdateUserSayRequestUserSayDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class UpdateUserSayRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, user_say_definition=None, user_say_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.user_say_definition = user_say_definition  # type: UpdateUserSayRequestUserSayDefinition
        self.user_say_id = user_say_id  # type: long

    def validate(self):
        if self.user_say_definition:
            self.user_say_definition.validate()

    def to_map(self):
        _map = super(UpdateUserSayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition is not None:
            result['UserSayDefinition'] = self.user_say_definition.to_map()
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            temp_model = UpdateUserSayRequestUserSayDefinition()
            self.user_say_definition = temp_model.from_map(m['UserSayDefinition'])
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class UpdateUserSayShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None, user_say_definition_shrink=None, user_say_id=None):
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str
        self.user_say_definition_shrink = user_say_definition_shrink  # type: str
        self.user_say_id = user_say_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserSayShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition_shrink is not None:
            result['UserSayDefinition'] = self.user_say_definition_shrink
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            self.user_say_definition_shrink = m.get('UserSayDefinition')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class UpdateUserSayResponseBody(TeaModel):
    def __init__(self, request_id=None, user_say_id=None):
        self.request_id = request_id  # type: str
        self.user_say_id = user_say_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserSayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class UpdateUserSayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserSayResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserSayResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


