# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class SendMessageRequest(TeaModel):
    def __init__(self, group_id=None, out_ids=None, phone_numbers=None, schedule_id=None, sign_name=None,
                 signature_id=None, sms_up_extend_codes=None, template_code=None, template_id=None, template_params=None):
        # 人群ID，用于关联人群。
        self.group_id = group_id  # type: str
        # 外部拓展字段。
        self.out_ids = out_ids  # type: list[str]
        # 手机号，每个手机号对应一个模板变量、上行拓展码和外部拓展字段。
        self.phone_numbers = phone_numbers  # type: list[str]
        # 发送计划ID，用于关联发送计划。
        self.schedule_id = schedule_id  # type: str
        # 签名名称。
        self.sign_name = sign_name  # type: str
        # 签名ID，同时只能指定签名名称或签名ID其中之一。
        self.signature_id = signature_id  # type: str
        # 短信上行拓展码。
        self.sms_up_extend_codes = sms_up_extend_codes  # type: list[str]
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板ID，同时只能指定模板Code或模板ID其中之一。
        self.template_id = template_id  # type: str
        # 短信模板变量对应的实际值，JSON格式。支持传入多个参数，示例：{"name":"张三","number":"15038****76"}。
        self.template_params = template_params  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.out_ids is not None:
            result['OutIds'] = self.out_ids
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.sms_up_extend_codes is not None:
            result['SmsUpExtendCodes'] = self.sms_up_extend_codes
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OutIds') is not None:
            self.out_ids = m.get('OutIds')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SmsUpExtendCodes') is not None:
            self.sms_up_extend_codes = m.get('SmsUpExtendCodes')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None):
        # 返回数据
        self.data = data  # type: str
        # 错误码
        self.error_code = error_code  # type: int
        # 错误信息
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class SendMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMessageResponse, self).to_map()
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


