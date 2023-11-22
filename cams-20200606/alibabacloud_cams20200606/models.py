# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddChatappPhoneNumberRequest(TeaModel):
    def __init__(self, cc=None, cust_space_id=None, phone_number=None, pre_validate_id=None, verified_name=None):
        self.cc = cc  # type: str
        self.cust_space_id = cust_space_id  # type: str
        self.phone_number = phone_number  # type: str
        self.pre_validate_id = pre_validate_id  # type: str
        self.verified_name = verified_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddChatappPhoneNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.pre_validate_id is not None:
            result['PreValidateId'] = self.pre_validate_id
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PreValidateId') is not None:
            self.pre_validate_id = m.get('PreValidateId')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class AddChatappPhoneNumberResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddChatappPhoneNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddChatappPhoneNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddChatappPhoneNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddChatappPhoneNumberResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddChatappPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeeBotAssociateRequest(TeaModel):
    def __init__(self, chat_bot_instance_id=None, cust_space_id=None, isv_code=None, perspective=None,
                 recommend_num=None, session_id=None, utterance=None):
        # The ID of a bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective = perspective  # type: list[str]
        # The number of recommended questions. The value ranges from 1 to 10.
        self.recommend_num = recommend_num  # type: int
        # The ID of the session, which is used to identify the session and store context information in the session.
        self.session_id = session_id  # type: str
        # The input of the visitor.
        self.utterance = utterance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotAssociateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
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
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class BeeBotAssociateShrinkRequest(TeaModel):
    def __init__(self, chat_bot_instance_id=None, cust_space_id=None, isv_code=None, perspective_shrink=None,
                 recommend_num=None, session_id=None, utterance=None):
        # The ID of a bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective_shrink = perspective_shrink  # type: str
        # The number of recommended questions. The value ranges from 1 to 10.
        self.recommend_num = recommend_num  # type: int
        # The ID of the session, which is used to identify the session and store context information in the session.
        self.session_id = session_id  # type: str
        # The input of the visitor.
        self.utterance = utterance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotAssociateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
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
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class BeeBotAssociateResponseBodyDataAssociate(TeaModel):
    def __init__(self, meta=None, title=None):
        # The additional information.
        self.meta = meta  # type: str
        # The title of the associated question.
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotAssociateResponseBodyDataAssociate, self).to_map()
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


class BeeBotAssociateResponseBodyData(TeaModel):
    def __init__(self, associate=None, message_id=None, session_id=None):
        # The list of associated recommendations.
        self.associate = associate  # type: list[BeeBotAssociateResponseBodyDataAssociate]
        # The ID of the response message.
        self.message_id = message_id  # type: str
        # The ID of the session.
        self.session_id = session_id  # type: str

    def validate(self):
        if self.associate:
            for k in self.associate:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BeeBotAssociateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Associate'] = []
        if self.associate is not None:
            for k in self.associate:
                result['Associate'].append(k.to_map() if k else None)
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = BeeBotAssociateResponseBodyDataAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class BeeBotAssociateResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # If OK is returned, the request is successful.
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: BeeBotAssociateResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BeeBotAssociateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BeeBotAssociateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BeeBotAssociateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BeeBotAssociateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BeeBotAssociateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BeeBotAssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeeBotChatRequest(TeaModel):
    def __init__(self, chat_bot_instance_id=None, cust_space_id=None, intent_name=None, isv_code=None,
                 knowledge_id=None, perspective=None, sender_id=None, sender_nick=None, session_id=None, utterance=None,
                 vendor_param=None):
        # The ID of the bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The name of the intent in the dialog flow. When this parameter is specified, the bot conducts a Q\&A based on the intent.
        self.intent_name = intent_name  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The ID of the knowledge title in the knowledge base.
        self.knowledge_id = knowledge_id  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective = perspective  # type: list[str]
        # The ID of the visitor, which is used to identify users in the current session.
        self.sender_id = sender_id  # type: str
        # The nickname of the visitor in the current session.
        self.sender_nick = sender_nick  # type: str
        # The ID of the session, which is used to identify the session and store context information of the session.
        self.session_id = session_id  # type: str
        # The input of the visitor.
        self.utterance = utterance  # type: str
        # The user-defined parameter set in JSON format. You can specify user-defined parameters for conversation engines.
        self.vendor_param = vendor_param  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotChatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
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
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
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


class BeeBotChatShrinkRequest(TeaModel):
    def __init__(self, chat_bot_instance_id=None, cust_space_id=None, intent_name=None, isv_code=None,
                 knowledge_id=None, perspective_shrink=None, sender_id=None, sender_nick=None, session_id=None, utterance=None,
                 vendor_param_shrink=None):
        # The ID of the bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The name of the intent in the dialog flow. When this parameter is specified, the bot conducts a Q\&A based on the intent.
        self.intent_name = intent_name  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The ID of the knowledge title in the knowledge base.
        self.knowledge_id = knowledge_id  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective_shrink = perspective_shrink  # type: str
        # The ID of the visitor, which is used to identify users in the current session.
        self.sender_id = sender_id  # type: str
        # The nickname of the visitor in the current session.
        self.sender_nick = sender_nick  # type: str
        # The ID of the session, which is used to identify the session and store context information of the session.
        self.session_id = session_id  # type: str
        # The input of the visitor.
        self.utterance = utterance  # type: str
        # The user-defined parameter set in JSON format. You can specify user-defined parameters for conversation engines.
        self.vendor_param_shrink = vendor_param_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotChatShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective_shrink is not None:
            result['Perspective'] = self.perspective_shrink
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.vendor_param_shrink is not None:
            result['VendorParam'] = self.vendor_param_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('VendorParam') is not None:
            self.vendor_param_shrink = m.get('VendorParam')
        return self


class BeeBotChatResponseBodyDataMessagesKnowledgeRelatedKnowledges(TeaModel):
    def __init__(self, knowledge_id=None, title=None):
        # The ID of the related knowledge.
        self.knowledge_id = knowledge_id  # type: str
        # The title of the related knowledge.
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotChatResponseBodyDataMessagesKnowledgeRelatedKnowledges, self).to_map()
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


class BeeBotChatResponseBodyDataMessagesKnowledge(TeaModel):
    def __init__(self, answer_source=None, category=None, content=None, content_type=None, hit_statement=None,
                 id=None, related_knowledges=None, summary=None, title=None):
        # The source of the answer.
        self.answer_source = answer_source  # type: str
        # The category of the knowledge.
        self.category = category  # type: str
        # The content of the hit question.
        self.content = content  # type: str
        # Indicates whether the answer is in plain text or rich text.
        self.content_type = content_type  # type: str
        # The hit text.
        self.hit_statement = hit_statement  # type: str
        # The ID of the hit question in the knowledge base.
        self.id = id  # type: str
        # The list of the related knowledge.
        self.related_knowledges = related_knowledges  # type: list[BeeBotChatResponseBodyDataMessagesKnowledgeRelatedKnowledges]
        # The summary to the hit question.
        self.summary = summary  # type: str
        # The title of the hit question.
        self.title = title  # type: str

    def validate(self):
        if self.related_knowledges:
            for k in self.related_knowledges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BeeBotChatResponseBodyDataMessagesKnowledge, self).to_map()
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
                temp_model = BeeBotChatResponseBodyDataMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class BeeBotChatResponseBodyDataMessagesRecommends(TeaModel):
    def __init__(self, answer_source=None, knowledge_id=None, title=None):
        # The source of the recommended answer.
        self.answer_source = answer_source  # type: str
        # The ID of the recommended knowledge.
        self.knowledge_id = knowledge_id  # type: str
        # The title of the recommended knowledge. Valid values: the entity in graph-based question answering, the knowledge title in knowledge-based question answering, or the column value in table-based question answering.
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotChatResponseBodyDataMessagesRecommends, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class BeeBotChatResponseBodyDataMessagesTextSlots(TeaModel):
    def __init__(self, hit=None, name=None, origin=None, value=None):
        # Indicates whether the slot is hit.
        self.hit = hit  # type: bool
        # The name.
        self.name = name  # type: str
        # The original value.
        self.origin = origin  # type: str
        # The specific value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeeBotChatResponseBodyDataMessagesTextSlots, self).to_map()
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


class BeeBotChatResponseBodyDataMessagesText(TeaModel):
    def __init__(self, answer_source=None, content=None, content_type=None, dialog_name=None, ext=None,
                 external_flags=None, hit_statement=None, intent_name=None, meta_data=None, node_id=None, node_name=None,
                 slots=None, user_defined_chat_title=None):
        # The source of the answer.
        self.answer_source = answer_source  # type: str
        # The content of the text message.
        self.content = content  # type: str
        # Indicates whether the answer is in plain text or rich text.
        self.content_type = content_type  # type: str
        # The name of the dialog. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.dialog_name = dialog_name  # type: str
        # The passthrough parameters are returned.
        self.ext = ext  # type: dict[str, any]
        # When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.external_flags = external_flags  # type: dict[str, any]
        # The hit text.
        self.hit_statement = hit_statement  # type: str
        # The name of the intent. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.intent_name = intent_name  # type: str
        # The metadata.
        self.meta_data = meta_data  # type: str
        # The ID of the node. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.node_id = node_id  # type: str
        # The name of the node. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.node_name = node_name  # type: str
        # The list of slots.
        self.slots = slots  # type: list[BeeBotChatResponseBodyDataMessagesTextSlots]
        # The title of the chitchat.
        self.user_defined_chat_title = user_defined_chat_title  # type: str

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BeeBotChatResponseBodyDataMessagesText, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
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
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = BeeBotChatResponseBodyDataMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        return self


class BeeBotChatResponseBodyDataMessages(TeaModel):
    def __init__(self, answer_source=None, answer_type=None, knowledge=None, recommends=None, text=None):
        # When the AnswerType parameter is set to Recommend, this parameter indicates the source of the recommended answer.
        self.answer_source = answer_source  # type: str
        # The type of the answer.
        self.answer_type = answer_type  # type: str
        # When the AnswerType parameter is set to Knowledge, this parameter contains the Knowledge object returned by the bot.
        self.knowledge = knowledge  # type: BeeBotChatResponseBodyDataMessagesKnowledge
        # The list of recommended knowledge. When the AnswerType parameter is set to Recommend, this parameter is returned.
        self.recommends = recommends  # type: list[BeeBotChatResponseBodyDataMessagesRecommends]
        # When the AnswerType parameter is set to Text, this parameter contains the Text object returned by the bot.
        self.text = text  # type: BeeBotChatResponseBodyDataMessagesText

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
        _map = super(BeeBotChatResponseBodyDataMessages, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Knowledge') is not None:
            temp_model = BeeBotChatResponseBodyDataMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = BeeBotChatResponseBodyDataMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            temp_model = BeeBotChatResponseBodyDataMessagesText()
            self.text = temp_model.from_map(m['Text'])
        return self


class BeeBotChatResponseBodyData(TeaModel):
    def __init__(self, message_id=None, messages=None, session_id=None):
        # The ID of the response message.
        self.message_id = message_id  # type: str
        # The list of messages.
        self.messages = messages  # type: list[BeeBotChatResponseBodyDataMessages]
        # The ID of the session.
        self.session_id = session_id  # type: str

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BeeBotChatResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
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
                temp_model = BeeBotChatResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class BeeBotChatResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # If OK is returned, the request is successful.
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: BeeBotChatResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BeeBotChatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BeeBotChatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BeeBotChatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BeeBotChatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BeeBotChatResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BeeBotChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappBindWabaRequest(TeaModel):
    def __init__(self, waba_id=None):
        # The ID of the WhatsApp Business account.
        self.waba_id = waba_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappBindWabaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ChatappBindWabaResponseBodyData(TeaModel):
    def __init__(self, cust_space_id=None, waba_id=None):
        # The space ID of the user.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp Business account.
        self.waba_id = waba_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappBindWabaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ChatappBindWabaResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: ChatappBindWabaResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChatappBindWabaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappBindWabaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappBindWabaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappBindWabaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappBindWabaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappEmbedSignUpRequest(TeaModel):
    def __init__(self, input_token=None):
        # The InputToken returned after the embedded signup flow is complete.
        self.input_token = input_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappEmbedSignUpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_token is not None:
            result['InputToken'] = self.input_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputToken') is not None:
            self.input_token = m.get('InputToken')
        return self


class ChatappEmbedSignUpResponseBodyWabas(TeaModel):
    def __init__(self, account_review_status=None, currency=None, id=None, message_template_namespace=None,
                 name=None):
        # The review status of the WhatsApp Business account.
        self.account_review_status = account_review_status  # type: str
        # The currency.
        self.currency = currency  # type: str
        # The ID of the WhatsApp Business account.
        self.id = id  # type: str
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace  # type: str
        # The name of the WhatsApp Business account.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappEmbedSignUpResponseBodyWabas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.id is not None:
            result['Id'] = self.id
        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ChatappEmbedSignUpResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None, wabas=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of the WhatsApp Business accounts.
        self.wabas = wabas  # type: list[ChatappEmbedSignUpResponseBodyWabas]

    def validate(self):
        if self.wabas:
            for k in self.wabas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatappEmbedSignUpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Wabas'] = []
        if self.wabas is not None:
            for k in self.wabas:
                result['Wabas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.wabas = []
        if m.get('Wabas') is not None:
            for k in m.get('Wabas'):
                temp_model = ChatappEmbedSignUpResponseBodyWabas()
                self.wabas.append(temp_model.from_map(k))
        return self


class ChatappEmbedSignUpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappEmbedSignUpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappEmbedSignUpResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappEmbedSignUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappMigrationRegisterRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappMigrationRegisterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappMigrationRegisterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappMigrationRegisterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappMigrationRegisterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappMigrationRegisterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappMigrationRegisterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappMigrationRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappMigrationVerifiedRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None, verify_code=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str
        # The verification code.
        self.verify_code = verify_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappMigrationVerifiedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ChatappMigrationVerifiedResponseBodyData(TeaModel):
    def __init__(self, id=None, phone_number=None):
        # The ID of the phone number.
        self.id = id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappMigrationVerifiedResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappMigrationVerifiedResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: ChatappMigrationVerifiedResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChatappMigrationVerifiedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChatappMigrationVerifiedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappMigrationVerifiedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappMigrationVerifiedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappMigrationVerifiedResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappMigrationVerifiedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappPhoneNumberDeregisterRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        self.cust_space_id = cust_space_id  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappPhoneNumberDeregisterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappPhoneNumberDeregisterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappPhoneNumberDeregisterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappPhoneNumberDeregisterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappPhoneNumberDeregisterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappPhoneNumberDeregisterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappPhoneNumberDeregisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappPhoneNumberRegisterRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappPhoneNumberRegisterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappPhoneNumberRegisterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappPhoneNumberRegisterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappPhoneNumberRegisterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappPhoneNumberRegisterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappPhoneNumberRegisterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappPhoneNumberRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappSyncPhoneNumberRequest(TeaModel):
    def __init__(self, cust_space_id=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappSyncPhoneNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        return self


class ChatappSyncPhoneNumberResponseBodyPhoneNumbers(TeaModel):
    def __init__(self, code_verification_status=None, messaging_limit_tier=None, name_status=None,
                 new_name_status=None, phone_number=None, quality_rating=None, status=None, status_callback_url=None,
                 status_queue=None, up_callback_url=None, up_queue=None, verified_name=None):
        # The verification status.
        self.code_verification_status = code_verification_status  # type: str
        # The number of phone numbers to which messages can be sent in a day.
        self.messaging_limit_tier = messaging_limit_tier  # type: str
        # The review status of the business display name.
        self.name_status = name_status  # type: str
        # The review status of the new business display name.
        self.new_name_status = new_name_status  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str
        # The quality rating of the phone number. Valid values: GREEN, YELLOW, and RED.
        self.quality_rating = quality_rating  # type: str
        # The status of the phone number.
        self.status = status  # type: str
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url  # type: str
        # The status report queue.
        self.status_queue = status_queue  # type: str
        # The callback URL to which MO messages are sent by using HTTP callbacks.
        self.up_callback_url = up_callback_url  # type: str
        # The mobile originated (MO) message queue.
        self.up_queue = up_queue  # type: str
        # The display name of the business to which the phone number belongs.
        self.verified_name = verified_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappSyncPhoneNumberResponseBodyPhoneNumbers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.messaging_limit_tier is not None:
            result['MessagingLimitTier'] = self.messaging_limit_tier
        if self.name_status is not None:
            result['NameStatus'] = self.name_status
        if self.new_name_status is not None:
            result['NewNameStatus'] = self.new_name_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.quality_rating is not None:
            result['QualityRating'] = self.quality_rating
        if self.status is not None:
            result['Status'] = self.status
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('MessagingLimitTier') is not None:
            self.messaging_limit_tier = m.get('MessagingLimitTier')
        if m.get('NameStatus') is not None:
            self.name_status = m.get('NameStatus')
        if m.get('NewNameStatus') is not None:
            self.new_name_status = m.get('NewNameStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualityRating') is not None:
            self.quality_rating = m.get('QualityRating')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class ChatappSyncPhoneNumberResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, phone_numbers=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # Details of the phone numbers.
        self.phone_numbers = phone_numbers  # type: list[ChatappSyncPhoneNumberResponseBodyPhoneNumbers]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.phone_numbers:
            for k in self.phone_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatappSyncPhoneNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PhoneNumbers'] = []
        if self.phone_numbers is not None:
            for k in self.phone_numbers:
                result['PhoneNumbers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.phone_numbers = []
        if m.get('PhoneNumbers') is not None:
            for k in m.get('PhoneNumbers'):
                temp_model = ChatappSyncPhoneNumberResponseBodyPhoneNumbers()
                self.phone_numbers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappSyncPhoneNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappSyncPhoneNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappSyncPhoneNumberResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappSyncPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappVerifyAndRegisterRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None, verify_code=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str
        # The verification code.
        self.verify_code = verify_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappVerifyAndRegisterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ChatappVerifyAndRegisterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatappVerifyAndRegisterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappVerifyAndRegisterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChatappVerifyAndRegisterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatappVerifyAndRegisterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappVerifyAndRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatappMigrationInitiateRequest(TeaModel):
    def __init__(self, country_code=None, cust_space_id=None, mobile_number=None):
        self.country_code = country_code  # type: str
        self.cust_space_id = cust_space_id  # type: str
        self.mobile_number = mobile_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappMigrationInitiateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        return self


class CreateChatappMigrationInitiateResponseBodyData(TeaModel):
    def __init__(self, id=None, phone_number=None, status=None):
        self.id = id  # type: str
        self.phone_number = phone_number  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappMigrationInitiateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateChatappMigrationInitiateResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.data = data  # type: CreateChatappMigrationInitiateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateChatappMigrationInitiateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateChatappMigrationInitiateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChatappMigrationInitiateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateChatappMigrationInitiateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateChatappMigrationInitiateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatappMigrationInitiateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(self, autofill_text=None, coupon_code=None, flow_action=None, flow_id=None, is_opt_out=None,
                 navigate_screen=None, package_name=None, phone_number=None, signature_hash=None, text=None, type=None, url=None,
                 url_type=None):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.autofill_text = autofill_text  # type: str
        self.coupon_code = coupon_code  # type: str
        self.flow_action = flow_action  # type: str
        self.flow_id = flow_id  # type: str
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY in a WhatsApp message template. After you configure message sending in the ChatApp Message Service console, marketing messages will not be sent to customers if they click this button.
        self.is_opt_out = is_opt_out  # type: bool
        self.navigate_screen = navigate_screen  # type: str
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.package_name = package_name  # type: str
        # The phone number. This parameter is valid only when the Type sub-parameter of the Buttons parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number  # type: str
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.signature_hash = signature_hash  # type: str
        # The display name of the button.
        self.text = text  # type: str
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: the phone call button
        # *   **URL**: the URL button
        # *   **QUICK_REPLY**: the quick reply button
        # *   **COPY_CODE**: the copy code button if Category is set to AUTHENTICATION
        # *   **ONE_TAP**: the one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   In a WhatsApp message template, the quick reply button cannot be used together with the phone call button or the URL button.
        # 
        # *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a WhatsApp message template.
        # 
        # *   If Category is set to AUTHENTICATION in a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If the Type sub-parameter of the Buttons parameter is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If the Type sub-parameter of the Buttons parameter is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        self.type = type  # type: str
        # The URL to which you are redirected when you click the URL button.
        self.url = url  # type: str
        # The type of the URL. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappTemplateRequestComponentsButtons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class CreateChatappTemplateRequestComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        self.phone_number = phone_number  # type: str
        self.text = text  # type: str
        self.type = type  # type: str
        self.url = url  # type: str
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappTemplateRequestComponentsCardsCardComponentsButtons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class CreateChatappTemplateRequestComponentsCardsCardComponents(TeaModel):
    def __init__(self, buttons=None, format=None, text=None, type=None, url=None):
        self.buttons = buttons  # type: list[CreateChatappTemplateRequestComponentsCardsCardComponentsButtons]
        self.format = format  # type: str
        self.text = text  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateChatappTemplateRequestComponentsCardsCardComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = CreateChatappTemplateRequestComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateChatappTemplateRequestComponentsCards(TeaModel):
    def __init__(self, card_components=None):
        self.card_components = card_components  # type: list[CreateChatappTemplateRequestComponentsCardsCardComponents]

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateChatappTemplateRequestComponentsCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = CreateChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class CreateChatappTemplateRequestComponents(TeaModel):
    def __init__(self, add_secret_recommendation=None, buttons=None, caption=None, cards=None,
                 code_expiration_minutes=None, duration=None, file_name=None, file_type=None, format=None, has_expiration=None, text=None,
                 thumb_url=None, type=None, url=None):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY in a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation  # type: bool
        # The buttons. This parameter applies only to **BUTTONS** components.
        self.buttons = buttons  # type: list[CreateChatappTemplateRequestComponentsButtons]
        # The description of the document.
        self.caption = caption  # type: str
        self.cards = cards  # type: list[CreateChatappTemplateRequestComponentsCards]
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER in a WhatsApp message template. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes  # type: int
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration  # type: int
        # The name of the document.
        self.file_name = file_name  # type: str
        # The type of the document attached in the Viber message template.
        self.file_type = file_type  # type: str
        # The type of the media resources that are included in the message. Valid values:
        # 
        # *   **TEXT**\
        # *   **IMAGE**\
        # *   **DOCUMENT**\
        # *   **VIDEO**\
        self.format = format  # type: str
        self.has_expiration = has_expiration  # type: bool
        # The text of the message that you want to send.
        # 
        # > If Category is set to AUTHENTICATION, the Text sub-parameter of the Components parameter is empty.
        self.text = text  # type: str
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url  # type: str
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # > 
        # 
        # *   In WhatsApp message templates, a **BODY** component cannot exceed 1,024 characters in length, and a **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER** components are not supported in Viber message templates.
        # 
        # *   In a Viber message template, media resources, such as images, videos, or documents, are placed in the **HEADER** component. If a Viber message contains text and an image, the image is placed under the text in the message received on a device.
        self.type = type  # type: str
        # The URL of the media resource.
        # 
        # > We recommend that the resolution of the image is 800 × 800 in a Viber message template.
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateChatappTemplateRequestComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.has_expiration is not None:
            result['HasExpiration'] = self.has_expiration
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = CreateChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = CreateChatappTemplateRequestComponentsCards()
                self.cards.append(temp_model.from_map(k))
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('HasExpiration') is not None:
            self.has_expiration = m.get('HasExpiration')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateChatappTemplateRequest(TeaModel):
    def __init__(self, allow_category_change=None, category=None, components=None, cust_space_id=None,
                 cust_waba_id=None, example=None, isv_code=None, language=None, message_send_ttl_seconds=None, name=None,
                 template_type=None):
        # Specifies whether to allow Facebook to automatically change the directory of the template. If you set this parameter to true, the review success rate of the template is improved. This parameter is valid only when TemplateType is set to WHATSAPP.
        self.allow_category_change = allow_category_change  # type: bool
        # The category of the template if TemplateType is set to WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: the transaction template
        # *   **MARKETING**: the marketing template
        # *   **AUTHENTICATION**: the authentication template
        # 
        # The category of the template if TemplateType is set to VIBER. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        self.category = category  # type: str
        # The components of the message template.
        # 
        # > If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter is empty.
        self.components = components  # type: list[CreateChatappTemplateRequestComponents]
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example = example  # type: dict[str, str]
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # Validity period of authentication template message sending in WhatsApp
        # 
        # > This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds  # type: int
        # The name of the message template.
        self.name = name  # type: str
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type  # type: str

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateChatappTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_category_change is not None:
            result['AllowCategoryChange'] = self.allow_category_change
        if self.category is not None:
            result['Category'] = self.category
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example is not None:
            result['Example'] = self.example
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.name is not None:
            result['Name'] = self.name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowCategoryChange') is not None:
            self.allow_category_change = m.get('AllowCategoryChange')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = CreateChatappTemplateRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, allow_category_change=None, category=None, components_shrink=None, cust_space_id=None,
                 cust_waba_id=None, example_shrink=None, isv_code=None, language=None, message_send_ttl_seconds=None, name=None,
                 template_type=None):
        # Specifies whether to allow Facebook to automatically change the directory of the template. If you set this parameter to true, the review success rate of the template is improved. This parameter is valid only when TemplateType is set to WHATSAPP.
        self.allow_category_change = allow_category_change  # type: bool
        # The category of the template if TemplateType is set to WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: the transaction template
        # *   **MARKETING**: the marketing template
        # *   **AUTHENTICATION**: the authentication template
        # 
        # The category of the template if TemplateType is set to VIBER. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        self.category = category  # type: str
        # The components of the message template.
        # 
        # > If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter is empty.
        self.components_shrink = components_shrink  # type: str
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink  # type: str
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # Validity period of authentication template message sending in WhatsApp
        # 
        # > This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds  # type: int
        # The name of the message template.
        self.name = name  # type: str
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_category_change is not None:
            result['AllowCategoryChange'] = self.allow_category_change
        if self.category is not None:
            result['Category'] = self.category
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example_shrink is not None:
            result['Example'] = self.example_shrink
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.name is not None:
            result['Name'] = self.name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowCategoryChange') is not None:
            self.allow_category_change = m.get('AllowCategoryChange')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateResponseBodyData(TeaModel):
    def __init__(self, template_code=None, template_name=None):
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The name of the message template.
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateChatappTemplateResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        # 访问被拒绝详细信息。
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: CreateChatappTemplateResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateChatappTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateChatappTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChatappTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateChatappTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateChatappTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(self, categories=None, cust_space_id=None, flow_name=None):
        self.categories = categories  # type: list[str]
        self.cust_space_id = cust_space_id  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateFlowShrinkRequest(TeaModel):
    def __init__(self, categories_shrink=None, cust_space_id=None, flow_name=None):
        self.categories_shrink = categories_shrink  # type: str
        self.cust_space_id = cust_space_id  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateFlowResponseBodyData(TeaModel):
    def __init__(self, categories=None, flow_id=None, flow_name=None):
        self.categories = categories  # type: list[str]
        # flow ID。
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateFlowResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhoneMessageQrdlRequest(TeaModel):
    def __init__(self, cust_space_id=None, generate_qr_image=None, phone_number=None, prefilled_message=None):
        self.cust_space_id = cust_space_id  # type: str
        self.generate_qr_image = generate_qr_image  # type: str
        self.phone_number = phone_number  # type: str
        self.prefilled_message = prefilled_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePhoneMessageQrdlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        return self


class CreatePhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(self, deep_link_url=None, generate_qr_image=None, phone_number=None, prefilled_message=None,
                 qr_image_url=None, qrdl_code=None):
        self.deep_link_url = deep_link_url  # type: str
        self.generate_qr_image = generate_qr_image  # type: str
        self.phone_number = phone_number  # type: str
        self.prefilled_message = prefilled_message  # type: str
        self.qr_image_url = qr_image_url  # type: str
        self.qrdl_code = qrdl_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePhoneMessageQrdlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class CreatePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreatePhoneMessageQrdlResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreatePhoneMessageQrdlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreatePhoneMessageQrdlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePhoneMessageQrdlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePhoneMessageQrdlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePhoneMessageQrdlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatappTemplateRequest(TeaModel):
    def __init__(self, cust_space_id=None, cust_waba_id=None, isv_code=None, template_code=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChatappTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DeleteChatappTemplateResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChatappTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChatappTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteChatappTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteChatappTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_id=None):
        self.cust_space_id = cust_space_id  # type: str
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhoneMessageQrdlRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None, qrdl_code=None):
        self.cust_space_id = cust_space_id  # type: str
        self.phone_number = phone_number  # type: str
        self.qrdl_code = qrdl_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePhoneMessageQrdlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class DeletePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePhoneMessageQrdlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePhoneMessageQrdlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePhoneMessageQrdlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePhoneMessageQrdlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeprecateFlowRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_id=None):
        self.cust_space_id = cust_space_id  # type: str
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeprecateFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DeprecateFlowResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeprecateFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeprecateFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeprecateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeprecateFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeprecateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWhatsappROIMetricRequest(TeaModel):
    def __init__(self, cust_space_id=None, isv_code=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWhatsappROIMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        return self


class EnableWhatsappROIMetricResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWhatsappROIMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableWhatsappROIMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableWhatsappROIMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableWhatsappROIMetricResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableWhatsappROIMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappPhoneNumberMetricRequest(TeaModel):
    def __init__(self, cust_space_id=None, end=None, granularity=None, isv_code=None, phone_number=None, start=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time. The interval between the start time and the end time cannot exceed 24 hours.
        self.end = end  # type: long
        # Metric granularity. Valid values:
        # 
        # - DAILY
        # - HALF_HOUR
        self.granularity = granularity  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The business phone number.
        self.phone_number = phone_number  # type: str
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start = start  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappPhoneNumberMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetChatappPhoneNumberMetricResponseBodyData(TeaModel):
    def __init__(self, delivered_count=None, end=None, granularity=None, phone_number=None, sent_count=None,
                 start=None):
        # Delivered count
        self.delivered_count = delivered_count  # type: int
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end = end  # type: long
        # The granularity at which bills are queried.
        self.granularity = granularity  # type: str
        # The business phone number.
        self.phone_number = phone_number  # type: str
        # Sent count
        self.sent_count = sent_count  # type: int
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start = start  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappPhoneNumberMetricResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetChatappPhoneNumberMetricResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: list[GetChatappPhoneNumberMetricResponseBodyData]
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappPhoneNumberMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetChatappPhoneNumberMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappPhoneNumberMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChatappPhoneNumberMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChatappPhoneNumberMetricResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappPhoneNumberMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappTemplateDetailRequest(TeaModel):
    def __init__(self, cust_space_id=None, cust_waba_id=None, isv_code=None, language=None, template_code=None,
                 template_type=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp account that you registered.
        self.cust_waba_id = cust_waba_id  # type: str
        # The independent software vendor (ISV) verification code. This parameter is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE (developing)
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappTemplateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs(TeaModel):
    def __init__(self, action=None, intent_code=None, next_language_code=None, next_template_code=None,
                 next_template_name=None):
        # 事件类型
        self.action = action  # type: str
        # 意图编码
        self.intent_code = intent_code  # type: str
        # 下一个模板语言
        self.next_language_code = next_language_code  # type: str
        # 下一个模板编码
        self.next_template_code = next_template_code  # type: str
        # 下一个模板名称
        self.next_template_name = next_template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.intent_code is not None:
            result['IntentCode'] = self.intent_code
        if self.next_language_code is not None:
            result['NextLanguageCode'] = self.next_language_code
        if self.next_template_code is not None:
            result['NextTemplateCode'] = self.next_template_code
        if self.next_template_name is not None:
            result['NextTemplateName'] = self.next_template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('IntentCode') is not None:
            self.intent_code = m.get('IntentCode')
        if m.get('NextLanguageCode') is not None:
            self.next_language_code = m.get('NextLanguageCode')
        if m.get('NextTemplateCode') is not None:
            self.next_template_code = m.get('NextTemplateCode')
        if m.get('NextTemplateName') is not None:
            self.next_template_name = m.get('NextTemplateName')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtons(TeaModel):
    def __init__(self, autofill_text=None, coupon_code=None, extend_attrs=None, flow_action=None, flow_id=None,
                 is_opt_out=None, navigate_screen=None, package_name=None, phone_number=None, signature_hash=None, text=None,
                 type=None, url=None, url_type=None):
        # Whatsapp模板，Category为Authentication，并且Button Type为ONE_TAP时必填，Whatsap Autofill操作的按钮文本
        self.autofill_text = autofill_text  # type: str
        self.coupon_code = coupon_code  # type: str
        # 扩展字段
        self.extend_attrs = extend_attrs  # type: GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs
        self.flow_action = flow_action  # type: str
        self.flow_id = flow_id  # type: str
        # Whatsapp模板，在Category为Marketing,并且Button type为QUICK_REPLY时有效，表示按钮为营销退订按钮，客户如果点击了此按钮，并且在chatapp平台上配置了发送控制操作，则后续Marketing消息则不会发送到客户
        self.is_opt_out = is_opt_out  # type: bool
        self.navigate_screen = navigate_screen  # type: str
        # Whatsapp模板，Category为Authentication，并且Button Type为ONE_TAP时必填，表示Whatsapp调起应用的包名
        self.package_name = package_name  # type: str
        # The phone number. This parameter is valid only if the returned value of the Type parameter is **PHONE_NUMBER**.
        self.phone_number = phone_number  # type: str
        # Whatsapp模板，Category为Authentication，并且Button Type为ONE_TAP时必填，表示Whatsapp调起应用的签名Hash值
        self.signature_hash = signature_hash  # type: str
        # The display name of the button.
        self.text = text  # type: str
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: a phone call button
        # *   **URL**: a URL button
        # *   **QUICK_REPLY**: a quick reply button
        # 
        # > 
        # 
        # *   A quick reply button cannot coexist with a phone call button or a URL button in a message template.
        # 
        # *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a message template.
        # 
        # *   You can add only one button to a Viber message template, and the button must be a URL button.
        self.type = type  # type: str
        # The URL to be accessed when you click the URL button.
        self.url = url  # type: str
        # The type of the URL. Valid values:
        # 
        # *   **static**: a static URL
        # *   **dynamic**: a dynamic URL
        self.url_type = url_type  # type: str

    def validate(self):
        if self.extend_attrs:
            self.extend_attrs.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponentsButtons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.extend_attrs is not None:
            result['ExtendAttrs'] = self.extend_attrs.to_map()
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('ExtendAttrs') is not None:
            temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs()
            self.extend_attrs = temp_model.from_map(m['ExtendAttrs'])
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        self.phone_number = phone_number  # type: str
        self.text = text  # type: str
        self.type = type  # type: str
        self.url = url  # type: str
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents(TeaModel):
    def __init__(self, buttons=None, format=None, text=None, type=None, url=None):
        self.buttons = buttons  # type: list[GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons]
        self.format = format  # type: str
        self.text = text  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCards(TeaModel):
    def __init__(self, card_components=None):
        self.card_components = card_components  # type: list[GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents]

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponentsCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class GetChatappTemplateDetailResponseBodyDataComponents(TeaModel):
    def __init__(self, add_secret_recommendation=None, buttons=None, caption=None, cards=None,
                 code_expiration_minutes=None, duration=None, file_name=None, file_type=None, format=None, latitude=None,
                 location_address=None, location_name=None, longitude=None, offer_expiration_time_ms=None, text=None, thumb_url=None,
                 type=None, url=None, has_expiration=None):
        # Whatsapp类型模板，Category为Authentication，并且Component Type为Body时有效，表示在Body上面显示不要将验证码信息提供给其它人的提示信息
        self.add_secret_recommendation = add_secret_recommendation  # type: bool
        # This parameter applies only to components of the **BUTTONS** type. This parameter is passed in by converting its original JSON structure into a string.
        self.buttons = buttons  # type: list[GetChatappTemplateDetailResponseBodyDataComponentsButtons]
        # The description of the file.
        self.caption = caption  # type: str
        self.cards = cards  # type: list[GetChatappTemplateDetailResponseBodyDataComponentsCards]
        # Whatsapp Authentication模板验证码有效期（分钟），只在Whatsapp类型消息，Category为Authentication并且Component Type为Footer时有效（此信息显示在Footer位置）
        self.code_expiration_minutes = code_expiration_minutes  # type: int
        # The length of the video in the Viber message template. Valid values: 0 to 600. Unit: seconds.
        self.duration = duration  # type: int
        # The name of the file.
        self.file_name = file_name  # type: str
        # The type of the file attached in the Viber message template.
        self.file_type = file_type  # type: str
        # The type of the media resources that are included in the message.
        self.format = format  # type: str
        # 位置纬度属性
        self.latitude = latitude  # type: str
        # 位置地址
        self.location_address = location_address  # type: str
        # 位置名称
        self.location_name = location_name  # type: str
        # 位置经度属性
        self.longitude = longitude  # type: str
        self.offer_expiration_time_ms = offer_expiration_time_ms  # type: str
        # The text of the message that you want to send.
        self.text = text  # type: str
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url  # type: str
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # > 
        # 
        # *   The following limits apply to components in WhatsApp message templates: A component of the **BODY** type cannot exceed 1,024 characters. A component of the **HEADER** or **FOOTER** type cannot exceed 60 characters in length.
        # 
        # > 
        # 
        # *   **FOOTER** components are not supported in Viber message templates.
        # 
        # > 
        # 
        # *   In a Viber message template, a media resource, such as an image, a video, or a file, is placed in the **HEADER** component. If a Viber message contains text and an image, the image is placed under the text in the message received on a device.
        self.type = type  # type: str
        # The URL of the material.
        self.url = url  # type: str
        self.has_expiration = has_expiration  # type: bool

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location_address is not None:
            result['LocationAddress'] = self.location_address
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.offer_expiration_time_ms is not None:
            result['OfferExpirationTimeMs'] = self.offer_expiration_time_ms
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.has_expiration is not None:
            result['hasExpiration'] = self.has_expiration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCards()
                self.cards.append(temp_model.from_map(k))
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('LocationAddress') is not None:
            self.location_address = m.get('LocationAddress')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('OfferExpirationTimeMs') is not None:
            self.offer_expiration_time_ms = m.get('OfferExpirationTimeMs')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('hasExpiration') is not None:
            self.has_expiration = m.get('hasExpiration')
        return self


class GetChatappTemplateDetailResponseBodyData(TeaModel):
    def __init__(self, audit_status=None, category=None, components=None, example=None, language=None,
                 message_send_ttl_seconds=None, name=None, quality_score=None, reason=None, template_code=None, template_type=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        # The category of the template when the returned value of TemplateType is WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: a transactional template
        # *   **MARKETING**: a marketing template
        # *   **AUTHENTICATION**: an identity authentication template
        # 
        # The category of the template when the returned value of the TemplateType parameter is VIBER. Valid values:
        # 
        # *   **text**: a template that contains only text
        # *   **image**: a template that contains only images
        # *   **text_image_button**: a template that contains text, images, and buttons
        # *   **text_button**: a template that contains text and buttons
        # *   **document**: a template that contains only files
        # *   **video**: a template that contains only videos
        # *   **text_video**: a template that contains text and videos
        # *   **text_video_button**: a template that contains text, videos, and buttons
        # *   **text_image**: a template that contains text and images
        # 
        # > If Category is set to text_video_button, users cannot open a web page by clicking the button. Users can open only the video in the message. In this case, you do not need to specify the Url parameter for the URL button in the template.
        self.category = category  # type: str
        # The components of the message template.
        self.components = components  # type: list[GetChatappTemplateDetailResponseBodyDataComponents]
        # The examples of variables.
        self.example = example  # type: dict[str, str]
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # Whatsapp中Authentication类型模板发送消息时的消息有效期
        self.message_send_ttl_seconds = message_send_ttl_seconds  # type: int
        # The name of the message template.
        self.name = name  # type: str
        # 模板质量
        self.quality_score = quality_score  # type: str
        self.reason = reason  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE (developing)
        self.template_type = template_type  # type: str

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.example is not None:
            result['Example'] = self.example
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.name is not None:
            result['Name'] = self.name
        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateDetailResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code.
        # 
        # *   Example: OK. This value indicates that the request is successful.
        # *   Other codes indicate that the request fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetChatappTemplateDetailResponseBodyData
        # The error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetChatappTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappTemplateDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChatappTemplateDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappTemplateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappTemplateMetricRequest(TeaModel):
    def __init__(self, cust_space_id=None, end=None, granularity=None, isv_code=None, language=None, start=None,
                 template_code=None, template_type=None):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end = end  # type: long
        # Metric granularity. Valid values:
        # 
        # - DAILY
        self.granularity = granularity  # type: str
        # The independent software vendor (ISV) verification code. This parameter is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start = start  # type: long
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappTemplateMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.start is not None:
            result['Start'] = self.start
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateMetricResponseBodyDataCliented(TeaModel):
    def __init__(self, button_content=None, count=None, type=None):
        # Button name
        self.button_content = button_content  # type: str
        # Clicked count
        self.count = count  # type: int
        # The type of button.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappTemplateMetricResponseBodyDataCliented, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.button_content is not None:
            result['ButtonContent'] = self.button_content
        if self.count is not None:
            result['Count'] = self.count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ButtonContent') is not None:
            self.button_content = m.get('ButtonContent')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetChatappTemplateMetricResponseBodyData(TeaModel):
    def __init__(self, cliented=None, delivered_count=None, end=None, language=None, read_count=None,
                 sent_count=None, start=None, template_code=None):
        # Click Statistics
        self.cliented = cliented  # type: list[GetChatappTemplateMetricResponseBodyDataCliented]
        # Delivered count
        self.delivered_count = delivered_count  # type: int
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end = end  # type: long
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # Read count
        self.read_count = read_count  # type: int
        # Sent count
        self.sent_count = sent_count  # type: int
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start = start  # type: long
        # The code of the message template.
        self.template_code = template_code  # type: str

    def validate(self):
        if self.cliented:
            for k in self.cliented:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappTemplateMetricResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cliented'] = []
        if self.cliented is not None:
            for k in self.cliented:
                result['Cliented'].append(k.to_map() if k else None)
        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count
        if self.end is not None:
            result['End'] = self.end
        if self.language is not None:
            result['Language'] = self.language
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.start is not None:
            result['Start'] = self.start
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cliented = []
        if m.get('Cliented') is not None:
            for k in m.get('Cliented'):
                temp_model = GetChatappTemplateMetricResponseBodyDataCliented()
                self.cliented.append(temp_model.from_map(k))
        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class GetChatappTemplateMetricResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: list[GetChatappTemplateMetricResponseBodyData]
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappTemplateMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetChatappTemplateMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappTemplateMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChatappTemplateMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChatappTemplateMetricResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappTemplateMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappUploadAuthorizationRequest(TeaModel):
    def __init__(self, cust_space_id=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappUploadAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        return self


class GetChatappUploadAuthorizationResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, bucket_name=None, dir=None, end_point=None,
                 expire=None, security_token=None):
        # The AccessKey ID that is used to authorize a user to upload a file to Object Storage Service (OSS).
        self.access_key_id = access_key_id  # type: str
        # The AccessKey secret that is used to authorize a user to upload a file to OSS.
        self.access_key_secret = access_key_secret  # type: str
        # The name of the bucket to which a file is uploaded in OSS.
        self.bucket_name = bucket_name  # type: str
        # The directory to which a file is uploaded in OSS.
        self.dir = dir  # type: str
        # The address of the OSS server to which a file is uploaded.
        self.end_point = end_point  # type: str
        # The timeout period.
        self.expire = expire  # type: int
        # The security token.
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappUploadAuthorizationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetChatappUploadAuthorizationResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: GetChatappUploadAuthorizationResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetChatappUploadAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetChatappUploadAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappUploadAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChatappUploadAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChatappUploadAuthorizationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappUploadAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappVerifyCodeRequest(TeaModel):
    def __init__(self, cust_space_id=None, locale=None, method=None, phone_number=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The language.
        self.locale = locale  # type: str
        # The method to obtain the verification code. Valid values: SMS and VOICE.
        self.method = method  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappVerifyCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.method is not None:
            result['Method'] = self.method
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetChatappVerifyCodeResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappVerifyCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappVerifyCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetChatappVerifyCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChatappVerifyCodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommerceSettingRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        self.cust_space_id = cust_space_id  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCommerceSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetCommerceSettingResponseBodyData(TeaModel):
    def __init__(self, cart_enable=None, catalog_visible=None):
        self.cart_enable = cart_enable  # type: bool
        self.catalog_visible = catalog_visible  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCommerceSettingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable
        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')
        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')
        return self


class GetCommerceSettingResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetCommerceSettingResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCommerceSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCommerceSettingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCommerceSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCommerceSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCommerceSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCommerceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_id=None):
        self.cust_space_id = cust_space_id  # type: str
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowResponseBodyData(TeaModel):
    def __init__(self, categories=None, data_api_version=None, flow_id=None, flow_name=None, jsonversion=None,
                 preview_url=None, preview_url_expires=None, status=None):
        self.categories = categories  # type: list[str]
        self.data_api_version = data_api_version  # type: str
        # flow ID。
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str
        self.jsonversion = jsonversion  # type: str
        self.preview_url = preview_url  # type: str
        self.preview_url_expires = preview_url_expires  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.data_api_version is not None:
            result['DataApiVersion'] = self.data_api_version
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.jsonversion is not None:
            result['JSONVersion'] = self.jsonversion
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.preview_url_expires is not None:
            result['PreviewUrlExpires'] = self.preview_url_expires
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('DataApiVersion') is not None:
            self.data_api_version = m.get('DataApiVersion')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('JSONVersion') is not None:
            self.jsonversion = m.get('JSONVersion')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('PreviewUrlExpires') is not None:
            self.preview_url_expires = m.get('PreviewUrlExpires')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFlowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetFlowResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowJSONAssestRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_id=None):
        self.cust_space_id = cust_space_id  # type: str
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowJSONAssestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowJSONAssestResponseBodyData(TeaModel):
    def __init__(self, file_path=None, flow_id=None):
        self.file_path = file_path  # type: str
        # flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowJSONAssestResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowJSONAssestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetFlowJSONAssestResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFlowJSONAssestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFlowJSONAssestResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowJSONAssestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFlowJSONAssestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFlowJSONAssestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFlowJSONAssestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowPreviewUrlRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_id=None):
        self.cust_space_id = cust_space_id  # type: str
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowPreviewUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowPreviewUrlResponseBodyData(TeaModel):
    def __init__(self, flow_id=None, preview_url=None, preview_url_expires=None):
        # flow ID。
        self.flow_id = flow_id  # type: str
        self.preview_url = preview_url  # type: str
        self.preview_url_expires = preview_url_expires  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowPreviewUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.preview_url_expires is not None:
            result['PreviewUrlExpires'] = self.preview_url_expires
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('PreviewUrlExpires') is not None:
            self.preview_url_expires = m.get('PreviewUrlExpires')
        return self


class GetFlowPreviewUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetFlowPreviewUrlResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFlowPreviewUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFlowPreviewUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowPreviewUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFlowPreviewUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFlowPreviewUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFlowPreviewUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMigrationVerifyCodeRequest(TeaModel):
    def __init__(self, cust_space_id=None, locale=None, method=None, phone_number=None):
        self.cust_space_id = cust_space_id  # type: str
        self.locale = locale  # type: str
        self.method = method  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMigrationVerifyCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.method is not None:
            result['Method'] = self.method
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetMigrationVerifyCodeResponseBodyData(TeaModel):
    def __init__(self, id=None, phone_number=None):
        self.id = id  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMigrationVerifyCodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetMigrationVerifyCodeResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.data = data  # type: GetMigrationVerifyCodeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMigrationVerifyCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetMigrationVerifyCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMigrationVerifyCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMigrationVerifyCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMigrationVerifyCodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMigrationVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermissionByCodeRequest(TeaModel):
    def __init__(self, code=None, cust_space_id=None, permissions=None):
        self.code = code  # type: str
        self.cust_space_id = cust_space_id  # type: str
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPermissionByCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        return self


class GetPermissionByCodeShrinkRequest(TeaModel):
    def __init__(self, code=None, cust_space_id=None, permissions_shrink=None):
        self.code = code  # type: str
        self.cust_space_id = cust_space_id  # type: str
        self.permissions_shrink = permissions_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPermissionByCodeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.permissions_shrink is not None:
            result['Permissions'] = self.permissions_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Permissions') is not None:
            self.permissions_shrink = m.get('Permissions')
        return self


class GetPermissionByCodeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPermissionByCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPermissionByCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPermissionByCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPermissionByCodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPermissionByCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneEncryptionPublicKeyRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        self.cust_space_id = cust_space_id  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneEncryptionPublicKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneEncryptionPublicKeyResponseBodyData(TeaModel):
    def __init__(self, encryption_public_key=None, encryption_public_key_status=None, phone_number=None):
        self.encryption_public_key = encryption_public_key  # type: str
        self.encryption_public_key_status = encryption_public_key_status  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneEncryptionPublicKeyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_public_key is not None:
            result['EncryptionPublicKey'] = self.encryption_public_key
        if self.encryption_public_key_status is not None:
            result['EncryptionPublicKeyStatus'] = self.encryption_public_key_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionPublicKey') is not None:
            self.encryption_public_key = m.get('EncryptionPublicKey')
        if m.get('EncryptionPublicKeyStatus') is not None:
            self.encryption_public_key_status = m.get('EncryptionPublicKeyStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneEncryptionPublicKeyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetPhoneEncryptionPublicKeyResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPhoneEncryptionPublicKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneEncryptionPublicKeyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneEncryptionPublicKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPhoneEncryptionPublicKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPhoneEncryptionPublicKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPhoneEncryptionPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberVerificationStatusRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberVerificationStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneNumberVerificationStatusResponseBodyData(TeaModel):
    def __init__(self, code_verification_status=None, id=None, phone_number=None):
        # The verification status.
        self.code_verification_status = code_verification_status  # type: str
        # The ID of the number.
        self.id = id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberVerificationStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneNumberVerificationStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: GetPhoneNumberVerificationStatusResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPhoneNumberVerificationStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneNumberVerificationStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneNumberVerificationStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPhoneNumberVerificationStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPhoneNumberVerificationStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPhoneNumberVerificationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreValidatePhoneIdRequest(TeaModel):
    def __init__(self, phone_number=None, verify_code=None):
        self.phone_number = phone_number  # type: str
        self.verify_code = verify_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPreValidatePhoneIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class GetPreValidatePhoneIdResponseBodyData(TeaModel):
    def __init__(self, phone_number=None, phone_number_id=None):
        self.phone_number = phone_number  # type: str
        self.phone_number_id = phone_number_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPreValidatePhoneIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_id is not None:
            result['PhoneNumberId'] = self.phone_number_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberId') is not None:
            self.phone_number_id = m.get('PhoneNumberId')
        return self


class GetPreValidatePhoneIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetPreValidatePhoneIdResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPreValidatePhoneIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPreValidatePhoneIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPreValidatePhoneIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPreValidatePhoneIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPreValidatePhoneIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPreValidatePhoneIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWhatsappConnectionCatalogRequest(TeaModel):
    def __init__(self, cust_space_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 waba_id=None):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The WABA ID.
        self.waba_id = waba_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWhatsappConnectionCatalogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class GetWhatsappConnectionCatalogResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, model=None, request_id=None, success=None):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail  # type: str
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message.
        self.message = message  # type: str
        # The returned results.
        self.model = model  # type: dict[str, any]
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWhatsappConnectionCatalogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWhatsappConnectionCatalogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWhatsappConnectionCatalogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWhatsappConnectionCatalogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWhatsappConnectionCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsvGetAppIdRequest(TeaModel):
    def __init__(self, permissions=None, type=None):
        self.permissions = permissions  # type: str
        # The type of the application. Set the value to WHATSAPP.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsvGetAppIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class IsvGetAppIdResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, app_id=None, code=None, config_id=None, message=None,
                 request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The message ID.
        self.app_id = app_id  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        self.config_id = config_id  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsvGetAppIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IsvGetAppIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IsvGetAppIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IsvGetAppIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IsvGetAppIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatappTemplateRequestPage(TeaModel):
    def __init__(self, index=None, size=None):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.index = index  # type: int
        # The number of message templates to return on each page. Default value: 10.
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChatappTemplateRequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListChatappTemplateRequest(TeaModel):
    def __init__(self, audit_status=None, cust_space_id=None, cust_waba_id=None, isv_code=None, language=None,
                 name=None, page=None, template_type=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The name of the message template.
        self.name = name  # type: str
        # The paging settings.
        self.page = page  # type: ListChatappTemplateRequestPage
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type  # type: str

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListChatappTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            temp_model = ListChatappTemplateRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, audit_status=None, cust_space_id=None, cust_waba_id=None, isv_code=None, language=None,
                 name=None, page_shrink=None, template_type=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The name of the message template.
        self.name = name  # type: str
        # The paging settings.
        self.page_shrink = page_shrink  # type: str
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChatappTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateResponseBodyListTemplate(TeaModel):
    def __init__(self, audit_status=None, category=None, language=None, reason=None, template_code=None,
                 template_name=None, template_type=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        # The category of the message template. Valid values:
        # 
        # *   **TRANSACTIONAL**: a transactional template
        # *   **MARKETING**: a marketing template
        # *   **OTP**: a one-time password template
        self.category = category  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # 模板审核被拒的原因
        self.reason = reason  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The name of the message template.
        self.template_name = template_name  # type: str
        # The type of the template. Valid values: WHATSAPP and VIBER.
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChatappTemplateResponseBodyListTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        if self.language is not None:
            result['Language'] = self.language
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, list_template=None, message=None, request_id=None,
                 total=None):
        # 访问被拒绝详细信息。
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The message templates.
        self.list_template = list_template  # type: list[ListChatappTemplateResponseBodyListTemplate]
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # 总记录条数。
        self.total = total  # type: int

    def validate(self):
        if self.list_template:
            for k in self.list_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChatappTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['ListTemplate'] = []
        if self.list_template is not None:
            for k in self.list_template:
                result['ListTemplate'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list_template = []
        if m.get('ListTemplate') is not None:
            for k in m.get('ListTemplate'):
                temp_model = ListChatappTemplateResponseBodyListTemplate()
                self.list_template.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListChatappTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListChatappTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChatappTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowRequestPage(TeaModel):
    def __init__(self, index=None, size=None):
        self.index = index  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowRequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListFlowRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_name=None, page=None):
        self.cust_space_id = cust_space_id  # type: str
        self.flow_name = flow_name  # type: str
        self.page = page  # type: ListFlowRequestPage

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Page') is not None:
            temp_model = ListFlowRequestPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListFlowShrinkRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_name=None, page_shrink=None):
        self.cust_space_id = cust_space_id  # type: str
        self.flow_name = flow_name  # type: str
        self.page_shrink = page_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        return self


class ListFlowResponseBodyData(TeaModel):
    def __init__(self, categories=None, flow_id=None, flow_name=None):
        self.categories = categories  # type: list[str]
        # flow ID。
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ListFlowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListFlowResponseBodyData]
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFlowResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhoneMessageQrdlRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        self.cust_space_id = cust_space_id  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPhoneMessageQrdlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ListPhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(self, deep_link_url=None, generate_qr_image=None, phone_number=None, prefilled_message=None,
                 qr_image_url=None, qrdl_code=None):
        self.deep_link_url = deep_link_url  # type: str
        self.generate_qr_image = generate_qr_image  # type: str
        self.phone_number = phone_number  # type: str
        self.prefilled_message = prefilled_message  # type: str
        self.qr_image_url = qr_image_url  # type: str
        self.qrdl_code = qrdl_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPhoneMessageQrdlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class ListPhoneMessageQrdlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListPhoneMessageQrdlResponseBodyData]
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPhoneMessageQrdlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPhoneMessageQrdlResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPhoneMessageQrdlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPhoneMessageQrdlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPhoneMessageQrdlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductRequest(TeaModel):
    def __init__(self, after=None, before=None, catalog_id=None, cust_space_id=None, fields=None, limit=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, waba_id=None):
        # The cursor that points to the end of the page of the returned data.
        self.after = after  # type: str
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before  # type: str
        # The ID of the product catalog.
        self.catalog_id = catalog_id  # type: str
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The fields. Separate multiple fields with commas (,).
        # 
        #  see [product fields](~~2579419~~)
        self.fields = fields  # type: str
        # The number of products to be queried. Valid values: 1 to 1000.
        self.limit = limit  # type: long
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the WhatsApp Business account (WABA).
        self.waba_id = waba_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ListProductResponseBodyModelPagingCursors(TeaModel):
    def __init__(self, after=None, before=None):
        # The cursor that points to the end of the page of the returned data.
        self.after = after  # type: str
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductResponseBodyModelPagingCursors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        return self


class ListProductResponseBodyModelPaging(TeaModel):
    def __init__(self, cursors=None):
        # The cursors for pagination.
        self.cursors = cursors  # type: ListProductResponseBodyModelPagingCursors

    def validate(self):
        if self.cursors:
            self.cursors.validate()

    def to_map(self):
        _map = super(ListProductResponseBodyModelPaging, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursors is not None:
            result['Cursors'] = self.cursors.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cursors') is not None:
            temp_model = ListProductResponseBodyModelPagingCursors()
            self.cursors = temp_model.from_map(m['Cursors'])
        return self


class ListProductResponseBodyModel(TeaModel):
    def __init__(self, data=None, paging=None):
        # The returned data.
        self.data = data  # type: list[dict[str, any]]
        # The pagination details.
        self.paging = paging  # type: ListProductResponseBodyModelPaging

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        _map = super(ListProductResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Paging') is not None:
            temp_model = ListProductResponseBodyModelPaging()
            self.paging = temp_model.from_map(m['Paging'])
        return self


class ListProductResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, model=None, request_id=None, success=None):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail  # type: str
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message.
        self.message = message  # type: str
        # The returned data.
        self.model = model  # type: ListProductResponseBodyModel
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success  # type: bool

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(ListProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ListProductResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductCatalogRequest(TeaModel):
    def __init__(self, after=None, before=None, business_id=None, cust_space_id=None, fields=None, limit=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        # The cursor that points to the end of the page of the returned data.
        self.after = after  # type: str
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before  # type: str
        # The Business Manager ID.
        self.business_id = business_id  # type: long
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The fields. Separate multiple fields with commas (,).
        # see  [catalog fields](~~2579419~~)
        self.fields = fields  # type: str
        # The number of catalogs to be queried. Valid values: 1 to 1000.
        self.limit = limit  # type: long
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductCatalogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListProductCatalogResponseBodyModelPagingCursors(TeaModel):
    def __init__(self, after=None, before=None):
        # The cursor that points to the end of the page of the returned data.
        self.after = after  # type: str
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductCatalogResponseBodyModelPagingCursors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        return self


class ListProductCatalogResponseBodyModelPaging(TeaModel):
    def __init__(self, cursors=None):
        # The cursors for pagination.
        self.cursors = cursors  # type: ListProductCatalogResponseBodyModelPagingCursors

    def validate(self):
        if self.cursors:
            self.cursors.validate()

    def to_map(self):
        _map = super(ListProductCatalogResponseBodyModelPaging, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursors is not None:
            result['Cursors'] = self.cursors.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cursors') is not None:
            temp_model = ListProductCatalogResponseBodyModelPagingCursors()
            self.cursors = temp_model.from_map(m['Cursors'])
        return self


class ListProductCatalogResponseBodyModel(TeaModel):
    def __init__(self, data=None, paging=None):
        # The returned data.
        self.data = data  # type: list[dict[str, any]]
        # The pagination details.
        self.paging = paging  # type: ListProductCatalogResponseBodyModelPaging

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        _map = super(ListProductCatalogResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Paging') is not None:
            temp_model = ListProductCatalogResponseBodyModelPaging()
            self.paging = temp_model.from_map(m['Paging'])
        return self


class ListProductCatalogResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, model=None, request_id=None, success=None):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail  # type: str
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message.
        self.message = message  # type: str
        # The returned results.
        self.model = model  # type: ListProductCatalogResponseBodyModel
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success  # type: bool

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(ListProductCatalogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ListProductCatalogResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductCatalogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductCatalogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductCatalogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(self, autofill_text=None, coupon_code=None, flow_action=None, flow_id=None, is_opt_out=None,
                 navigate_screen=None, package_name=None, phone_number=None, signature_hash=None, text=None, type=None, url=None,
                 url_type=None):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.autofill_text = autofill_text  # type: str
        self.coupon_code = coupon_code  # type: str
        self.flow_action = flow_action  # type: str
        self.flow_id = flow_id  # type: str
        # The unsubscribe button. This parameter is valid only when Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY in a WhatsApp message template. After you configure message sending in the ChatApp Message Service console, marketing messages will not be sent to customers if they click this button.
        self.is_opt_out = is_opt_out  # type: bool
        self.navigate_screen = navigate_screen  # type: str
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.package_name = package_name  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.signature_hash = signature_hash  # type: str
        # The text of the button.
        self.text = text  # type: str
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: the phone call button
        # *   **URL**: the URL button
        # *   **QUICK_REPLY**: the quick reply button
        # *   **COPY_CODE**: the copy code button if Category is set to AUTHENTICATION
        # *   **ONE_TAP**: the one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   In a WhatsApp message template, the quick reply button cannot be used together with the phone call button or the URL button.
        # 
        # *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a WhatsApp message template.
        # 
        # *   If Category is set to AUTHENTICATION in a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If the Type sub-parameter of the Buttons parameter is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If the Type sub-parameter of the Buttons parameter is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        self.type = type  # type: str
        # The URL to which you are redirected when you click the URL button.
        self.url = url  # type: str
        # The type of the URL. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyChatappTemplateRequestComponentsButtons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        self.phone_number = phone_number  # type: str
        self.text = text  # type: str
        self.type = type  # type: str
        self.url = url  # type: str
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class ModifyChatappTemplateRequestComponentsCardsCardComponents(TeaModel):
    def __init__(self, buttons=None, format=None, text=None, type=None, url=None):
        self.buttons = buttons  # type: list[ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons]
        self.format = format  # type: str
        self.text = text  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyChatappTemplateRequestComponentsCardsCardComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyChatappTemplateRequestComponentsCards(TeaModel):
    def __init__(self, card_components=None):
        self.card_components = card_components  # type: list[ModifyChatappTemplateRequestComponentsCardsCardComponents]

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyChatappTemplateRequestComponentsCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = ModifyChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class ModifyChatappTemplateRequestComponents(TeaModel):
    def __init__(self, add_secret_recommendation=None, buttons=None, caption=None, cards=None,
                 code_expiration_minutes=None, duration=None, file_name=None, file_type=None, format=None, has_expiration=None, text=None,
                 thumb_url=None, type=None, url=None):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY in a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation  # type: bool
        # The buttons. This parameter applies only to **BUTTONS** components.
        self.buttons = buttons  # type: list[ModifyChatappTemplateRequestComponentsButtons]
        # The description of the media resource.
        # 
        # > If the Type sub-parameter of the Components parameter is set to **HEADER** and the Format sub-parameter of the Components parameter is set to **IMAGE, DOCUMENT, or VIDEO**, you can specify this parameter.
        self.caption = caption  # type: str
        self.cards = cards  # type: list[ModifyChatappTemplateRequestComponentsCards]
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER in a WhatsApp message template. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes  # type: int
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration  # type: int
        # The name of the document.
        # 
        # > If the Type sub-parameter of the Components parameter is set to **HEADER** and the Format sub-parameter of the Components parameter is set to **DOCUMENT**, you can specify this parameter.
        self.file_name = file_name  # type: str
        # The type of the document attached in the Viber message template.
        self.file_type = file_type  # type: str
        # The type of the media resources that are included in the message. Valid values:
        # 
        # *   **TEXT**\
        # *   **IMAGE**\
        # *   **DOCUMENT**\
        # *   **VIDEO**\
        self.format = format  # type: str
        self.has_expiration = has_expiration  # type: bool
        # The text of the message that you want to send.
        # 
        # > If Category is set to AUTHENTICATION, the Text sub-parameter of the Components parameter is empty.
        self.text = text  # type: str
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url  # type: str
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # > 
        # 
        # *   In WhatsApp message templates, a **BODY** component cannot exceed 1,024 characters in length, and a **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER** components are not supported in Viber message templates.
        # 
        # *   In a Viber message template, media resources, such as images, videos, or documents, are placed in the **HEADER** component. If a Viber message contains text and an image, the image is placed under the text in the message received on a device.
        self.type = type  # type: str
        # The URL of the media resource.
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyChatappTemplateRequestComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.has_expiration is not None:
            result['HasExpiration'] = self.has_expiration
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = ModifyChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = ModifyChatappTemplateRequestComponentsCards()
                self.cards.append(temp_model.from_map(k))
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('HasExpiration') is not None:
            self.has_expiration = m.get('HasExpiration')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyChatappTemplateRequest(TeaModel):
    def __init__(self, category=None, components=None, cust_space_id=None, cust_waba_id=None, example=None,
                 isv_code=None, language=None, message_send_ttl_seconds=None, template_code=None, template_type=None):
        # The category of the Viber message template. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # > This parameter applies only to Viber message templates.
        self.category = category  # type: str
        # The components of the message template.
        # 
        # > If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter is empty and text in the body or footer is automatically generated.
        self.components = components  # type: list[ModifyChatappTemplateRequestComponents]
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example = example  # type: dict[str, str]
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # Validity period of authentication template message sending in WhatsApp
        # 
        # >This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds  # type: int
        # The message template code.
        self.template_code = template_code  # type: str
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type  # type: str

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyChatappTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example is not None:
            result['Example'] = self.example
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ModifyChatappTemplateRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, category=None, components_shrink=None, cust_space_id=None, cust_waba_id=None,
                 example_shrink=None, isv_code=None, language=None, message_send_ttl_seconds=None, template_code=None,
                 template_type=None):
        # The category of the Viber message template. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # > This parameter applies only to Viber message templates.
        self.category = category  # type: str
        # The components of the message template.
        # 
        # > If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter is empty and text in the body or footer is automatically generated.
        self.components_shrink = components_shrink  # type: str
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # Validity period of authentication template message sending in WhatsApp
        # 
        # >This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds  # type: int
        # The message template code.
        self.template_code = template_code  # type: str
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyChatappTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example_shrink is not None:
            result['Example'] = self.example_shrink
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplateResponseBodyData(TeaModel):
    def __init__(self, template_code=None, template_name=None):
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The name of the message template.
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyChatappTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ModifyChatappTemplateResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: ModifyChatappTemplateResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyChatappTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ModifyChatappTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyChatappTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyChatappTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyChatappTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowRequest(TeaModel):
    def __init__(self, categories=None, cust_space_id=None, flow_id=None, flow_name=None):
        self.categories = categories  # type: list[str]
        self.cust_space_id = cust_space_id  # type: str
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ModifyFlowShrinkRequest(TeaModel):
    def __init__(self, categories_shrink=None, cust_space_id=None, flow_id=None, flow_name=None):
        self.categories_shrink = categories_shrink  # type: str
        self.cust_space_id = cust_space_id  # type: str
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ModifyFlowResponseBodyData(TeaModel):
    def __init__(self, categories=None, flow_id=None, flow_name=None):
        self.categories = categories  # type: list[str]
        # flow ID。
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ModifyFlowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: ModifyFlowResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ModifyFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPhoneBusinessProfileRequest(TeaModel):
    def __init__(self, address=None, cust_space_id=None, description=None, email=None, phone_number=None,
                 profile_picture_url=None, vertical=None, websites=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.address = address  # type: str
        # Modifies the business information of the account to which a specified phone number is bound.
        self.cust_space_id = cust_space_id  # type: str
        # The address.
        self.description = description  # type: str
        # The description.
        self.email = email  # type: str
        # You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        self.phone_number = phone_number  # type: str
        # The industry.
        # 
        # > Enum: {OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, TRAVEL, RESTAURANT}
        self.profile_picture_url = profile_picture_url  # type: str
        # Sichuan
        self.vertical = vertical  # type: str
        # The email address.
        self.websites = websites  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPhoneBusinessProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites is not None:
            result['Websites'] = self.websites
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileShrinkRequest(TeaModel):
    def __init__(self, address=None, cust_space_id=None, description=None, email=None, phone_number=None,
                 profile_picture_url=None, vertical=None, websites_shrink=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.address = address  # type: str
        # Modifies the business information of the account to which a specified phone number is bound.
        self.cust_space_id = cust_space_id  # type: str
        # The address.
        self.description = description  # type: str
        # The description.
        self.email = email  # type: str
        # You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        self.phone_number = phone_number  # type: str
        # The industry.
        # 
        # > Enum: {OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, TRAVEL, RESTAURANT}
        self.profile_picture_url = profile_picture_url  # type: str
        # Sichuan
        self.vertical = vertical  # type: str
        # The email address.
        self.websites_shrink = websites_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPhoneBusinessProfileShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites_shrink is not None:
            result['Websites'] = self.websites_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites_shrink = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The URL of the website.
        self.code = code  # type: str
        # The ID of the request.
        self.message = message  # type: str
        # The websites.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPhoneBusinessProfileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPhoneBusinessProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPhoneBusinessProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPhoneBusinessProfileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPhoneBusinessProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFlowRequest(TeaModel):
    def __init__(self, cust_space_id=None, flow_id=None):
        self.cust_space_id = cust_space_id  # type: str
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class PublishFlowResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatappBindWabaRequest(TeaModel):
    def __init__(self, cust_space_id=None, isv_code=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChatappBindWabaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        return self


class QueryChatappBindWabaResponseBodyData(TeaModel):
    def __init__(self, account_review_status=None, currency=None, id=None, message_template_namespace=None,
                 name=None):
        # The review status of the WhatsApp Business account.
        self.account_review_status = account_review_status  # type: str
        # The currency.
        self.currency = currency  # type: str
        # The ID of the WhatsApp Business account.
        self.id = id  # type: str
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace  # type: str
        # The name of the WhatsApp Business account.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChatappBindWabaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.id is not None:
            result['Id'] = self.id
        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryChatappBindWabaResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: QueryChatappBindWabaResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryChatappBindWabaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryChatappBindWabaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryChatappBindWabaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryChatappBindWabaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryChatappBindWabaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatappPhoneNumbersRequest(TeaModel):
    def __init__(self, cust_space_id=None, isv_code=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChatappPhoneNumbersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        return self


class QueryChatappPhoneNumbersResponseBodyPhoneNumbers(TeaModel):
    def __init__(self, code_verification_status=None, messaging_limit_tier=None, name_status=None,
                 new_name_status=None, phone_number=None, quality_rating=None, status=None, status_callback_url=None,
                 status_queue=None, up_callback_url=None, up_queue=None, verified_name=None):
        # The verification status of the phone number.
        self.code_verification_status = code_verification_status  # type: str
        # The maximum number of messages that can be sent to users by using the phone number.
        self.messaging_limit_tier = messaging_limit_tier  # type: str
        # The status of the business name.
        self.name_status = name_status  # type: str
        # The review status of the new business name.
        self.new_name_status = new_name_status  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str
        # The quality rating of the phone number. Valid values:
        # 
        # *   **GREEN**\
        # *   **YELLOW**\
        # *   **RED**\
        # *   **UNKNOWN**\
        self.quality_rating = quality_rating  # type: str
        # The status of the phone number.
        # 
        # *   PENDING
        # *   DELETED
        # *   MIGRATED
        # *   BANNED
        # *   RESTRICTED
        # *   RATE_LIMITED
        # *   FLAGGED
        # *   CONNECTED
        # *   DISCONNECTED
        # *   UNKNOWN
        # *   UNVERIFIED
        self.status = status  # type: str
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url  # type: str
        # The status report notification queue.
        self.status_queue = status_queue  # type: str
        # The callback URL to which MO messages are sent by using HTTP callbacks.
        self.up_callback_url = up_callback_url  # type: str
        # The mobile originated (MO) message notification queue.
        self.up_queue = up_queue  # type: str
        # The name of the company with which the phone number is associated.
        self.verified_name = verified_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChatappPhoneNumbersResponseBodyPhoneNumbers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.messaging_limit_tier is not None:
            result['MessagingLimitTier'] = self.messaging_limit_tier
        if self.name_status is not None:
            result['NameStatus'] = self.name_status
        if self.new_name_status is not None:
            result['NewNameStatus'] = self.new_name_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.quality_rating is not None:
            result['QualityRating'] = self.quality_rating
        if self.status is not None:
            result['Status'] = self.status
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('MessagingLimitTier') is not None:
            self.messaging_limit_tier = m.get('MessagingLimitTier')
        if m.get('NameStatus') is not None:
            self.name_status = m.get('NameStatus')
        if m.get('NewNameStatus') is not None:
            self.new_name_status = m.get('NewNameStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualityRating') is not None:
            self.quality_rating = m.get('QualityRating')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class QueryChatappPhoneNumbersResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, phone_numbers=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The message returned.
        self.message = message  # type: str
        # The list of phone numbers.
        self.phone_numbers = phone_numbers  # type: list[QueryChatappPhoneNumbersResponseBodyPhoneNumbers]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.phone_numbers:
            for k in self.phone_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryChatappPhoneNumbersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PhoneNumbers'] = []
        if self.phone_numbers is not None:
            for k in self.phone_numbers:
                result['PhoneNumbers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.phone_numbers = []
        if m.get('PhoneNumbers') is not None:
            for k in m.get('PhoneNumbers'):
                temp_model = QueryChatappPhoneNumbersResponseBodyPhoneNumbers()
                self.phone_numbers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryChatappPhoneNumbersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryChatappPhoneNumbersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryChatappPhoneNumbersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryChatappPhoneNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPhoneBusinessProfileRequest(TeaModel):
    def __init__(self, cust_space_id=None, phone_number=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPhoneBusinessProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class QueryPhoneBusinessProfileResponseBodyData(TeaModel):
    def __init__(self, address=None, description=None, email=None, profile_picture_url=None, vertical=None,
                 websites=None):
        # The address.
        self.address = address  # type: str
        # The description.
        self.description = description  # type: str
        # The email address.
        self.email = email  # type: str
        # The URL of the profile picture.
        self.profile_picture_url = profile_picture_url  # type: str
        # The industry.
        self.vertical = vertical  # type: str
        # The websites.
        self.websites = websites  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPhoneBusinessProfileResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites is not None:
            result['Websites'] = self.websites
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites = m.get('Websites')
        return self


class QueryPhoneBusinessProfileResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: QueryPhoneBusinessProfileResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPhoneBusinessProfileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryPhoneBusinessProfileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPhoneBusinessProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPhoneBusinessProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPhoneBusinessProfileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPhoneBusinessProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWabaBusinessInfoRequest(TeaModel):
    def __init__(self, cust_space_id=None, waba_id=None):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WABA.
        self.waba_id = waba_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWabaBusinessInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class QueryWabaBusinessInfoResponseBodyData(TeaModel):
    def __init__(self, business_id=None, business_name=None, verification_status=None, vertical=None):
        # The ID of the business platform.
        self.business_id = business_id  # type: str
        # The name of the business platform.
        self.business_name = business_name  # type: str
        # The verification status.
        self.verification_status = verification_status  # type: str
        # The industry.
        self.vertical = vertical  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWabaBusinessInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        return self


class QueryWabaBusinessInfoResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, data=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The business information about the WABA.
        self.data = data  # type: QueryWabaBusinessInfoResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryWabaBusinessInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryWabaBusinessInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryWabaBusinessInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryWabaBusinessInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWabaBusinessInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWabaBusinessInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendChatappMassMessageRequestSenderListFlowAction(TeaModel):
    def __init__(self, flow_action_data=None, flow_token=None):
        self.flow_action_data = flow_action_data  # type: dict[str, str]
        self.flow_token = flow_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMassMessageRequestSenderListFlowAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action_data is not None:
            result['FlowActionData'] = self.flow_action_data
        if self.flow_token is not None:
            result['FlowToken'] = self.flow_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowActionData') is not None:
            self.flow_action_data = m.get('FlowActionData')
        if m.get('FlowToken') is not None:
            self.flow_token = m.get('FlowToken')
        return self


class SendChatappMassMessageRequestSenderListProductActionSectionsProductItems(TeaModel):
    def __init__(self, product_retailer_id=None):
        self.product_retailer_id = product_retailer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMassMessageRequestSenderListProductActionSectionsProductItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_retailer_id is not None:
            result['ProductRetailerId'] = self.product_retailer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductRetailerId') is not None:
            self.product_retailer_id = m.get('ProductRetailerId')
        return self


class SendChatappMassMessageRequestSenderListProductActionSections(TeaModel):
    def __init__(self, product_items=None, title=None):
        self.product_items = product_items  # type: list[SendChatappMassMessageRequestSenderListProductActionSectionsProductItems]
        self.title = title  # type: str

    def validate(self):
        if self.product_items:
            for k in self.product_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendChatappMassMessageRequestSenderListProductActionSections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItems'] = []
        if self.product_items is not None:
            for k in self.product_items:
                result['ProductItems'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_items = []
        if m.get('ProductItems') is not None:
            for k in m.get('ProductItems'):
                temp_model = SendChatappMassMessageRequestSenderListProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SendChatappMassMessageRequestSenderListProductAction(TeaModel):
    def __init__(self, sections=None, thumbnail_product_retailer_id=None):
        self.sections = sections  # type: list[SendChatappMassMessageRequestSenderListProductActionSections]
        self.thumbnail_product_retailer_id = thumbnail_product_retailer_id  # type: str

    def validate(self):
        if self.sections:
            for k in self.sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendChatappMassMessageRequestSenderListProductAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sections'] = []
        if self.sections is not None:
            for k in self.sections:
                result['Sections'].append(k.to_map() if k else None)
        if self.thumbnail_product_retailer_id is not None:
            result['ThumbnailProductRetailerId'] = self.thumbnail_product_retailer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sections = []
        if m.get('Sections') is not None:
            for k in m.get('Sections'):
                temp_model = SendChatappMassMessageRequestSenderListProductActionSections()
                self.sections.append(temp_model.from_map(k))
        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')
        return self


class SendChatappMassMessageRequestSenderList(TeaModel):
    def __init__(self, flow_action=None, payload=None, product_action=None, template_params=None, to=None):
        self.flow_action = flow_action  # type: SendChatappMassMessageRequestSenderListFlowAction
        # payload
        self.payload = payload  # type: list[str]
        self.product_action = product_action  # type: SendChatappMassMessageRequestSenderListProductAction
        # The parameters of the message template.
        self.template_params = template_params  # type: dict[str, str]
        # The phone number that receives the message.
        self.to = to  # type: str

    def validate(self):
        if self.flow_action:
            self.flow_action.validate()
        if self.product_action:
            self.product_action.validate()

    def to_map(self):
        _map = super(SendChatappMassMessageRequestSenderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowAction') is not None:
            temp_model = SendChatappMassMessageRequestSenderListFlowAction()
            self.flow_action = temp_model.from_map(m['FlowAction'])
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ProductAction') is not None:
            temp_model = SendChatappMassMessageRequestSenderListProductAction()
            self.product_action = temp_model.from_map(m['ProductAction'])
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SendChatappMassMessageRequest(TeaModel):
    def __init__(self, channel_type=None, cust_space_id=None, cust_waba_id=None, fall_back_content=None,
                 fall_back_duration=None, fall_back_id=None, fall_back_rule=None, from_=None, isv_code=None, label=None, language=None,
                 sender_list=None, tag=None, task_id=None, template_code=None, ttl=None):
        # The channel type. Valid values: whatsapp, viber, and line.
        self.channel_type = channel_type  # type: str
        # The space ID of the user.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp Business account under the ISV account.
        self.cust_waba_id = cust_waba_id  # type: str
        # The fallback content.
        self.fall_back_content = fall_back_content  # type: str
        # 消息在指定时间内没有返回已到达回执时回落, 不填代表不根据此时间判断回落，只有发送失败和有失败的状态报告时才会回落。时间单位为秒 最小值为60，最大值43200
        self.fall_back_duration = fall_back_duration  # type: int
        # The ID of the fallback strategy.
        self.fall_back_id = fall_back_id  # type: str
        self.fall_back_rule = fall_back_rule  # type: str
        # The phone number of the message sender.
        self.from_ = from_  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The message type when the ChannelType parameter is set to viber. Valid values: promotion and transaction.
        self.label = label  # type: str
        # The language. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The list of phone numbers that receive the message.
        self.sender_list = sender_list  # type: list[SendChatappMassMessageRequestSenderList]
        # The tag information when the ChannelType parameter is set to viber.
        self.tag = tag  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str
        # The encoding of the message template.
        self.template_code = template_code  # type: str
        # The timeout period for sending messages when the ChannelType parameter is set to viber. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl  # type: long

    def validate(self):
        if self.sender_list:
            for k in self.sender_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendChatappMassMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        result['SenderList'] = []
        if self.sender_list is not None:
            for k in self.sender_list:
                result['SenderList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        self.sender_list = []
        if m.get('SenderList') is not None:
            for k in m.get('SenderList'):
                temp_model = SendChatappMassMessageRequestSenderList()
                self.sender_list.append(temp_model.from_map(k))
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SendChatappMassMessageShrinkRequest(TeaModel):
    def __init__(self, channel_type=None, cust_space_id=None, cust_waba_id=None, fall_back_content=None,
                 fall_back_duration=None, fall_back_id=None, fall_back_rule=None, from_=None, isv_code=None, label=None, language=None,
                 sender_list_shrink=None, tag=None, task_id=None, template_code=None, ttl=None):
        # The channel type. Valid values: whatsapp, viber, and line.
        self.channel_type = channel_type  # type: str
        # The space ID of the user.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp Business account under the ISV account.
        self.cust_waba_id = cust_waba_id  # type: str
        # The fallback content.
        self.fall_back_content = fall_back_content  # type: str
        # 消息在指定时间内没有返回已到达回执时回落, 不填代表不根据此时间判断回落，只有发送失败和有失败的状态报告时才会回落。时间单位为秒 最小值为60，最大值43200
        self.fall_back_duration = fall_back_duration  # type: int
        # The ID of the fallback strategy.
        self.fall_back_id = fall_back_id  # type: str
        self.fall_back_rule = fall_back_rule  # type: str
        # The phone number of the message sender.
        self.from_ = from_  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The message type when the ChannelType parameter is set to viber. Valid values: promotion and transaction.
        self.label = label  # type: str
        # The language. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The list of phone numbers that receive the message.
        self.sender_list_shrink = sender_list_shrink  # type: str
        # The tag information when the ChannelType parameter is set to viber.
        self.tag = tag  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str
        # The encoding of the message template.
        self.template_code = template_code  # type: str
        # The timeout period for sending messages when the ChannelType parameter is set to viber. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMassMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.sender_list_shrink is not None:
            result['SenderList'] = self.sender_list_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SenderList') is not None:
            self.sender_list_shrink = m.get('SenderList')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SendChatappMassMessageResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, group_message_id=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The ID of the group of messages.
        self.group_message_id = group_message_id  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMassMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.group_message_id is not None:
            result['GroupMessageId'] = self.group_message_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupMessageId') is not None:
            self.group_message_id = m.get('GroupMessageId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendChatappMassMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendChatappMassMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendChatappMassMessageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendChatappMassMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendChatappMessageRequestFlowAction(TeaModel):
    def __init__(self, flow_action_data=None, flow_token=None):
        self.flow_action_data = flow_action_data  # type: dict[str, str]
        self.flow_token = flow_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMessageRequestFlowAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action_data is not None:
            result['FlowActionData'] = self.flow_action_data
        if self.flow_token is not None:
            result['FlowToken'] = self.flow_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowActionData') is not None:
            self.flow_action_data = m.get('FlowActionData')
        if m.get('FlowToken') is not None:
            self.flow_token = m.get('FlowToken')
        return self


class SendChatappMessageRequestProductActionSectionsProductItems(TeaModel):
    def __init__(self, product_retailer_id=None):
        # The retailer ID of the product.
        self.product_retailer_id = product_retailer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMessageRequestProductActionSectionsProductItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_retailer_id is not None:
            result['ProductRetailerId'] = self.product_retailer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductRetailerId') is not None:
            self.product_retailer_id = m.get('ProductRetailerId')
        return self


class SendChatappMessageRequestProductActionSections(TeaModel):
    def __init__(self, product_items=None, title=None):
        # The products.
        self.product_items = product_items  # type: list[SendChatappMessageRequestProductActionSectionsProductItems]
        # The name of the category.
        self.title = title  # type: str

    def validate(self):
        if self.product_items:
            for k in self.product_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendChatappMessageRequestProductActionSections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItems'] = []
        if self.product_items is not None:
            for k in self.product_items:
                result['ProductItems'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_items = []
        if m.get('ProductItems') is not None:
            for k in m.get('ProductItems'):
                temp_model = SendChatappMessageRequestProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SendChatappMessageRequestProductAction(TeaModel):
    def __init__(self, sections=None, thumbnail_product_retailer_id=None):
        # The products. Up to 30 products can be added. The products can be divided into up to 10 categories.
        self.sections = sections  # type: list[SendChatappMessageRequestProductActionSections]
        # The retailer ID of the product.
        self.thumbnail_product_retailer_id = thumbnail_product_retailer_id  # type: str

    def validate(self):
        if self.sections:
            for k in self.sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendChatappMessageRequestProductAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sections'] = []
        if self.sections is not None:
            for k in self.sections:
                result['Sections'].append(k.to_map() if k else None)
        if self.thumbnail_product_retailer_id is not None:
            result['ThumbnailProductRetailerId'] = self.thumbnail_product_retailer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sections = []
        if m.get('Sections') is not None:
            for k in m.get('Sections'):
                temp_model = SendChatappMessageRequestProductActionSections()
                self.sections.append(temp_model.from_map(k))
        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')
        return self


class SendChatappMessageRequest(TeaModel):
    def __init__(self, channel_type=None, content=None, context_message_id=None, cust_space_id=None,
                 cust_waba_id=None, fall_back_content=None, fall_back_duration=None, fall_back_id=None, fall_back_rule=None,
                 flow_action=None, from_=None, isv_code=None, label=None, language=None, message_type=None, payload=None,
                 product_action=None, tag=None, task_id=None, template_code=None, template_params=None, to=None, tracking_data=None,
                 ttl=None, type=None):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   **viber**\
        # *   line. The feature that ChatAPP sends messages by using Line is under development.
        self.channel_type = channel_type  # type: str
        # The content of the message.
        # 
        # **Usage notes when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required and the **caption** parameter cannot be specified.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **audio**, the **link** parameter is required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **document**, the **link** and **fileName** parameters are required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **interactive**, the **type** and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **contacts**, the **name** parameter is required.
        # *   When you set the **MessageType** parameter to **location**, the **longitude** and **latitude** parameters are required.
        # *   When you set the **MessageType** parameter to **sticker**, the **link** parameter is required, and the **caption** and **fileName** parameters are invalid.
        # *   When you set the **MessageType** parameter to **reaction**, the **messageId** and **emoji** parameters are required.
        # 
        # **Usage notes when you set the ChannelType parameter to viber:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **document**, the **link**, **fileName**, and **fileType** parameters are required.
        # *   When you set the **MessageType** parameter to **text_button**, the **text**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_image_button**, the **text**, **link**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video**, the **text**, **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video_button**, the **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption** parameters are required. The **action** parameter is invalid.
        self.content = content  # type: str
        # The ID of the message to reply to.
        self.context_message_id = context_message_id  # type: str
        # The space ID of the user.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # The content of the fallback message.
        self.fall_back_content = fall_back_content  # type: str
        self.fall_back_duration = fall_back_duration  # type: int
        # The ID of the fallback strategy. You can create a fallback strategy and view the information in the console.
        self.fall_back_id = fall_back_id  # type: str
        self.fall_back_rule = fall_back_rule  # type: str
        self.flow_action = flow_action  # type: SendChatappMessageRequestFlowAction
        # The phone number of the message sender.
        # 
        # > You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatAPP console.
        self.from_ = from_  # type: str
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The type of the Viber message. This parameter is required if you set the ChannelType parameter to viber. Valid values: promotion and transaction.
        self.label = label  # type: str
        # The language that is used in the message template. This parameter is required only if you set the Type parameter to **template**. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The specific type of the message. This parameter is required only if you set the Type parameter to **message**.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **audio**: an audio message.
        # *   **document**: a document message.
        # *   **interactive**: an interactive message.
        # *   **contacts**: a contact message.
        # *   **location**: a location message.
        # *   **sticker**: a sticker message.
        # *   **reaction**: a reaction message.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to viber:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **document**: a document message.
        # *   **text_button**: a message that contains the text and button media objects.
        # *   **text_image_button**: a message that contains multiple media objects, including the text, image, and button.
        # *   **text_video**: a message that contains the text and video media objects.
        # *   **text_video_button**: a message that contains multiple media objects, including text, video, and button.
        # *   **text_image**: a message that contains the text and image media objects.
        # 
        # > For more information, see [Parameters of a message template](~~454530~~).
        self.message_type = message_type  # type: str
        # The payload of the button.
        self.payload = payload  # type: list[str]
        # The information about the products included in the WhatsApp catalog message or multi-product message (MPM).
        self.product_action = product_action  # type: SendChatappMessageRequestProductAction
        # The tag information of the Viber message.
        self.tag = tag  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str
        # The code of the message template. This parameter is required only if you set the Type parameter to **template**.
        self.template_code = template_code  # type: str
        # The variables of the message template.
        self.template_params = template_params  # type: dict[str, str]
        # The phone number that receives the message.
        self.to = to  # type: str
        # The tracking ID of the Viber message.
        self.tracking_data = tracking_data  # type: str
        # The timeout period for sending the Viber message. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl  # type: int
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatAPP console and is approved. You can send template messages at any time based on your business requirements.
        # *   **message**: a custom message. You can send a custom message to a user only within 24 hours after you receive the last message from the user.
        self.type = type  # type: str

    def validate(self):
        if self.flow_action:
            self.flow_action.validate()
        if self.product_action:
            self.product_action.validate()

    def to_map(self):
        _map = super(SendChatappMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.content is not None:
            result['Content'] = self.content
        if self.context_message_id is not None:
            result['ContextMessageId'] = self.context_message_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        if self.tracking_data is not None:
            result['TrackingData'] = self.tracking_data
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContextMessageId') is not None:
            self.context_message_id = m.get('ContextMessageId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('FlowAction') is not None:
            temp_model = SendChatappMessageRequestFlowAction()
            self.flow_action = temp_model.from_map(m['FlowAction'])
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ProductAction') is not None:
            temp_model = SendChatappMessageRequestProductAction()
            self.product_action = temp_model.from_map(m['ProductAction'])
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TrackingData') is not None:
            self.tracking_data = m.get('TrackingData')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageShrinkRequest(TeaModel):
    def __init__(self, channel_type=None, content=None, context_message_id=None, cust_space_id=None,
                 cust_waba_id=None, fall_back_content=None, fall_back_duration=None, fall_back_id=None, fall_back_rule=None,
                 flow_action_shrink=None, from_=None, isv_code=None, label=None, language=None, message_type=None, payload_shrink=None,
                 product_action_shrink=None, tag=None, task_id=None, template_code=None, template_params_shrink=None, to=None,
                 tracking_data=None, ttl=None, type=None):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   **viber**\
        # *   line. The feature that ChatAPP sends messages by using Line is under development.
        self.channel_type = channel_type  # type: str
        # The content of the message.
        # 
        # **Usage notes when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required and the **caption** parameter cannot be specified.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **audio**, the **link** parameter is required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **document**, the **link** and **fileName** parameters are required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **interactive**, the **type** and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **contacts**, the **name** parameter is required.
        # *   When you set the **MessageType** parameter to **location**, the **longitude** and **latitude** parameters are required.
        # *   When you set the **MessageType** parameter to **sticker**, the **link** parameter is required, and the **caption** and **fileName** parameters are invalid.
        # *   When you set the **MessageType** parameter to **reaction**, the **messageId** and **emoji** parameters are required.
        # 
        # **Usage notes when you set the ChannelType parameter to viber:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **document**, the **link**, **fileName**, and **fileType** parameters are required.
        # *   When you set the **MessageType** parameter to **text_button**, the **text**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_image_button**, the **text**, **link**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video**, the **text**, **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video_button**, the **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption** parameters are required. The **action** parameter is invalid.
        self.content = content  # type: str
        # The ID of the message to reply to.
        self.context_message_id = context_message_id  # type: str
        # The space ID of the user.
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # The content of the fallback message.
        self.fall_back_content = fall_back_content  # type: str
        self.fall_back_duration = fall_back_duration  # type: int
        # The ID of the fallback strategy. You can create a fallback strategy and view the information in the console.
        self.fall_back_id = fall_back_id  # type: str
        self.fall_back_rule = fall_back_rule  # type: str
        self.flow_action_shrink = flow_action_shrink  # type: str
        # The phone number of the message sender.
        # 
        # > You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatAPP console.
        self.from_ = from_  # type: str
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code  # type: str
        # The type of the Viber message. This parameter is required if you set the ChannelType parameter to viber. Valid values: promotion and transaction.
        self.label = label  # type: str
        # The language that is used in the message template. This parameter is required only if you set the Type parameter to **template**. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language  # type: str
        # The specific type of the message. This parameter is required only if you set the Type parameter to **message**.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **audio**: an audio message.
        # *   **document**: a document message.
        # *   **interactive**: an interactive message.
        # *   **contacts**: a contact message.
        # *   **location**: a location message.
        # *   **sticker**: a sticker message.
        # *   **reaction**: a reaction message.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to viber:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **document**: a document message.
        # *   **text_button**: a message that contains the text and button media objects.
        # *   **text_image_button**: a message that contains multiple media objects, including the text, image, and button.
        # *   **text_video**: a message that contains the text and video media objects.
        # *   **text_video_button**: a message that contains multiple media objects, including text, video, and button.
        # *   **text_image**: a message that contains the text and image media objects.
        # 
        # > For more information, see [Parameters of a message template](~~454530~~).
        self.message_type = message_type  # type: str
        # The payload of the button.
        self.payload_shrink = payload_shrink  # type: str
        # The information about the products included in the WhatsApp catalog message or multi-product message (MPM).
        self.product_action_shrink = product_action_shrink  # type: str
        # The tag information of the Viber message.
        self.tag = tag  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str
        # The code of the message template. This parameter is required only if you set the Type parameter to **template**.
        self.template_code = template_code  # type: str
        # The variables of the message template.
        self.template_params_shrink = template_params_shrink  # type: str
        # The phone number that receives the message.
        self.to = to  # type: str
        # The tracking ID of the Viber message.
        self.tracking_data = tracking_data  # type: str
        # The timeout period for sending the Viber message. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl  # type: int
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatAPP console and is approved. You can send template messages at any time based on your business requirements.
        # *   **message**: a custom message. You can send a custom message to a user only within 24 hours after you receive the last message from the user.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.content is not None:
            result['Content'] = self.content
        if self.context_message_id is not None:
            result['ContextMessageId'] = self.context_message_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.flow_action_shrink is not None:
            result['FlowAction'] = self.flow_action_shrink
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.product_action_shrink is not None:
            result['ProductAction'] = self.product_action_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params_shrink is not None:
            result['TemplateParams'] = self.template_params_shrink
        if self.to is not None:
            result['To'] = self.to
        if self.tracking_data is not None:
            result['TrackingData'] = self.tracking_data
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContextMessageId') is not None:
            self.context_message_id = m.get('ContextMessageId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('FlowAction') is not None:
            self.flow_action_shrink = m.get('FlowAction')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('ProductAction') is not None:
            self.product_action_shrink = m.get('ProductAction')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params_shrink = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TrackingData') is not None:
            self.tracking_data = m.get('TrackingData')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, message_id=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the message that was sent.
        self.message_id = message_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendChatappMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendChatappMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendChatappMessageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendChatappMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIsvCustomerTermsRequest(TeaModel):
    def __init__(self, business_desc=None, contact_mail=None, country_id=None, cust_name=None, cust_space_id=None,
                 isv_terms=None, office_address=None):
        # The use scenario.
        self.business_desc = business_desc  # type: str
        # The email address of your business.
        self.contact_mail = contact_mail  # type: str
        # The country code.
        self.country_id = country_id  # type: str
        # The display name of your business.
        self.cust_name = cust_name  # type: str
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ISV or Client Agreement.
        # 
        # > Before you upload files to Object Storage Service (OSS) servers, you must call the GetChatappUploadAuthorization operation to obtain the authentication information required to upload files. You can use the SDK provided by OSS to upload files. When you upload a file, you must set the key parameter value. To set the value for the key parameter, concatenate the value of the Dir parameter and the file name by using a forward slash (/). You can obtain the value of the Dir parameter by calling the GetChatappUploadAuthorization operation.
        # 
        # > The value of this parameter is the name of the uploaded file.
        self.isv_terms = isv_terms  # type: str
        # The address of your business.
        self.office_address = office_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitIsvCustomerTermsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_desc is not None:
            result['BusinessDesc'] = self.business_desc
        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.cust_name is not None:
            result['CustName'] = self.cust_name
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_terms is not None:
            result['IsvTerms'] = self.isv_terms
        if self.office_address is not None:
            result['OfficeAddress'] = self.office_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessDesc') is not None:
            self.business_desc = m.get('BusinessDesc')
        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('CustName') is not None:
            self.cust_name = m.get('CustName')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvTerms') is not None:
            self.isv_terms = m.get('IsvTerms')
        if m.get('OfficeAddress') is not None:
            self.office_address = m.get('OfficeAddress')
        return self


class SubmitIsvCustomerTermsResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitIsvCustomerTermsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitIsvCustomerTermsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitIsvCustomerTermsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitIsvCustomerTermsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitIsvCustomerTermsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccountWebhookRequest(TeaModel):
    def __init__(self, cust_space_id=None, http_flag=None, queue_flag=None, status_callback_url=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # Specifies whether to use HTTP callbacks to receive message receipts. Valid values:
        # 
        # *   Y: indicates that HTTP callbacks are used to receive receipts.
        # *   N: indicates that HTTP callbacks are not used to receive receipts.
        self.http_flag = http_flag  # type: str
        # Specifies whether to use Message Service (MNS) queues to receive receipts. Valid values:
        # 
        # *   Y: indicates that MNS queues are used to receive receipts.
        # *   N: indicates that MNS queues are not used to receive receipts.
        self.queue_flag = queue_flag  # type: str
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccountWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag
        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')
        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        return self


class UpdateAccountWebhookResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccountWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccountWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAccountWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAccountWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAccountWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCommerceSettingRequest(TeaModel):
    def __init__(self, cart_enable=None, catalog_visible=None, cust_space_id=None, phone_number=None):
        self.cart_enable = cart_enable  # type: bool
        self.catalog_visible = catalog_visible  # type: bool
        self.cust_space_id = cust_space_id  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCommerceSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable
        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')
        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class UpdateCommerceSettingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCommerceSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCommerceSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCommerceSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCommerceSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCommerceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowJSONAssetRequest(TeaModel):
    def __init__(self, cust_space_id=None, file_path=None, flow_id=None):
        self.cust_space_id = cust_space_id  # type: str
        self.file_path = file_path  # type: str
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowJSONAssetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class UpdateFlowJSONAssetResponseBodyData(TeaModel):
    def __init__(self, flow_id=None):
        # Flow ID。
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowJSONAssetResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class UpdateFlowJSONAssetResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateFlowJSONAssetResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateFlowJSONAssetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateFlowJSONAssetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFlowJSONAssetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFlowJSONAssetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFlowJSONAssetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFlowJSONAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneEncryptionPublicKeyRequest(TeaModel):
    def __init__(self, cust_space_id=None, encryption_public_key=None, phone_number=None):
        self.cust_space_id = cust_space_id  # type: str
        self.encryption_public_key = encryption_public_key  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePhoneEncryptionPublicKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.encryption_public_key is not None:
            result['EncryptionPublicKey'] = self.encryption_public_key
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EncryptionPublicKey') is not None:
            self.encryption_public_key = m.get('EncryptionPublicKey')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class UpdatePhoneEncryptionPublicKeyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePhoneEncryptionPublicKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneEncryptionPublicKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePhoneEncryptionPublicKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePhoneEncryptionPublicKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePhoneEncryptionPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneMessageQrdlRequest(TeaModel):
    def __init__(self, cust_space_id=None, generate_qr_image=None, phone_number=None, prefilled_message=None,
                 qrdl_code=None):
        self.cust_space_id = cust_space_id  # type: str
        self.generate_qr_image = generate_qr_image  # type: str
        self.phone_number = phone_number  # type: str
        self.prefilled_message = prefilled_message  # type: str
        self.qrdl_code = qrdl_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePhoneMessageQrdlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class UpdatePhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(self, deep_link_url=None, generate_qr_image=None, phone_number=None, prefilled_message=None,
                 qr_image_url=None, qrdl_code=None):
        self.deep_link_url = deep_link_url  # type: str
        self.generate_qr_image = generate_qr_image  # type: str
        self.phone_number = phone_number  # type: str
        self.prefilled_message = prefilled_message  # type: str
        self.qr_image_url = qr_image_url  # type: str
        self.qrdl_code = qrdl_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePhoneMessageQrdlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class UpdatePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: UpdatePhoneMessageQrdlResponseBodyData
        self.message = message  # type: str
        # Id of the request。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdatePhoneMessageQrdlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdatePhoneMessageQrdlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneMessageQrdlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePhoneMessageQrdlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePhoneMessageQrdlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneWebhookRequest(TeaModel):
    def __init__(self, cust_space_id=None, http_flag=None, phone_number=None, queue_flag=None,
                 status_callback_url=None, up_callback_url=None):
        self.cust_space_id = cust_space_id  # type: str
        self.http_flag = http_flag  # type: str
        self.phone_number = phone_number  # type: str
        self.queue_flag = queue_flag  # type: str
        self.status_callback_url = status_callback_url  # type: str
        self.up_callback_url = up_callback_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePhoneWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        return self


class UpdatePhoneWebhookResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, message=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePhoneWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePhoneWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePhoneWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePhoneWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


