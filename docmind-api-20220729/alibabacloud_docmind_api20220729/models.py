# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetSingleDocumentExtractResultRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSingleDocumentExtractResultRequest, self).to_map()
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


class GetSingleDocumentExtractResultResponseBody(TeaModel):
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
        _map = super(GetSingleDocumentExtractResultResponseBody, self).to_map()
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


class GetSingleDocumentExtractResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSingleDocumentExtractResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSingleDocumentExtractResultResponse, self).to_map()
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
            temp_model = GetSingleDocumentExtractResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAirWaybillExtractJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAirWaybillExtractJobRequest, self).to_map()
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


class SubmitAirWaybillExtractJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAirWaybillExtractJobAdvanceRequest, self).to_map()
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


class SubmitAirWaybillExtractJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAirWaybillExtractJobResponseBodyData, self).to_map()
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


class SubmitAirWaybillExtractJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitAirWaybillExtractJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitAirWaybillExtractJobResponseBody, self).to_map()
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
            temp_model = SubmitAirWaybillExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitAirWaybillExtractJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAirWaybillExtractJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAirWaybillExtractJobResponse, self).to_map()
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
            temp_model = SubmitAirWaybillExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBillOfLadingExtractJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitBillOfLadingExtractJobRequest, self).to_map()
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


class SubmitBillOfLadingExtractJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitBillOfLadingExtractJobAdvanceRequest, self).to_map()
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


class SubmitBillOfLadingExtractJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitBillOfLadingExtractJobResponseBodyData, self).to_map()
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


class SubmitBillOfLadingExtractJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitBillOfLadingExtractJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitBillOfLadingExtractJobResponseBody, self).to_map()
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
            temp_model = SubmitBillOfLadingExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitBillOfLadingExtractJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitBillOfLadingExtractJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitBillOfLadingExtractJobResponse, self).to_map()
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
            temp_model = SubmitBillOfLadingExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitExportDeclarationSheetExtractJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitExportDeclarationSheetExtractJobRequest, self).to_map()
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


class SubmitExportDeclarationSheetExtractJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitExportDeclarationSheetExtractJobAdvanceRequest, self).to_map()
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


class SubmitExportDeclarationSheetExtractJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitExportDeclarationSheetExtractJobResponseBodyData, self).to_map()
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


class SubmitExportDeclarationSheetExtractJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitExportDeclarationSheetExtractJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitExportDeclarationSheetExtractJobResponseBody, self).to_map()
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
            temp_model = SubmitExportDeclarationSheetExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitExportDeclarationSheetExtractJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitExportDeclarationSheetExtractJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitExportDeclarationSheetExtractJobResponse, self).to_map()
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
            temp_model = SubmitExportDeclarationSheetExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInvoiceExtractJobRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitInvoiceExtractJobRequest, self).to_map()
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


class SubmitInvoiceExtractJobAdvanceRequest(TeaModel):
    def __init__(self, file_name=None, file_name_extension=None, file_url_object=None):
        self.file_name = file_name  # type: str
        self.file_name_extension = file_name_extension  # type: str
        self.file_url_object = file_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitInvoiceExtractJobAdvanceRequest, self).to_map()
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


class SubmitInvoiceExtractJobResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitInvoiceExtractJobResponseBodyData, self).to_map()
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


class SubmitInvoiceExtractJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitInvoiceExtractJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitInvoiceExtractJobResponseBody, self).to_map()
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
            temp_model = SubmitInvoiceExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitInvoiceExtractJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitInvoiceExtractJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitInvoiceExtractJobResponse, self).to_map()
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
            temp_model = SubmitInvoiceExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


