# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class RecognizeDrivingLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDrivingLicenseRequest, self).to_map()
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


class RecognizeDrivingLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeDrivingLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeDrivingLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponse, self).to_map()
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
            temp_model = RecognizeDrivingLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeKoreanRequest(TeaModel):
    def __init__(self, url=None, output_char_info=None, need_rotate=None, output_table=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeKoreanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        return self


class RecognizeKoreanResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeKoreanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeKoreanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeKoreanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeKoreanResponse, self).to_map()
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
            temp_model = RecognizeKoreanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCarInvoiceRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarInvoiceRequest, self).to_map()
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


class RecognizeCarInvoiceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarInvoiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeCarInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeCarInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCarInvoiceResponse, self).to_map()
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
            temp_model = RecognizeCarInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMixedInvoicesRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMixedInvoicesRequest, self).to_map()
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


class RecognizeMixedInvoicesResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMixedInvoicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeMixedInvoicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeMixedInvoicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMixedInvoicesResponse, self).to_map()
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
            temp_model = RecognizeMixedInvoicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEstateCertificationRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEstateCertificationRequest, self).to_map()
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


class RecognizeEstateCertificationResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEstateCertificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEstateCertificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEstateCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEstateCertificationResponse, self).to_map()
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
            temp_model = RecognizeEstateCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCarNumberRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarNumberRequest, self).to_map()
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


class RecognizeCarNumberResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeCarNumberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeCarNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCarNumberResponse, self).to_map()
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
            temp_model = RecognizeCarNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduPaperOcrRequest(TeaModel):
    def __init__(self, url=None, image_type=None, subject=None, output_oricoord=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 图片类型
        self.image_type = image_type  # type: str
        # 年级学科
        self.subject = subject  # type: str
        # 是否输出原图坐标信息(如果图片被做过旋转，图片校正等处理)
        self.output_oricoord = output_oricoord  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperOcrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.output_oricoord is not None:
            result['OutputOricoord'] = self.output_oricoord
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('OutputOricoord') is not None:
            self.output_oricoord = m.get('OutputOricoord')
        return self


class RecognizeEduPaperOcrResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperOcrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEduPaperOcrResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEduPaperOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduPaperOcrResponse, self).to_map()
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
            temp_model = RecognizeEduPaperOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTradeMarkCertificationRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTradeMarkCertificationRequest, self).to_map()
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


class RecognizeTradeMarkCertificationResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTradeMarkCertificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeTradeMarkCertificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTradeMarkCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTradeMarkCertificationResponse, self).to_map()
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
            temp_model = RecognizeTradeMarkCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBirthCertificationRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBirthCertificationRequest, self).to_map()
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


class RecognizeBirthCertificationResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBirthCertificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeBirthCertificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBirthCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBirthCertificationResponse, self).to_map()
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
            temp_model = RecognizeBirthCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDoctypeRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDoctypeRequest, self).to_map()
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


class RecognizeDoctypeResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDoctypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeDoctypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeDoctypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeDoctypeResponse, self).to_map()
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
            temp_model = RecognizeDoctypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankAccountLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankAccountLicenseRequest, self).to_map()
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


class RecognizeBankAccountLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankAccountLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeBankAccountLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBankAccountLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBankAccountLicenseResponse, self).to_map()
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
            temp_model = RecognizeBankAccountLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFoodManageLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodManageLicenseRequest, self).to_map()
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


class RecognizeFoodManageLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodManageLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeFoodManageLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeFoodManageLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeFoodManageLicenseResponse, self).to_map()
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
            temp_model = RecognizeFoodManageLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeRollTicketRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRollTicketRequest, self).to_map()
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


class RecognizeRollTicketResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRollTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeRollTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeRollTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeRollTicketResponse, self).to_map()
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
            temp_model = RecognizeRollTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduFormulaRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（不支持 base64）,图片最大尺寸 1024*1024
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduFormulaRequest, self).to_map()
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


class RecognizeEduFormulaResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduFormulaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEduFormulaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEduFormulaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduFormulaResponse, self).to_map()
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
            temp_model = RecognizeEduFormulaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePassportRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePassportRequest, self).to_map()
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


class RecognizePassportResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePassportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizePassportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizePassportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizePassportResponse, self).to_map()
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
            temp_model = RecognizePassportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTaxiInvoiceRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceRequest, self).to_map()
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


class RecognizeTaxiInvoiceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeTaxiInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTaxiInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponse, self).to_map()
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
            temp_model = RecognizeTaxiInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFoodProduceLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodProduceLicenseRequest, self).to_map()
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


class RecognizeFoodProduceLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodProduceLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeFoodProduceLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeFoodProduceLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeFoodProduceLicenseResponse, self).to_map()
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
            temp_model = RecognizeFoodProduceLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMedicalDeviceProduceLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceProduceLicenseRequest, self).to_map()
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


class RecognizeMedicalDeviceProduceLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceProduceLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeMedicalDeviceProduceLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeMedicalDeviceProduceLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMedicalDeviceProduceLicenseResponse, self).to_map()
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
            temp_model = RecognizeMedicalDeviceProduceLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHandwritingRequest(TeaModel):
    def __init__(self, url=None, output_char_info=None, need_rotate=None, output_table=None, need_sort_page=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool
        # 是否按顺序输出文字块。false表示从左往右，从上到下的顺序；true表示从上到下，从左往右的顺序
        self.need_sort_page = need_sort_page  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHandwritingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        return self


class RecognizeHandwritingResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHandwritingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeHandwritingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeHandwritingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHandwritingResponse, self).to_map()
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
            temp_model = RecognizeHandwritingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeAirItineraryRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAirItineraryRequest, self).to_map()
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


class RecognizeAirItineraryResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAirItineraryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeAirItineraryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeAirItineraryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeAirItineraryResponse, self).to_map()
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
            temp_model = RecognizeAirItineraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeJanpaneseRequest(TeaModel):
    def __init__(self, url=None, output_char_info=None, need_rotate=None, output_table=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeJanpaneseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        return self


class RecognizeJanpaneseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeJanpaneseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeJanpaneseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeJanpaneseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeJanpaneseResponse, self).to_map()
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
            temp_model = RecognizeJanpaneseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCtwoMedicalDeviceManageLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCtwoMedicalDeviceManageLicenseRequest, self).to_map()
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


class RecognizeCtwoMedicalDeviceManageLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCtwoMedicalDeviceManageLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeCtwoMedicalDeviceManageLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeCtwoMedicalDeviceManageLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCtwoMedicalDeviceManageLicenseResponse, self).to_map()
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
            temp_model = RecognizeCtwoMedicalDeviceManageLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeThaiRequest(TeaModel):
    def __init__(self, url=None, output_char_info=None, need_rotate=None, output_table=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeThaiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        return self


class RecognizeThaiResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeThaiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeThaiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeThaiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeThaiResponse, self).to_map()
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
            temp_model = RecognizeThaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMedicalDeviceManageLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceManageLicenseRequest, self).to_map()
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


class RecognizeMedicalDeviceManageLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceManageLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeMedicalDeviceManageLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeMedicalDeviceManageLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMedicalDeviceManageLicenseResponse, self).to_map()
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
            temp_model = RecognizeMedicalDeviceManageLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeLatinRequest(TeaModel):
    def __init__(self, url=None, output_char_info=None, need_rotate=None, output_table=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeLatinRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        return self


class RecognizeLatinResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeLatinResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeLatinResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeLatinResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeLatinResponse, self).to_map()
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
            temp_model = RecognizeLatinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeInvoiceRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInvoiceRequest, self).to_map()
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


class RecognizeInvoiceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInvoiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeInvoiceResponse, self).to_map()
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
            temp_model = RecognizeInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMixedCardsRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMixedCardsRequest, self).to_map()
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


class RecognizeMixedCardsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMixedCardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeMixedCardsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeMixedCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMixedCardsResponse, self).to_map()
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
            temp_model = RecognizeMixedCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeWaybillRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeWaybillRequest, self).to_map()
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


class RecognizeWaybillResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeWaybillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeWaybillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeWaybillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeWaybillResponse, self).to_map()
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
            temp_model = RecognizeWaybillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCarVinCodeRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarVinCodeRequest, self).to_map()
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


class RecognizeCarVinCodeResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarVinCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeCarVinCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeCarVinCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCarVinCodeResponse, self).to_map()
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
            temp_model = RecognizeCarVinCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeAdvancedRequest(TeaModel):
    def __init__(self, url=None, output_char_info=None, need_rotate=None, output_table=None, need_sort_page=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool
        # 是否按顺序输出文字块。false表示从左往右，从上到下的顺序；true表示从上到下，从左往右的顺序
        self.need_sort_page = need_sort_page  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAdvancedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        return self


class RecognizeAdvancedResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        # 请求唯一 ID
        self.request_id = request_id  # type: str
        # 返回数据
        self.data = data  # type: str
        # 错误码
        self.code = code  # type: str
        # 错误提示
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAdvancedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeAdvancedResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeAdvancedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeAdvancedResponse, self).to_map()
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
            temp_model = RecognizeAdvancedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleLicenseRequest, self).to_map()
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


class RecognizeVehicleLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeVehicleLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeVehicleLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVehicleLicenseResponse, self).to_map()
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
            temp_model = RecognizeVehicleLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeRussianRequest(TeaModel):
    def __init__(self, url=None, output_char_info=None, need_rotate=None, output_table=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRussianRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        return self


class RecognizeRussianResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRussianResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeRussianResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeRussianResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeRussianResponse, self).to_map()
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
            temp_model = RecognizeRussianResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHouseCertificationRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHouseCertificationRequest, self).to_map()
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


class RecognizeHouseCertificationResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHouseCertificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeHouseCertificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeHouseCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHouseCertificationResponse, self).to_map()
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
            temp_model = RecognizeHouseCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBasicRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBasicRequest, self).to_map()
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


class RecognizeBasicResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBasicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeBasicResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBasicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBasicResponse, self).to_map()
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
            temp_model = RecognizeBasicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessLicenseRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseRequest, self).to_map()
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


class RecognizeBusinessLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeBusinessLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBusinessLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponse, self).to_map()
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
            temp_model = RecognizeBusinessLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankCardRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankCardRequest, self).to_map()
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


class RecognizeBankCardResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeBankCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBankCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBankCardResponse, self).to_map()
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
            temp_model = RecognizeBankCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduPaperCutRequest(TeaModel):
    def __init__(self, url=None, cut_type=None, image_type=None, subject=None, output_oricoord=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 切题类型
        self.cut_type = cut_type  # type: str
        # 图片类型
        self.image_type = image_type  # type: str
        # 年级学科
        self.subject = subject  # type: str
        # 是否输出原图坐标信息(如果图片被做过旋转，图片校正等处理)
        self.output_oricoord = output_oricoord  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperCutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.cut_type is not None:
            result['CutType'] = self.cut_type
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.output_oricoord is not None:
            result['OutputOricoord'] = self.output_oricoord
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('CutType') is not None:
            self.cut_type = m.get('CutType')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('OutputOricoord') is not None:
            self.output_oricoord = m.get('OutputOricoord')
        return self


class RecognizeEduPaperCutResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperCutResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEduPaperCutResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEduPaperCutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduPaperCutResponse, self).to_map()
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
            temp_model = RecognizeEduPaperCutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHouseholdRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHouseholdRequest, self).to_map()
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


class RecognizeHouseholdResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHouseholdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeHouseholdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeHouseholdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHouseholdResponse, self).to_map()
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
            temp_model = RecognizeHouseholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduQuestionOcrRequest(TeaModel):
    def __init__(self, url=None, need_rotate=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduQuestionOcrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        return self


class RecognizeEduQuestionOcrResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduQuestionOcrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEduQuestionOcrResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEduQuestionOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduQuestionOcrResponse, self).to_map()
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
            temp_model = RecognizeEduQuestionOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTrainInvoiceRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTrainInvoiceRequest, self).to_map()
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


class RecognizeTrainInvoiceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTrainInvoiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeTrainInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTrainInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTrainInvoiceResponse, self).to_map()
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
            temp_model = RecognizeTrainInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTableOcrRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTableOcrRequest, self).to_map()
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


class RecognizeTableOcrResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTableOcrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeTableOcrResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTableOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTableOcrResponse, self).to_map()
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
            temp_model = RecognizeTableOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEnglishRequest(TeaModel):
    def __init__(self, url=None, need_rotate=None, output_table=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEnglishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        return self


class RecognizeEnglishResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEnglishResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEnglishResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEnglishResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEnglishResponse, self).to_map()
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
            temp_model = RecognizeEnglishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMultiLanguageRequest(TeaModel):
    def __init__(self, url=None, languages=None, output_char_info=None, need_rotate=None, output_table=None,
                 need_sort_page=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 识别语种
        self.languages = languages  # type: list[str]
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool
        # 是否按顺序输出文字块。false表示从左往右，从上到下的顺序；true表示从上到下，从左往右的顺序
        self.need_sort_page = need_sort_page  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMultiLanguageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.languages is not None:
            result['Languages'] = self.languages
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Languages') is not None:
            self.languages = m.get('Languages')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        return self


class RecognizeMultiLanguageShrinkRequest(TeaModel):
    def __init__(self, url=None, languages_shrink=None, output_char_info=None, need_rotate=None, output_table=None,
                 need_sort_page=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 识别语种
        self.languages_shrink = languages_shrink  # type: str
        # 是否输出单字识别结果
        self.output_char_info = output_char_info  # type: bool
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool
        # 是否输出表格识别结果，包含单元格信息
        self.output_table = output_table  # type: bool
        # 是否按顺序输出文字块。false表示从左往右，从上到下的顺序；true表示从上到下，从左往右的顺序
        self.need_sort_page = need_sort_page  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMultiLanguageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.languages_shrink is not None:
            result['Languages'] = self.languages_shrink
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Languages') is not None:
            self.languages_shrink = m.get('Languages')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        return self


class RecognizeMultiLanguageResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMultiLanguageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeMultiLanguageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeMultiLanguageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMultiLanguageResponse, self).to_map()
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
            temp_model = RecognizeMultiLanguageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduOralCalculationRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduOralCalculationRequest, self).to_map()
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


class RecognizeEduOralCalculationResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduOralCalculationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEduOralCalculationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEduOralCalculationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduOralCalculationResponse, self).to_map()
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
            temp_model = RecognizeEduOralCalculationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQuotaInvoiceRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceRequest, self).to_map()
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


class RecognizeQuotaInvoiceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeQuotaInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeQuotaInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponse, self).to_map()
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
            temp_model = RecognizeQuotaInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeGeneralRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeGeneralRequest, self).to_map()
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


class RecognizeGeneralResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeGeneralResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeGeneralResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeGeneralResponse, self).to_map()
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
            temp_model = RecognizeGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduPaperStructedRequest(TeaModel):
    def __init__(self, url=None, need_rotate=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str
        # 是否需要自动旋转功能(结构化检测、混贴场景、教育相关场景会自动做旋转，无需设置)，返回角度信息
        self.need_rotate = need_rotate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperStructedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        return self


class RecognizeEduPaperStructedResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperStructedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeEduPaperStructedResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeEduPaperStructedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduPaperStructedResponse, self).to_map()
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
            temp_model = RecognizeEduPaperStructedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeIdcardRequest(TeaModel):
    def __init__(self, url=None):
        # 图片链接（长度不超 1014，不支持 base64）
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdcardRequest, self).to_map()
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


class RecognizeIdcardResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, message=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdcardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecognizeIdcardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeIdcardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeIdcardResponse, self).to_map()
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
            temp_model = RecognizeIdcardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


