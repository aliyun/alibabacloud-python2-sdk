# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddImageRequest(TeaModel):
    def __init__(self, category_id=None, crop=None, custom_content=None, instance_name=None, int_attr=None,
                 pic_content=None, pic_name=None, product_id=None, region=None, str_attr=None):
        self.category_id = category_id  # type: int
        self.crop = crop  # type: bool
        self.custom_content = custom_content  # type: str
        self.instance_name = instance_name  # type: str
        self.int_attr = int_attr  # type: int
        self.pic_content = pic_content  # type: str
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str
        self.region = region  # type: str
        self.str_attr = str_attr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region is not None:
            result['Region'] = self.region
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageResponseBodyPicInfo(TeaModel):
    def __init__(self, category_id=None, region=None):
        self.category_id = category_id  # type: int
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageResponseBodyPicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, pic_info=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.pic_info = pic_info  # type: AddImageResponseBodyPicInfo
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super(AddImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PicInfo') is not None:
            temp_model = AddImageResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageResponse, self).to_map()
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, instance_name=None, pic_name=None, product_id=None):
        self.instance_name = instance_name  # type: str
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageResponse, self).to_map()
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageRequest(TeaModel):
    def __init__(self, category_id=None, crop=None, filter=None, instance_name=None, num=None, pic_content=None,
                 pic_name=None, product_id=None, region=None, start=None, type=None):
        self.category_id = category_id  # type: int
        self.crop = crop  # type: bool
        self.filter = filter  # type: str
        self.instance_name = instance_name  # type: str
        self.num = num  # type: int
        self.pic_content = pic_content  # type: str
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str
        self.region = region  # type: str
        self.start = start  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchImageResponseBodyAuctions(TeaModel):
    def __init__(self, category_id=None, custom_content=None, int_attr=None, pic_name=None, product_id=None,
                 score=None, sort_expr_values=None, str_attr=None):
        self.category_id = category_id  # type: int
        self.custom_content = custom_content  # type: str
        self.int_attr = int_attr  # type: int
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str
        self.score = score  # type: float
        self.sort_expr_values = sort_expr_values  # type: str
        self.str_attr = str_attr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageResponseBodyAuctions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class SearchImageResponseBodyHead(TeaModel):
    def __init__(self, docs_found=None, docs_return=None, search_time=None):
        self.docs_found = docs_found  # type: int
        self.docs_return = docs_return  # type: int
        self.search_time = search_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageResponseBodyHead, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: int
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageResponseBodyPicInfoAllCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchImageResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageResponseBodyPicInfoMultiRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageResponseBodyPicInfo(TeaModel):
    def __init__(self, all_categories=None, category_id=None, multi_region=None, region=None):
        self.all_categories = all_categories  # type: list[SearchImageResponseBodyPicInfoAllCategories]
        self.category_id = category_id  # type: int
        self.multi_region = multi_region  # type: list[SearchImageResponseBodyPicInfoMultiRegion]
        self.region = region  # type: str

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageResponseBodyPicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageResponseBody(TeaModel):
    def __init__(self, auctions=None, code=None, head=None, msg=None, pic_info=None, request_id=None, success=None):
        self.auctions = auctions  # type: list[SearchImageResponseBodyAuctions]
        self.code = code  # type: int
        self.head = head  # type: SearchImageResponseBodyHead
        self.msg = msg  # type: str
        self.pic_info = pic_info  # type: SearchImageResponseBodyPicInfo
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super(SearchImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchImageResponse, self).to_map()
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
            temp_model = SearchImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


