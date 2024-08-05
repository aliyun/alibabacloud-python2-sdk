# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class TestStructTestString(TeaModel):
    def __init__(self, abc=None):
        self.abc = abc  # type: bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestStructTestString, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abc is not None:
            result['abc'] = self.abc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('abc') is not None:
            self.abc = m.get('abc')
        return self


class TestStruct(TeaModel):
    def __init__(self, test_string=None):
        self.test_string = test_string  # type: TestStructTestString

    def validate(self):
        if self.test_string:
            self.test_string.validate()

    def to_map(self):
        _map = super(TestStruct, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.test_string is not None:
            result['testString'] = self.test_string.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('testString') is not None:
            temp_model = TestStructTestString()
            self.test_string = temp_model.from_map(m['testString'])
        return self


class GetApiMetaRequest(TeaModel):
    def __init__(self, api_name=None, product_name=None, version=None):
        self.api_name = api_name  # type: str
        self.product_name = product_name  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApiMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetApiMetaResponseBody(TeaModel):
    def __init__(self, api=None, description=None, error_codes=None, extra_info=None, method=None, params=None,
                 path=None, protocol=None, request=None, response=None, response_doc=None, summary=None, timeout=None,
                 title=None, version=None):
        self.api = api  # type: str
        self.description = description  # type: str
        self.error_codes = error_codes  # type: str
        self.extra_info = extra_info  # type: str
        self.method = method  # type: str
        self.params = params  # type: str
        self.path = path  # type: str
        self.protocol = protocol  # type: str
        self.request = request  # type: str
        self.response = response  # type: str
        self.response_doc = response_doc  # type: str
        self.summary = summary  # type: str
        self.timeout = timeout  # type: long
        self.title = title  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApiMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['api'] = self.api
        if self.description is not None:
            result['description'] = self.description
        if self.error_codes is not None:
            result['error_codes'] = self.error_codes
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.method is not None:
            result['method'] = self.method
        if self.params is not None:
            result['params'] = self.params
        if self.path is not None:
            result['path'] = self.path
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.request is not None:
            result['request'] = self.request
        if self.response is not None:
            result['response'] = self.response
        if self.response_doc is not None:
            result['responseDoc'] = self.response_doc
        if self.summary is not None:
            result['summary'] = self.summary
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.title is not None:
            result['title'] = self.title
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('error_codes') is not None:
            self.error_codes = m.get('error_codes')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('request') is not None:
            self.request = m.get('request')
        if m.get('response') is not None:
            self.response = m.get('response')
        if m.get('responseDoc') is not None:
            self.response_doc = m.get('responseDoc')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetApiMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApiMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApiMetaResponse, self).to_map()
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
            temp_model = GetApiMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeCodeRequest(TeaModel):
    def __init__(self, api_name=None, api_style=None, api_version=None, endpoint=None, meta=None, params=None,
                 product=None, sdk_type=None):
        self.api_name = api_name  # type: str
        self.api_style = api_style  # type: str
        self.api_version = api_version  # type: str
        self.endpoint = endpoint  # type: str
        self.meta = meta  # type: str
        self.params = params  # type: str
        self.product = product  # type: str
        self.sdk_type = sdk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_style is not None:
            result['apiStyle'] = self.api_style
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.meta is not None:
            result['meta'] = self.meta
        if self.params is not None:
            result['params'] = self.params
        if self.product is not None:
            result['product'] = self.product
        if self.sdk_type is not None:
            result['sdkType'] = self.sdk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('apiStyle') is not None:
            self.api_style = m.get('apiStyle')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('sdkType') is not None:
            self.sdk_type = m.get('sdkType')
        return self


class MakeCodeResponseBody(TeaModel):
    def __init__(self, request_id=None, sdk_demos=None):
        self.request_id = request_id  # type: str
        self.sdk_demos = sdk_demos  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_demos is not None:
            result['sdkDemos'] = self.sdk_demos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('sdkDemos') is not None:
            self.sdk_demos = m.get('sdkDemos')
        return self


class MakeCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MakeCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MakeCodeResponse, self).to_map()
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
            temp_model = MakeCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchProductRequest(TeaModel):
    def __init__(self, biz_type=None, page=None, page_size=None, query=None, token=None):
        self.biz_type = biz_type  # type: str
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class SearchProductResponseBodyDataList(TeaModel):
    def __init__(self, belong_group=None, default_version=None, description=None, id=None, location_code=None,
                 name=None, search_summary=None, short_name=None, show_name_cn=None, show_name_en=None, status=None):
        self.belong_group = belong_group  # type: str
        self.default_version = default_version  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.location_code = location_code  # type: str
        self.name = name  # type: str
        self.search_summary = search_summary  # type: str
        self.short_name = short_name  # type: str
        self.show_name_cn = show_name_cn  # type: str
        self.show_name_en = show_name_en  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchProductResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belong_group is not None:
            result['belong_group'] = self.belong_group
        if self.default_version is not None:
            result['default_version'] = self.default_version
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.location_code is not None:
            result['location_code'] = self.location_code
        if self.name is not None:
            result['name'] = self.name
        if self.search_summary is not None:
            result['search_summary'] = self.search_summary
        if self.short_name is not None:
            result['short_name'] = self.short_name
        if self.show_name_cn is not None:
            result['show_name_cn'] = self.show_name_cn
        if self.show_name_en is not None:
            result['show_name_en'] = self.show_name_en
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('belong_group') is not None:
            self.belong_group = m.get('belong_group')
        if m.get('default_version') is not None:
            self.default_version = m.get('default_version')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location_code') is not None:
            self.location_code = m.get('location_code')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('search_summary') is not None:
            self.search_summary = m.get('search_summary')
        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')
        if m.get('show_name_cn') is not None:
            self.show_name_cn = m.get('show_name_cn')
        if m.get('show_name_en') is not None:
            self.show_name_en = m.get('show_name_en')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SearchProductResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, pages=None, per_page=None, real_total=None, request_id=None, total=None):
        self.list = list  # type: list[SearchProductResponseBodyDataList]
        self.page = page  # type: long
        self.pages = pages  # type: long
        self.per_page = per_page  # type: long
        self.real_total = real_total  # type: long
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchProductResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page is not None:
            result['page'] = self.page
        if self.pages is not None:
            result['pages'] = self.pages
        if self.per_page is not None:
            result['perPage'] = self.per_page
        if self.real_total is not None:
            result['real_total'] = self.real_total
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = SearchProductResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pages') is not None:
            self.pages = m.get('pages')
        if m.get('perPage') is not None:
            self.per_page = m.get('perPage')
        if m.get('real_total') is not None:
            self.real_total = m.get('real_total')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class SearchProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: SearchProductResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SearchProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = SearchProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SearchProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchProductResponse, self).to_map()
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
            temp_model = SearchProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestOpenApiRequestRequest(TeaModel):
    def __init__(self, api_name=None, api_version=None, meta=None, params=None, product=None):
        self.api_name = api_name  # type: str
        self.api_version = api_version  # type: str
        self.meta = meta  # type: str
        self.params = params  # type: dict[str, any]
        self.product = product  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestOpenApiRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.meta is not None:
            result['meta'] = self.meta
        if self.params is not None:
            result['params'] = self.params
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class TestOpenApiRequestResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: dict[str, str]
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestOpenApiRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['headers'] = self.headers
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class TestOpenApiRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TestOpenApiRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TestOpenApiRequestResponse, self).to_map()
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
            temp_model = TestOpenApiRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


