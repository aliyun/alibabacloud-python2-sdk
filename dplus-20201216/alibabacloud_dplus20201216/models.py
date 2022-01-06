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


class AlivisionImgdupRequest(TeaModel):
    def __init__(self, image_height=None, image_width=None, output_image_num=None, pic_num=None, pic_url=None):
        self.image_height = image_height  # type: int
        self.image_width = image_width  # type: int
        self.output_image_num = output_image_num  # type: int
        self.pic_num = pic_num  # type: int
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AlivisionImgdupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.output_image_num is not None:
            result['OutputImageNum'] = self.output_image_num
        if self.pic_num is not None:
            result['PicNum'] = self.pic_num
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('OutputImageNum') is not None:
            self.output_image_num = m.get('OutputImageNum')
        if m.get('PicNum') is not None:
            self.pic_num = m.get('PicNum')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class AlivisionImgdupAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None, image_height=None, image_width=None, output_image_num=None,
                 pic_num=None):
        self.pic_url_object = pic_url_object  # type: READABLE
        self.image_height = image_height  # type: int
        self.image_width = image_width  # type: int
        self.output_image_num = output_image_num  # type: int
        self.pic_num = pic_num  # type: int

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(AlivisionImgdupAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url_object is not None:
            result['PicUrlObject'] = self.pic_url_object
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.output_image_num is not None:
            result['OutputImageNum'] = self.output_image_num
        if self.pic_num is not None:
            result['PicNum'] = self.pic_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrlObject') is not None:
            self.pic_url_object = m.get('PicUrlObject')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('OutputImageNum') is not None:
            self.output_image_num = m.get('OutputImageNum')
        if m.get('PicNum') is not None:
            self.pic_num = m.get('PicNum')
        return self


class AlivisionImgdupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(AlivisionImgdupResponse, self).to_map()
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


class FaceshifterTRequest(TeaModel):
    def __init__(self, age=None, gender=None, pic_url=None, race=None):
        self.age = age  # type: int
        self.gender = gender  # type: int
        self.pic_url = pic_url  # type: str
        self.race = race  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FaceshifterTRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.race is not None:
            result['Race'] = self.race
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Race') is not None:
            self.race = m.get('Race')
        return self


class FaceshifterTAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None, age=None, gender=None, race=None):
        self.pic_url_object = pic_url_object  # type: READABLE
        self.age = age  # type: int
        self.gender = gender  # type: int
        self.race = race  # type: int

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(FaceshifterTAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url_object is not None:
            result['PicUrlObject'] = self.pic_url_object
        if self.age is not None:
            result['Age'] = self.age
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.race is not None:
            result['Race'] = self.race
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrlObject') is not None:
            self.pic_url_object = m.get('PicUrlObject')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Race') is not None:
            self.race = m.get('Race')
        return self


class FaceshifterTResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(FaceshifterTResponse, self).to_map()
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


class KuajingSegRequest(TeaModel):
    def __init__(self, pic_url=None, return_pic_format=None, return_pic_type=None):
        self.pic_url = pic_url  # type: str
        self.return_pic_format = return_pic_format  # type: str
        self.return_pic_type = return_pic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KuajingSegRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.return_pic_format is not None:
            result['ReturnPicFormat'] = self.return_pic_format
        if self.return_pic_type is not None:
            result['ReturnPicType'] = self.return_pic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ReturnPicFormat') is not None:
            self.return_pic_format = m.get('ReturnPicFormat')
        if m.get('ReturnPicType') is not None:
            self.return_pic_type = m.get('ReturnPicType')
        return self


class KuajingSegAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None, return_pic_format=None, return_pic_type=None):
        self.pic_url_object = pic_url_object  # type: READABLE
        self.return_pic_format = return_pic_format  # type: str
        self.return_pic_type = return_pic_type  # type: str

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(KuajingSegAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url_object is not None:
            result['PicUrlObject'] = self.pic_url_object
        if self.return_pic_format is not None:
            result['ReturnPicFormat'] = self.return_pic_format
        if self.return_pic_type is not None:
            result['ReturnPicType'] = self.return_pic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrlObject') is not None:
            self.pic_url_object = m.get('PicUrlObject')
        if m.get('ReturnPicFormat') is not None:
            self.return_pic_format = m.get('ReturnPicFormat')
        if m.get('ReturnPicType') is not None:
            self.return_pic_type = m.get('ReturnPicType')
        return self


class KuajingSegResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(KuajingSegResponse, self).to_map()
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


class TbPredictCategoryRequest(TeaModel):
    def __init__(self, pic_url=None):
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TbPredictCategoryRequest, self).to_map()
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


class TbPredictCategoryAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None):
        self.pic_url_object = pic_url_object  # type: READABLE

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(TbPredictCategoryAdvanceRequest, self).to_map()
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


class TbPredictCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(TbPredictCategoryResponse, self).to_map()
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


class TbPropRecRequest(TeaModel):
    def __init__(self, pic_url=None):
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TbPropRecRequest, self).to_map()
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


class TbPropRecAdvanceRequest(TeaModel):
    def __init__(self, pic_url_object=None):
        self.pic_url_object = pic_url_object  # type: READABLE

    def validate(self):
        self.validate_required(self.pic_url_object, 'pic_url_object')

    def to_map(self):
        _map = super(TbPropRecAdvanceRequest, self).to_map()
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


class TbPropRecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(TbPropRecResponse, self).to_map()
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


