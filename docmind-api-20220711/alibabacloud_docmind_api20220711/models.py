# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AyncTradeDocumentPackageExtractSmartAppRequest(TeaModel):
    def __init__(self, custom_extraction_range=None, file_name=None, file_url=None, option=None, template_name=None):
        self.custom_extraction_range = custom_extraction_range  # type: list[str]
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.option = option  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AyncTradeDocumentPackageExtractSmartAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_extraction_range is not None:
            result['CustomExtractionRange'] = self.custom_extraction_range
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.option is not None:
            result['Option'] = self.option
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range = m.get('CustomExtractionRange')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class AyncTradeDocumentPackageExtractSmartAppShrinkRequest(TeaModel):
    def __init__(self, custom_extraction_range_shrink=None, file_name=None, file_url=None, option=None,
                 template_name=None):
        self.custom_extraction_range_shrink = custom_extraction_range_shrink  # type: str
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.option = option  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AyncTradeDocumentPackageExtractSmartAppShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_extraction_range_shrink is not None:
            result['CustomExtractionRange'] = self.custom_extraction_range_shrink
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.option is not None:
            result['Option'] = self.option
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range_shrink = m.get('CustomExtractionRange')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class AyncTradeDocumentPackageExtractSmartAppResponseBody(TeaModel):
    def __init__(self, completed=None, create_time=None, data=None, request_id=None, status=None, success=None):
        self.completed = completed  # type: bool
        self.create_time = create_time  # type: str
        self.data = data  # type: any
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AyncTradeDocumentPackageExtractSmartAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AyncTradeDocumentPackageExtractSmartAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AyncTradeDocumentPackageExtractSmartAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AyncTradeDocumentPackageExtractSmartAppResponse, self).to_map()
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
            temp_model = AyncTradeDocumentPackageExtractSmartAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocStructureResultRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocStructureResultRequest, self).to_map()
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


class GetDocStructureResultResponseBody(TeaModel):
    def __init__(self, code=None, completed=None, data=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.completed = completed  # type: bool
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocStructureResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDocStructureResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDocStructureResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocStructureResultResponse, self).to_map()
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
            temp_model = GetDocStructureResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentCompareResultRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocumentCompareResultRequest, self).to_map()
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


class GetDocumentCompareResultResponseBody(TeaModel):
    def __init__(self, code=None, completed=None, data=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.completed = completed  # type: bool
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocumentCompareResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDocumentCompareResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDocumentCompareResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocumentCompareResultResponse, self).to_map()
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
            temp_model = GetDocumentCompareResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentConvertResultRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocumentConvertResultRequest, self).to_map()
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


class GetDocumentConvertResultResponseBodyData(TeaModel):
    def __init__(self, md_5=None, size=None, type=None, url=None):
        self.md_5 = md_5  # type: str
        self.size = size  # type: long
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocumentConvertResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetDocumentConvertResultResponseBody(TeaModel):
    def __init__(self, code=None, completed=None, data=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.completed = completed  # type: bool
        self.data = data  # type: list[GetDocumentConvertResultResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDocumentConvertResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDocumentConvertResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDocumentConvertResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDocumentConvertResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocumentConvertResultResponse, self).to_map()
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
            temp_model = GetDocumentConvertResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentExtractResultRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocumentExtractResultRequest, self).to_map()
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


class GetDocumentExtractResultResponseBody(TeaModel):
    def __init__(self, code=None, completed=None, data=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.completed = completed  # type: bool
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDocumentExtractResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDocumentExtractResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDocumentExtractResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDocumentExtractResultResponse, self).to_map()
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
            temp_model = GetDocumentExtractResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableUnderstandingResultRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTableUnderstandingResultRequest, self).to_map()
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


class GetTableUnderstandingResultResponseBody(TeaModel):
    def __init__(self, code=None, completed=None, data=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.completed = completed  # type: bool
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTableUnderstandingResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTableUnderstandingResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTableUnderstandingResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTableUnderstandingResultResponse, self).to_map()
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
            temp_model = GetTableUnderstandingResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertImageToExcelJobRequest(TeaModel):
    def __init__(self, force_merge_excel=None, image_name_extension=None, image_names=None, image_urls=None):
        self.force_merge_excel = force_merge_excel  # type: bool
        self.image_name_extension = image_name_extension  # type: str
        self.image_names = image_names  # type: list[str]
        self.image_urls = image_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToExcelJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class SubmitConvertImageToExcelJobShrinkRequest(TeaModel):
    def __init__(self, force_merge_excel=None, image_name_extension=None, image_names_shrink=None,
                 image_urls_shrink=None):
        self.force_merge_excel = force_merge_excel  # type: bool
        self.image_name_extension = image_name_extension  # type: str
        self.image_names_shrink = image_names_shrink  # type: str
        self.image_urls_shrink = image_urls_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToExcelJobShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')
        return self


class SubmitConvertImageToExcelJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToExcelJobResponseBodyData, self).to_map()
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


class SubmitConvertImageToExcelJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitConvertImageToExcelJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitConvertImageToExcelJobResponseBody, self).to_map()
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
            temp_model = SubmitConvertImageToExcelJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertImageToExcelJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitConvertImageToExcelJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitConvertImageToExcelJobResponse, self).to_map()
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
            temp_model = SubmitConvertImageToExcelJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertImageToPdfJobRequest(TeaModel):
    def __init__(self, image_name_extension=None, image_names=None, image_urls=None):
        self.image_name_extension = image_name_extension  # type: str
        self.image_names = image_names  # type: list[str]
        self.image_urls = image_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToPdfJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class SubmitConvertImageToPdfJobShrinkRequest(TeaModel):
    def __init__(self, image_name_extension=None, image_names_shrink=None, image_urls_shrink=None):
        self.image_name_extension = image_name_extension  # type: str
        self.image_names_shrink = image_names_shrink  # type: str
        self.image_urls_shrink = image_urls_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToPdfJobShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')
        return self


class SubmitConvertImageToPdfJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToPdfJobResponseBodyData, self).to_map()
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


class SubmitConvertImageToPdfJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitConvertImageToPdfJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitConvertImageToPdfJobResponseBody, self).to_map()
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
            temp_model = SubmitConvertImageToPdfJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertImageToPdfJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitConvertImageToPdfJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitConvertImageToPdfJobResponse, self).to_map()
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
            temp_model = SubmitConvertImageToPdfJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertImageToWordJobRequest(TeaModel):
    def __init__(self, image_name_extension=None, image_names=None, image_urls=None):
        self.image_name_extension = image_name_extension  # type: str
        self.image_names = image_names  # type: list[str]
        self.image_urls = image_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToWordJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class SubmitConvertImageToWordJobShrinkRequest(TeaModel):
    def __init__(self, image_name_extension=None, image_names_shrink=None, image_urls_shrink=None):
        self.image_name_extension = image_name_extension  # type: str
        self.image_names_shrink = image_names_shrink  # type: str
        self.image_urls_shrink = image_urls_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToWordJobShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')
        return self


class SubmitConvertImageToWordJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertImageToWordJobResponseBodyData, self).to_map()
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


class SubmitConvertImageToWordJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitConvertImageToWordJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitConvertImageToWordJobResponseBody, self).to_map()
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
            temp_model = SubmitConvertImageToWordJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertImageToWordJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitConvertImageToWordJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitConvertImageToWordJobResponse, self).to_map()
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
            temp_model = SubmitConvertImageToWordJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertPdfToExcelJobRequest(TeaModel):
    def __init__(self, file_name=None, file_url=None, force_export_inner_image=None, force_merge_excel=None):
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.force_export_inner_image = force_export_inner_image  # type: bool
        self.force_merge_excel = force_merge_excel  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToExcelJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        return self


class SubmitConvertPdfToExcelJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_url_object=None, force_export_inner_image=None, force_merge_excel=None):
        self.file_name = file_name  # type: str
        self.file_url_object = file_url_object  # type: READABLE
        self.force_export_inner_image = force_export_inner_image  # type: bool
        self.force_merge_excel = force_merge_excel  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToExcelJobAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        return self


class SubmitConvertPdfToExcelJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToExcelJobResponseBodyData, self).to_map()
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


class SubmitConvertPdfToExcelJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitConvertPdfToExcelJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitConvertPdfToExcelJobResponseBody, self).to_map()
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
            temp_model = SubmitConvertPdfToExcelJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertPdfToExcelJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitConvertPdfToExcelJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitConvertPdfToExcelJobResponse, self).to_map()
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
            temp_model = SubmitConvertPdfToExcelJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertPdfToImageJobRequest(TeaModel):
    def __init__(self, file_name=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToImageJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitConvertPdfToImageJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToImageJobAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitConvertPdfToImageJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToImageJobResponseBodyData, self).to_map()
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


class SubmitConvertPdfToImageJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitConvertPdfToImageJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitConvertPdfToImageJobResponseBody, self).to_map()
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
            temp_model = SubmitConvertPdfToImageJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertPdfToImageJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitConvertPdfToImageJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitConvertPdfToImageJobResponse, self).to_map()
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
            temp_model = SubmitConvertPdfToImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertPdfToWordJobRequest(TeaModel):
    def __init__(self, file_name=None, file_url=None, force_export_inner_image=None):
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.force_export_inner_image = force_export_inner_image  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToWordJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        return self


class SubmitConvertPdfToWordJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_url_object=None, force_export_inner_image=None):
        self.file_name = file_name  # type: str
        self.file_url_object = file_url_object  # type: READABLE
        self.force_export_inner_image = force_export_inner_image  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToWordJobAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        return self


class SubmitConvertPdfToWordJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitConvertPdfToWordJobResponseBodyData, self).to_map()
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


class SubmitConvertPdfToWordJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitConvertPdfToWordJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitConvertPdfToWordJobResponseBody, self).to_map()
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
            temp_model = SubmitConvertPdfToWordJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertPdfToWordJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitConvertPdfToWordJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitConvertPdfToWordJobResponse, self).to_map()
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
            temp_model = SubmitConvertPdfToWordJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDigitalDocStructureJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDigitalDocStructureJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitDigitalDocStructureJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDigitalDocStructureJobAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitDigitalDocStructureJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, id=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.data = data  # type: any
        self.id = id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDigitalDocStructureJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SubmitDigitalDocStructureJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitDigitalDocStructureJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDigitalDocStructureJobResponse, self).to_map()
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
            temp_model = SubmitDigitalDocStructureJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocStructureJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None, structure_type=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str
        self.structure_type = structure_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocStructureJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        return self


class SubmitDocStructureJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None, structure_type=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE
        self.structure_type = structure_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocStructureJobAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        return self


class SubmitDocStructureJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocStructureJobResponseBodyData, self).to_map()
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


class SubmitDocStructureJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitDocStructureJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitDocStructureJobResponseBody, self).to_map()
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
            temp_model = SubmitDocStructureJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDocStructureJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitDocStructureJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDocStructureJobResponse, self).to_map()
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
            temp_model = SubmitDocStructureJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocumentCompareJobRequest(TeaModel):
    def __init__(self, compare_file_name=None, compare_file_url=None, origin_file_name=None, origin_file_url=None):
        self.compare_file_name = compare_file_name  # type: str
        self.compare_file_url = compare_file_url  # type: str
        self.origin_file_name = origin_file_name  # type: str
        self.origin_file_url = origin_file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocumentCompareJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_file_name is not None:
            result['CompareFileName'] = self.compare_file_name
        if self.compare_file_url is not None:
            result['CompareFileUrl'] = self.compare_file_url
        if self.origin_file_name is not None:
            result['OriginFileName'] = self.origin_file_name
        if self.origin_file_url is not None:
            result['OriginFileUrl'] = self.origin_file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompareFileName') is not None:
            self.compare_file_name = m.get('CompareFileName')
        if m.get('CompareFileUrl') is not None:
            self.compare_file_url = m.get('CompareFileUrl')
        if m.get('OriginFileName') is not None:
            self.origin_file_name = m.get('OriginFileName')
        if m.get('OriginFileUrl') is not None:
            self.origin_file_url = m.get('OriginFileUrl')
        return self


class SubmitDocumentCompareJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocumentCompareJobResponseBodyData, self).to_map()
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


class SubmitDocumentCompareJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitDocumentCompareJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitDocumentCompareJobResponseBody, self).to_map()
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
            temp_model = SubmitDocumentCompareJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDocumentCompareJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitDocumentCompareJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDocumentCompareJobResponse, self).to_map()
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
            temp_model = SubmitDocumentCompareJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocumentExtractJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocumentExtractJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitDocumentExtractJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocumentExtractJobAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitDocumentExtractJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDocumentExtractJobResponseBodyData, self).to_map()
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


class SubmitDocumentExtractJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitDocumentExtractJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitDocumentExtractJobResponseBody, self).to_map()
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
            temp_model = SubmitDocumentExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDocumentExtractJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitDocumentExtractJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDocumentExtractJobResponse, self).to_map()
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
            temp_model = SubmitDocumentExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTableUnderstandingJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTableUnderstandingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitTableUnderstandingJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTableUnderstandingJobAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitTableUnderstandingJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTableUnderstandingJobResponseBodyData, self).to_map()
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


class SubmitTableUnderstandingJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitTableUnderstandingJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitTableUnderstandingJobResponseBody, self).to_map()
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
            temp_model = SubmitTableUnderstandingJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitTableUnderstandingJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTableUnderstandingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTableUnderstandingJobResponse, self).to_map()
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
            temp_model = SubmitTableUnderstandingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


