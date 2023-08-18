# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeAdvicesRequest(TeaModel):
    def __init__(self, advice_id=None, check_id=None, exclude_advice_id=None, language=None, product=None,
                 resource_id=None):
        self.advice_id = advice_id  # type: long
        self.check_id = check_id  # type: str
        self.exclude_advice_id = exclude_advice_id  # type: long
        self.language = language  # type: str
        self.product = product  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.exclude_advice_id is not None:
            result['ExcludeAdviceId'] = self.exclude_advice_id
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('ExcludeAdviceId') is not None:
            self.exclude_advice_id = m.get('ExcludeAdviceId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeAdvicesResponseBodyDataAdvice(TeaModel):
    def __init__(self, aliyun_id=None, check_id=None, check_name=None, content=None, description=None,
                 gmt_created=None, gmt_modified=None, id=None, is_expired=None, product=None, resource=None, resource_id=None,
                 severity=None):
        self.aliyun_id = aliyun_id  # type: long
        self.check_id = check_id  # type: str
        self.check_name = check_name  # type: str
        self.content = content  # type: str
        self.description = description  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        # ID
        self.id = id  # type: long
        self.is_expired = is_expired  # type: bool
        self.product = product  # type: str
        self.resource = resource  # type: str
        self.resource_id = resource_id  # type: str
        self.severity = severity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvicesResponseBodyDataAdvice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.product is not None:
            result['Product'] = self.product
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeAdvicesResponseBodyData(TeaModel):
    def __init__(self, advice=None):
        self.advice = advice  # type: list[DescribeAdvicesResponseBodyDataAdvice]

    def validate(self):
        if self.advice:
            for k in self.advice:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAdvicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Advice'] = []
        if self.advice is not None:
            for k in self.advice:
                result['Advice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.advice = []
        if m.get('Advice') is not None:
            for k in m.get('Advice'):
                temp_model = DescribeAdvicesResponseBodyDataAdvice()
                self.advice.append(temp_model.from_map(k))
        return self


class DescribeAdvicesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeAdvicesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAdvicesResponseBody, self).to_map()
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
            temp_model = DescribeAdvicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAdvicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAdvicesResponse, self).to_map()
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
            temp_model = DescribeAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdvicesPageRequest(TeaModel):
    def __init__(self, advice_id=None, check_id=None, language=None, page_number=None, page_size=None, product=None,
                 resource_id=None):
        self.advice_id = advice_id  # type: long
        self.check_id = check_id  # type: str
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product = product  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvicesPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeAdvicesPageResponseBodyDataResult(TeaModel):
    def __init__(self, aliyun_id=None, check_id=None, check_name=None, content=None, description=None,
                 gmt_created=None, gmt_modified=None, id=None, is_expired=None, product=None, resource=None, resource_id=None,
                 severity=None):
        self.aliyun_id = aliyun_id  # type: long
        self.check_id = check_id  # type: str
        self.check_name = check_name  # type: str
        self.content = content  # type: str
        self.description = description  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        # ID
        self.id = id  # type: long
        self.is_expired = is_expired  # type: bool
        self.product = product  # type: str
        self.resource = resource  # type: str
        self.resource_id = resource_id  # type: str
        self.severity = severity  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvicesPageResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.product is not None:
            result['Product'] = self.product
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeAdvicesPageResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, result=None, total=None):
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.result = result  # type: list[DescribeAdvicesPageResponseBodyDataResult]
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAdvicesPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeAdvicesPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAdvicesPageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeAdvicesPageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAdvicesPageResponseBody, self).to_map()
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
            temp_model = DescribeAdvicesPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvicesPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAdvicesPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAdvicesPageResponse, self).to_map()
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
            temp_model = DescribeAdvicesPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdvisorChecksRequest(TeaModel):
    def __init__(self, language=None, product=None):
        self.language = language  # type: str
        self.product = product  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvisorChecksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class DescribeAdvisorChecksResponseBodyDataAdvisorCheck(TeaModel):
    def __init__(self, category=None, code=None, description=None, gmt_created=None, gmt_modified=None, name=None,
                 operate_column=None, product=None, status=None, tips=None, view_column=None):
        self.category = category  # type: str
        self.code = code  # type: str
        self.description = description  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.name = name  # type: str
        self.operate_column = operate_column  # type: str
        self.product = product  # type: str
        self.status = status  # type: str
        self.tips = tips  # type: str
        self.view_column = view_column  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvisorChecksResponseBodyDataAdvisorCheck, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.operate_column is not None:
            result['OperateColumn'] = self.operate_column
        if self.product is not None:
            result['Product'] = self.product
        if self.status is not None:
            result['Status'] = self.status
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.view_column is not None:
            result['ViewColumn'] = self.view_column
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperateColumn') is not None:
            self.operate_column = m.get('OperateColumn')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('ViewColumn') is not None:
            self.view_column = m.get('ViewColumn')
        return self


class DescribeAdvisorChecksResponseBodyData(TeaModel):
    def __init__(self, advisor_check=None):
        self.advisor_check = advisor_check  # type: list[DescribeAdvisorChecksResponseBodyDataAdvisorCheck]

    def validate(self):
        if self.advisor_check:
            for k in self.advisor_check:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAdvisorChecksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdvisorCheck'] = []
        if self.advisor_check is not None:
            for k in self.advisor_check:
                result['AdvisorCheck'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.advisor_check = []
        if m.get('AdvisorCheck') is not None:
            for k in m.get('AdvisorCheck'):
                temp_model = DescribeAdvisorChecksResponseBodyDataAdvisorCheck()
                self.advisor_check.append(temp_model.from_map(k))
        return self


class DescribeAdvisorChecksResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeAdvisorChecksResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAdvisorChecksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAdvisorChecksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvisorChecksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAdvisorChecksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAdvisorChecksResponse, self).to_map()
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
            temp_model = DescribeAdvisorChecksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdvisorResourcesRequest(TeaModel):
    def __init__(self, keyword=None, language=None, page_number=None, page_size=None, product=None, resource_id=None):
        self.keyword = keyword  # type: str
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product = product  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvisorResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeAdvisorResourcesResponseBodyDataResultResource(TeaModel):
    def __init__(self, data=None, product=None, region_id=None, resource_id=None, resource_name=None):
        self.data = data  # type: str
        self.product = product  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvisorResourcesResponseBodyDataResultResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class DescribeAdvisorResourcesResponseBodyDataResult(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource  # type: list[DescribeAdvisorResourcesResponseBodyDataResultResource]

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAdvisorResourcesResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeAdvisorResourcesResponseBodyDataResultResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeAdvisorResourcesResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, result=None, total=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.result = result  # type: DescribeAdvisorResourcesResponseBodyDataResult
        self.total = total  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAdvisorResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Result') is not None:
            temp_model = DescribeAdvisorResourcesResponseBodyDataResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAdvisorResourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeAdvisorResourcesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAdvisorResourcesResponseBody, self).to_map()
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
            temp_model = DescribeAdvisorResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvisorResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAdvisorResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAdvisorResourcesResponse, self).to_map()
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
            temp_model = DescribeAdvisorResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoryAdvicesRequest(TeaModel):
    def __init__(self, end_date=None, language=None, page_num=None, page_size=None, product=None, reverse=None,
                 severity=None, start_date=None):
        self.end_date = end_date  # type: str
        self.language = language  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product = product  # type: str
        self.reverse = reverse  # type: bool
        self.severity = severity  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistoryAdvicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.language is not None:
            result['Language'] = self.language
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetHistoryAdvicesResponseBodyDataResult(TeaModel):
    def __init__(self, check_id=None, check_name=None, description=None, gmt_created=None, product=None,
                 resource_id=None, severity=None, url=None):
        self.check_id = check_id  # type: str
        self.check_name = check_name  # type: str
        self.description = description  # type: str
        self.gmt_created = gmt_created  # type: str
        self.product = product  # type: str
        self.resource_id = resource_id  # type: str
        self.severity = severity  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistoryAdvicesResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetHistoryAdvicesResponseBodyData(TeaModel):
    def __init__(self, page_no=None, result=None, total=None):
        self.page_no = page_no  # type: int
        self.result = result  # type: list[GetHistoryAdvicesResponseBodyDataResult]
        self.total = total  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHistoryAdvicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHistoryAdvicesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetHistoryAdvicesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetHistoryAdvicesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHistoryAdvicesResponseBody, self).to_map()
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
            temp_model = GetHistoryAdvicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHistoryAdvicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHistoryAdvicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHistoryAdvicesResponse, self).to_map()
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
            temp_model = GetHistoryAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshAdvisorCheckRequest(TeaModel):
    def __init__(self, check_id=None, language=None, product=None, resource_id=None):
        self.check_id = check_id  # type: str
        self.language = language  # type: str
        self.product = product  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshAdvisorCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class RefreshAdvisorCheckResponseBodyData(TeaModel):
    def __init__(self, success=None, task_id=None, trace_id=None):
        self.success = success  # type: bool
        self.task_id = task_id  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshAdvisorCheckResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RefreshAdvisorCheckResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RefreshAdvisorCheckResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RefreshAdvisorCheckResponseBody, self).to_map()
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
            temp_model = RefreshAdvisorCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshAdvisorCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshAdvisorCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshAdvisorCheckResponse, self).to_map()
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
            temp_model = RefreshAdvisorCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshAdvisorResourceRequest(TeaModel):
    def __init__(self, product=None, resource_id=None):
        self.product = product  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshAdvisorResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class RefreshAdvisorResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshAdvisorResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshAdvisorResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshAdvisorResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshAdvisorResourceResponse, self).to_map()
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
            temp_model = RefreshAdvisorResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


