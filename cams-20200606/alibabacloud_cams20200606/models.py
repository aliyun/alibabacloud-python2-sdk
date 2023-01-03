# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BeeBotAssociateRequest(TeaModel):
    def __init__(self, chat_bot_instance_id=None, cust_space_id=None, isv_code=None, perspective=None,
                 recommend_num=None, session_id=None, utterance=None):
        # The ID of chatbot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # ISV verification code, which is used to verify whether the sub-account is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective = perspective  # type: list[str]
        # The number of recommended questions, which ranges from 1 to 10.
        self.recommend_num = recommend_num  # type: int
        # The ID of the session, which identifies the session and context information of the visitor.
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
        # The ID of chatbot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # ISV verification code, which is used to verify whether the sub-account is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective_shrink = perspective_shrink  # type: str
        # The number of recommended questions, which ranges from 1 to 10.
        self.recommend_num = recommend_num  # type: int
        # The ID of the session, which identifies the session and context information of the visitor.
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # If OK is returned, the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: BeeBotAssociateResponseBodyData
        # The error message.
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
        # The ID of chatbot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The name of the intent in the dialog flow. When this parameter is specified, the bot will conduct a Q\&A according to the intent.
        self.intent_name = intent_name  # type: str
        # ISV verification code, which is used to verify whether the sub-account is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The ID of the knowledge title in the knowledge base.
        self.knowledge_id = knowledge_id  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective = perspective  # type: list[str]
        # The ID of the visitor, which is used to identify users in the current session.
        self.sender_id = sender_id  # type: str
        # The nickname of the visitor in the current session.
        self.sender_nick = sender_nick  # type: str
        # The ID of the session, which identifies the session and context information of the visitor.
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
        # The ID of chatbot instance.
        self.chat_bot_instance_id = chat_bot_instance_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The name of the intent in the dialog flow. When this parameter is specified, the bot will conduct a Q\&A according to the intent.
        self.intent_name = intent_name  # type: str
        # ISV verification code, which is used to verify whether the sub-account is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The ID of the knowledge title in the knowledge base.
        self.knowledge_id = knowledge_id  # type: str
        # The list of codes for answers from different perspectives.
        self.perspective_shrink = perspective_shrink  # type: str
        # The ID of the visitor, which is used to identify users in the current session.
        self.sender_id = sender_id  # type: str
        # The nickname of the visitor in the current session.
        self.sender_nick = sender_nick  # type: str
        # The ID of the session, which identifies the session and context information of the visitor.
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
        # The ID of the hit problem in the knowledge base.
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
        # The recommended content, which may be the entity in graph-based question answering, the standard knowledge in knowledge-based question answering, or the column value in table-based question answering.
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
        # The name of the slot.
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
        # When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.dialog_name = dialog_name  # type: str
        # The passthrough parameters are returned.
        self.ext = ext  # type: dict[str, any]
        # When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.external_flags = external_flags  # type: dict[str, any]
        # The hit text.
        self.hit_statement = hit_statement  # type: str
        # When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.intent_name = intent_name  # type: str
        # The metadata.
        self.meta_data = meta_data  # type: str
        # When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.node_id = node_id  # type: str
        # When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
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
        # If the AnswerType parameter is set to Recommend, this parameter indicates the source of the recommended answer.
        self.answer_source = answer_source  # type: str
        # The type of the message.
        self.answer_type = answer_type  # type: str
        # When the AnswerType parameter is set to Knowledge, this parameter contains the Knowledge object returned by the bot.
        self.knowledge = knowledge  # type: BeeBotChatResponseBodyDataMessagesKnowledge
        # When the AnswerType parameter is set to Recommend, this parameter contains a list of recommends returned by the bot.
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
        # The list of the message.
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # If OK is returned, the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: BeeBotChatResponseBodyData
        # The error message.
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


class CreateChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        # The mobile phone number. This parameter is valid only if the Type parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number  # type: str
        # The display name of the button.
        self.text = text  # type: str
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: a phone call button
        # *   **URL**: a URL button
        # *   **QUICK_REPLY**: a quick reply button
        # 
        # > *   A quick reply button cannot coexist with a phone call button or a URL button in a message template.
        # > *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a message template.
        self.type = type  # type: str
        # The URL to be accessed when you click the URL button.
        self.url = url  # type: str
        # The type of the URL. Valid values:
        # 
        # *   **static**: a static URL
        # *   **dynamic**: a dynamic URL
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappTemplateRequestComponentsButtons, self).to_map()
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


class CreateChatappTemplateRequestComponents(TeaModel):
    def __init__(self, buttons=None, caption=None, file_name=None, format=None, text=None, type=None, url=None):
        # This parameter applies only to components of the **BUTTONS** type.
        self.buttons = buttons  # type: list[CreateChatappTemplateRequestComponentsButtons]
        # The description of the file.
        self.caption = caption  # type: str
        # The name of the file.
        self.file_name = file_name  # type: str
        # The format of the message.
        # 
        # *   **TEXT**: text
        # *   **IMGAGE**: image
        # *   **DOCUMENT**: document
        # *   **VIDEO**: video
        self.format = format  # type: str
        # The text of the message to be sent.
        self.text = text  # type: str
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # > A component of the **BODY** type cannot exceed 1,024 characters in length. A component of the **HEADER** or **FOOTER** type cannot exceed 60 characters in length.
        self.type = type  # type: str
        # The URL of the material.
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateChatappTemplateRequestComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.file_name is not None:
            result['FileName'] = self.file_name
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
                temp_model = CreateChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateChatappTemplateRequest(TeaModel):
    def __init__(self, category=None, components=None, cust_space_id=None, cust_waba_id=None, example=None,
                 isv_code=None, language=None, name=None, template_type=None):
        # The category of the message template. Valid values:
        # 
        # *   **ACCOUNT_UPDATE**: account update
        # *   **PAYMENT_UPDATE**: payment update
        # *   **PERSONAL_FINANCE\_UPDATE**: personal finance update
        # *   **SHIPPING_UPDATE**: traffic update
        # *   **RESERVATION_UPDATE**: reservation update
        # *   **ISSUE_RESOLUTION**: issue resolution
        # *   **APPOINTMENT_UPDATE**: appointment update
        # *   **TRANSPORTATION_UPDATE**: logistics information update
        # *   **TICKET_UPDATE**: ticket update
        # *   **ALERT_UPDATE**: alert update
        # *   **AUTO_REPLY**: auto reply
        self.category = category  # type: str
        # The components of the message template.
        self.components = components  # type: list[CreateChatappTemplateRequestComponents]
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example = example  # type: dict[str, str]
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The name of the message template.
        self.name = name  # type: str
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   VIBER (under development)
        # *   LINE (under development)
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
        if self.name is not None:
            result['Name'] = self.name
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, category=None, components_shrink=None, cust_space_id=None, cust_waba_id=None,
                 example_shrink=None, isv_code=None, language=None, name=None, template_type=None):
        # The category of the message template. Valid values:
        # 
        # *   **ACCOUNT_UPDATE**: account update
        # *   **PAYMENT_UPDATE**: payment update
        # *   **PERSONAL_FINANCE\_UPDATE**: personal finance update
        # *   **SHIPPING_UPDATE**: traffic update
        # *   **RESERVATION_UPDATE**: reservation update
        # *   **ISSUE_RESOLUTION**: issue resolution
        # *   **APPOINTMENT_UPDATE**: appointment update
        # *   **TRANSPORTATION_UPDATE**: logistics information update
        # *   **TICKET_UPDATE**: ticket update
        # *   **ALERT_UPDATE**: alert update
        # *   **AUTO_REPLY**: auto reply
        self.category = category  # type: str
        # The components of the message template.
        self.components_shrink = components_shrink  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The name of the message template.
        self.name = name  # type: str
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   VIBER (under development)
        # *   LINE (under development)
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChatappTemplateShrinkRequest, self).to_map()
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
        if self.name is not None:
            result['Name'] = self.name
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A code of OK indicates that the call is successful.
        # *   Other codes indicate that the call fails. For more information, see [Error codes](~~196974~~).
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


class DeleteChatappTemplateRequest(TeaModel):
    def __init__(self, cust_space_id=None, cust_waba_id=None, isv_code=None, template_code=None):
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
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
    def __init__(self, code=None, message=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A code of OK indicates that the call is successful.
        # *   Other codes indicate that the call fails. For more information, see [Error codes](~~196974~~).
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


class GetChatappTemplateDetailRequest(TeaModel):
    def __init__(self, cust_space_id=None, cust_waba_id=None, isv_code=None, language=None, template_code=None):
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str

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
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        # The mobile phone number. This parameter is valid only if the Type parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number  # type: str
        # The display name of the button.
        self.text = text  # type: str
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: a phone call button
        # *   **URL**: a URL button
        # *   **QUICK_REPLY**: a quick reply button
        # 
        # **\
        # 
        # **Note**\
        # 
        # *   A quick reply button cannot coexist with a phone call button or a URL button in a message template.
        # 
        # *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a message template.
        self.type = type  # type: str
        # The URL to be accessed when you click the URL button.
        self.url = url  # type: str
        # The type of the URL. Valid values:
        # 
        # *   **static**: a static URL
        # *   **dynamic**: a dynamic URL
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponentsButtons, self).to_map()
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


class GetChatappTemplateDetailResponseBodyDataComponents(TeaModel):
    def __init__(self, buttons=None, caption=None, file_name=None, format=None, text=None, type=None, url=None):
        # This parameter applies only to components of the **BUTTONS** type. This parameter is passed in by converting its original JSON structure into a string.
        self.buttons = buttons  # type: list[GetChatappTemplateDetailResponseBodyDataComponentsButtons]
        # The description of the file.
        self.caption = caption  # type: str
        # The name of the file.
        self.file_name = file_name  # type: str
        # The format.
        self.format = format  # type: str
        # The text of the message to be sent.
        self.text = text  # type: str
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # **\
        # 
        # **Note** A component of the **BODY** type cannot exceed 1,024 characters in length. A component of the **HEADER** or **FOOTER** type cannot exceed 60 characters in length.
        self.type = type  # type: str
        # The URL of the material.
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBodyDataComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.file_name is not None:
            result['FileName'] = self.file_name
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
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetChatappTemplateDetailResponseBodyData(TeaModel):
    def __init__(self, audit_status=None, category=None, components=None, example=None, language=None, name=None,
                 template_code=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        # The category of the message template. Valid values:
        # 
        # *   **ACCOUNT_UPDATE**: account update
        # *   **PAYMENT_UPDATE**: payment update
        # *   **PERSONAL_FINANCE\_UPDATE**: personal finance update
        # *   **SHIPPING_UPDATE**: traffic update
        # *   **RESERVATION_UPDATE**: reservation update
        # *   **ISSUE_RESOLUTION**: issue resolution
        # *   **APPOINTMENT_UPDATE**: appointment update
        # *   **TRANSPORTATION_UPDATE**: logistics information update
        # *   **TICKET_UPDATE**: ticket update
        # *   **ALERT_UPDATE**: alert update
        # *   **AUTO_REPLY**: auto reply
        self.category = category  # type: str
        # The components of the message template.
        self.components = components  # type: list[GetChatappTemplateDetailResponseBodyDataComponents]
        # The examples of variables.
        self.example = example  # type: dict[str, str]
        # The language that is used in the message template.
        self.language = language  # type: str
        # The name of the message template.
        self.name = name  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str

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
        if self.name is not None:
            result['Name'] = self.name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class GetChatappTemplateDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A code of OK indicates that the call is successful.
        # *   Other codes indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: GetChatappTemplateDetailResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetChatappTemplateDetailResponseBody, self).to_map()
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


class ListChatappTemplateRequestPage(TeaModel):
    def __init__(self, index=None, size=None):
        # The number of the page to return. Default value: 1.
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
                 name=None, page=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The name of the message template.
        self.name = name  # type: str
        # The paging settings.
        self.page = page  # type: ListChatappTemplateRequestPage

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
        return self


class ListChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, audit_status=None, cust_space_id=None, cust_waba_id=None, isv_code=None, language=None,
                 name=None, page_shrink=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The name of the message template.
        self.name = name  # type: str
        # The paging settings.
        self.page_shrink = page_shrink  # type: str

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
        return self


class ListChatappTemplateResponseBodyListTemplate(TeaModel):
    def __init__(self, audit_status=None, category=None, language=None, template_code=None, template_name=None):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status  # type: str
        # The category of the message template. Valid values:
        # 
        # *   **ACCOUNT_UPDATE**: account update
        # *   **PAYMENT_UPDATE**: payment update
        # *   **PERSONAL_FINANCE\_UPDATE**: personal finance update
        # *   **SHIPPING_UPDATE**: traffic update
        # *   **RESERVATION_UPDATE**: reservation update
        # *   **ISSUE_RESOLUTION**: issue resolution
        # *   **APPOINTMENT_UPDATE**: appointment update
        # *   **TRANSPORTATION_UPDATE**: logistics information update
        # *   **TICKET_UPDATE**: ticket update
        # *   **ALERT_UPDATE**: alert update
        # *   **AUTO_REPLY**: auto reply
        self.category = category  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The name of the message template.
        self.template_name = template_name  # type: str

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
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListChatappTemplateResponseBody(TeaModel):
    def __init__(self, code=None, list_template=None, message=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A code of OK indicates that the call is successful.
        # *   Other codes indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The message templates.
        self.list_template = list_template  # type: list[ListChatappTemplateResponseBodyListTemplate]
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
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


class ModifyChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        # The phone number.
        self.phone_number = phone_number  # type: str
        # The text of the message to be sent.
        self.text = text  # type: str
        # The type of the button.
        # 
        # *   **PHONE_NUMBER**: the phone call button
        # *   **URL**: the URL button
        # *   **QUICK_REPLY**: the quick reply button
        self.type = type  # type: str
        # The URL to be visited after clicking the button.
        self.url = url  # type: str
        # The type of the URL. Valid values:
        # 
        # *   **static**: the static URL
        # *   **dynamic**: the dynamic URL
        self.url_type = url_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyChatappTemplateRequestComponentsButtons, self).to_map()
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


class ModifyChatappTemplateRequestComponents(TeaModel):
    def __init__(self, buttons=None, caption=None, file_name=None, format=None, text=None, type=None, url=None):
        # The list of buttons, which applies only to the **BUTTONS** component.
        self.buttons = buttons  # type: list[ModifyChatappTemplateRequestComponentsButtons]
        # The description.
        # 
        # >  When the Type parameter is set to **HEADER** and the Format parameter is set to **IMAGE/DOCUMENT/VIDEO**, you can specify the description.
        self.caption = caption  # type: str
        # The name of the file.
        # 
        # > : When the Type parameter is set to **HEADER** and the Format parameter is set to **DOCUMENT**, you can specify a name of the file.
        self.file_name = file_name  # type: str
        # The type of the media resource.
        # 
        # *   **TEXT**: text
        # *   **IMAGE**: image
        # *   **DOCUMENT**: document
        # *   **VIDEO**: video
        self.format = format  # type: str
        # The text of the message to be sent.
        self.text = text  # type: str
        # The type of the component.
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        self.type = type  # type: str
        # The URL of the material.
        self.url = url  # type: str

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyChatappTemplateRequestComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.file_name is not None:
            result['FileName'] = self.file_name
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
                temp_model = ModifyChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyChatappTemplateRequest(TeaModel):
    def __init__(self, components=None, cust_space_id=None, cust_waba_id=None, example=None, isv_code=None,
                 language=None, template_code=None):
        # The list of components of the message template.
        self.components = components  # type: list[ModifyChatappTemplateRequestComponents]
        # Isv customer space id
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatApp Business account of the ISV customer.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example = example  # type: dict[str, str]
        # ISV verification code, which is used to verify whether the sub-account is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The language.
        self.language = language  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str

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
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class ModifyChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, components_shrink=None, cust_space_id=None, cust_waba_id=None, example_shrink=None,
                 isv_code=None, language=None, template_code=None):
        # The list of components of the message template.
        self.components_shrink = components_shrink  # type: str
        # Isv customer space id
        self.cust_space_id = cust_space_id  # type: str
        # The ID of the WhatApp Business account of the ISV customer.
        self.cust_waba_id = cust_waba_id  # type: str
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink  # type: str
        # ISV verification code, which is used to verify whether the sub-account is authorized by ISV.
        self.isv_code = isv_code  # type: str
        # The language.
        self.language = language  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyChatappTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class ModifyChatappTemplateResponseBodyData(TeaModel):
    def __init__(self, template_code=None, template_name=None):
        # The code of the message template.
        self.template_code = template_code  # type: str
        # The name of the template.
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other codes indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: ModifyChatappTemplateResponseBodyData
        # The error message.
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


class QueryChatappBindWabaRequest(TeaModel):
    def __init__(self, cust_space_id=None, isv_code=None):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id  # type: str
        # The ISV verification code, which is used to verify whether the user is authorized by ISV.
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
        # The audit status of the WhatApp Business account.
        self.account_review_status = account_review_status  # type: str
        # Currency
        self.currency = currency  # type: str
        # WabaID
        self.id = id  # type: str
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace  # type: str
        # The name of the WhatApp Business account.
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The returned data.
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
        # The ISV verification code, which is used to verify whether the user is authorized by ISV.
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
        # 号码校验状态。
        self.code_verification_status = code_verification_status  # type: str
        # 号码发送量。
        self.messaging_limit_tier = messaging_limit_tier  # type: str
        # 名称状态。
        self.name_status = name_status  # type: str
        # 新名称审核状态。
        self.new_name_status = new_name_status  # type: str
        # The phone number.
        self.phone_number = phone_number  # type: str
        # The quality rating of the phone number. Valid values: GREEN, YELLOW, RED, and UNKNOWN.
        self.quality_rating = quality_rating  # type: str
        # The status of the phone number. Valid values: PENDING, DELETED, MIGRATED, BANNED, RESTRICTED, RATE_LIMITED, FLAGGED, CONNECTED, DISCONNECTED, UNKNOWN, and UNVERIFIED.
        self.status = status  # type: str
        # The status report notification URL.
        self.status_callback_url = status_callback_url  # type: str
        # The status report notification queue.
        self.status_queue = status_queue  # type: str
        # The MO message notification URL.
        self.up_callback_url = up_callback_url  # type: str
        # The mobile originated (MO) message notification queue.
        self.up_queue = up_queue  # type: str
        # The name of the company to which the phone number is associated with.
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
    def __init__(self, code=None, message=None, phone_numbers=None, request_id=None):
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


class SendChatappMassMessageRequestSenderList(TeaModel):
    def __init__(self, payload=None, template_params=None, to=None):
        # Payload list.
        self.payload = payload  # type: list[str]
        # Template parameters.
        self.template_params = template_params  # type: dict[str, str]
        # Target number.
        self.to = to  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendChatappMassMessageRequestSenderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SendChatappMassMessageRequest(TeaModel):
    def __init__(self, channel_type=None, cust_space_id=None, cust_waba_id=None, fall_back_content=None,
                 fall_back_id=None, from_=None, isv_code=None, language=None, sender_list=None, task_id=None, template_code=None):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   viber (under development)
        # *   line (under development)
        self.channel_type = channel_type  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Fallback message content.
        self.fall_back_content = fall_back_content  # type: str
        # Fallback strategy id. Fallback Strategy can be created on the ChatApp console.
        self.fall_back_id = fall_back_id  # type: str
        # The mobile phone number of the message sender.
        # 
        # <notice>You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatApp console.</notice>
        self.from_ = from_  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # Target number and parameter list.
        self.sender_list = sender_list  # type: list[SendChatappMassMessageRequestSenderList]
        # User-define ID to identify a single batch of messages.
        self.task_id = task_id  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str

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
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        result['SenderList'] = []
        if self.sender_list is not None:
            for k in self.sender_list:
                result['SenderList'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
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
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        self.sender_list = []
        if m.get('SenderList') is not None:
            for k in m.get('SenderList'):
                temp_model = SendChatappMassMessageRequestSenderList()
                self.sender_list.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class SendChatappMassMessageShrinkRequest(TeaModel):
    def __init__(self, channel_type=None, cust_space_id=None, cust_waba_id=None, fall_back_content=None,
                 fall_back_id=None, from_=None, isv_code=None, language=None, sender_list_shrink=None, task_id=None,
                 template_code=None):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   viber (under development)
        # *   line (under development)
        self.channel_type = channel_type  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Fallback message content.
        self.fall_back_content = fall_back_content  # type: str
        # Fallback strategy id. Fallback Strategy can be created on the ChatApp console.
        self.fall_back_id = fall_back_id  # type: str
        # The mobile phone number of the message sender.
        # 
        # <notice>You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatApp console.</notice>
        self.from_ = from_  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # Target number and parameter list.
        self.sender_list_shrink = sender_list_shrink  # type: str
        # User-define ID to identify a single batch of messages.
        self.task_id = task_id  # type: str
        # The code of the message template.
        self.template_code = template_code  # type: str

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
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.sender_list_shrink is not None:
            result['SenderList'] = self.sender_list_shrink
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
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
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SenderList') is not None:
            self.sender_list_shrink = m.get('SenderList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class SendChatappMassMessageResponseBody(TeaModel):
    def __init__(self, code=None, group_message_id=None, message=None, request_id=None):
        # The HTTP status code returned.
        # 
        # *   A code of OK indicates that the call is successful.
        # *   Other codes indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # Batch send message ID.
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


class SendChatappMessageRequest(TeaModel):
    def __init__(self, channel_type=None, content=None, context_message_id=None, cust_space_id=None,
                 cust_waba_id=None, fall_back_content=None, fall_back_id=None, from_=None, isv_code=None, label=None,
                 language=None, message_type=None, payload=None, tag=None, template_code=None, template_params=None, to=None,
                 tracking_data=None, ttl=None, type=None):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   viber (under development)
        # *   line (under development)
        self.channel_type = channel_type  # type: str
        # The content of the message.
        # 
        # **\
        # 
        # **Note** The **Content** parameter is required if you set the **Type** parameter to **message**.
        self.content = content  # type: str
        self.context_message_id = context_message_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Fallback message content.
        self.fall_back_content = fall_back_content  # type: str
        # Fallback strategy id. Fallback Strategy can be created on the ChatApp console.
        self.fall_back_id = fall_back_id  # type: str
        # The mobile phone number of the message sender.
        # 
        # <notice>You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatApp console.</notice>
        self.from_ = from_  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        self.label = label  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The type of the message. This parameter is required if you set the Type parameter to **message**. Valid values:
        # 
        # *   **text**: a text message. The **Text** parameter is required if you set the MessageType parameter to text.
        # *   **image**: an image message. The **Link** parameter is required and the **Caption** parameter is optional if you set the MessageType parameter to image.
        # *   **video**: a video message. The **Link** parameter is required and the **Caption** parameter is optional if you set the MessageType parameter to video.
        # *   **audio**: an audio message. The **Link** parameter is required and the **Caption** parameter is invalid if you set the MessageType parameter to audio.
        # *   **document**: a document message. The **Link** and **FileName** parameters are required and the **Caption** parameter is invalid if you set the MessageType parameter to document.
        self.message_type = message_type  # type: str
        # The payload of the button.
        self.payload = payload  # type: list[str]
        self.tag = tag  # type: str
        # The code of the message template. This parameter is required if you set the Type parameter to **template**.
        self.template_code = template_code  # type: str
        # The variables of the message template.
        self.template_params = template_params  # type: dict[str, str]
        # The mobile phone number of the message recipient.
        self.to = to  # type: str
        self.tracking_data = tracking_data  # type: str
        self.ttl = ttl  # type: int
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatApp console and is approved. You can send template messages based on your business requirements.
        # *   **message**: a custom message. You can send a custom message to a user only within 24 hours after you receive the last message from the user.
        self.type = type  # type: str

    def validate(self):
        pass

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
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
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
        if self.tag is not None:
            result['Tag'] = self.tag
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
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
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
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
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
                 cust_waba_id=None, fall_back_content=None, fall_back_id=None, from_=None, isv_code=None, label=None,
                 language=None, message_type=None, payload_shrink=None, tag=None, template_code=None,
                 template_params_shrink=None, to=None, tracking_data=None, ttl=None, type=None):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   viber (under development)
        # *   line (under development)
        self.channel_type = channel_type  # type: str
        # The content of the message.
        # 
        # **\
        # 
        # **Note** The **Content** parameter is required if you set the **Type** parameter to **message**.
        self.content = content  # type: str
        self.context_message_id = context_message_id  # type: str
        self.cust_space_id = cust_space_id  # type: str
        # The unique identifier of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id  # type: str
        # Fallback message content.
        self.fall_back_content = fall_back_content  # type: str
        # Fallback strategy id. Fallback Strategy can be created on the ChatApp console.
        self.fall_back_id = fall_back_id  # type: str
        # The mobile phone number of the message sender.
        # 
        # <notice>You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatApp console.</notice>
        self.from_ = from_  # type: str
        # Assigned by ISV for RAM user authentication and authorization.
        self.isv_code = isv_code  # type: str
        self.label = label  # type: str
        # The language that is used in the message template.
        self.language = language  # type: str
        # The type of the message. This parameter is required if you set the Type parameter to **message**. Valid values:
        # 
        # *   **text**: a text message. The **Text** parameter is required if you set the MessageType parameter to text.
        # *   **image**: an image message. The **Link** parameter is required and the **Caption** parameter is optional if you set the MessageType parameter to image.
        # *   **video**: a video message. The **Link** parameter is required and the **Caption** parameter is optional if you set the MessageType parameter to video.
        # *   **audio**: an audio message. The **Link** parameter is required and the **Caption** parameter is invalid if you set the MessageType parameter to audio.
        # *   **document**: a document message. The **Link** and **FileName** parameters are required and the **Caption** parameter is invalid if you set the MessageType parameter to document.
        self.message_type = message_type  # type: str
        # The payload of the button.
        self.payload_shrink = payload_shrink  # type: str
        self.tag = tag  # type: str
        # The code of the message template. This parameter is required if you set the Type parameter to **template**.
        self.template_code = template_code  # type: str
        # The variables of the message template.
        self.template_params_shrink = template_params_shrink  # type: str
        # The mobile phone number of the message recipient.
        self.to = to  # type: str
        self.tracking_data = tracking_data  # type: str
        self.ttl = ttl  # type: int
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatApp console and is approved. You can send template messages based on your business requirements.
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
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
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
        if self.tag is not None:
            result['Tag'] = self.tag
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
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
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
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
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
        # *   A code of OK indicates that the call is successful.
        # *   Other codes indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The ID of the message.
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


