# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateSheetHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateSheetHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: CreateSheetHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(CreateSheetHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateSheetHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateSheetShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateSheetRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateSheetRequest(TeaModel):
    def __init__(self, name=None, tenant_context=None, workbook_id=None):
        self.name = name  # type: str
        self.tenant_context = tenant_context  # type: CreateSheetRequestTenantContext
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(CreateSheetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            temp_model = CreateSheetRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class CreateSheetShrinkRequest(TeaModel):
    def __init__(self, name=None, tenant_context_shrink=None, workbook_id=None):
        self.name = name  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class CreateSheetResponseBody(TeaModel):
    def __init__(self, id=None, name=None, request_id=None, visibility=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSheetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.visibility is not None:
            result['visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')
        return self


class CreateSheetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSheetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSheetResponse, self).to_map()
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
            temp_model = CreateSheetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRowsBeforeHeadersAccountContext(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeHeadersAccountContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class InsertRowsBeforeHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context = account_context  # type: InsertRowsBeforeHeadersAccountContext

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super(InsertRowsBeforeHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = InsertRowsBeforeHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class InsertRowsBeforeShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, account_context_shrink=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.account_context_shrink = account_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeShrinkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class InsertRowsBeforeRequestTenantContext(TeaModel):
    def __init__(self, tenant_id=None):
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeRequestTenantContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class InsertRowsBeforeRequest(TeaModel):
    def __init__(self, row=None, row_count=None, sheet_id=None, tenant_context=None, workbook_id=None):
        self.row = row  # type: long
        self.row_count = row_count  # type: long
        self.sheet_id = sheet_id  # type: str
        self.tenant_context = tenant_context  # type: InsertRowsBeforeRequestTenantContext
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super(InsertRowsBeforeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['Row'] = self.row
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')
        if m.get('TenantContext') is not None:
            temp_model = InsertRowsBeforeRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class InsertRowsBeforeShrinkRequest(TeaModel):
    def __init__(self, row=None, row_count=None, sheet_id=None, tenant_context_shrink=None, workbook_id=None):
        self.row = row  # type: long
        self.row_count = row_count  # type: long
        self.sheet_id = sheet_id  # type: str
        self.tenant_context_shrink = tenant_context_shrink  # type: str
        self.workbook_id = workbook_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['Row'] = self.row
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class InsertRowsBeforeResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRowsBeforeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class InsertRowsBeforeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertRowsBeforeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertRowsBeforeResponse, self).to_map()
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
            temp_model = InsertRowsBeforeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


