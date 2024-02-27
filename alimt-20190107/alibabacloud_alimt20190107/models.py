# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class TranslateECommerceRequest(TeaModel):
    def __init__(self, format_type=None, scene=None, source_language=None, source_text=None, target_language=None):
        self.format_type = format_type  # type: str
        self.scene = scene  # type: str
        self.source_language = source_language  # type: str
        self.source_text = source_text  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateECommerceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateECommerceResponseBodyData(TeaModel):
    def __init__(self, translated=None):
        self.translated = translated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateECommerceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        return self


class TranslateECommerceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: TranslateECommerceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TranslateECommerceResponseBody, self).to_map()
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
            temp_model = TranslateECommerceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateECommerceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TranslateECommerceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TranslateECommerceResponse, self).to_map()
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
            temp_model = TranslateECommerceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateGeneralRequest(TeaModel):
    def __init__(self, format_type=None, scene=None, source_language=None, source_text=None, target_language=None):
        self.format_type = format_type  # type: str
        self.scene = scene  # type: str
        self.source_language = source_language  # type: str
        self.source_text = source_text  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateGeneralResponseBodyData(TeaModel):
    def __init__(self, translated=None):
        self.translated = translated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateGeneralResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        return self


class TranslateGeneralResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: TranslateGeneralResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TranslateGeneralResponseBody, self).to_map()
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
            temp_model = TranslateGeneralResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TranslateGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TranslateGeneralResponse, self).to_map()
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
            temp_model = TranslateGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


