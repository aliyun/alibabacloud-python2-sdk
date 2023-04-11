# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateDocTranslateTaskRequest(TeaModel):
    def __init__(self, callback_url=None, client_token=None, file_url=None, scene=None, source_language=None,
                 target_language=None):
        self.callback_url = callback_url  # type: str
        self.client_token = client_token  # type: str
        self.file_url = file_url  # type: str
        self.scene = scene  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDocTranslateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class CreateDocTranslateTaskAdvanceRequest(TeaModel):
    def __init__(self, callback_url=None, client_token=None, file_url_object=None, scene=None, source_language=None,
                 target_language=None):
        self.callback_url = callback_url  # type: str
        self.client_token = client_token  # type: str
        self.file_url_object = file_url_object  # type: READABLE
        self.scene = scene  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDocTranslateTaskAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class CreateDocTranslateTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None, task_id=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDocTranslateTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDocTranslateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDocTranslateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDocTranslateTaskResponse, self).to_map()
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
            temp_model = CreateDocTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageTranslateTaskRequest(TeaModel):
    def __init__(self, client_token=None, extra=None, source_language=None, target_language=None, url_list=None):
        self.client_token = client_token  # type: str
        self.extra = extra  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str
        self.url_list = url_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageTranslateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        if self.url_list is not None:
            result['UrlList'] = self.url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        if m.get('UrlList') is not None:
            self.url_list = m.get('UrlList')
        return self


class CreateImageTranslateTaskResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageTranslateTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageTranslateTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: CreateImageTranslateTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateImageTranslateTaskResponseBody, self).to_map()
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
            temp_model = CreateImageTranslateTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageTranslateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateImageTranslateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageTranslateTaskResponse, self).to_map()
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
            temp_model = CreateImageTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBatchTranslateRequest(TeaModel):
    def __init__(self, api_type=None, format_type=None, scene=None, source_language=None, source_text=None,
                 target_language=None):
        self.api_type = api_type  # type: str
        self.format_type = format_type  # type: str
        self.scene = scene  # type: str
        self.source_language = source_language  # type: str
        self.source_text = source_text  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBatchTranslateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
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
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
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


class GetBatchTranslateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, translated_list=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.translated_list = translated_list  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBatchTranslateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.translated_list is not None:
            result['TranslatedList'] = self.translated_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranslatedList') is not None:
            self.translated_list = m.get('TranslatedList')
        return self


class GetBatchTranslateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBatchTranslateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBatchTranslateResponse, self).to_map()
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
            temp_model = GetBatchTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectLanguageRequest(TeaModel):
    def __init__(self, source_text=None):
        self.source_text = source_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDetectLanguageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        return self


class GetDetectLanguageResponseBody(TeaModel):
    def __init__(self, detected_language=None, request_id=None):
        self.detected_language = detected_language  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDetectLanguageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detected_language is not None:
            result['DetectedLanguage'] = self.detected_language
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetectedLanguage') is not None:
            self.detected_language = m.get('DetectedLanguage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDetectLanguageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDetectLanguageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDetectLanguageResponse, self).to_map()
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
            temp_model = GetDetectLanguageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocTranslateTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocTranslateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetDocTranslateTaskResponseBody(TeaModel):
    def __init__(self, page_count=None, request_id=None, status=None, task_id=None, translate_error_code=None,
                 translate_error_message=None, translate_file_url=None):
        self.page_count = page_count  # type: int
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.translate_error_code = translate_error_code  # type: str
        self.translate_error_message = translate_error_message  # type: str
        self.translate_file_url = translate_file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocTranslateTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.translate_error_code is not None:
            result['TranslateErrorCode'] = self.translate_error_code
        if self.translate_error_message is not None:
            result['TranslateErrorMessage'] = self.translate_error_message
        if self.translate_file_url is not None:
            result['TranslateFileUrl'] = self.translate_file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TranslateErrorCode') is not None:
            self.translate_error_code = m.get('TranslateErrorCode')
        if m.get('TranslateErrorMessage') is not None:
            self.translate_error_message = m.get('TranslateErrorMessage')
        if m.get('TranslateFileUrl') is not None:
            self.translate_file_url = m.get('TranslateFileUrl')
        return self


class GetDocTranslateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDocTranslateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocTranslateTaskResponse, self).to_map()
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
            temp_model = GetDocTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageDiagnoseRequest(TeaModel):
    def __init__(self, extra=None, url=None):
        self.extra = extra  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageDiagnoseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImageDiagnoseResponseBodyData(TeaModel):
    def __init__(self, language=None):
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageDiagnoseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetImageDiagnoseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: GetImageDiagnoseResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetImageDiagnoseResponseBody, self).to_map()
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
            temp_model = GetImageDiagnoseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageDiagnoseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageDiagnoseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageDiagnoseResponse, self).to_map()
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
            temp_model = GetImageDiagnoseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageTranslateRequest(TeaModel):
    def __init__(self, extra=None, source_language=None, target_language=None, url=None):
        self.extra = extra  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageTranslateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImageTranslateResponseBodyData(TeaModel):
    def __init__(self, orc=None, picture_editor=None, url=None):
        self.orc = orc  # type: str
        self.picture_editor = picture_editor  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageTranslateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.orc is not None:
            result['Orc'] = self.orc
        if self.picture_editor is not None:
            result['PictureEditor'] = self.picture_editor
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Orc') is not None:
            self.orc = m.get('Orc')
        if m.get('PictureEditor') is not None:
            self.picture_editor = m.get('PictureEditor')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImageTranslateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: GetImageTranslateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetImageTranslateResponseBody, self).to_map()
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
            temp_model = GetImageTranslateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageTranslateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageTranslateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageTranslateResponse, self).to_map()
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
            temp_model = GetImageTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageTranslateTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageTranslateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetImageTranslateTaskResponseBodyData(TeaModel):
    def __init__(self, image_data=None):
        self.image_data = image_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageTranslateTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        return self


class GetImageTranslateTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: GetImageTranslateTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetImageTranslateTaskResponseBody, self).to_map()
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
            temp_model = GetImageTranslateTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageTranslateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageTranslateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageTranslateTaskResponse, self).to_map()
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
            temp_model = GetImageTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTitleDiagnoseRequest(TeaModel):
    def __init__(self, category_id=None, extra=None, language=None, platform=None, title=None):
        self.category_id = category_id  # type: str
        self.extra = extra  # type: str
        self.language = language  # type: str
        self.platform = platform  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTitleDiagnoseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.language is not None:
            result['Language'] = self.language
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTitleDiagnoseResponseBodyData(TeaModel):
    def __init__(self, all_uppercase_words=None, contain_core_classes=None, disable_words=None,
                 duplicate_words=None, language_quality_score=None, no_first_uppercase_list=None, over_length_limit=None,
                 total_score=None, word_count=None, word_spelled_correct_error=None):
        self.all_uppercase_words = all_uppercase_words  # type: str
        self.contain_core_classes = contain_core_classes  # type: str
        self.disable_words = disable_words  # type: str
        self.duplicate_words = duplicate_words  # type: str
        self.language_quality_score = language_quality_score  # type: str
        self.no_first_uppercase_list = no_first_uppercase_list  # type: str
        self.over_length_limit = over_length_limit  # type: str
        self.total_score = total_score  # type: str
        self.word_count = word_count  # type: str
        self.word_spelled_correct_error = word_spelled_correct_error  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTitleDiagnoseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_uppercase_words is not None:
            result['AllUppercaseWords'] = self.all_uppercase_words
        if self.contain_core_classes is not None:
            result['ContainCoreClasses'] = self.contain_core_classes
        if self.disable_words is not None:
            result['DisableWords'] = self.disable_words
        if self.duplicate_words is not None:
            result['DuplicateWords'] = self.duplicate_words
        if self.language_quality_score is not None:
            result['LanguageQualityScore'] = self.language_quality_score
        if self.no_first_uppercase_list is not None:
            result['NoFirstUppercaseList'] = self.no_first_uppercase_list
        if self.over_length_limit is not None:
            result['OverLengthLimit'] = self.over_length_limit
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        if self.word_spelled_correct_error is not None:
            result['WordSpelledCorrectError'] = self.word_spelled_correct_error
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllUppercaseWords') is not None:
            self.all_uppercase_words = m.get('AllUppercaseWords')
        if m.get('ContainCoreClasses') is not None:
            self.contain_core_classes = m.get('ContainCoreClasses')
        if m.get('DisableWords') is not None:
            self.disable_words = m.get('DisableWords')
        if m.get('DuplicateWords') is not None:
            self.duplicate_words = m.get('DuplicateWords')
        if m.get('LanguageQualityScore') is not None:
            self.language_quality_score = m.get('LanguageQualityScore')
        if m.get('NoFirstUppercaseList') is not None:
            self.no_first_uppercase_list = m.get('NoFirstUppercaseList')
        if m.get('OverLengthLimit') is not None:
            self.over_length_limit = m.get('OverLengthLimit')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
        if m.get('WordSpelledCorrectError') is not None:
            self.word_spelled_correct_error = m.get('WordSpelledCorrectError')
        return self


class GetTitleDiagnoseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: GetTitleDiagnoseResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTitleDiagnoseResponseBody, self).to_map()
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
            temp_model = GetTitleDiagnoseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTitleDiagnoseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTitleDiagnoseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTitleDiagnoseResponse, self).to_map()
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
            temp_model = GetTitleDiagnoseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTitleGenerateRequest(TeaModel):
    def __init__(self, attributes=None, category_id=None, extra=None, hot_words=None, language=None, platform=None,
                 title=None):
        self.attributes = attributes  # type: str
        self.category_id = category_id  # type: str
        self.extra = extra  # type: str
        self.hot_words = hot_words  # type: str
        self.language = language  # type: str
        self.platform = platform  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTitleGenerateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.hot_words is not None:
            result['HotWords'] = self.hot_words
        if self.language is not None:
            result['Language'] = self.language
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('HotWords') is not None:
            self.hot_words = m.get('HotWords')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTitleGenerateResponseBodyData(TeaModel):
    def __init__(self, titles=None):
        self.titles = titles  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTitleGenerateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.titles is not None:
            result['Titles'] = self.titles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        return self


class GetTitleGenerateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: GetTitleGenerateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTitleGenerateResponseBody, self).to_map()
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
            temp_model = GetTitleGenerateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTitleGenerateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTitleGenerateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTitleGenerateResponse, self).to_map()
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
            temp_model = GetTitleGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTitleIntelligenceRequest(TeaModel):
    def __init__(self, cat_level_three_id=None, cat_level_two_id=None, extra=None, keywords=None, platform=None):
        self.cat_level_three_id = cat_level_three_id  # type: long
        self.cat_level_two_id = cat_level_two_id  # type: long
        self.extra = extra  # type: str
        self.keywords = keywords  # type: str
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTitleIntelligenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cat_level_three_id is not None:
            result['CatLevelThreeId'] = self.cat_level_three_id
        if self.cat_level_two_id is not None:
            result['CatLevelTwoId'] = self.cat_level_two_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CatLevelThreeId') is not None:
            self.cat_level_three_id = m.get('CatLevelThreeId')
        if m.get('CatLevelTwoId') is not None:
            self.cat_level_two_id = m.get('CatLevelTwoId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class GetTitleIntelligenceResponseBodyData(TeaModel):
    def __init__(self, titles=None):
        self.titles = titles  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTitleIntelligenceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.titles is not None:
            result['Titles'] = self.titles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        return self


class GetTitleIntelligenceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: GetTitleIntelligenceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTitleIntelligenceResponseBody, self).to_map()
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
            temp_model = GetTitleIntelligenceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTitleIntelligenceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTitleIntelligenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTitleIntelligenceResponse, self).to_map()
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
            temp_model = GetTitleIntelligenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranslateImageBatchResultRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranslateImageBatchResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTranslateImageBatchResultResponseBodyDataResult(TeaModel):
    def __init__(self, code=None, final_image_url=None, in_painting_url=None, message=None, source_image_url=None,
                 success=None, template_json=None):
        self.code = code  # type: int
        self.final_image_url = final_image_url  # type: str
        self.in_painting_url = in_painting_url  # type: str
        self.message = message  # type: str
        self.source_image_url = source_image_url  # type: str
        self.success = success  # type: bool
        self.template_json = template_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranslateImageBatchResultResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.final_image_url is not None:
            result['FinalImageUrl'] = self.final_image_url
        if self.in_painting_url is not None:
            result['InPaintingUrl'] = self.in_painting_url
        if self.message is not None:
            result['Message'] = self.message
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.success is not None:
            result['Success'] = self.success
        if self.template_json is not None:
            result['TemplateJson'] = self.template_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FinalImageUrl') is not None:
            self.final_image_url = m.get('FinalImageUrl')
        if m.get('InPaintingUrl') is not None:
            self.in_painting_url = m.get('InPaintingUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateJson') is not None:
            self.template_json = m.get('TemplateJson')
        return self


class GetTranslateImageBatchResultResponseBodyData(TeaModel):
    def __init__(self, result=None, status=None):
        self.result = result  # type: list[GetTranslateImageBatchResultResponseBodyDataResult]
        self.status = status  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTranslateImageBatchResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetTranslateImageBatchResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTranslateImageBatchResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: GetTranslateImageBatchResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTranslateImageBatchResultResponseBody, self).to_map()
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
            temp_model = GetTranslateImageBatchResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTranslateImageBatchResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTranslateImageBatchResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTranslateImageBatchResultResponse, self).to_map()
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
            temp_model = GetTranslateImageBatchResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranslateReportRequest(TeaModel):
    def __init__(self, api_name=None, begin_time=None, end_time=None, group=None):
        self.api_name = api_name  # type: str
        self.begin_time = begin_time  # type: str
        self.end_time = end_time  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranslateReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class GetTranslateReportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranslateReportResponseBody, self).to_map()
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
        return self


class GetTranslateReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTranslateReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTranslateReportResponse, self).to_map()
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
            temp_model = GetTranslateReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenAlimtServiceRequest(TeaModel):
    def __init__(self, owner_id=None, type=None):
        self.owner_id = owner_id  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenAlimtServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OpenAlimtServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenAlimtServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenAlimtServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenAlimtServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenAlimtServiceResponse, self).to_map()
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
            temp_model = OpenAlimtServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateRequest(TeaModel):
    def __init__(self, context=None, format_type=None, scene=None, source_language=None, source_text=None,
                 target_language=None):
        self.context = context  # type: str
        self.format_type = format_type  # type: str
        self.scene = scene  # type: str
        self.source_language = source_language  # type: str
        self.source_text = source_text  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
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
        if m.get('Context') is not None:
            self.context = m.get('Context')
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


class TranslateResponseBodyData(TeaModel):
    def __init__(self, translated=None, word_count=None):
        self.translated = translated  # type: str
        self.word_count = word_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
        return self


class TranslateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: TranslateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TranslateResponseBody, self).to_map()
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
            temp_model = TranslateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TranslateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TranslateResponse, self).to_map()
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
            temp_model = TranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateCertificateRequest(TeaModel):
    def __init__(self, certificate_type=None, image_url=None, result_type=None, source_language=None,
                 target_language=None):
        self.certificate_type = certificate_type  # type: str
        self.image_url = image_url  # type: str
        self.result_type = result_type  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateCertificateAdvanceRequest(TeaModel):
    def __init__(self, certificate_type=None, image_url_object=None, result_type=None, source_language=None,
                 target_language=None):
        self.certificate_type = certificate_type  # type: str
        self.image_url_object = image_url_object  # type: READABLE
        self.result_type = result_type  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateCertificateAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateCertificateResponseBodyDataTranslatedValues(TeaModel):
    def __init__(self, key=None, key_translation=None, value=None, value_translation=None):
        self.key = key  # type: str
        self.key_translation = key_translation  # type: str
        self.value = value  # type: str
        self.value_translation = value_translation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateCertificateResponseBodyDataTranslatedValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_translation is not None:
            result['KeyTranslation'] = self.key_translation
        if self.value is not None:
            result['Value'] = self.value
        if self.value_translation is not None:
            result['ValueTranslation'] = self.value_translation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyTranslation') is not None:
            self.key_translation = m.get('KeyTranslation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueTranslation') is not None:
            self.value_translation = m.get('ValueTranslation')
        return self


class TranslateCertificateResponseBodyData(TeaModel):
    def __init__(self, translated_values=None):
        self.translated_values = translated_values  # type: list[TranslateCertificateResponseBodyDataTranslatedValues]

    def validate(self):
        if self.translated_values:
            for k in self.translated_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TranslateCertificateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TranslatedValues'] = []
        if self.translated_values is not None:
            for k in self.translated_values:
                result['TranslatedValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.translated_values = []
        if m.get('TranslatedValues') is not None:
            for k in m.get('TranslatedValues'):
                temp_model = TranslateCertificateResponseBodyDataTranslatedValues()
                self.translated_values.append(temp_model.from_map(k))
        return self


class TranslateCertificateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: TranslateCertificateResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TranslateCertificateResponseBody, self).to_map()
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
            temp_model = TranslateCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TranslateCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TranslateCertificateResponse, self).to_map()
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
            temp_model = TranslateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateECommerceRequest(TeaModel):
    def __init__(self, context=None, format_type=None, scene=None, source_language=None, source_text=None,
                 target_language=None):
        self.context = context  # type: str
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
        if self.context is not None:
            result['Context'] = self.context
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
        if m.get('Context') is not None:
            self.context = m.get('Context')
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
    def __init__(self, translated=None, word_count=None):
        self.translated = translated  # type: str
        self.word_count = word_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateECommerceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
    def __init__(self, context=None, format_type=None, scene=None, source_language=None, source_text=None,
                 target_language=None):
        self.context = context  # type: str
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
        if self.context is not None:
            result['Context'] = self.context
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
        if m.get('Context') is not None:
            self.context = m.get('Context')
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
    def __init__(self, translated=None, word_count=None):
        self.translated = translated  # type: str
        self.word_count = word_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateGeneralResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class TranslateImageRequest(TeaModel):
    def __init__(self, ext=None, field=None, image_base_64=None, image_url=None, source_language=None,
                 target_language=None):
        self.ext = ext  # type: str
        self.field = field  # type: str
        self.image_base_64 = image_base_64  # type: str
        self.image_url = image_url  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.field is not None:
            result['Field'] = self.field
        if self.image_base_64 is not None:
            result['ImageBase64'] = self.image_base_64
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('ImageBase64') is not None:
            self.image_base_64 = m.get('ImageBase64')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateImageResponseBodyData(TeaModel):
    def __init__(self, final_image_url=None, in_painting_url=None, template_json=None):
        self.final_image_url = final_image_url  # type: str
        self.in_painting_url = in_painting_url  # type: str
        self.template_json = template_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.final_image_url is not None:
            result['FinalImageUrl'] = self.final_image_url
        if self.in_painting_url is not None:
            result['InPaintingUrl'] = self.in_painting_url
        if self.template_json is not None:
            result['TemplateJson'] = self.template_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FinalImageUrl') is not None:
            self.final_image_url = m.get('FinalImageUrl')
        if m.get('InPaintingUrl') is not None:
            self.in_painting_url = m.get('InPaintingUrl')
        if m.get('TemplateJson') is not None:
            self.template_json = m.get('TemplateJson')
        return self


class TranslateImageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: TranslateImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TranslateImageResponseBody, self).to_map()
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
            temp_model = TranslateImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TranslateImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TranslateImageResponse, self).to_map()
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
            temp_model = TranslateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateImageBatchRequest(TeaModel):
    def __init__(self, custom_task_id=None, ext=None, field=None, image_urls=None, source_language=None,
                 target_language=None):
        self.custom_task_id = custom_task_id  # type: str
        self.ext = ext  # type: str
        self.field = field  # type: str
        self.image_urls = image_urls  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateImageBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.field is not None:
            result['Field'] = self.field
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateImageBatchResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TranslateImageBatchResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TranslateImageBatchResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: TranslateImageBatchResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TranslateImageBatchResponseBody, self).to_map()
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
            temp_model = TranslateImageBatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateImageBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TranslateImageBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TranslateImageBatchResponse, self).to_map()
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
            temp_model = TranslateImageBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


