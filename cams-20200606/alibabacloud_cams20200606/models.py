# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CheckChatappContactsRequest(TeaModel):
    def __init__(self, channel_type=None, contacts=None, cust_waba_id=None, from_=None):
        # 通道类型
        self.channel_type = channel_type  # type: str
        # 需要查询的用户列表,单次调用最多查询10个。注意：用户号码必须加国家码
        self.contacts = contacts  # type: list[str]
        # ISV客户wabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 发送号码,所选择ChannelType下的Business账号，即在控制台上审核通过的Number
        self.from_ = from_  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckChatappContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.contacts is not None:
            result['Contacts'] = self.contacts
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.from_ is not None:
            result['From'] = self.from_
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        return self


class CheckChatappContactsShrinkRequest(TeaModel):
    def __init__(self, channel_type=None, contacts_shrink=None, cust_waba_id=None, from_=None):
        # 通道类型
        self.channel_type = channel_type  # type: str
        # 需要查询的用户列表,单次调用最多查询10个。注意：用户号码必须加国家码
        self.contacts_shrink = contacts_shrink  # type: str
        # ISV客户wabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 发送号码,所选择ChannelType下的Business账号，即在控制台上审核通过的Number
        self.from_ = from_  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckChatappContactsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.contacts_shrink is not None:
            result['Contacts'] = self.contacts_shrink
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.from_ is not None:
            result['From'] = self.from_
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Contacts') is not None:
            self.contacts_shrink = m.get('Contacts')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        return self


class CheckChatappContactsResponseBodyData(TeaModel):
    def __init__(self, phone_number=None, status=None):
        # 号码
        self.phone_number = phone_number  # type: str
        # 状态
        # 有效账号为"valid"，无法账号为"invalid"，查询失败返回"failed"
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckChatappContactsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckChatappContactsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # 返回结果 OK 为正常
        self.code = code  # type: str
        self.data = data  # type: list[CheckChatappContactsResponseBodyData]
        # 提示信息，当返回异常时有值
        self.message = message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckChatappContactsResponseBody, self).to_map()
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
                temp_model = CheckChatappContactsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckChatappContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckChatappContactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckChatappContactsResponse, self).to_map()
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
            temp_model = CheckChatappContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        # 号码
        self.phone_number = phone_number  # type: str
        # 所发送消息的文本
        self.text = text  # type: str
        # 按钮类型
        # PHONE_NUMBER（电话）,URL（网页按钮）和QUICK_REPLY（快速回复）
        self.type = type  # type: str
        # 点击按钮后将访问的网址
        self.url = url  # type: str
        # 网址类型 static-静态dynamic-动态
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
        # 按钮
        self.buttons = buttons  # type: list[CreateChatappTemplateRequestComponentsButtons]
        # 描述，当Type为Header，且Format为IMGAGE/DOCUMENT/VIDEO 可以增加描述
        self.caption = caption  # type: str
        # 文件名称，当Type为Header，且Format为DOCUMENT时可以给文件指定名称
        self.file_name = file_name  # type: str
        # 格式
        # TEXT-文本 IMGAGE-图片 DOCUMENT-文档 VIDEO-视频
        self.format = format  # type: str
        # 所发送消息的文本
        self.text = text  # type: str
        # 组件类型
        # 值：BODY、HEADER、FOOTER 和 BUTTONS
        self.type = type  # type: str
        # 素材路径
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
    def __init__(self, category=None, components=None, cust_waba_id=None, example=None, language=None, name=None,
                 template_type=None):
        # 模板分类
        self.category = category  # type: str
        self.components = components  # type: list[CreateChatappTemplateRequestComponents]
        # ISV客户WabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 变量，KEY-VALUE结构
        self.example = example  # type: dict[str, str]
        # 语言
        self.language = language  # type: str
        # 模板名称
        self.name = name  # type: str
        # 模板类型
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
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example is not None:
            result['Example'] = self.example
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
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, category=None, components_shrink=None, cust_waba_id=None, example_shrink=None, language=None,
                 name=None, template_type=None):
        # 模板分类
        self.category = category  # type: str
        self.components_shrink = components_shrink  # type: str
        # ISV客户WabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 变量，KEY-VALUE结构
        self.example_shrink = example_shrink  # type: str
        # 语言
        self.language = language  # type: str
        # 模板名称
        self.name = name  # type: str
        # 模板类型
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
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example_shrink is not None:
            result['Example'] = self.example_shrink
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
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateResponseBodyData(TeaModel):
    def __init__(self, template_code=None, template_name=None):
        # 模板Code
        self.template_code = template_code  # type: str
        # 模板名称
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
        # 返回结果 OK 为正常
        self.code = code  # type: str
        self.data = data  # type: CreateChatappTemplateResponseBodyData
        # 提示信息，当返回异常时有值
        self.message = message  # type: str
        # 请求ID
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
    def __init__(self, cust_waba_id=None, template_code=None):
        # ISV客户wabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 模板编码
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChatappTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DeleteChatappTemplateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        # 返回结果 OK 为正常
        self.code = code  # type: str
        # 提示信息，当返回异常时有值
        self.message = message  # type: str
        # 请求ID
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
    def __init__(self, cust_waba_id=None, language=None, template_code=None):
        # ISV客户WabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 语言
        self.language = language  # type: str
        # 模板分类
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChatappTemplateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.language is not None:
            result['Language'] = self.language
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtons(TeaModel):
    def __init__(self, phone_number=None, text=None, type=None, url=None, url_type=None):
        # 电话号码
        self.phone_number = phone_number  # type: str
        # 所发送消息的文本
        self.text = text  # type: str
        # 按钮类型
        self.type = type  # type: str
        # 当按钮类型是
        # URL 时有效
        self.url = url  # type: str
        # WEB地址类型
        # static-静态
        # dynamic-动态
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
        # 仅适用于 BUTTONS 类型。
        # 与按钮相关的参数。
        self.buttons = buttons  # type: list[GetChatappTemplateDetailResponseBodyDataComponentsButtons]
        # 描述，当Type为Header，且Format为IMGAGE/DOCUMENT/VIDEO 可以增加描述
        self.caption = caption  # type: str
        # 文件名称，当Type为Header，且Format为DOCUMENT时可以给文件指定名称
        self.file_name = file_name  # type: str
        # 格式
        self.format = format  # type: str
        # 所发送消息的文本
        self.text = text  # type: str
        # 组件类型
        self.type = type  # type: str
        # 素材路径
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
        # 审核状态
        self.audit_status = audit_status  # type: str
        # 模板分类
        self.category = category  # type: str
        # 消息模板组件
        self.components = components  # type: list[GetChatappTemplateDetailResponseBodyDataComponents]
        # 变量例子
        self.example = example  # type: dict[str, str]
        # 语言
        self.language = language  # type: str
        # 模板名称
        self.name = name  # type: str
        # 模板编码
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
        # 返回结果 OK 为正常
        self.code = code  # type: str
        # TemplateDetail
        self.data = data  # type: GetChatappTemplateDetailResponseBodyData
        self.message = message  # type: str
        # 请求ID
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
        # 查询开始数
        self.index = index  # type: int
        # 每次查询返回的条数
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
    def __init__(self, audit_status=None, cust_waba_id=None, language=None, name=None, page=None):
        # 审核状态
        self.audit_status = audit_status  # type: str
        # ISV客户WabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 语言
        self.language = language  # type: str
        # 模板名称
        self.name = name  # type: str
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
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
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
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            temp_model = ListChatappTemplateRequestPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListChatappTemplateShrinkRequest(TeaModel):
    def __init__(self, audit_status=None, cust_waba_id=None, language=None, name=None, page_shrink=None):
        # 审核状态
        self.audit_status = audit_status  # type: str
        # ISV客户WabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 语言
        self.language = language  # type: str
        # 模板名称
        self.name = name  # type: str
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
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
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
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        return self


class ListChatappTemplateResponseBodyListTemplate(TeaModel):
    def __init__(self, audit_status=None, category=None, language=None, template_code=None, template_name=None):
        # 审核状态
        self.audit_status = audit_status  # type: str
        # 模板分类
        self.category = category  # type: str
        # 语言
        self.language = language  # type: str
        # 模板编码
        self.template_code = template_code  # type: str
        # 模板名称
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
        self.code = code  # type: str
        # 模板列表
        self.list_template = list_template  # type: list[ListChatappTemplateResponseBodyListTemplate]
        self.message = message  # type: str
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


class SendChatappMessageRequest(TeaModel):
    def __init__(self, channel_type=None, content=None, cust_waba_id=None, fall_back_content=None,
                 fall_back_id=None, from_=None, language=None, message_type=None, payload=None, template_code=None,
                 template_params=None, to=None, type=None):
        # 通道类型 whatsapp/viber/line
        self.channel_type = channel_type  # type: str
        # 消息内容
        self.content = content  # type: str
        # ISV客户wabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 回落消息内容
        self.fall_back_content = fall_back_content  # type: str
        # 回落策略ID，可在控制台创建策略并查看
        self.fall_back_id = fall_back_id  # type: str
        # 发送方
        self.from_ = from_  # type: str
        # 语言
        self.language = language  # type: str
        # 消息类型
        self.message_type = message_type  # type: str
        self.payload = payload  # type: list[str]
        # 模板编码
        self.template_code = template_code  # type: str
        self.template_params = template_params  # type: dict[str, str]
        # 接收号码
        self.to = to  # type: str
        # 消息大类
        # template--模板
        # message--非模板
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
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageShrinkRequest(TeaModel):
    def __init__(self, channel_type=None, content=None, cust_waba_id=None, fall_back_content=None,
                 fall_back_id=None, from_=None, language=None, message_type=None, payload_shrink=None, template_code=None,
                 template_params_shrink=None, to=None, type=None):
        # 通道类型 whatsapp/viber/line
        self.channel_type = channel_type  # type: str
        # 消息内容
        self.content = content  # type: str
        # ISV客户wabaId
        self.cust_waba_id = cust_waba_id  # type: str
        # 回落消息内容
        self.fall_back_content = fall_back_content  # type: str
        # 回落策略ID，可在控制台创建策略并查看
        self.fall_back_id = fall_back_id  # type: str
        # 发送方
        self.from_ = from_  # type: str
        # 语言
        self.language = language  # type: str
        # 消息类型
        self.message_type = message_type  # type: str
        self.payload_shrink = payload_shrink  # type: str
        # 模板编码
        self.template_code = template_code  # type: str
        self.template_params_shrink = template_params_shrink  # type: str
        # 接收号码
        self.to = to  # type: str
        # 消息大类
        # template--模板
        # message--非模板
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
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params_shrink is not None:
            result['TemplateParams'] = self.template_params_shrink
        if self.to is not None:
            result['To'] = self.to
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params_shrink = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, message_id=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # 消息ID
        self.message_id = message_id  # type: str
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


