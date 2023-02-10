# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Box(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(Box, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class AddImageRequest(TeaModel):
    def __init__(self, boxes=None, custom_content=None, detect_limit=None, int_attr=None, pic_content=None,
                 pic_name=None, pic_url=None, str_attr=None):
        self.boxes = boxes  # type: list[Box]
        self.custom_content = custom_content  # type: str
        self.detect_limit = detect_limit  # type: int
        self.int_attr = int_attr  # type: int
        self.pic_content = pic_content  # type: str
        self.pic_name = pic_name  # type: str
        self.pic_url = pic_url  # type: str
        self.str_attr = str_attr  # type: str

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = Box()
                self.boxes.append(temp_model.from_map(k))
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageAdvanceRequest(TeaModel):
    def __init__(self, boxes=None, custom_content=None, detect_limit=None, int_attr=None, pic_content_object=None,
                 pic_name=None, pic_url=None, str_attr=None):
        self.boxes = boxes  # type: list[Box]
        self.custom_content = custom_content  # type: str
        self.detect_limit = detect_limit  # type: int
        self.int_attr = int_attr  # type: int
        self.pic_content_object = pic_content_object  # type: READABLE
        self.pic_name = pic_name  # type: str
        self.pic_url = pic_url  # type: str
        self.str_attr = str_attr  # type: str

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = Box()
                self.boxes.append(temp_model.from_map(k))
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageShrinkRequest(TeaModel):
    def __init__(self, boxes_shrink=None, custom_content=None, detect_limit=None, int_attr=None, pic_content=None,
                 pic_name=None, pic_url=None, str_attr=None):
        self.boxes_shrink = boxes_shrink  # type: str
        self.custom_content = custom_content  # type: str
        self.detect_limit = detect_limit  # type: int
        self.int_attr = int_attr  # type: int
        self.pic_content = pic_content  # type: str
        self.pic_name = pic_name  # type: str
        self.pic_url = pic_url  # type: str
        self.str_attr = str_attr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes_shrink is not None:
            result['Boxes'] = self.boxes_shrink
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes_shrink = m.get('Boxes')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CheckOssIncrementMetaExistRequest(TeaModel):
    def __init__(self, bucket_name=None, key=None, oss_path=None):
        # oss bucket
        self.bucket_name = bucket_name  # type: str
        self.key = key  # type: str
        # oss path
        self.oss_path = oss_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckOssIncrementMetaExistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.key is not None:
            result['Key'] = self.key
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class CheckOssIncrementMetaExistResponseBodyData(TeaModel):
    def __init__(self, exist=None):
        self.exist = exist  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckOssIncrementMetaExistResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist is not None:
            result['Exist'] = self.exist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        return self


class CheckOssIncrementMetaExistResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: CheckOssIncrementMetaExistResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckOssIncrementMetaExistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckOssIncrementMetaExistResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckOssIncrementMetaExistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckOssIncrementMetaExistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckOssIncrementMetaExistResponse, self).to_map()
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
            temp_model = CheckOssIncrementMetaExistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBatchTasksRequest(TeaModel):
    def __init__(self, bucket_name=None, callback_address=None, oss_path=None):
        # oss bucket
        self.bucket_name = bucket_name  # type: str
        self.callback_address = callback_address  # type: str
        # oss path
        self.oss_path = oss_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBatchTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class CreateBatchTasksResponseBodyData(TeaModel):
    def __init__(self, id=None, status=None):
        self.id = id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBatchTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateBatchTasksResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: CreateBatchTasksResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateBatchTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateBatchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBatchTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBatchTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBatchTasksResponse, self).to_map()
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
            temp_model = CreateBatchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDumpMetaResponseBodyData(TeaModel):
    def __init__(self, id=None, status=None):
        self.id = id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDumpMetaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateDumpMetaResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: CreateDumpMetaResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateDumpMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDumpMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDumpMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDumpMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDumpMetaResponse, self).to_map()
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
            temp_model = CreateDumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, pic_name=None):
        self.pic_name = pic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        return self


class DeleteImageResponseBodyData(TeaModel):
    def __init__(self, pic_names=None):
        self.pic_names = pic_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_names is not None:
            result['PicNames'] = self.pic_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicNames') is not None:
            self.pic_names = m.get('PicNames')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DeleteImageResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetImageRequest(TeaModel):
    def __init__(self, pic_name=None):
        self.pic_name = pic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        return self


class GetImageResponseBodyDataBoxes(TeaModel):
    def __init__(self, bbox=None, confidence=None):
        self.bbox = bbox  # type: list[int]
        self.confidence = confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyDataBoxes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class GetImageResponseBodyData(TeaModel):
    def __init__(self, boxes=None, custom_content=None, int_attr=None, pic_name=None, product_id=None, str_attr=None):
        self.boxes = boxes  # type: list[GetImageResponseBodyDataBoxes]
        self.custom_content = custom_content  # type: str
        self.int_attr = int_attr  # type: int
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str
        self.str_attr = str_attr  # type: str

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = GetImageResponseBodyDataBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: GetImageResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageResponse, self).to_map()
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyData(TeaModel):
    def __init__(self, capacity=None, instance_id=None, instance_name=None, qps=None, region=None, service_type=None,
                 status=None, total_count=None, utc_create_time=None, utc_expire_time=None):
        self.capacity = capacity  # type: int
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.qps = qps  # type: str
        self.region = region  # type: str
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.total_count = total_count  # type: long
        self.utc_create_time = utc_create_time  # type: long
        self.utc_expire_time = utc_expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: GetInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBatchTasksRequest(TeaModel):
    def __init__(self, bucket_name=None, id=None, oss_path=None, page_number=None, page_size=None):
        # oss bucket
        self.bucket_name = bucket_name  # type: str
        self.id = id  # type: long
        # oss path
        self.oss_path = oss_path  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBatchTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListBatchTasksResponseBodyDataIncrements(TeaModel):
    def __init__(self, bucket_name=None, callback_address=None, callback_task_status=None, error_url=None, id=None,
                 msg=None, oss_path=None, status=None, utc_create_time=None, utc_update_time=None):
        self.bucket_name = bucket_name  # type: str
        self.callback_address = callback_address  # type: str
        self.callback_task_status = callback_task_status  # type: str
        self.error_url = error_url  # type: str
        self.id = id  # type: long
        self.msg = msg  # type: str
        self.oss_path = oss_path  # type: str
        self.status = status  # type: str
        self.utc_create_time = utc_create_time  # type: str
        self.utc_update_time = utc_update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBatchTasksResponseBodyDataIncrements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.callback_task_status is not None:
            result['CallbackTaskStatus'] = self.callback_task_status
        if self.error_url is not None:
            result['ErrorUrl'] = self.error_url
        if self.id is not None:
            result['Id'] = self.id
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_update_time is not None:
            result['UtcUpdateTime'] = self.utc_update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('CallbackTaskStatus') is not None:
            self.callback_task_status = m.get('CallbackTaskStatus')
        if m.get('ErrorUrl') is not None:
            self.error_url = m.get('ErrorUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcUpdateTime') is not None:
            self.utc_update_time = m.get('UtcUpdateTime')
        return self


class ListBatchTasksResponseBodyData(TeaModel):
    def __init__(self, increments=None, page_number=None, page_size=None, total=None):
        self.increments = increments  # type: list[ListBatchTasksResponseBodyDataIncrements]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.increments:
            for k in self.increments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBatchTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Increments'] = []
        if self.increments is not None:
            for k in self.increments:
                result['Increments'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.increments = []
        if m.get('Increments') is not None:
            for k in m.get('Increments'):
                temp_model = ListBatchTasksResponseBodyDataIncrements()
                self.increments.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListBatchTasksResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: ListBatchTasksResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListBatchTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListBatchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBatchTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBatchTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBatchTasksResponse, self).to_map()
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
            temp_model = ListBatchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDumpMetaRequest(TeaModel):
    def __init__(self, id=None, page_number=None, page_size=None):
        self.id = id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDumpMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDumpMetaResponseBodyDataDumpMetaList(TeaModel):
    def __init__(self, id=None, meta_url=None, msg=None, status=None, utc_create_time=None, utc_update_time=None):
        self.id = id  # type: long
        self.meta_url = meta_url  # type: str
        self.msg = msg  # type: str
        self.status = status  # type: str
        self.utc_create_time = utc_create_time  # type: str
        self.utc_update_time = utc_update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDumpMetaResponseBodyDataDumpMetaList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_update_time is not None:
            result['UtcUpdateTime'] = self.utc_update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcUpdateTime') is not None:
            self.utc_update_time = m.get('UtcUpdateTime')
        return self


class ListDumpMetaResponseBodyData(TeaModel):
    def __init__(self, dump_meta_list=None, page_number=None, page_size=None, total=None):
        self.dump_meta_list = dump_meta_list  # type: list[ListDumpMetaResponseBodyDataDumpMetaList]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.dump_meta_list:
            for k in self.dump_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDumpMetaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DumpMetaList'] = []
        if self.dump_meta_list is not None:
            for k in self.dump_meta_list:
                result['DumpMetaList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dump_meta_list = []
        if m.get('DumpMetaList') is not None:
            for k in m.get('DumpMetaList'):
                temp_model = ListDumpMetaResponseBodyDataDumpMetaList()
                self.dump_meta_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDumpMetaResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: ListDumpMetaResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDumpMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDumpMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDumpMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDumpMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDumpMetaResponse, self).to_map()
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
            temp_model = ListDumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, page_number=None, page_size=None, service_type=None):
        self.instance_name = instance_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListInstanceResponseBodyDataInstances(TeaModel):
    def __init__(self, capacity=None, instance_id=None, instance_name=None, qps=None, region=None, service_type=None,
                 status=None, utc_create_time=None, utc_expire_time=None):
        self.capacity = capacity  # type: int
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.qps = qps  # type: str
        self.region = region  # type: str
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.utc_create_time = utc_create_time  # type: long
        self.utc_expire_time = utc_expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyDataInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class ListInstanceResponseBodyData(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, total=None):
        self.instances = instances  # type: list[ListInstanceResponseBodyDataInstances]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: ListInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceResponse, self).to_map()
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOssBucketAndPathRequest(TeaModel):
    def __init__(self, bucket_name=None, oss_path=None):
        self.bucket_name = bucket_name  # type: str
        self.oss_path = oss_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOssBucketAndPathRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class ListOssBucketAndPathResponseBodyData(TeaModel):
    def __init__(self, bucket_list=None, path_list=None):
        self.bucket_list = bucket_list  # type: list[str]
        self.path_list = path_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOssBucketAndPathResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_list is not None:
            result['BucketList'] = self.bucket_list
        if self.path_list is not None:
            result['PathList'] = self.path_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketList') is not None:
            self.bucket_list = m.get('BucketList')
        if m.get('PathList') is not None:
            self.path_list = m.get('PathList')
        return self


class ListOssBucketAndPathResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: ListOssBucketAndPathResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListOssBucketAndPathResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListOssBucketAndPathResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOssBucketAndPathResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOssBucketAndPathResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOssBucketAndPathResponse, self).to_map()
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
            temp_model = ListOssBucketAndPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetInstanceResponseBodyData(TeaModel):
    def __init__(self, capacity=None, instance_id=None, instance_name=None, service_type=None, status=None,
                 utc_create_time=None, utc_expire_time=None):
        self.capacity = capacity  # type: int
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.utc_create_time = utc_create_time  # type: long
        self.utc_expire_time = utc_expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class ResetInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: ResetInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ResetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ResetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetInstanceResponse, self).to_map()
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
            temp_model = ResetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByNameRequest(TeaModel):
    def __init__(self, filter=None, num=None, pic_name=None, product_id=None, start=None, text=None):
        self.filter = filter  # type: str
        self.num = num  # type: int
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str
        self.start = start  # type: int
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByNameResponseBodyDataPicInfos(TeaModel):
    def __init__(self, bbox=None, confidence=None):
        self.bbox = bbox  # type: list[int]
        self.confidence = confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyDataPicInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByNameResponseBodyDataPicListOtherBoxes(TeaModel):
    def __init__(self, bbox=None, confidence=None):
        self.bbox = bbox  # type: list[int]
        self.confidence = confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyDataPicListOtherBoxes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByNameResponseBodyDataPicListSimilarBoxes(TeaModel):
    def __init__(self, bbox=None, confidence=None, score=None):
        self.bbox = bbox  # type: list[int]
        self.confidence = confidence  # type: float
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyDataPicListSimilarBoxes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchImageByNameResponseBodyDataPicList(TeaModel):
    def __init__(self, custom_content=None, int_attr=None, other_boxes=None, pic_name=None, product_id=None,
                 score=None, similar_boxes=None, str_attr=None):
        self.custom_content = custom_content  # type: str
        self.int_attr = int_attr  # type: int
        self.other_boxes = other_boxes  # type: list[SearchImageByNameResponseBodyDataPicListOtherBoxes]
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str
        self.score = score  # type: float
        self.similar_boxes = similar_boxes  # type: list[SearchImageByNameResponseBodyDataPicListSimilarBoxes]
        self.str_attr = str_attr  # type: str

    def validate(self):
        if self.other_boxes:
            for k in self.other_boxes:
                if k:
                    k.validate()
        if self.similar_boxes:
            for k in self.similar_boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyDataPicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        result['OtherBoxes'] = []
        if self.other_boxes is not None:
            for k in self.other_boxes:
                result['OtherBoxes'].append(k.to_map() if k else None)
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        result['SimilarBoxes'] = []
        if self.similar_boxes is not None:
            for k in self.similar_boxes:
                result['SimilarBoxes'].append(k.to_map() if k else None)
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        self.other_boxes = []
        if m.get('OtherBoxes') is not None:
            for k in m.get('OtherBoxes'):
                temp_model = SearchImageByNameResponseBodyDataPicListOtherBoxes()
                self.other_boxes.append(temp_model.from_map(k))
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.similar_boxes = []
        if m.get('SimilarBoxes') is not None:
            for k in m.get('SimilarBoxes'):
                temp_model = SearchImageByNameResponseBodyDataPicListSimilarBoxes()
                self.similar_boxes.append(temp_model.from_map(k))
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class SearchImageByNameResponseBodyData(TeaModel):
    def __init__(self, pic_infos=None, pic_list=None):
        self.pic_infos = pic_infos  # type: list[SearchImageByNameResponseBodyDataPicInfos]
        self.pic_list = pic_list  # type: list[SearchImageByNameResponseBodyDataPicList]

    def validate(self):
        if self.pic_infos:
            for k in self.pic_infos:
                if k:
                    k.validate()
        if self.pic_list:
            for k in self.pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PicInfos'] = []
        if self.pic_infos is not None:
            for k in self.pic_infos:
                result['PicInfos'].append(k.to_map() if k else None)
        result['PicList'] = []
        if self.pic_list is not None:
            for k in self.pic_list:
                result['PicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.pic_infos = []
        if m.get('PicInfos') is not None:
            for k in m.get('PicInfos'):
                temp_model = SearchImageByNameResponseBodyDataPicInfos()
                self.pic_infos.append(temp_model.from_map(k))
        self.pic_list = []
        if m.get('PicList') is not None:
            for k in m.get('PicList'):
                temp_model = SearchImageByNameResponseBodyDataPicList()
                self.pic_list.append(temp_model.from_map(k))
        return self


class SearchImageByNameResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: SearchImageByNameResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SearchImageByNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SearchImageByNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchImageByNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchImageByNameResponse, self).to_map()
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
            temp_model = SearchImageByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByPicRequest(TeaModel):
    def __init__(self, box=None, detect_limit=None, filter=None, num=None, pic_content=None, pic_url=None, start=None,
                 text=None):
        self.box = box  # type: Box
        self.detect_limit = detect_limit  # type: int
        self.filter = filter  # type: str
        self.num = num  # type: int
        self.pic_content = pic_content  # type: str
        self.pic_url = pic_url  # type: str
        self.start = start  # type: int
        self.text = text  # type: str

    def validate(self):
        if self.box:
            self.box.validate()

    def to_map(self):
        _map = super(SearchImageByPicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box.to_map()
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Box') is not None:
            temp_model = Box()
            self.box = temp_model.from_map(m['Box'])
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByPicAdvanceRequest(TeaModel):
    def __init__(self, box=None, detect_limit=None, filter=None, num=None, pic_content_object=None, pic_url=None,
                 start=None, text=None):
        self.box = box  # type: Box
        self.detect_limit = detect_limit  # type: int
        self.filter = filter  # type: str
        self.num = num  # type: int
        self.pic_content_object = pic_content_object  # type: READABLE
        self.pic_url = pic_url  # type: str
        self.start = start  # type: int
        self.text = text  # type: str

    def validate(self):
        if self.box:
            self.box.validate()

    def to_map(self):
        _map = super(SearchImageByPicAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box.to_map()
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Box') is not None:
            temp_model = Box()
            self.box = temp_model.from_map(m['Box'])
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByPicShrinkRequest(TeaModel):
    def __init__(self, box_shrink=None, detect_limit=None, filter=None, num=None, pic_content=None, pic_url=None,
                 start=None, text=None):
        self.box_shrink = box_shrink  # type: str
        self.detect_limit = detect_limit  # type: int
        self.filter = filter  # type: str
        self.num = num  # type: int
        self.pic_content = pic_content  # type: str
        self.pic_url = pic_url  # type: str
        self.start = start  # type: int
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box_shrink is not None:
            result['Box'] = self.box_shrink
        if self.detect_limit is not None:
            result['DetectLimit'] = self.detect_limit
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Box') is not None:
            self.box_shrink = m.get('Box')
        if m.get('DetectLimit') is not None:
            self.detect_limit = m.get('DetectLimit')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByPicResponseBodyDataPicInfos(TeaModel):
    def __init__(self, bbox=None, confidence=None):
        self.bbox = bbox  # type: list[int]
        self.confidence = confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyDataPicInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByPicResponseBodyDataPicListOtherBoxes(TeaModel):
    def __init__(self, bbox=None, confidence=None):
        self.bbox = bbox  # type: list[int]
        self.confidence = confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyDataPicListOtherBoxes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class SearchImageByPicResponseBodyDataPicListSimilarBoxes(TeaModel):
    def __init__(self, bbox=None, confidence=None, score=None):
        self.bbox = bbox  # type: list[int]
        self.confidence = confidence  # type: float
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyDataPicListSimilarBoxes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchImageByPicResponseBodyDataPicList(TeaModel):
    def __init__(self, custom_content=None, int_attr=None, other_boxes=None, pic_name=None, product_id=None,
                 score=None, similar_boxes=None, str_attr=None):
        self.custom_content = custom_content  # type: str
        self.int_attr = int_attr  # type: int
        self.other_boxes = other_boxes  # type: list[SearchImageByPicResponseBodyDataPicListOtherBoxes]
        self.pic_name = pic_name  # type: str
        self.product_id = product_id  # type: str
        self.score = score  # type: float
        self.similar_boxes = similar_boxes  # type: list[SearchImageByPicResponseBodyDataPicListSimilarBoxes]
        self.str_attr = str_attr  # type: str

    def validate(self):
        if self.other_boxes:
            for k in self.other_boxes:
                if k:
                    k.validate()
        if self.similar_boxes:
            for k in self.similar_boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyDataPicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        result['OtherBoxes'] = []
        if self.other_boxes is not None:
            for k in self.other_boxes:
                result['OtherBoxes'].append(k.to_map() if k else None)
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        result['SimilarBoxes'] = []
        if self.similar_boxes is not None:
            for k in self.similar_boxes:
                result['SimilarBoxes'].append(k.to_map() if k else None)
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        self.other_boxes = []
        if m.get('OtherBoxes') is not None:
            for k in m.get('OtherBoxes'):
                temp_model = SearchImageByPicResponseBodyDataPicListOtherBoxes()
                self.other_boxes.append(temp_model.from_map(k))
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.similar_boxes = []
        if m.get('SimilarBoxes') is not None:
            for k in m.get('SimilarBoxes'):
                temp_model = SearchImageByPicResponseBodyDataPicListSimilarBoxes()
                self.similar_boxes.append(temp_model.from_map(k))
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class SearchImageByPicResponseBodyData(TeaModel):
    def __init__(self, pic_infos=None, pic_list=None):
        self.pic_infos = pic_infos  # type: list[SearchImageByPicResponseBodyDataPicInfos]
        self.pic_list = pic_list  # type: list[SearchImageByPicResponseBodyDataPicList]

    def validate(self):
        if self.pic_infos:
            for k in self.pic_infos:
                if k:
                    k.validate()
        if self.pic_list:
            for k in self.pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PicInfos'] = []
        if self.pic_infos is not None:
            for k in self.pic_infos:
                result['PicInfos'].append(k.to_map() if k else None)
        result['PicList'] = []
        if self.pic_list is not None:
            for k in self.pic_list:
                result['PicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.pic_infos = []
        if m.get('PicInfos') is not None:
            for k in m.get('PicInfos'):
                temp_model = SearchImageByPicResponseBodyDataPicInfos()
                self.pic_infos.append(temp_model.from_map(k))
        self.pic_list = []
        if m.get('PicList') is not None:
            for k in m.get('PicList'):
                temp_model = SearchImageByPicResponseBodyDataPicList()
                self.pic_list.append(temp_model.from_map(k))
        return self


class SearchImageByPicResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: SearchImageByPicResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SearchImageByPicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SearchImageByPicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByPicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchImageByPicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchImageByPicResponse, self).to_map()
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
            temp_model = SearchImageByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBatchTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopBatchTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopBatchTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopBatchTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopBatchTasksResponse, self).to_map()
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
            temp_model = StopBatchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDumpMetaResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDumpMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopDumpMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopDumpMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDumpMetaResponse, self).to_map()
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
            temp_model = StopDumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(self, custom_content=None, int_attr=None, pic_name=None, str_attr=None):
        self.custom_content = custom_content  # type: str
        self.int_attr = int_attr  # type: int
        self.pic_name = pic_name  # type: str
        self.str_attr = str_attr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateImageResponse, self).to_map()
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
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


