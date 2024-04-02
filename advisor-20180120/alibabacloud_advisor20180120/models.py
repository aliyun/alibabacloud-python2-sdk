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


class DescribeAdvicesFlatPageRequest(TeaModel):
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
        _map = super(DescribeAdvicesFlatPageRequest, self).to_map()
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


class DescribeAdvicesFlatPageResponseBodyDataResult(TeaModel):
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
        self.id = id  # type: long
        self.is_expired = is_expired  # type: bool
        self.product = product  # type: str
        self.resource = resource  # type: str
        self.resource_id = resource_id  # type: str
        self.severity = severity  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAdvicesFlatPageResponseBodyDataResult, self).to_map()
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


class DescribeAdvicesFlatPageResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, result=None, total=None):
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.result = result  # type: list[DescribeAdvicesFlatPageResponseBodyDataResult]
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAdvicesFlatPageResponseBodyData, self).to_map()
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
                temp_model = DescribeAdvicesFlatPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAdvicesFlatPageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeAdvicesFlatPageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAdvicesFlatPageResponseBody, self).to_map()
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
            temp_model = DescribeAdvicesFlatPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdvicesFlatPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAdvicesFlatPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAdvicesFlatPageResponse, self).to_map()
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
            temp_model = DescribeAdvicesFlatPageResponseBody()
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


class DescribeCostCheckAdvicesRequest(TeaModel):
    def __init__(self, check_id=None, language=None, page_number=None, page_size=None, region_ids=None,
                 resource_ids=None, resource_name=None, severity=None):
        self.check_id = check_id  # type: str
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_ids = region_ids  # type: list[str]
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_name = resource_name  # type: str
        self.severity = severity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCostCheckAdvicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeCostCheckAdvicesShrinkRequest(TeaModel):
    def __init__(self, check_id=None, language=None, page_number=None, page_size=None, region_ids_shrink=None,
                 resource_ids_shrink=None, resource_name=None, severity=None):
        self.check_id = check_id  # type: str
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.resource_ids_shrink = resource_ids_shrink  # type: str
        self.resource_name = resource_name  # type: str
        self.severity = severity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCostCheckAdvicesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeCostCheckAdvicesResponseBodyDataAdviceListTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCostCheckAdvicesResponseBodyDataAdviceListTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeCostCheckAdvicesResponseBodyDataAdviceList(TeaModel):
    def __init__(self, aliyun_id=None, content=None, end_time=None, gmt_deleted=None, product=None, region_id=None,
                 resource_id=None, resource_name=None, severity=None, start_time=None, tags=None, url=None, user_name=None,
                 zone_id=None):
        self.aliyun_id = aliyun_id  # type: long
        self.content = content  # type: str
        self.end_time = end_time  # type: long
        self.gmt_deleted = gmt_deleted  # type: long
        self.product = product  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.severity = severity  # type: str
        self.start_time = start_time  # type: long
        self.tags = tags  # type: list[DescribeCostCheckAdvicesResponseBodyDataAdviceListTags]
        self.url = url  # type: str
        self.user_name = user_name  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCostCheckAdvicesResponseBodyDataAdviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.content is not None:
            result['Content'] = self.content
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_deleted is not None:
            result['GmtDeleted'] = self.gmt_deleted
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.url is not None:
            result['Url'] = self.url
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtDeleted') is not None:
            self.gmt_deleted = m.get('GmtDeleted')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeCostCheckAdvicesResponseBodyDataAdviceListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeCostCheckAdvicesResponseBodyData(TeaModel):
    def __init__(self, advice_list=None, check_id=None, page_number=None, page_size=None, total_count=None):
        self.advice_list = advice_list  # type: list[DescribeCostCheckAdvicesResponseBodyDataAdviceList]
        self.check_id = check_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.advice_list:
            for k in self.advice_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCostCheckAdvicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdviceList'] = []
        if self.advice_list is not None:
            for k in self.advice_list:
                result['AdviceList'].append(k.to_map() if k else None)
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.advice_list = []
        if m.get('AdviceList') is not None:
            for k in m.get('AdviceList'):
                temp_model = DescribeCostCheckAdvicesResponseBodyDataAdviceList()
                self.advice_list.append(temp_model.from_map(k))
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCostCheckAdvicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeCostCheckAdvicesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCostCheckAdvicesResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeCostCheckAdvicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCostCheckAdvicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCostCheckAdvicesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCostCheckAdvicesResponse, self).to_map()
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
            temp_model = DescribeCostCheckAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCostCheckResultsRequest(TeaModel):
    def __init__(self, check_ids=None, group_by=None, product=None, region_ids=None, resource_ids=None,
                 resource_name=None, severity=None):
        self.check_ids = check_ids  # type: list[str]
        self.group_by = group_by  # type: str
        self.product = product  # type: str
        self.region_ids = region_ids  # type: list[str]
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_name = resource_name  # type: str
        self.severity = severity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCostCheckResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.product is not None:
            result['Product'] = self.product
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeCostCheckResultsShrinkRequest(TeaModel):
    def __init__(self, check_ids_shrink=None, group_by=None, product=None, region_ids_shrink=None,
                 resource_ids_shrink=None, resource_name=None, severity=None):
        self.check_ids_shrink = check_ids_shrink  # type: str
        self.group_by = group_by  # type: str
        self.product = product  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.resource_ids_shrink = resource_ids_shrink  # type: str
        self.resource_name = resource_name  # type: str
        self.severity = severity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCostCheckResultsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_ids_shrink is not None:
            result['CheckIds'] = self.check_ids_shrink
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.product is not None:
            result['Product'] = self.product
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids_shrink = m.get('CheckIds')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems(TeaModel):
    def __init__(self, advice_count=None, advice_resource_count=None, category=None, check_id=None, check_name=None,
                 current_cost=None, description=None, expected_saving_cost=None, optimized_cost=None, product=None,
                 severity=None, summary=None, tips=None):
        self.advice_count = advice_count  # type: int
        self.advice_resource_count = advice_resource_count  # type: int
        self.category = category  # type: str
        self.check_id = check_id  # type: str
        self.check_name = check_name  # type: str
        self.current_cost = current_cost  # type: float
        self.description = description  # type: str
        self.expected_saving_cost = expected_saving_cost  # type: float
        self.optimized_cost = optimized_cost  # type: float
        self.product = product  # type: str
        self.severity = severity  # type: int
        self.summary = summary  # type: str
        self.tips = tips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_count is not None:
            result['AdviceCount'] = self.advice_count
        if self.advice_resource_count is not None:
            result['AdviceResourceCount'] = self.advice_resource_count
        if self.category is not None:
            result['Category'] = self.category
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.current_cost is not None:
            result['CurrentCost'] = self.current_cost
        if self.description is not None:
            result['Description'] = self.description
        if self.expected_saving_cost is not None:
            result['ExpectedSavingCost'] = self.expected_saving_cost
        if self.optimized_cost is not None:
            result['OptimizedCost'] = self.optimized_cost
        if self.product is not None:
            result['Product'] = self.product
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdviceCount') is not None:
            self.advice_count = m.get('AdviceCount')
        if m.get('AdviceResourceCount') is not None:
            self.advice_resource_count = m.get('AdviceResourceCount')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CurrentCost') is not None:
            self.current_cost = m.get('CurrentCost')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpectedSavingCost') is not None:
            self.expected_saving_cost = m.get('ExpectedSavingCost')
        if m.get('OptimizedCost') is not None:
            self.optimized_cost = m.get('OptimizedCost')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class DescribeCostCheckResultsResponseBodyDataViewGroup(TeaModel):
    def __init__(self, check_items=None, group_code=None, group_count=None, group_expected_saving_cost=None,
                 group_name=None):
        self.check_items = check_items  # type: list[DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems]
        self.group_code = group_code  # type: str
        self.group_count = group_count  # type: int
        self.group_expected_saving_cost = group_expected_saving_cost  # type: float
        self.group_name = group_name  # type: str

    def validate(self):
        if self.check_items:
            for k in self.check_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCostCheckResultsResponseBodyDataViewGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItems'] = []
        if self.check_items is not None:
            for k in self.check_items:
                result['CheckItems'].append(k.to_map() if k else None)
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_count is not None:
            result['GroupCount'] = self.group_count
        if self.group_expected_saving_cost is not None:
            result['GroupExpectedSavingCost'] = self.group_expected_saving_cost
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k in m.get('CheckItems'):
                temp_model = DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems()
                self.check_items.append(temp_model.from_map(k))
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')
        if m.get('GroupExpectedSavingCost') is not None:
            self.group_expected_saving_cost = m.get('GroupExpectedSavingCost')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeCostCheckResultsResponseBodyData(TeaModel):
    def __init__(self, advice_resource_count=None, group_by=None, normal_count=None, resource_count=None,
                 total_count=None, view_group=None, warning_count=None):
        self.advice_resource_count = advice_resource_count  # type: int
        self.group_by = group_by  # type: str
        self.normal_count = normal_count  # type: int
        self.resource_count = resource_count  # type: int
        self.total_count = total_count  # type: int
        self.view_group = view_group  # type: list[DescribeCostCheckResultsResponseBodyDataViewGroup]
        self.warning_count = warning_count  # type: int

    def validate(self):
        if self.view_group:
            for k in self.view_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCostCheckResultsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_resource_count is not None:
            result['AdviceResourceCount'] = self.advice_resource_count
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ViewGroup'] = []
        if self.view_group is not None:
            for k in self.view_group:
                result['ViewGroup'].append(k.to_map() if k else None)
        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdviceResourceCount') is not None:
            self.advice_resource_count = m.get('AdviceResourceCount')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.view_group = []
        if m.get('ViewGroup') is not None:
            for k in m.get('ViewGroup'):
                temp_model = DescribeCostCheckResultsResponseBodyDataViewGroup()
                self.view_group.append(temp_model.from_map(k))
        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')
        return self


class DescribeCostCheckResultsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeCostCheckResultsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCostCheckResultsResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeCostCheckResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCostCheckResultsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCostCheckResultsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCostCheckResultsResponse, self).to_map()
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
            temp_model = DescribeCostCheckResultsResponseBody()
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


class GetTaskStatusByIdRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatusByIdRequest, self).to_map()
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


class GetTaskStatusByIdResponseBodyData(TeaModel):
    def __init__(self, task_id=None, task_status=None):
        self.task_id = task_id  # type: long
        self.task_status = task_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatusByIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetTaskStatusByIdResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetTaskStatusByIdResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTaskStatusByIdResponseBody, self).to_map()
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
            temp_model = GetTaskStatusByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTaskStatusByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskStatusByIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskStatusByIdResponse, self).to_map()
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
            temp_model = GetTaskStatusByIdResponseBody()
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


class ReportBizAlertInfoRequest(TeaModel):
    def __init__(self, alert_description=None, alert_detail=None, alert_grade=None, alert_labels=None,
                 alert_scene=None, alert_token=None, alert_uid=None, language=None):
        self.alert_description = alert_description  # type: str
        self.alert_detail = alert_detail  # type: str
        self.alert_grade = alert_grade  # type: str
        self.alert_labels = alert_labels  # type: str
        self.alert_scene = alert_scene  # type: str
        self.alert_token = alert_token  # type: str
        self.alert_uid = alert_uid  # type: list[long]
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportBizAlertInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_description is not None:
            result['AlertDescription'] = self.alert_description
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        if self.alert_grade is not None:
            result['AlertGrade'] = self.alert_grade
        if self.alert_labels is not None:
            result['AlertLabels'] = self.alert_labels
        if self.alert_scene is not None:
            result['AlertScene'] = self.alert_scene
        if self.alert_token is not None:
            result['AlertToken'] = self.alert_token
        if self.alert_uid is not None:
            result['AlertUid'] = self.alert_uid
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDescription') is not None:
            self.alert_description = m.get('AlertDescription')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        if m.get('AlertGrade') is not None:
            self.alert_grade = m.get('AlertGrade')
        if m.get('AlertLabels') is not None:
            self.alert_labels = m.get('AlertLabels')
        if m.get('AlertScene') is not None:
            self.alert_scene = m.get('AlertScene')
        if m.get('AlertToken') is not None:
            self.alert_token = m.get('AlertToken')
        if m.get('AlertUid') is not None:
            self.alert_uid = m.get('AlertUid')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ReportBizAlertInfoShrinkRequest(TeaModel):
    def __init__(self, alert_description=None, alert_detail=None, alert_grade=None, alert_labels=None,
                 alert_scene=None, alert_token=None, alert_uid_shrink=None, language=None):
        self.alert_description = alert_description  # type: str
        self.alert_detail = alert_detail  # type: str
        self.alert_grade = alert_grade  # type: str
        self.alert_labels = alert_labels  # type: str
        self.alert_scene = alert_scene  # type: str
        self.alert_token = alert_token  # type: str
        self.alert_uid_shrink = alert_uid_shrink  # type: str
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportBizAlertInfoShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_description is not None:
            result['AlertDescription'] = self.alert_description
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        if self.alert_grade is not None:
            result['AlertGrade'] = self.alert_grade
        if self.alert_labels is not None:
            result['AlertLabels'] = self.alert_labels
        if self.alert_scene is not None:
            result['AlertScene'] = self.alert_scene
        if self.alert_token is not None:
            result['AlertToken'] = self.alert_token
        if self.alert_uid_shrink is not None:
            result['AlertUid'] = self.alert_uid_shrink
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDescription') is not None:
            self.alert_description = m.get('AlertDescription')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        if m.get('AlertGrade') is not None:
            self.alert_grade = m.get('AlertGrade')
        if m.get('AlertLabels') is not None:
            self.alert_labels = m.get('AlertLabels')
        if m.get('AlertScene') is not None:
            self.alert_scene = m.get('AlertScene')
        if m.get('AlertToken') is not None:
            self.alert_token = m.get('AlertToken')
        if m.get('AlertUid') is not None:
            self.alert_uid_shrink = m.get('AlertUid')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ReportBizAlertInfoResponseBodyData(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportBizAlertInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ReportBizAlertInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ReportBizAlertInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ReportBizAlertInfoResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReportBizAlertInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportBizAlertInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportBizAlertInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportBizAlertInfoResponse, self).to_map()
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
            temp_model = ReportBizAlertInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


