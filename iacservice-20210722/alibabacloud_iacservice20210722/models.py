# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateResourceRequest(TeaModel):
    def __init__(self, body=None, resource_type_version=None):
        self.body = body  # type: str
        self.resource_type_version = resource_type_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_id=None, task_id=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 资源id
        self.resource_id = resource_id  # type: str
        # 任务id
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceResponse, self).to_map()
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
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRequest(TeaModel):
    def __init__(self, region_id=None, resource_type_version=None):
        self.region_id = region_id  # type: str
        self.resource_type_version = resource_type_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceResponse, self).to_map()
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
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetResourceResponseBodyResource(TeaModel):
    def __init__(self, product_code=None, region_id=None, resource_attributes=None, resource_id=None,
                 resource_type_code=None):
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str
        self.resource_attributes = resource_attributes  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type_code = resource_type_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceResponseBodyResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        return self


class GetResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, resource=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.resource = resource  # type: GetResourceResponseBodyResource

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super(GetResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resource') is not None:
            temp_model = GetResourceResponseBodyResource()
            self.resource = temp_model.from_map(m['resource'])
        return self


class GetResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceResponse, self).to_map()
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
            temp_model = GetResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBodyTaskError(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskError, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetTaskResponseBodyTask(TeaModel):
    def __init__(self, create_time=None, error=None, product_code=None, resource_id=None, resource_type_code=None,
                 retry_after=None, status=None, task_action=None, task_id=None):
        self.create_time = create_time  # type: str
        self.error = error  # type: GetTaskResponseBodyTaskError
        self.product_code = product_code  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type_code = resource_type_code  # type: str
        self.retry_after = retry_after  # type: int
        self.status = status  # type: str
        self.task_action = task_action  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        _map = super(GetTaskResponseBodyTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.error is not None:
            result['error'] = self.error.to_map()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        if self.retry_after is not None:
            result['retryAfter'] = self.retry_after
        if self.status is not None:
            result['status'] = self.status
        if self.task_action is not None:
            result['taskAction'] = self.task_action
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('error') is not None:
            temp_model = GetTaskResponseBodyTaskError()
            self.error = temp_model.from_map(m['error'])
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        if m.get('retryAfter') is not None:
            self.retry_after = m.get('retryAfter')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.task = task  # type: GetTaskResponseBodyTask

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super(GetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResponse, self).to_map()
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
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(self, filter=None):
        self.filter = filter  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        return self


class ListDataSourcesShrinkRequest(TeaModel):
    def __init__(self, filter_shrink=None):
        self.filter_shrink = filter_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        return self


class ListDataSourcesResponseBodyDataSources(TeaModel):
    def __init__(self, data_source_attributes=None, id=None):
        self.data_source_attributes = data_source_attributes  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesResponseBodyDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_attributes is not None:
            result['dataSourceAttributes'] = self.data_source_attributes
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSourceAttributes') is not None:
            self.data_source_attributes = m.get('dataSourceAttributes')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(self, data_sources=None, request_id=None):
        self.data_sources = data_sources  # type: list[ListDataSourcesResponseBodyDataSources]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = ListDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponse, self).to_map()
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListProductsResponseBodyProductsProductName(TeaModel):
    def __init__(self, en_us=None, zh_cn=None):
        self.en_us = en_us  # type: str
        self.zh_cn = zh_cn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsResponseBodyProductsProductName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.en_us is not None:
            result['en_US'] = self.en_us
        if self.zh_cn is not None:
            result['zh_CN'] = self.zh_cn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('en_US') is not None:
            self.en_us = m.get('en_US')
        if m.get('zh_CN') is not None:
            self.zh_cn = m.get('zh_CN')
        return self


class ListProductsResponseBodyProducts(TeaModel):
    def __init__(self, product_code=None, product_name=None):
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: ListProductsResponseBodyProductsProductName

    def validate(self):
        if self.product_name:
            self.product_name.validate()

    def to_map(self):
        _map = super(ListProductsResponseBodyProducts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_name is not None:
            result['productName'] = self.product_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productName') is not None:
            temp_model = ListProductsResponseBodyProductsProductName()
            self.product_name = temp_model.from_map(m['productName'])
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, products=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: long
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        self.products = products  # type: list[ListProductsResponseBodyProducts]
        # Id of the request
        self.request_id = request_id  # type: str
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: long

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['products'] = []
        if self.products is not None:
            for k in self.products:
                result['products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.products = []
        if m.get('products') is not None:
            for k in m.get('products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProductsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductsResponse, self).to_map()
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_type_codes=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.resource_type_codes = resource_type_codes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_type_codes is not None:
            result['resourceTypeCodes'] = self.resource_type_codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes = m.get('resourceTypeCodes')
        return self


class ListResourceTypesShrinkRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_type_codes_shrink=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.resource_type_codes_shrink = resource_type_codes_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_type_codes_shrink is not None:
            result['resourceTypeCodes'] = self.resource_type_codes_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes_shrink = m.get('resourceTypeCodes')
        return self


class ListResourceTypesResponseBodyResourceTypesIdentityDefinition(TeaModel):
    def __init__(self, arn_pattern=None, second_unique_key_fields=None, unique_key_fields=None):
        # 资源ARN
        self.arn_pattern = arn_pattern  # type: str
        # 备选Id字段列表，有顺序
        self.second_unique_key_fields = second_unique_key_fields  # type: list[str]
        # uniqueKey的字段列表，有顺序
        self.unique_key_fields = unique_key_fields  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesIdentityDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn_pattern is not None:
            result['arnPattern'] = self.arn_pattern
        if self.second_unique_key_fields is not None:
            result['secondUniqueKeyFields'] = self.second_unique_key_fields
        if self.unique_key_fields is not None:
            result['uniqueKeyFields'] = self.unique_key_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arnPattern') is not None:
            self.arn_pattern = m.get('arnPattern')
        if m.get('secondUniqueKeyFields') is not None:
            self.second_unique_key_fields = m.get('secondUniqueKeyFields')
        if m.get('uniqueKeyFields') is not None:
            self.unique_key_fields = m.get('uniqueKeyFields')
        return self


class ListResourceTypesResponseBodyResourceTypesInfo(TeaModel):
    def __init__(self, available_sites=None, category=None, charge_type=None, delivery_scope=None, description=None,
                 title=None):
        # 允许资源展示的站点  枚举:china(中国站)/intl(国际站)/japan(日本站)
        self.available_sites = available_sites  # type: list[str]
        # 资源分类 枚举:normal(普通资源)/singleton(单例资源)/virtual(虚拟资源)/readonly(只读资源)
        self.category = category  # type: str
        # 付费形式  枚举:paid(付费)/free(免费)
        self.charge_type = charge_type  # type: str
        # 交付级别 枚举:center(中心化部署级别)/region(地域部署级别)/zone(可用区部署级别)
        self.delivery_scope = delivery_scope  # type: str
        # 描述
        self.description = description  # type: str
        # 资源类型的中文名称，如实例
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_sites is not None:
            result['availableSites'] = self.available_sites
        if self.category is not None:
            result['category'] = self.category
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.delivery_scope is not None:
            result['deliveryScope'] = self.delivery_scope
        if self.description is not None:
            result['description'] = self.description
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('availableSites') is not None:
            self.available_sites = m.get('availableSites')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('deliveryScope') is not None:
            self.delivery_scope = m.get('deliveryScope')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListResourceTypesResponseBodyResourceTypesResourceRelations(TeaModel):
    def __init__(self, description=None, product=None, relation=None, resource_type=None):
        # 资源关系描述 枚举：枚举:关联关系/依赖关系/子父关系
        self.description = description  # type: str
        # 云产品B
        self.product = product  # type: str
        # 资源关系  枚举:relevance(关联关系)/dependency(依赖关系)/childParent(子父关系)
        self.relation = relation  # type: str
        # 资源类型B
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesResourceRelations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.product is not None:
            result['product'] = self.product
        if self.relation is not None:
            result['relation'] = self.relation
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('relation') is not None:
            self.relation = m.get('relation')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListResourceTypesResponseBodyResourceTypesStatusDefinition(TeaModel):
    def __init__(self, code=None, description=None, type=None):
        # 状态code
        self.code = code  # type: str
        # 描述
        self.description = description  # type: str
        # 资源状态分类，必须对代表资源创建后的初始状态进行initial标识。枚举:initial(初始状态)
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesStatusDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListResourceTypesResponseBodyResourceTypes(TeaModel):
    def __init__(self, identity_definition=None, info=None, product_code=None, resource_properties=None,
                 resource_relations=None, resource_type_code=None, status_definition=None):
        self.identity_definition = identity_definition  # type: ListResourceTypesResponseBodyResourceTypesIdentityDefinition
        self.info = info  # type: ListResourceTypesResponseBodyResourceTypesInfo
        self.product_code = product_code  # type: str
        self.resource_properties = resource_properties  # type: str
        self.resource_relations = resource_relations  # type: list[ListResourceTypesResponseBodyResourceTypesResourceRelations]
        self.resource_type_code = resource_type_code  # type: str
        self.status_definition = status_definition  # type: list[ListResourceTypesResponseBodyResourceTypesStatusDefinition]

    def validate(self):
        if self.identity_definition:
            self.identity_definition.validate()
        if self.info:
            self.info.validate()
        if self.resource_relations:
            for k in self.resource_relations:
                if k:
                    k.validate()
        if self.status_definition:
            for k in self.status_definition:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_definition is not None:
            result['identityDefinition'] = self.identity_definition.to_map()
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_properties is not None:
            result['resourceProperties'] = self.resource_properties
        result['resourceRelations'] = []
        if self.resource_relations is not None:
            for k in self.resource_relations:
                result['resourceRelations'].append(k.to_map() if k else None)
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        result['statusDefinition'] = []
        if self.status_definition is not None:
            for k in self.status_definition:
                result['statusDefinition'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identityDefinition') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesIdentityDefinition()
            self.identity_definition = temp_model.from_map(m['identityDefinition'])
        if m.get('info') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceProperties') is not None:
            self.resource_properties = m.get('resourceProperties')
        self.resource_relations = []
        if m.get('resourceRelations') is not None:
            for k in m.get('resourceRelations'):
                temp_model = ListResourceTypesResponseBodyResourceTypesResourceRelations()
                self.resource_relations.append(temp_model.from_map(k))
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        self.status_definition = []
        if m.get('statusDefinition') is not None:
            for k in m.get('statusDefinition'):
                temp_model = ListResourceTypesResponseBodyResourceTypesStatusDefinition()
                self.status_definition.append(temp_model.from_map(k))
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, resource_types=None, total_count=None):
        self.max_results = max_results  # type: long
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.resource_types = resource_types  # type: list[ListResourceTypesResponseBodyResourceTypes]
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: long

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['resourceTypes'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resource_types = []
        if m.get('resourceTypes') is not None:
            for k in m.get('resourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponse, self).to_map()
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
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_roag_cache=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_roag_cache = x_roag_cache  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_roag_cache is not None:
            result['x-roag-cache'] = self.x_roag_cache
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-roag-cache') is not None:
            self.x_roag_cache = m.get('x-roag-cache')
        return self


class ListResourcesRequest(TeaModel):
    def __init__(self, data_type=None, filter=None, max_results=None, next_token=None, page_num=None, page_size=None,
                 region_ids=None):
        self.data_type = data_type  # type: str
        self.filter = filter  # type: dict[str, any]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.region_ids = region_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.filter is not None:
            result['filter'] = self.filter
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        return self


class ListResourcesShrinkRequest(TeaModel):
    def __init__(self, data_type=None, filter_shrink=None, max_results=None, next_token=None, page_num=None,
                 page_size=None, region_ids_shrink=None):
        self.data_type = data_type  # type: str
        self.filter_shrink = filter_shrink  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.region_ids_shrink = region_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_ids_shrink is not None:
            result['regionIds'] = self.region_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionIds') is not None:
            self.region_ids_shrink = m.get('regionIds')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(self, product_code=None, region_id=None, resource_attributes=None, resource_id=None,
                 resource_type_code=None):
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str
        self.resource_attributes = resource_attributes  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type_code = resource_type_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, page_num=None, page_size=None, request_id=None,
                 resources=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[ListResourcesResponseBodyResources]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourcesResponse, self).to_map()
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
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, task_ids=None):
        # 本次读取的最大数据记录数量
        self.max_results = max_results  # type: int
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 任务Id列表
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, task_ids_shrink=None):
        # 本次读取的最大数据记录数量
        self.max_results = max_results  # type: int
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 任务Id列表
        self.task_ids_shrink = task_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.task_ids_shrink is not None:
            result['taskIds'] = self.task_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('taskIds') is not None:
            self.task_ids_shrink = m.get('taskIds')
        return self


class ListTasksResponseBodyTasksError(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyTasksError, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(self, create_time=None, error=None, product_code=None, resource_id=None, resource_type_code=None,
                 retry_after=None, status=None, task_action=None, task_id=None):
        self.create_time = create_time  # type: str
        self.error = error  # type: ListTasksResponseBodyTasksError
        self.product_code = product_code  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type_code = resource_type_code  # type: str
        self.retry_after = retry_after  # type: int
        self.status = status  # type: str
        self.task_action = task_action  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        _map = super(ListTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.error is not None:
            result['error'] = self.error.to_map()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        if self.retry_after is not None:
            result['retryAfter'] = self.retry_after
        if self.status is not None:
            result['status'] = self.status
        if self.task_action is not None:
            result['taskAction'] = self.task_action
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('error') is not None:
            temp_model = ListTasksResponseBodyTasksError()
            self.error = temp_model.from_map(m['error'])
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        if m.get('retryAfter') is not None:
            self.retry_after = m.get('retryAfter')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, tasks=None, total_count=None):
        # maxResults本次请求所返回的最大记录条数
        self.max_results = max_results  # type: int
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[ListTasksResponseBodyTasks]
        # totalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTasksResponse, self).to_map()
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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReloadResourcesRequest(TeaModel):
    def __init__(self, region_ids=None):
        self.region_ids = region_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReloadResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        return self


class ReloadResourcesShrinkRequest(TeaModel):
    def __init__(self, region_ids_shrink=None):
        self.region_ids_shrink = region_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReloadResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids_shrink is not None:
            result['regionIds'] = self.region_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids_shrink = m.get('regionIds')
        return self


class ReloadResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReloadResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ReloadResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReloadResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReloadResourcesResponse, self).to_map()
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
            temp_model = ReloadResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(self, body=None, resource_type_version=None):
        self.body = body  # type: str
        self.resource_type_version = resource_type_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.resource_type_version is not None:
            result['resourceTypeVersion'] = self.resource_type_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('resourceTypeVersion') is not None:
            self.resource_type_version = m.get('resourceTypeVersion')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # 请求id
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceResponse, self).to_map()
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
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


