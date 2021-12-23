# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AePredictCategoryRequest(TeaModel):
    def __init__(self, pic_url=None):
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AePredictCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class AePredictCategoryAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None):
        self.pic_url_object = pic_url_object  # type: READABLE

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(AePredictCategoryAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url_object is not None:
            result['PicUrlObject'] = self.pic_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrlObject') is not None:
            self.pic_url_object = m.get('PicUrlObject')
        return self


class AePredictCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(AePredictCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class AePropRecRequest(TeaModel):
    def __init__(self, pic_url=None):
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AePropRecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class AePropRecAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None):
        self.pic_url_object = pic_url_object  # type: READABLE

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(AePropRecAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url_object is not None:
            result['PicUrlObject'] = self.pic_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrlObject') is not None:
            self.pic_url_object = m.get('PicUrlObject')
        return self


class AePropRecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(AePropRecResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateImageAmazonTaskRequest(TeaModel):
    def __init__(self, gif=None, img_url_list=None, template_mode=None, text_list=None):
        self.gif = gif  # type: bool
        self.img_url_list = img_url_list  # type: list[str]
        self.template_mode = template_mode  # type: str
        self.text_list = text_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageAmazonTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gif is not None:
            result['Gif'] = self.gif
        if self.img_url_list is not None:
            result['ImgUrlList'] = self.img_url_list
        if self.template_mode is not None:
            result['TemplateMode'] = self.template_mode
        if self.text_list is not None:
            result['TextList'] = self.text_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gif') is not None:
            self.gif = m.get('Gif')
        if m.get('ImgUrlList') is not None:
            self.img_url_list = m.get('ImgUrlList')
        if m.get('TemplateMode') is not None:
            self.template_mode = m.get('TemplateMode')
        if m.get('TextList') is not None:
            self.text_list = m.get('TextList')
        return self


class CreateImageAmazonTaskShrinkRequest(TeaModel):
    def __init__(self, gif=None, img_url_list_shrink=None, template_mode=None, text_list_shrink=None):
        self.gif = gif  # type: bool
        self.img_url_list_shrink = img_url_list_shrink  # type: str
        self.template_mode = template_mode  # type: str
        self.text_list_shrink = text_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageAmazonTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gif is not None:
            result['Gif'] = self.gif
        if self.img_url_list_shrink is not None:
            result['ImgUrlList'] = self.img_url_list_shrink
        if self.template_mode is not None:
            result['TemplateMode'] = self.template_mode
        if self.text_list_shrink is not None:
            result['TextList'] = self.text_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gif') is not None:
            self.gif = m.get('Gif')
        if m.get('ImgUrlList') is not None:
            self.img_url_list_shrink = m.get('ImgUrlList')
        if m.get('TemplateMode') is not None:
            self.template_mode = m.get('TemplateMode')
        if m.get('TextList') is not None:
            self.text_list_shrink = m.get('TextList')
        return self


class CreateImageAmazonTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success_response=None):
        self.code = code  # type: long
        self.data = data  # type: long
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success_response = success_response  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageAmazonTaskResponseBody, self).to_map()
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
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
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
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class CreateImageAmazonTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateImageAmazonTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageAmazonTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImageAmazonTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResultRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResultRequest, self).to_map()
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


class GetTaskResultResponseBodyData(TeaModel):
    def __init__(self, resuslt=None, status=None, status_name=None, task_id=None):
        self.resuslt = resuslt  # type: str
        self.status = status  # type: long
        self.status_name = status_name  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resuslt is not None:
            result['Resuslt'] = self.resuslt
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Resuslt') is not None:
            self.resuslt = m.get('Resuslt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success_response=None):
        self.code = code  # type: long
        self.data = data  # type: GetTaskResultResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success_response = success_response  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTaskResultResponseBody, self).to_map()
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
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTaskResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetTaskResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTaskResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatusRequest, self).to_map()
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


class GetTaskStatusResponseBodyData(TeaModel):
    def __init__(self, status=None, status_name=None, task_id=None):
        self.status = status  # type: long
        self.status_name = status_name  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success_response=None):
        self.code = code  # type: long
        self.data = data  # type: GetTaskStatusResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success_response = success_response  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTaskStatusResponseBody, self).to_map()
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
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTaskStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveWordsRequest(TeaModel):
    def __init__(self, pic_url=None):
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveWordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class RemoveWordsAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None):
        self.pic_url_object = pic_url_object  # type: READABLE

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(RemoveWordsAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url_object is not None:
            result['PicUrlObject'] = self.pic_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrlObject') is not None:
            self.pic_url_object = m.get('PicUrlObject')
        return self


class RemoveWordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(RemoveWordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ReplaceBackgroundRequest(TeaModel):
    def __init__(self, background_id=None, num=None, pic_background_url=None, pic_url=None):
        # 返回的图片背景图片ID
        self.background_id = background_id  # type: str
        self.num = num  # type: int
        self.pic_background_url = pic_background_url  # type: str
        # 图片地址
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceBackgroundRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_id is not None:
            result['BackgroundId'] = self.background_id
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_background_url is not None:
            result['PicBackgroundUrl'] = self.pic_background_url
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackgroundId') is not None:
            self.background_id = m.get('BackgroundId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicBackgroundUrl') is not None:
            self.pic_background_url = m.get('PicBackgroundUrl')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class ReplaceBackgroundAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None, background_id=None, num=None, pic_background_url=None):
        self.pic_url_object = pic_url_object  # type: READABLE
        # 返回的图片背景图片ID
        self.background_id = background_id  # type: str
        self.num = num  # type: int
        self.pic_background_url = pic_background_url  # type: str

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(ReplaceBackgroundAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url_object is not None:
            result['PicUrlObject'] = self.pic_url_object
        if self.background_id is not None:
            result['BackgroundId'] = self.background_id
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_background_url is not None:
            result['PicBackgroundUrl'] = self.pic_background_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrlObject') is not None:
            self.pic_url_object = m.get('PicUrlObject')
        if m.get('BackgroundId') is not None:
            self.background_id = m.get('BackgroundId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicBackgroundUrl') is not None:
            self.pic_background_url = m.get('PicBackgroundUrl')
        return self


class ReplaceBackgroundResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(ReplaceBackgroundResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


