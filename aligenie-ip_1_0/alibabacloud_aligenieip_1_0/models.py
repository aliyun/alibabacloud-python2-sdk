# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddCartoonHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCartoonHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddCartoonRequest(TeaModel):
    def __init__(self, hotel_id=None, start_video_md_5=None, start_video_url=None):
        self.hotel_id = hotel_id  # type: str
        self.start_video_md_5 = start_video_md_5  # type: str
        self.start_video_url = start_video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCartoonRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.start_video_md_5 is not None:
            result['StartVideoMd5'] = self.start_video_md_5
        if self.start_video_url is not None:
            result['StartVideoUrl'] = self.start_video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('StartVideoMd5') is not None:
            self.start_video_md_5 = m.get('StartVideoMd5')
        if m.get('StartVideoUrl') is not None:
            self.start_video_url = m.get('StartVideoUrl')
        return self


class AddCartoonResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCartoonResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddCartoonResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddCartoonResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCartoonResponse, self).to_map()
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
            temp_model = AddCartoonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCustomQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCustomQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddCustomQARequest(TeaModel):
    def __init__(self, answers=None, hotel_id=None, key_words=None, major_question=None,
                 supplementary_questions=None):
        self.answers = answers  # type: list[str]
        self.hotel_id = hotel_id  # type: str
        self.key_words = key_words  # type: list[str]
        self.major_question = major_question  # type: str
        self.supplementary_questions = supplementary_questions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCustomQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions = m.get('SupplementaryQuestions')
        return self


class AddCustomQAShrinkRequest(TeaModel):
    def __init__(self, answers_shrink=None, hotel_id=None, key_words_shrink=None, major_question=None,
                 supplementary_questions_shrink=None):
        self.answers_shrink = answers_shrink  # type: str
        self.hotel_id = hotel_id  # type: str
        self.key_words_shrink = key_words_shrink  # type: str
        self.major_question = major_question  # type: str
        self.supplementary_questions_shrink = supplementary_questions_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCustomQAShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers_shrink is not None:
            result['Answers'] = self.answers_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words_shrink is not None:
            result['KeyWords'] = self.key_words_shrink
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions_shrink is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers_shrink = m.get('Answers')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words_shrink = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions_shrink = m.get('SupplementaryQuestions')
        return self


class AddCustomQAResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCustomQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddCustomQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddCustomQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCustomQAResponse, self).to_map()
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
            temp_model = AddCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMessageTemplateHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMessageTemplateHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddMessageTemplateRequest(TeaModel):
    def __init__(self, template_detail=None, template_name=None):
        self.template_detail = template_detail  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMessageTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            self.template_detail = m.get('TemplateDetail')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class AddMessageTemplateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMessageTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AddMessageTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddMessageTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddMessageTemplateResponse, self).to_map()
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
            temp_model = AddMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateDisPlayModesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateDisPlayModesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateDisPlayModesRequest(TeaModel):
    def __init__(self, hotel_device_mode_list=None, hotel_id=None):
        self.hotel_device_mode_list = hotel_device_mode_list  # type: list[str]
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateDisPlayModesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class AddOrUpdateDisPlayModesShrinkRequest(TeaModel):
    def __init__(self, hotel_device_mode_list_shrink=None, hotel_id=None):
        self.hotel_device_mode_list_shrink = hotel_device_mode_list_shrink  # type: str
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateDisPlayModesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list_shrink is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list_shrink = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class AddOrUpdateDisPlayModesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateDisPlayModesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateDisPlayModesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddOrUpdateDisPlayModesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddOrUpdateDisPlayModesResponse, self).to_map()
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
            temp_model = AddOrUpdateDisPlayModesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateHotelSettingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateHotelSettingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateHotelSettingRequestHotelScreenSaver(TeaModel):
    def __init__(self, screen_saver_pic_url=None, screen_saver_style=None):
        self.screen_saver_pic_url = screen_saver_pic_url  # type: str
        self.screen_saver_style = screen_saver_style  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateHotelSettingRequestHotelScreenSaver, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_saver_pic_url is not None:
            result['ScreenSaverPicUrl'] = self.screen_saver_pic_url
        if self.screen_saver_style is not None:
            result['ScreenSaverStyle'] = self.screen_saver_style
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScreenSaverPicUrl') is not None:
            self.screen_saver_pic_url = m.get('ScreenSaverPicUrl')
        if m.get('ScreenSaverStyle') is not None:
            self.screen_saver_style = m.get('ScreenSaverStyle')
        return self


class AddOrUpdateHotelSettingRequestNightMode(TeaModel):
    def __init__(self, default_bright=None, default_volume=None, enable=None, end=None, standby_action=None,
                 start=None):
        self.default_bright = default_bright  # type: str
        self.default_volume = default_volume  # type: str
        self.enable = enable  # type: bool
        self.end = end  # type: str
        self.standby_action = standby_action  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateHotelSettingRequestNightMode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_bright is not None:
            result['DefaultBright'] = self.default_bright
        if self.default_volume is not None:
            result['DefaultVolume'] = self.default_volume
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end is not None:
            result['End'] = self.end
        if self.standby_action is not None:
            result['StandbyAction'] = self.standby_action
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultBright') is not None:
            self.default_bright = m.get('DefaultBright')
        if m.get('DefaultVolume') is not None:
            self.default_volume = m.get('DefaultVolume')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('StandbyAction') is not None:
            self.standby_action = m.get('StandbyAction')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class AddOrUpdateHotelSettingRequest(TeaModel):
    def __init__(self, hotel_device_mode_list=None, hotel_id=None, hotel_screen_saver=None, night_mode=None,
                 setting_type=None, value=None):
        self.hotel_device_mode_list = hotel_device_mode_list  # type: list[str]
        self.hotel_id = hotel_id  # type: str
        self.hotel_screen_saver = hotel_screen_saver  # type: AddOrUpdateHotelSettingRequestHotelScreenSaver
        self.night_mode = night_mode  # type: AddOrUpdateHotelSettingRequestNightMode
        self.setting_type = setting_type  # type: str
        self.value = value  # type: str

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()
        if self.night_mode:
            self.night_mode.validate()

    def to_map(self):
        _map = super(AddOrUpdateHotelSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()
        if self.night_mode is not None:
            result['NightMode'] = self.night_mode.to_map()
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            temp_model = AddOrUpdateHotelSettingRequestHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m['HotelScreenSaver'])
        if m.get('NightMode') is not None:
            temp_model = AddOrUpdateHotelSettingRequestNightMode()
            self.night_mode = temp_model.from_map(m['NightMode'])
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddOrUpdateHotelSettingShrinkRequest(TeaModel):
    def __init__(self, hotel_device_mode_list_shrink=None, hotel_id=None, hotel_screen_saver_shrink=None,
                 night_mode_shrink=None, setting_type=None, value=None):
        self.hotel_device_mode_list_shrink = hotel_device_mode_list_shrink  # type: str
        self.hotel_id = hotel_id  # type: str
        self.hotel_screen_saver_shrink = hotel_screen_saver_shrink  # type: str
        self.night_mode_shrink = night_mode_shrink  # type: str
        self.setting_type = setting_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateHotelSettingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list_shrink is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver_shrink is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver_shrink
        if self.night_mode_shrink is not None:
            result['NightMode'] = self.night_mode_shrink
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list_shrink = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            self.hotel_screen_saver_shrink = m.get('HotelScreenSaver')
        if m.get('NightMode') is not None:
            self.night_mode_shrink = m.get('NightMode')
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddOrUpdateHotelSettingResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateHotelSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateHotelSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddOrUpdateHotelSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddOrUpdateHotelSettingResponse, self).to_map()
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
            temp_model = AddOrUpdateHotelSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateScreenSaverHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateScreenSaverHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateScreenSaverRequestHotelScreenSaver(TeaModel):
    def __init__(self, screen_saver_pic_url=None, screen_saver_style=None):
        self.screen_saver_pic_url = screen_saver_pic_url  # type: str
        self.screen_saver_style = screen_saver_style  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateScreenSaverRequestHotelScreenSaver, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_saver_pic_url is not None:
            result['ScreenSaverPicUrl'] = self.screen_saver_pic_url
        if self.screen_saver_style is not None:
            result['ScreenSaverStyle'] = self.screen_saver_style
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScreenSaverPicUrl') is not None:
            self.screen_saver_pic_url = m.get('ScreenSaverPicUrl')
        if m.get('ScreenSaverStyle') is not None:
            self.screen_saver_style = m.get('ScreenSaverStyle')
        return self


class AddOrUpdateScreenSaverRequest(TeaModel):
    def __init__(self, hotel_id=None, hotel_screen_saver=None):
        self.hotel_id = hotel_id  # type: str
        self.hotel_screen_saver = hotel_screen_saver  # type: AddOrUpdateScreenSaverRequestHotelScreenSaver

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()

    def to_map(self):
        _map = super(AddOrUpdateScreenSaverRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            temp_model = AddOrUpdateScreenSaverRequestHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m['HotelScreenSaver'])
        return self


class AddOrUpdateScreenSaverShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, hotel_screen_saver_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.hotel_screen_saver_shrink = hotel_screen_saver_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateScreenSaverShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver_shrink is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            self.hotel_screen_saver_shrink = m.get('HotelScreenSaver')
        return self


class AddOrUpdateScreenSaverResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateScreenSaverResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateScreenSaverResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddOrUpdateScreenSaverResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddOrUpdateScreenSaverResponse, self).to_map()
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
            temp_model = AddOrUpdateScreenSaverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateWelcomeTextHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateWelcomeTextHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateWelcomeTextRequest(TeaModel):
    def __init__(self, hotel_id=None, music_url=None, welcome_text=None):
        self.hotel_id = hotel_id  # type: str
        self.music_url = music_url  # type: str
        self.welcome_text = welcome_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateWelcomeTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        if self.welcome_text is not None:
            result['WelcomeText'] = self.welcome_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        if m.get('WelcomeText') is not None:
            self.welcome_text = m.get('WelcomeText')
        return self


class AddOrUpdateWelcomeTextResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOrUpdateWelcomeTextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateWelcomeTextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddOrUpdateWelcomeTextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddOrUpdateWelcomeTextResponse, self).to_map()
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
            temp_model = AddOrUpdateWelcomeTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuditHotelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuditHotelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AuditHotelRequestAuditHotelReq(TeaModel):
    def __init__(self, audit_opinion=None, hotel_id=None, status=None):
        self.audit_opinion = audit_opinion  # type: str
        self.hotel_id = hotel_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuditHotelRequestAuditHotelReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_opinion is not None:
            result['AuditOpinion'] = self.audit_opinion
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditOpinion') is not None:
            self.audit_opinion = m.get('AuditOpinion')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class AuditHotelRequest(TeaModel):
    def __init__(self, audit_hotel_req=None):
        self.audit_hotel_req = audit_hotel_req  # type: AuditHotelRequestAuditHotelReq

    def validate(self):
        if self.audit_hotel_req:
            self.audit_hotel_req.validate()

    def to_map(self):
        _map = super(AuditHotelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_hotel_req is not None:
            result['AuditHotelReq'] = self.audit_hotel_req.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditHotelReq') is not None:
            temp_model = AuditHotelRequestAuditHotelReq()
            self.audit_hotel_req = temp_model.from_map(m['AuditHotelReq'])
        return self


class AuditHotelShrinkRequest(TeaModel):
    def __init__(self, audit_hotel_req_shrink=None):
        self.audit_hotel_req_shrink = audit_hotel_req_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuditHotelShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_hotel_req_shrink is not None:
            result['AuditHotelReq'] = self.audit_hotel_req_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditHotelReq') is not None:
            self.audit_hotel_req_shrink = m.get('AuditHotelReq')
        return self


class AuditHotelResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuditHotelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AuditHotelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuditHotelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuditHotelResponse, self).to_map()
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
            temp_model = AuditHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddHotelRoomHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddHotelRoomHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class BatchAddHotelRoomRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no_list=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no_list = room_no_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddHotelRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list is not None:
            result['RoomNoList'] = self.room_no_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list = m.get('RoomNoList')
        return self


class BatchAddHotelRoomShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no_list_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no_list_shrink = room_no_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddHotelRoomShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list_shrink is not None:
            result['RoomNoList'] = self.room_no_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list_shrink = m.get('RoomNoList')
        return self


class BatchAddHotelRoomResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddHotelRoomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BatchAddHotelRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchAddHotelRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchAddHotelRoomResponse, self).to_map()
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
            temp_model = BatchAddHotelRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteHotelRoomHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteHotelRoomHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class BatchDeleteHotelRoomRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no_list=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no_list = room_no_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteHotelRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list is not None:
            result['RoomNoList'] = self.room_no_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list = m.get('RoomNoList')
        return self


class BatchDeleteHotelRoomShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no_list_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no_list_shrink = room_no_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteHotelRoomShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list_shrink is not None:
            result['RoomNoList'] = self.room_no_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list_shrink = m.get('RoomNoList')
        return self


class BatchDeleteHotelRoomResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteHotelRoomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BatchDeleteHotelRoomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchDeleteHotelRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteHotelRoomResponse, self).to_map()
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
            temp_model = BatchDeleteHotelRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckoutWithAKHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckoutWithAKHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CheckoutWithAKRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckoutWithAKRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class CheckoutWithAKResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckoutWithAKResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CheckoutWithAKResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckoutWithAKResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckoutWithAKResponse, self).to_map()
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
            temp_model = CheckoutWithAKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChildAccountAuthHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChildAccountAuthHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ChildAccountAuthRequest(TeaModel):
    def __init__(self, account=None, app_key=None, hotel_id=None, tb_open_id=None):
        self.account = account  # type: str
        self.app_key = app_key  # type: str
        self.hotel_id = hotel_id  # type: str
        self.tb_open_id = tb_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChildAccountAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class ChildAccountAuthResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChildAccountAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ChildAccountAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChildAccountAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChildAccountAuthResponse, self).to_map()
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
            temp_model = ChildAccountAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ControlRoomDeviceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ControlRoomDeviceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ControlRoomDeviceRequest(TeaModel):
    def __init__(self, cmd=None, device_index=None, device_number=None, hotel_id=None, properties=None, room_no=None):
        self.cmd = cmd  # type: str
        self.device_index = device_index  # type: int
        self.device_number = device_number  # type: str
        self.hotel_id = hotel_id  # type: str
        self.properties = properties  # type: dict[str, str]
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ControlRoomDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ControlRoomDeviceShrinkRequest(TeaModel):
    def __init__(self, cmd=None, device_index=None, device_number=None, hotel_id=None, properties_shrink=None,
                 room_no=None):
        self.cmd = cmd  # type: str
        self.device_index = device_index  # type: int
        self.device_number = device_number  # type: str
        self.hotel_id = hotel_id  # type: str
        self.properties_shrink = properties_shrink  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ControlRoomDeviceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ControlRoomDeviceResponseBodyResult(TeaModel):
    def __init__(self, message=None, status=None):
        self.message = message  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ControlRoomDeviceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ControlRoomDeviceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ControlRoomDeviceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ControlRoomDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ControlRoomDeviceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ControlRoomDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ControlRoomDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ControlRoomDeviceResponse, self).to_map()
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
            temp_model = ControlRoomDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHotelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateHotelRequest(TeaModel):
    def __init__(self, app_key=None, est_open_time=None, hotel_address=None, hotel_email=None, hotel_name=None,
                 phone_number=None, related_pk=None, related_pks=None, remark=None, room_num=None, tb_open_id=None):
        self.app_key = app_key  # type: str
        self.est_open_time = est_open_time  # type: str
        self.hotel_address = hotel_address  # type: str
        self.hotel_email = hotel_email  # type: str
        self.hotel_name = hotel_name  # type: str
        self.phone_number = phone_number  # type: str
        self.related_pk = related_pk  # type: str
        # 酒店关联产品列表
        self.related_pks = related_pks  # type: list[str]
        self.remark = remark  # type: str
        self.room_num = room_num  # type: int
        self.tb_open_id = tb_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pk is not None:
            result['RelatedPk'] = self.related_pk
        if self.related_pks is not None:
            result['RelatedPks'] = self.related_pks
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPk') is not None:
            self.related_pk = m.get('RelatedPk')
        if m.get('RelatedPks') is not None:
            self.related_pks = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class CreateHotelShrinkRequest(TeaModel):
    def __init__(self, app_key=None, est_open_time=None, hotel_address=None, hotel_email=None, hotel_name=None,
                 phone_number=None, related_pk=None, related_pks_shrink=None, remark=None, room_num=None, tb_open_id=None):
        self.app_key = app_key  # type: str
        self.est_open_time = est_open_time  # type: str
        self.hotel_address = hotel_address  # type: str
        self.hotel_email = hotel_email  # type: str
        self.hotel_name = hotel_name  # type: str
        self.phone_number = phone_number  # type: str
        self.related_pk = related_pk  # type: str
        # 酒店关联产品列表
        self.related_pks_shrink = related_pks_shrink  # type: str
        self.remark = remark  # type: str
        self.room_num = room_num  # type: int
        self.tb_open_id = tb_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pk is not None:
            result['RelatedPk'] = self.related_pk
        if self.related_pks_shrink is not None:
            result['RelatedPks'] = self.related_pks_shrink
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPk') is not None:
            self.related_pk = m.get('RelatedPk')
        if m.get('RelatedPks') is not None:
            self.related_pks_shrink = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class CreateHotelResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CreateHotelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHotelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHotelResponse, self).to_map()
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
            temp_model = CreateHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHotelAlarmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelAlarmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateHotelAlarmRequestScheduleInfoOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelAlarmRequestScheduleInfoOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateHotelAlarmRequestScheduleInfoWeekly(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelAlarmRequestScheduleInfoWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class CreateHotelAlarmRequestScheduleInfo(TeaModel):
    def __init__(self, once=None, type=None, weekly=None):
        self.once = once  # type: CreateHotelAlarmRequestScheduleInfoOnce
        # ONCE, WEEKLY
        self.type = type  # type: str
        self.weekly = weekly  # type: CreateHotelAlarmRequestScheduleInfoWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(CreateHotelAlarmRequestScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = CreateHotelAlarmRequestScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = CreateHotelAlarmRequestScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class CreateHotelAlarmRequest(TeaModel):
    def __init__(self, hotel_id=None, music_type=None, rooms=None, schedule_info=None):
        self.hotel_id = hotel_id  # type: str
        self.music_type = music_type  # type: str
        self.rooms = rooms  # type: list[str]
        self.schedule_info = schedule_info  # type: CreateHotelAlarmRequestScheduleInfo

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(CreateHotelAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.rooms is not None:
            result['Rooms'] = self.rooms
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('Rooms') is not None:
            self.rooms = m.get('Rooms')
        if m.get('ScheduleInfo') is not None:
            temp_model = CreateHotelAlarmRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        return self


class CreateHotelAlarmShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, music_type=None, rooms_shrink=None, schedule_info_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.music_type = music_type  # type: str
        self.rooms_shrink = rooms_shrink  # type: str
        self.schedule_info_shrink = schedule_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelAlarmShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.rooms_shrink is not None:
            result['Rooms'] = self.rooms_shrink
        if self.schedule_info_shrink is not None:
            result['ScheduleInfo'] = self.schedule_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('Rooms') is not None:
            self.rooms_shrink = m.get('Rooms')
        if m.get('ScheduleInfo') is not None:
            self.schedule_info_shrink = m.get('ScheduleInfo')
        return self


class CreateHotelAlarmResponseBodyResult(TeaModel):
    def __init__(self, alarm_id=None, device_open_id=None, fail_msg=None, room_no=None, user_open_id=None):
        self.alarm_id = alarm_id  # type: long
        self.device_open_id = device_open_id  # type: str
        self.fail_msg = fail_msg  # type: str
        self.room_no = room_no  # type: str
        self.user_open_id = user_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHotelAlarmResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.fail_msg is not None:
            result['FailMsg'] = self.fail_msg
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('FailMsg') is not None:
            self.fail_msg = m.get('FailMsg')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class CreateHotelAlarmResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[CreateHotelAlarmResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateHotelAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = CreateHotelAlarmResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CreateHotelAlarmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHotelAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHotelAlarmResponse, self).to_map()
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
            temp_model = CreateHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRcuSceneHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRcuSceneHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateRcuSceneRequestSceneRelationExtDTO(TeaModel):
    def __init__(self, corpus_list=None, description=None, icon=None, name=None):
        self.corpus_list = corpus_list  # type: list[str]
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRcuSceneRequestSceneRelationExtDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateRcuSceneRequest(TeaModel):
    def __init__(self, hotel_id=None, scene_id=None, scene_relation_ext_dto=None):
        self.hotel_id = hotel_id  # type: str
        self.scene_id = scene_id  # type: str
        self.scene_relation_ext_dto = scene_relation_ext_dto  # type: CreateRcuSceneRequestSceneRelationExtDTO

    def validate(self):
        if self.scene_relation_ext_dto:
            self.scene_relation_ext_dto.validate()

    def to_map(self):
        _map = super(CreateRcuSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dto is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            temp_model = CreateRcuSceneRequestSceneRelationExtDTO()
            self.scene_relation_ext_dto = temp_model.from_map(m['SceneRelationExtDTO'])
        return self


class CreateRcuSceneShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, scene_id=None, scene_relation_ext_dtoshrink=None):
        self.hotel_id = hotel_id  # type: str
        self.scene_id = scene_id  # type: str
        self.scene_relation_ext_dtoshrink = scene_relation_ext_dtoshrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRcuSceneShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dtoshrink is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dtoshrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            self.scene_relation_ext_dtoshrink = m.get('SceneRelationExtDTO')
        return self


class CreateRcuSceneResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRcuSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CreateRcuSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRcuSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRcuSceneResponse, self).to_map()
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
            temp_model = CreateRcuSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCartoonHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCartoonHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteCartoonRequest(TeaModel):
    def __init__(self, hotel_id=None):
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCartoonRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteCartoonResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCartoonResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteCartoonResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCartoonResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCartoonResponse, self).to_map()
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
            temp_model = DeleteCartoonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteCustomQARequest(TeaModel):
    def __init__(self, custom_qaids=None, hotel_id=None):
        self.custom_qaids = custom_qaids  # type: list[str]
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_qaids is not None:
            result['CustomQAIds'] = self.custom_qaids
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomQAIds') is not None:
            self.custom_qaids = m.get('CustomQAIds')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteCustomQAShrinkRequest(TeaModel):
    def __init__(self, custom_qaids_shrink=None, hotel_id=None):
        self.custom_qaids_shrink = custom_qaids_shrink  # type: str
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomQAShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_qaids_shrink is not None:
            result['CustomQAIds'] = self.custom_qaids_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomQAIds') is not None:
            self.custom_qaids_shrink = m.get('CustomQAIds')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteCustomQAResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteCustomQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomQAResponse, self).to_map()
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
            temp_model = DeleteCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHotelAlarmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelAlarmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteHotelAlarmRequestAlarms(TeaModel):
    def __init__(self, alarm_id=None, device_open_id=None, room_no=None, user_open_id=None):
        self.alarm_id = alarm_id  # type: long
        self.device_open_id = device_open_id  # type: str
        self.room_no = room_no  # type: str
        self.user_open_id = user_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelAlarmRequestAlarms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class DeleteHotelAlarmRequest(TeaModel):
    def __init__(self, alarms=None, hotel_id=None):
        self.alarms = alarms  # type: list[DeleteHotelAlarmRequestAlarms]
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteHotelAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = DeleteHotelAlarmRequestAlarms()
                self.alarms.append(temp_model.from_map(k))
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteHotelAlarmShrinkRequest(TeaModel):
    def __init__(self, alarms_shrink=None, hotel_id=None):
        self.alarms_shrink = alarms_shrink  # type: str
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelAlarmShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarms_shrink is not None:
            result['Alarms'] = self.alarms_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alarms') is not None:
            self.alarms_shrink = m.get('Alarms')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteHotelAlarmResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: int
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteHotelAlarmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHotelAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHotelAlarmResponse, self).to_map()
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
            temp_model = DeleteHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHotelSceneBookItemHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelSceneBookItemHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteHotelSceneBookItemRequest(TeaModel):
    def __init__(self, hotel_id=None, id=None, name=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelSceneBookItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteHotelSceneBookItemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelSceneBookItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteHotelSceneBookItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHotelSceneBookItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHotelSceneBookItemResponse, self).to_map()
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
            temp_model = DeleteHotelSceneBookItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHotelSettingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelSettingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteHotelSettingRequest(TeaModel):
    def __init__(self, hotel_id=None, setting_type=None):
        self.hotel_id = hotel_id  # type: str
        self.setting_type = setting_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        return self


class DeleteHotelSettingResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHotelSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteHotelSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHotelSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHotelSettingResponse, self).to_map()
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
            temp_model = DeleteHotelSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMessageTemplateHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMessageTemplateHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteMessageTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMessageTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteMessageTemplateResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMessageTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteMessageTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMessageTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMessageTemplateResponse, self).to_map()
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
            temp_model = DeleteMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRcuSceneHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRcuSceneHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteRcuSceneRequest(TeaModel):
    def __init__(self, hotel_id=None, scene_id=None):
        self.hotel_id = hotel_id  # type: str
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRcuSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DeleteRcuSceneResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRcuSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteRcuSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRcuSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRcuSceneResponse, self).to_map()
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
            temp_model = DeleteRcuSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeviceControlHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeviceControlRequestPayload(TeaModel):
    def __init__(self, category=None, cmd=None, device_number=None, extend_info=None, location=None, properties=None):
        self.category = category  # type: str
        self.cmd = cmd  # type: str
        self.device_number = device_number  # type: str
        self.extend_info = extend_info  # type: str
        self.location = location  # type: str
        self.properties = properties  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.location is not None:
            result['Location'] = self.location
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class DeviceControlRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeviceControlRequest(TeaModel):
    def __init__(self, payload=None, user_info=None):
        self.payload = payload  # type: DeviceControlRequestPayload
        self.user_info = user_info  # type: DeviceControlRequestUserInfo

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(DeviceControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = DeviceControlRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeviceControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeviceControlShrinkRequest(TeaModel):
    def __init__(self, payload_shrink=None, user_info_shrink=None):
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeviceControlResponseBodyResult(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeviceControlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeviceControlResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeviceControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeviceControlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeviceControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeviceControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeviceControlResponse, self).to_map()
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
            temp_model = DeviceControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicInfoQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicInfoQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetBasicInfoQARequest(TeaModel):
    def __init__(self, hotel_id=None):
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicInfoQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetBasicInfoQAResponseBodyResult(TeaModel):
    def __init__(self, check_in_time=None, check_out_time=None, hotel_address=None, hotel_introduction=None,
                 hotel_member=None, hotel_service=None, parking_expenses=None, parking_position=None, phone_number=None,
                 wifi_name=None, wifi_password=None):
        self.check_in_time = check_in_time  # type: str
        self.check_out_time = check_out_time  # type: str
        self.hotel_address = hotel_address  # type: str
        self.hotel_introduction = hotel_introduction  # type: str
        self.hotel_member = hotel_member  # type: str
        self.hotel_service = hotel_service  # type: str
        self.parking_expenses = parking_expenses  # type: str
        self.parking_position = parking_position  # type: str
        self.phone_number = phone_number  # type: str
        self.wifi_name = wifi_name  # type: str
        self.wifi_password = wifi_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicInfoQAResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in_time is not None:
            result['CheckInTime'] = self.check_in_time
        if self.check_out_time is not None:
            result['CheckOutTime'] = self.check_out_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_introduction is not None:
            result['HotelIntroduction'] = self.hotel_introduction
        if self.hotel_member is not None:
            result['HotelMember'] = self.hotel_member
        if self.hotel_service is not None:
            result['HotelService'] = self.hotel_service
        if self.parking_expenses is not None:
            result['ParkingExpenses'] = self.parking_expenses
        if self.parking_position is not None:
            result['ParkingPosition'] = self.parking_position
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.wifi_name is not None:
            result['WifiName'] = self.wifi_name
        if self.wifi_password is not None:
            result['WifiPassword'] = self.wifi_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckInTime') is not None:
            self.check_in_time = m.get('CheckInTime')
        if m.get('CheckOutTime') is not None:
            self.check_out_time = m.get('CheckOutTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelIntroduction') is not None:
            self.hotel_introduction = m.get('HotelIntroduction')
        if m.get('HotelMember') is not None:
            self.hotel_member = m.get('HotelMember')
        if m.get('HotelService') is not None:
            self.hotel_service = m.get('HotelService')
        if m.get('ParkingExpenses') is not None:
            self.parking_expenses = m.get('ParkingExpenses')
        if m.get('ParkingPosition') is not None:
            self.parking_position = m.get('ParkingPosition')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('WifiName') is not None:
            self.wifi_name = m.get('WifiName')
        if m.get('WifiPassword') is not None:
            self.wifi_password = m.get('WifiPassword')
        return self


class GetBasicInfoQAResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetBasicInfoQAResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetBasicInfoQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetBasicInfoQAResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetBasicInfoQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBasicInfoQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBasicInfoQAResponse, self).to_map()
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
            temp_model = GetBasicInfoQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCartoonHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCartoonHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetCartoonRequest(TeaModel):
    def __init__(self, hotel_id=None):
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCartoonRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetCartoonResponseBodyResult(TeaModel):
    def __init__(self, start_video_md_5=None, start_video_url=None):
        self.start_video_md_5 = start_video_md_5  # type: str
        self.start_video_url = start_video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCartoonResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_video_md_5 is not None:
            result['StartVideoMd5'] = self.start_video_md_5
        if self.start_video_url is not None:
            result['StartVideoUrl'] = self.start_video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartVideoMd5') is not None:
            self.start_video_md_5 = m.get('StartVideoMd5')
        if m.get('StartVideoUrl') is not None:
            self.start_video_url = m.get('StartVideoUrl')
        return self


class GetCartoonResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetCartoonResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetCartoonResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetCartoonResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetCartoonResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCartoonResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCartoonResponse, self).to_map()
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
            temp_model = GetCartoonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelContactByGenieDeviceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelContactByGenieDeviceRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactByGenieDeviceRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactByGenieDeviceRequest(TeaModel):
    def __init__(self, device_info=None, user_info=None):
        self.device_info = device_info  # type: GetHotelContactByGenieDeviceRequestDeviceInfo
        self.user_info = user_info  # type: GetHotelContactByGenieDeviceRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetHotelContactByGenieDeviceRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetHotelContactByGenieDeviceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelContactByGenieDeviceShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelContactByGenieDeviceResponseBodyResult(TeaModel):
    def __init__(self, expire_at=None, gmt_create=None, gmt_modified=None, hotel_id=None, icon=None, id=None,
                 name=None, number=None, status=None, type=None, uuid=None):
        self.expire_at = expire_at  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.hotel_id = hotel_id  # type: str
        self.icon = icon  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.number = number  # type: str
        self.status = status  # type: int
        self.type = type  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetHotelContactByGenieDeviceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetHotelContactByGenieDeviceResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelContactByGenieDeviceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelContactByGenieDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelContactByGenieDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelContactByGenieDeviceResponse, self).to_map()
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
            temp_model = GetHotelContactByGenieDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelContactByNumberHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByNumberHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelContactByNumberRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByNumberRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactByNumberRequest(TeaModel):
    def __init__(self, number=None, user_info=None):
        self.number = number  # type: str
        self.user_info = user_info  # type: GetHotelContactByNumberRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelContactByNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('UserInfo') is not None:
            temp_model = GetHotelContactByNumberRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelContactByNumberShrinkRequest(TeaModel):
    def __init__(self, number=None, user_info_shrink=None):
        self.number = number  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByNumberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelContactByNumberResponseBodyResult(TeaModel):
    def __init__(self, expire_at=None, hotel_id=None, icon=None, name=None, number=None, status=None, type=None,
                 uuid=None):
        self.expire_at = expire_at  # type: str
        self.hotel_id = hotel_id  # type: str
        self.icon = icon  # type: str
        self.name = name  # type: str
        self.number = number  # type: str
        self.status = status  # type: int
        self.type = type  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactByNumberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetHotelContactByNumberResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetHotelContactByNumberResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetHotelContactByNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelContactByNumberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelContactByNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelContactByNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelContactByNumberResponse, self).to_map()
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
            temp_model = GetHotelContactByNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelContactsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelContactsRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactsRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactsRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: GetHotelContactsRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelContactsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelContactsShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelContactsResponseBodyResult(TeaModel):
    def __init__(self, expire_at=None, hotel_id=None, icon=None, name=None, number=None, status=None, type=None,
                 uuid=None):
        self.expire_at = expire_at  # type: str
        self.hotel_id = hotel_id  # type: str
        self.icon = icon  # type: str
        self.name = name  # type: str
        self.number = number  # type: str
        self.status = status  # type: int
        self.type = type  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelContactsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetHotelContactsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetHotelContactsResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotelContactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelContactsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelContactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelContactsResponse, self).to_map()
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
            temp_model = GetHotelContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelHomeBackImageAndModesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelHomeBackImageAndModesRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelHomeBackImageAndModesRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: GetHotelHomeBackImageAndModesRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelHomeBackImageAndModesRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelHomeBackImageAndModesShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelHomeBackImageAndModesResponseBodyResultModeList(TeaModel):
    def __init__(self, cn_name=None, code=None, icon=None):
        self.cn_name = cn_name  # type: str
        self.code = code  # type: str
        self.icon = icon  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesResponseBodyResultModeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.code is not None:
            result['Code'] = self.code
        if self.icon is not None:
            result['Icon'] = self.icon
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        return self


class GetHotelHomeBackImageAndModesResponseBodyResult(TeaModel):
    def __init__(self, background_image=None, hotel_name=None, mode_list=None):
        self.background_image = background_image  # type: str
        self.hotel_name = hotel_name  # type: str
        self.mode_list = mode_list  # type: list[GetHotelHomeBackImageAndModesResponseBodyResultModeList]

    def validate(self):
        if self.mode_list:
            for k in self.mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_image is not None:
            result['BackgroundImage'] = self.background_image
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        result['ModeList'] = []
        if self.mode_list is not None:
            for k in self.mode_list:
                result['ModeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackgroundImage') is not None:
            self.background_image = m.get('BackgroundImage')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        self.mode_list = []
        if m.get('ModeList') is not None:
            for k in m.get('ModeList'):
                temp_model = GetHotelHomeBackImageAndModesResponseBodyResultModeList()
                self.mode_list.append(temp_model.from_map(k))
        return self


class GetHotelHomeBackImageAndModesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetHotelHomeBackImageAndModesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelHomeBackImageAndModesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetHotelHomeBackImageAndModesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelHomeBackImageAndModesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelHomeBackImageAndModesResponse, self).to_map()
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
            temp_model = GetHotelHomeBackImageAndModesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelNoticeHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelNoticeRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelNoticeRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: GetHotelNoticeRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelNoticeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelNoticeRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelNoticeShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelNoticeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetHotelNoticeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelNoticeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelNoticeResponse, self).to_map()
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
            temp_model = GetHotelNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelNoticeV2Headers(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeV2Headers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelNoticeV2RequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeV2RequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelNoticeV2Request(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: GetHotelNoticeV2RequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelNoticeV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelNoticeV2RequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelNoticeV2ShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeV2ShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelNoticeV2ResponseBodyResult(TeaModel):
    def __init__(self, content=None, hotel_id=None, title=None):
        self.content = content  # type: str
        self.hotel_id = hotel_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelNoticeV2ResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetHotelNoticeV2ResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetHotelNoticeV2ResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetHotelNoticeV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelNoticeV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelNoticeV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelNoticeV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelNoticeV2Response, self).to_map()
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
            temp_model = GetHotelNoticeV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelOrderDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelOrderDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelOrderDetailRequestPayload(TeaModel):
    def __init__(self, order_no=None):
        self.order_no = order_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelOrderDetailRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        return self


class GetHotelOrderDetailRequest(TeaModel):
    def __init__(self, payload=None):
        self.payload = payload  # type: GetHotelOrderDetailRequestPayload

    def validate(self):
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super(GetHotelOrderDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = GetHotelOrderDetailRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        return self


class GetHotelOrderDetailShrinkRequest(TeaModel):
    def __init__(self, payload_shrink=None):
        self.payload_shrink = payload_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelOrderDetailShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        return self


class GetHotelOrderDetailResponseBodyResult(TeaModel):
    def __init__(self, apply_amt=None, gmt_create=None, item_url=None, name=None, quantity=None):
        self.apply_amt = apply_amt  # type: long
        self.gmt_create = gmt_create  # type: long
        self.item_url = item_url  # type: str
        self.name = name  # type: str
        self.quantity = quantity  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelOrderDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_amt is not None:
            result['ApplyAmt'] = self.apply_amt
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyAmt') is not None:
            self.apply_amt = m.get('ApplyAmt')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class GetHotelOrderDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetHotelOrderDetailResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotelOrderDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelOrderDetailResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetHotelOrderDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelOrderDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelOrderDetailResponse, self).to_map()
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
            temp_model = GetHotelOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelRoomDeviceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelRoomDeviceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelRoomDeviceRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelRoomDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class GetHotelRoomDeviceResponseBodyResult(TeaModel):
    def __init__(self, firmware_version=None, hotel_id=None, mac=None, online_status=None, room_no=None, sn=None):
        self.firmware_version = firmware_version  # type: str
        self.hotel_id = hotel_id  # type: str
        self.mac = mac  # type: str
        self.online_status = online_status  # type: int
        self.room_no = room_no  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelRoomDeviceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class GetHotelRoomDeviceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetHotelRoomDeviceResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotelRoomDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelRoomDeviceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetHotelRoomDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelRoomDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelRoomDeviceResponse, self).to_map()
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
            temp_model = GetHotelRoomDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelSampleUtterancesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSampleUtterancesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelSampleUtterancesRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSampleUtterancesRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelSampleUtterancesRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: GetHotelSampleUtterancesRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelSampleUtterancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelSampleUtterancesRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelSampleUtterancesShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSampleUtterancesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelSampleUtterancesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSampleUtterancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetHotelSampleUtterancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelSampleUtterancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelSampleUtterancesResponse, self).to_map()
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
            temp_model = GetHotelSampleUtterancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelSceneItemDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSceneItemDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelSceneItemDetailRequest(TeaModel):
    def __init__(self, hotel_id=None, item_id=None, name=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        self.item_id = item_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSceneItemDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetHotelSceneItemDetailResponseBodyResultDialogueList(TeaModel):
    def __init__(self, create_time=None, dialogue_id=None, no_answer=None, no_answer_template=None, process=None,
                 question=None, service_id=None, update_time=None, yes_answer=None, yes_answer_template=None):
        self.create_time = create_time  # type: long
        self.dialogue_id = dialogue_id  # type: str
        self.no_answer = no_answer  # type: str
        self.no_answer_template = no_answer_template  # type: str
        self.process = process  # type: int
        self.question = question  # type: str
        self.service_id = service_id  # type: str
        self.update_time = update_time  # type: long
        self.yes_answer = yes_answer  # type: str
        self.yes_answer_template = yes_answer_template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSceneItemDetailResponseBodyResultDialogueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id
        if self.no_answer is not None:
            result['NoAnswer'] = self.no_answer
        if self.no_answer_template is not None:
            result['NoAnswerTemplate'] = self.no_answer_template
        if self.process is not None:
            result['Process'] = self.process
        if self.question is not None:
            result['Question'] = self.question
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.yes_answer is not None:
            result['YesAnswer'] = self.yes_answer
        if self.yes_answer_template is not None:
            result['YesAnswerTemplate'] = self.yes_answer_template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')
        if m.get('NoAnswer') is not None:
            self.no_answer = m.get('NoAnswer')
        if m.get('NoAnswerTemplate') is not None:
            self.no_answer_template = m.get('NoAnswerTemplate')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('YesAnswer') is not None:
            self.yes_answer = m.get('YesAnswer')
        if m.get('YesAnswerTemplate') is not None:
            self.yes_answer_template = m.get('YesAnswerTemplate')
        return self


class GetHotelSceneItemDetailResponseBodyResult(TeaModel):
    def __init__(self, category=None, dialogue_list=None, icon=None, id=None, name=None, price=None, status=None,
                 type=None, update_time=None):
        self.category = category  # type: str
        self.dialogue_list = dialogue_list  # type: list[GetHotelSceneItemDetailResponseBodyResultDialogueList]
        self.icon = icon  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.price = price  # type: long
        self.status = status  # type: str
        self.type = type  # type: str
        self.update_time = update_time  # type: long

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotelSceneItemDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['DialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['DialogueList'].append(k.to_map() if k else None)
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.dialogue_list = []
        if m.get('DialogueList') is not None:
            for k in m.get('DialogueList'):
                temp_model = GetHotelSceneItemDetailResponseBodyResultDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetHotelSceneItemDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetHotelSceneItemDetailResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetHotelSceneItemDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelSceneItemDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetHotelSceneItemDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelSceneItemDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelSceneItemDetailResponse, self).to_map()
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
            temp_model = GetHotelSceneItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelScreenSaverHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelScreenSaverHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelScreenSaverRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelScreenSaverRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelScreenSaverRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: GetHotelScreenSaverRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetHotelScreenSaverRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelScreenSaverRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelScreenSaverShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelScreenSaverShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelScreenSaverResponseBodyResult(TeaModel):
    def __init__(self, pic_url=None, style_code=None):
        self.pic_url = pic_url  # type: str
        self.style_code = style_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelScreenSaverResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.style_code is not None:
            result['StyleCode'] = self.style_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StyleCode') is not None:
            self.style_code = m.get('StyleCode')
        return self


class GetHotelScreenSaverResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetHotelScreenSaverResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetHotelScreenSaverResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelScreenSaverResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetHotelScreenSaverResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelScreenSaverResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelScreenSaverResponse, self).to_map()
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
            temp_model = GetHotelScreenSaverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelScreenSaverStyleHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelScreenSaverStyleHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelScreenSaverStyleRequest(TeaModel):
    def __init__(self, hotel_id=None):
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelScreenSaverStyleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetHotelScreenSaverStyleResponseBodyResult(TeaModel):
    def __init__(self, cn_name=None, code=None, en_name=None, pic_url=None):
        self.cn_name = cn_name  # type: str
        self.code = code  # type: str
        self.en_name = en_name  # type: str
        self.pic_url = pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelScreenSaverStyleResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.code is not None:
            result['Code'] = self.code
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class GetHotelScreenSaverStyleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetHotelScreenSaverStyleResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotelScreenSaverStyleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelScreenSaverStyleResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelScreenSaverStyleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelScreenSaverStyleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelScreenSaverStyleResponse, self).to_map()
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
            temp_model = GetHotelScreenSaverStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelSettingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSettingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelSettingRequest(TeaModel):
    def __init__(self, hotel_id=None, setting_type=None):
        self.hotel_id = hotel_id  # type: str
        self.setting_type = setting_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        return self


class GetHotelSettingResponseBodyResultHotelScreenSaver(TeaModel):
    def __init__(self, screen_saver_pic_url=None, screen_saver_style=None):
        self.screen_saver_pic_url = screen_saver_pic_url  # type: str
        self.screen_saver_style = screen_saver_style  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSettingResponseBodyResultHotelScreenSaver, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_saver_pic_url is not None:
            result['ScreenSaverPicUrl'] = self.screen_saver_pic_url
        if self.screen_saver_style is not None:
            result['ScreenSaverStyle'] = self.screen_saver_style
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScreenSaverPicUrl') is not None:
            self.screen_saver_pic_url = m.get('ScreenSaverPicUrl')
        if m.get('ScreenSaverStyle') is not None:
            self.screen_saver_style = m.get('ScreenSaverStyle')
        return self


class GetHotelSettingResponseBodyResultNightMode(TeaModel):
    def __init__(self, default_bright=None, default_volume=None, enable=None, end=None, standby_action=None,
                 start=None):
        # 夜间模式下的默认亮度
        self.default_bright = default_bright  # type: str
        # 夜间模式下的默认音量
        self.default_volume = default_volume  # type: str
        self.enable = enable  # type: bool
        self.end = end  # type: str
        self.standby_action = standby_action  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotelSettingResponseBodyResultNightMode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_bright is not None:
            result['DefaultBright'] = self.default_bright
        if self.default_volume is not None:
            result['DefaultVolume'] = self.default_volume
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end is not None:
            result['End'] = self.end
        if self.standby_action is not None:
            result['StandbyAction'] = self.standby_action
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultBright') is not None:
            self.default_bright = m.get('DefaultBright')
        if m.get('DefaultVolume') is not None:
            self.default_volume = m.get('DefaultVolume')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('StandbyAction') is not None:
            self.standby_action = m.get('StandbyAction')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetHotelSettingResponseBodyResult(TeaModel):
    def __init__(self, delete_token=None, ext_info=None, hotel_device_mode_list=None, hotel_id=None,
                 hotel_screen_saver=None, night_mode=None, setting_type=None, value=None):
        self.delete_token = delete_token  # type: long
        self.ext_info = ext_info  # type: str
        self.hotel_device_mode_list = hotel_device_mode_list  # type: list[str]
        self.hotel_id = hotel_id  # type: str
        self.hotel_screen_saver = hotel_screen_saver  # type: GetHotelSettingResponseBodyResultHotelScreenSaver
        self.night_mode = night_mode  # type: GetHotelSettingResponseBodyResultNightMode
        self.setting_type = setting_type  # type: str
        self.value = value  # type: str

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()
        if self.night_mode:
            self.night_mode.validate()

    def to_map(self):
        _map = super(GetHotelSettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_token is not None:
            result['DeleteToken'] = self.delete_token
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()
        if self.night_mode is not None:
            result['NightMode'] = self.night_mode.to_map()
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteToken') is not None:
            self.delete_token = m.get('DeleteToken')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            temp_model = GetHotelSettingResponseBodyResultHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m['HotelScreenSaver'])
        if m.get('NightMode') is not None:
            temp_model = GetHotelSettingResponseBodyResultNightMode()
            self.night_mode = temp_model.from_map(m['NightMode'])
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetHotelSettingResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetHotelSettingResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetHotelSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHotelSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotelSettingResponse, self).to_map()
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
            temp_model = GetHotelSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRelationProductListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRelationProductListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetRelationProductListResponseBodyResult(TeaModel):
    def __init__(self, name=None, pk=None):
        self.name = name  # type: str
        self.pk = pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRelationProductListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class GetRelationProductListResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetRelationProductListResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRelationProductListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetRelationProductListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetRelationProductListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRelationProductListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRelationProductListResponse, self).to_map()
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
            temp_model = GetRelationProductListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUnionIdHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnionIdHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUnionIdRequest(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnionIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class GetUnionIdResponseBodyResult(TeaModel):
    def __init__(self, organization_id=None, union_id=None):
        self.organization_id = organization_id  # type: str
        self.union_id = union_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnionIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        return self


class GetUnionIdResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetUnionIdResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUnionIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetUnionIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetUnionIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUnionIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUnionIdResponse, self).to_map()
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
            temp_model = GetUnionIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWelcomeTextAndMusicHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWelcomeTextAndMusicHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetWelcomeTextAndMusicRequest(TeaModel):
    def __init__(self, hotel_id=None):
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWelcomeTextAndMusicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetWelcomeTextAndMusicResponseBodyResult(TeaModel):
    def __init__(self, hotel_id=None, music_url=None, text=None):
        self.hotel_id = hotel_id  # type: str
        self.music_url = music_url  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWelcomeTextAndMusicResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetWelcomeTextAndMusicResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetWelcomeTextAndMusicResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetWelcomeTextAndMusicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetWelcomeTextAndMusicResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetWelcomeTextAndMusicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWelcomeTextAndMusicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWelcomeTextAndMusicResponse, self).to_map()
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
            temp_model = GetWelcomeTextAndMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotelQrBindHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HotelQrBindHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class HotelQrBindRequest(TeaModel):
    def __init__(self, client_id=None, code=None, ext_info=None, hotel_id=None, room_no=None):
        self.client_id = client_id  # type: str
        self.code = code  # type: str
        self.ext_info = ext_info  # type: str
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HotelQrBindRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.code is not None:
            result['Code'] = self.code
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class HotelQrBindResponseBodyResultOpenDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HotelQrBindResponseBodyResultOpenDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class HotelQrBindResponseBodyResultOpenUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HotelQrBindResponseBodyResultOpenUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class HotelQrBindResponseBodyResult(TeaModel):
    def __init__(self, open_device_info=None, open_user_info=None):
        self.open_device_info = open_device_info  # type: HotelQrBindResponseBodyResultOpenDeviceInfo
        self.open_user_info = open_user_info  # type: HotelQrBindResponseBodyResultOpenUserInfo

    def validate(self):
        if self.open_device_info:
            self.open_device_info.validate()
        if self.open_user_info:
            self.open_user_info.validate()

    def to_map(self):
        _map = super(HotelQrBindResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_device_info is not None:
            result['OpenDeviceInfo'] = self.open_device_info.to_map()
        if self.open_user_info is not None:
            result['OpenUserInfo'] = self.open_user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenDeviceInfo') is not None:
            temp_model = HotelQrBindResponseBodyResultOpenDeviceInfo()
            self.open_device_info = temp_model.from_map(m['OpenDeviceInfo'])
        if m.get('OpenUserInfo') is not None:
            temp_model = HotelQrBindResponseBodyResultOpenUserInfo()
            self.open_user_info = temp_model.from_map(m['OpenUserInfo'])
        return self


class HotelQrBindResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: HotelQrBindResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(HotelQrBindResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = HotelQrBindResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class HotelQrBindResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: HotelQrBindResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HotelQrBindResponse, self).to_map()
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
            temp_model = HotelQrBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportHotelConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportHotelConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ImportHotelConfigRequestImportHotelConfigRcuCustomScenes(TeaModel):
    def __init__(self, corpus_list=None, description=None, icon=None, name=None, scene_id=None):
        self.corpus_list = corpus_list  # type: list[str]
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.name = name  # type: str
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportHotelConfigRequestImportHotelConfigRcuCustomScenes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ImportHotelConfigRequestImportHotelConfig(TeaModel):
    def __init__(self, rcu_custom_scenes=None):
        self.rcu_custom_scenes = rcu_custom_scenes  # type: list[ImportHotelConfigRequestImportHotelConfigRcuCustomScenes]

    def validate(self):
        if self.rcu_custom_scenes:
            for k in self.rcu_custom_scenes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportHotelConfigRequestImportHotelConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RcuCustomScenes'] = []
        if self.rcu_custom_scenes is not None:
            for k in self.rcu_custom_scenes:
                result['RcuCustomScenes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rcu_custom_scenes = []
        if m.get('RcuCustomScenes') is not None:
            for k in m.get('RcuCustomScenes'):
                temp_model = ImportHotelConfigRequestImportHotelConfigRcuCustomScenes()
                self.rcu_custom_scenes.append(temp_model.from_map(k))
        return self


class ImportHotelConfigRequest(TeaModel):
    def __init__(self, hotel_id=None, import_hotel_config=None):
        self.hotel_id = hotel_id  # type: str
        self.import_hotel_config = import_hotel_config  # type: ImportHotelConfigRequestImportHotelConfig

    def validate(self):
        if self.import_hotel_config:
            self.import_hotel_config.validate()

    def to_map(self):
        _map = super(ImportHotelConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.import_hotel_config is not None:
            result['ImportHotelConfig'] = self.import_hotel_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ImportHotelConfig') is not None:
            temp_model = ImportHotelConfigRequestImportHotelConfig()
            self.import_hotel_config = temp_model.from_map(m['ImportHotelConfig'])
        return self


class ImportHotelConfigShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, import_hotel_config_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.import_hotel_config_shrink = import_hotel_config_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportHotelConfigShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.import_hotel_config_shrink is not None:
            result['ImportHotelConfig'] = self.import_hotel_config_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ImportHotelConfig') is not None:
            self.import_hotel_config_shrink = m.get('ImportHotelConfig')
        return self


class ImportHotelConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportHotelConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ImportHotelConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportHotelConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportHotelConfigResponse, self).to_map()
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
            temp_model = ImportHotelConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportRoomControlDevicesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomControlDevicesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList(TeaModel):
    def __init__(self, alias_list=None, category=None, device_index=None, device_name=None, location=None):
        self.alias_list = alias_list  # type: list[str]
        self.category = category  # type: str
        self.device_index = device_index  # type: int
        self.device_name = device_name  # type: str
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt(TeaModel):
    def __init__(self, switch_list=None):
        self.switch_list = switch_list  # type: list[ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList]

    def validate(self):
        if self.switch_list:
            for k in self.switch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SwitchList'] = []
        if self.switch_list is not None:
            for k in self.switch_list:
                result['SwitchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.switch_list = []
        if m.get('SwitchList') is not None:
            for k in m.get('SwitchList'):
                temp_model = ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k))
        return self


class ImportRoomControlDevicesRequestLocationDevicesDevices(TeaModel):
    def __init__(self, alias_list=None, brand=None, city=None, connect_type=None, device_name=None, dn=None,
                 infrared_id=None, infrared_index=None, infrared_version=None, multi_key_switch_ext=None, name=None,
                 number=None, pk=None, province=None, service_provider=None):
        self.alias_list = alias_list  # type: list[str]
        self.brand = brand  # type: str
        self.city = city  # type: str
        self.connect_type = connect_type  # type: str
        self.device_name = device_name  # type: str
        self.dn = dn  # type: str
        self.infrared_id = infrared_id  # type: str
        self.infrared_index = infrared_index  # type: str
        self.infrared_version = infrared_version  # type: str
        self.multi_key_switch_ext = multi_key_switch_ext  # type: ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt
        self.name = name  # type: str
        self.number = number  # type: str
        self.pk = pk  # type: str
        self.province = province  # type: str
        self.service_provider = service_provider  # type: str

    def validate(self):
        if self.multi_key_switch_ext:
            self.multi_key_switch_ext.validate()

    def to_map(self):
        _map = super(ImportRoomControlDevicesRequestLocationDevicesDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.city is not None:
            result['City'] = self.city
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.dn is not None:
            result['Dn'] = self.dn
        if self.infrared_id is not None:
            result['InfraredId'] = self.infrared_id
        if self.infrared_index is not None:
            result['InfraredIndex'] = self.infrared_index
        if self.infrared_version is not None:
            result['InfraredVersion'] = self.infrared_version
        if self.multi_key_switch_ext is not None:
            result['MultiKeySwitchExt'] = self.multi_key_switch_ext.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.province is not None:
            result['Province'] = self.province
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Dn') is not None:
            self.dn = m.get('Dn')
        if m.get('InfraredId') is not None:
            self.infrared_id = m.get('InfraredId')
        if m.get('InfraredIndex') is not None:
            self.infrared_index = m.get('InfraredIndex')
        if m.get('InfraredVersion') is not None:
            self.infrared_version = m.get('InfraredVersion')
        if m.get('MultiKeySwitchExt') is not None:
            temp_model = ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt()
            self.multi_key_switch_ext = temp_model.from_map(m['MultiKeySwitchExt'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        return self


class ImportRoomControlDevicesRequestLocationDevices(TeaModel):
    def __init__(self, devices=None, location=None, location_name=None):
        self.devices = devices  # type: list[ImportRoomControlDevicesRequestLocationDevicesDevices]
        self.location = location  # type: str
        self.location_name = location_name  # type: str

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportRoomControlDevicesRequestLocationDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ImportRoomControlDevicesRequestLocationDevicesDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        return self


class ImportRoomControlDevicesRequest(TeaModel):
    def __init__(self, enable_infrared_device_import=None, hotel_id=None, location_devices=None, room_no=None):
        self.enable_infrared_device_import = enable_infrared_device_import  # type: str
        self.hotel_id = hotel_id  # type: str
        self.location_devices = location_devices  # type: list[ImportRoomControlDevicesRequestLocationDevices]
        self.room_no = room_no  # type: str

    def validate(self):
        if self.location_devices:
            for k in self.location_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportRoomControlDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_infrared_device_import is not None:
            result['EnableInfraredDeviceImport'] = self.enable_infrared_device_import
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        result['LocationDevices'] = []
        if self.location_devices is not None:
            for k in self.location_devices:
                result['LocationDevices'].append(k.to_map() if k else None)
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableInfraredDeviceImport') is not None:
            self.enable_infrared_device_import = m.get('EnableInfraredDeviceImport')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        self.location_devices = []
        if m.get('LocationDevices') is not None:
            for k in m.get('LocationDevices'):
                temp_model = ImportRoomControlDevicesRequestLocationDevices()
                self.location_devices.append(temp_model.from_map(k))
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ImportRoomControlDevicesShrinkRequest(TeaModel):
    def __init__(self, enable_infrared_device_import=None, hotel_id=None, location_devices_shrink=None,
                 room_no=None):
        self.enable_infrared_device_import = enable_infrared_device_import  # type: str
        self.hotel_id = hotel_id  # type: str
        self.location_devices_shrink = location_devices_shrink  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomControlDevicesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_infrared_device_import is not None:
            result['EnableInfraredDeviceImport'] = self.enable_infrared_device_import
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.location_devices_shrink is not None:
            result['LocationDevices'] = self.location_devices_shrink
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableInfraredDeviceImport') is not None:
            self.enable_infrared_device_import = m.get('EnableInfraredDeviceImport')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('LocationDevices') is not None:
            self.location_devices_shrink = m.get('LocationDevices')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ImportRoomControlDevicesResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: int
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomControlDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ImportRoomControlDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportRoomControlDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportRoomControlDevicesResponse, self).to_map()
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
            temp_model = ImportRoomControlDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportRoomGenieScenesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomGenieScenesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ImportRoomGenieScenesRequestSceneListActionsAttributeValues(TeaModel):
    def __init__(self, attribute_name=None, attribute_value=None):
        self.attribute_name = attribute_name  # type: str
        self.attribute_value = attribute_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequestSceneListActionsAttributeValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class ImportRoomGenieScenesRequestSceneListActionsDevice(TeaModel):
    def __init__(self, category=None, device_index=None, device_number=None, type=None):
        self.category = category  # type: str
        self.device_index = device_index  # type: int
        self.device_number = device_number  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequestSceneListActionsDevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ImportRoomGenieScenesRequestSceneListActions(TeaModel):
    def __init__(self, attribute_values=None, device=None, reply=None, type=None):
        self.attribute_values = attribute_values  # type: list[ImportRoomGenieScenesRequestSceneListActionsAttributeValues]
        self.device = device  # type: ImportRoomGenieScenesRequestSceneListActionsDevice
        self.reply = reply  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.attribute_values:
            for k in self.attribute_values:
                if k:
                    k.validate()
        if self.device:
            self.device.validate()

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequestSceneListActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttributeValues'] = []
        if self.attribute_values is not None:
            for k in self.attribute_values:
                result['AttributeValues'].append(k.to_map() if k else None)
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.reply is not None:
            result['Reply'] = self.reply
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attribute_values = []
        if m.get('AttributeValues') is not None:
            for k in m.get('AttributeValues'):
                temp_model = ImportRoomGenieScenesRequestSceneListActionsAttributeValues()
                self.attribute_values.append(temp_model.from_map(k))
        if m.get('Device') is not None:
            temp_model = ImportRoomGenieScenesRequestSceneListActionsDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('Reply') is not None:
            self.reply = m.get('Reply')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ImportRoomGenieScenesRequestSceneListTriggersAttributeValues(TeaModel):
    def __init__(self, attribute_name=None, attribute_value=None):
        self.attribute_name = attribute_name  # type: str
        self.attribute_value = attribute_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequestSceneListTriggersAttributeValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class ImportRoomGenieScenesRequestSceneListTriggersDevice(TeaModel):
    def __init__(self, category=None, device_index=None, device_number=None):
        self.category = category  # type: str
        self.device_index = device_index  # type: str
        self.device_number = device_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequestSceneListTriggersDevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        return self


class ImportRoomGenieScenesRequestSceneListTriggers(TeaModel):
    def __init__(self, attribute_values=None, corpus_list=None, device=None, type=None):
        self.attribute_values = attribute_values  # type: list[ImportRoomGenieScenesRequestSceneListTriggersAttributeValues]
        self.corpus_list = corpus_list  # type: list[str]
        self.device = device  # type: ImportRoomGenieScenesRequestSceneListTriggersDevice
        self.type = type  # type: int

    def validate(self):
        if self.attribute_values:
            for k in self.attribute_values:
                if k:
                    k.validate()
        if self.device:
            self.device.validate()

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequestSceneListTriggers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttributeValues'] = []
        if self.attribute_values is not None:
            for k in self.attribute_values:
                result['AttributeValues'].append(k.to_map() if k else None)
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attribute_values = []
        if m.get('AttributeValues') is not None:
            for k in m.get('AttributeValues'):
                temp_model = ImportRoomGenieScenesRequestSceneListTriggersAttributeValues()
                self.attribute_values.append(temp_model.from_map(k))
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Device') is not None:
            temp_model = ImportRoomGenieScenesRequestSceneListTriggersDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ImportRoomGenieScenesRequestSceneList(TeaModel):
    def __init__(self, actions=None, description=None, display=None, icon=None, scene_name=None,
                 trigger_logical=None, triggers=None):
        self.actions = actions  # type: list[ImportRoomGenieScenesRequestSceneListActions]
        self.description = description  # type: str
        self.display = display  # type: bool
        self.icon = icon  # type: str
        self.scene_name = scene_name  # type: str
        self.trigger_logical = trigger_logical  # type: int
        self.triggers = triggers  # type: list[ImportRoomGenieScenesRequestSceneListTriggers]

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequestSceneList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.display is not None:
            result['Display'] = self.display
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.trigger_logical is not None:
            result['TriggerLogical'] = self.trigger_logical
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ImportRoomGenieScenesRequestSceneListActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('TriggerLogical') is not None:
            self.trigger_logical = m.get('TriggerLogical')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = ImportRoomGenieScenesRequestSceneListTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ImportRoomGenieScenesRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no=None, scene_list=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str
        self.scene_list = scene_list  # type: list[ImportRoomGenieScenesRequestSceneList]

    def validate(self):
        if self.scene_list:
            for k in self.scene_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportRoomGenieScenesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        result['SceneList'] = []
        if self.scene_list is not None:
            for k in self.scene_list:
                result['SceneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        self.scene_list = []
        if m.get('SceneList') is not None:
            for k in m.get('SceneList'):
                temp_model = ImportRoomGenieScenesRequestSceneList()
                self.scene_list.append(temp_model.from_map(k))
        return self


class ImportRoomGenieScenesShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no=None, scene_list_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str
        self.scene_list_shrink = scene_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomGenieScenesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.scene_list_shrink is not None:
            result['SceneList'] = self.scene_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('SceneList') is not None:
            self.scene_list_shrink = m.get('SceneList')
        return self


class ImportRoomGenieScenesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportRoomGenieScenesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ImportRoomGenieScenesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportRoomGenieScenesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportRoomGenieScenesResponse, self).to_map()
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
            temp_model = ImportRoomGenieScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertHotelSceneBookItemHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertHotelSceneBookItemHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class InsertHotelSceneBookItemRequestAddHotelSceneItemReq(TeaModel):
    def __init__(self, icon=None, name=None, price=None, type=None):
        # icon
        self.icon = icon  # type: str
        self.name = name  # type: str
        self.price = price  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertHotelSceneBookItemRequestAddHotelSceneItemReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InsertHotelSceneBookItemRequest(TeaModel):
    def __init__(self, add_hotel_scene_item_req=None, hotel_id=None):
        # addHotelSceneItemReq
        self.add_hotel_scene_item_req = add_hotel_scene_item_req  # type: InsertHotelSceneBookItemRequestAddHotelSceneItemReq
        # hotelID
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        if self.add_hotel_scene_item_req:
            self.add_hotel_scene_item_req.validate()

    def to_map(self):
        _map = super(InsertHotelSceneBookItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_hotel_scene_item_req is not None:
            result['AddHotelSceneItemReq'] = self.add_hotel_scene_item_req.to_map()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddHotelSceneItemReq') is not None:
            temp_model = InsertHotelSceneBookItemRequestAddHotelSceneItemReq()
            self.add_hotel_scene_item_req = temp_model.from_map(m['AddHotelSceneItemReq'])
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class InsertHotelSceneBookItemShrinkRequest(TeaModel):
    def __init__(self, add_hotel_scene_item_req_shrink=None, hotel_id=None):
        # addHotelSceneItemReq
        self.add_hotel_scene_item_req_shrink = add_hotel_scene_item_req_shrink  # type: str
        # hotelID
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertHotelSceneBookItemShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_hotel_scene_item_req_shrink is not None:
            result['AddHotelSceneItemReq'] = self.add_hotel_scene_item_req_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddHotelSceneItemReq') is not None:
            self.add_hotel_scene_item_req_shrink = m.get('AddHotelSceneItemReq')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class InsertHotelSceneBookItemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertHotelSceneBookItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InsertHotelSceneBookItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertHotelSceneBookItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertHotelSceneBookItemResponse, self).to_map()
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
            temp_model = InsertHotelSceneBookItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeRobotPushHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeRobotPushHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class InvokeRobotPushRequest(TeaModel):
    def __init__(self, hotel_id=None, push_type=None, room_no=None):
        self.hotel_id = hotel_id  # type: str
        self.push_type = push_type  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeRobotPushRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class InvokeRobotPushResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeRobotPushResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class InvokeRobotPushResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InvokeRobotPushResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InvokeRobotPushResponse, self).to_map()
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
            temp_model = InvokeRobotPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllProvincesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllProvincesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListAllProvincesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllProvincesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListAllProvincesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAllProvincesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAllProvincesResponse, self).to_map()
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
            temp_model = ListAllProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCitiesByProvinceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCitiesByProvinceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCitiesByProvinceRequest(TeaModel):
    def __init__(self, province=None):
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCitiesByProvinceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class ListCitiesByProvinceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCitiesByProvinceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListCitiesByProvinceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCitiesByProvinceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCitiesByProvinceResponse, self).to_map()
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
            temp_model = ListCitiesByProvinceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCustomQARequestPage(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomQARequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCustomQARequest(TeaModel):
    def __init__(self, hotel_id=None, keyword=None, page=None):
        self.hotel_id = hotel_id  # type: str
        self.keyword = keyword  # type: str
        self.page = page  # type: ListCustomQARequestPage

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListCustomQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            temp_model = ListCustomQARequestPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListCustomQAShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, keyword=None, page_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.keyword = keyword  # type: str
        self.page_shrink = page_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomQAShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        return self


class ListCustomQAResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomQAResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCustomQAResponseBodyResult(TeaModel):
    def __init__(self, answers=None, create_time=None, custom_qaid=None, hotel_id=None, key_words=None,
                 major_question=None, status=None, supplementary_question=None, update_time=None):
        self.answers = answers  # type: str
        self.create_time = create_time  # type: str
        self.custom_qaid = custom_qaid  # type: str
        self.hotel_id = hotel_id  # type: str
        self.key_words = key_words  # type: str
        self.major_question = major_question  # type: str
        self.status = status  # type: int
        self.supplementary_question = supplementary_question  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomQAResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_qaid is not None:
            result['CustomQAId'] = self.custom_qaid
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.status is not None:
            result['Status'] = self.status
        if self.supplementary_question is not None:
            result['SupplementaryQuestion'] = self.supplementary_question
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomQAId') is not None:
            self.custom_qaid = m.get('CustomQAId')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementaryQuestion') is not None:
            self.supplementary_question = m.get('SupplementaryQuestion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListCustomQAResponseBody(TeaModel):
    def __init__(self, message=None, page=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.page = page  # type: ListCustomQAResponseBodyPage
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListCustomQAResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListCustomQAResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCustomQAResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListCustomQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomQAResponse, self).to_map()
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
            temp_model = ListCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDialogueTemplateHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDialogueTemplateHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDialogueTemplateRequest(TeaModel):
    def __init__(self, hotel_id=None):
        # hotelId
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDialogueTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate(TeaModel):
    def __init__(self, nonzero_price_yes_answer=None, zero_price_no_answer=None, zero_price_yes_answer=None):
        self.nonzero_price_yes_answer = nonzero_price_yes_answer  # type: str
        self.zero_price_no_answer = zero_price_no_answer  # type: str
        self.zero_price_yes_answer = zero_price_yes_answer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonzero_price_yes_answer is not None:
            result['NonzeroPriceYesAnswer'] = self.nonzero_price_yes_answer
        if self.zero_price_no_answer is not None:
            result['ZeroPriceNoAnswer'] = self.zero_price_no_answer
        if self.zero_price_yes_answer is not None:
            result['ZeroPriceYesAnswer'] = self.zero_price_yes_answer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonzeroPriceYesAnswer') is not None:
            self.nonzero_price_yes_answer = m.get('NonzeroPriceYesAnswer')
        if m.get('ZeroPriceNoAnswer') is not None:
            self.zero_price_no_answer = m.get('ZeroPriceNoAnswer')
        if m.get('ZeroPriceYesAnswer') is not None:
            self.zero_price_yes_answer = m.get('ZeroPriceYesAnswer')
        return self


class ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate(TeaModel):
    def __init__(self, nonzero_price_no_answer=None, nonzero_price_yes_answer=None):
        self.nonzero_price_no_answer = nonzero_price_no_answer  # type: str
        self.nonzero_price_yes_answer = nonzero_price_yes_answer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonzero_price_no_answer is not None:
            result['NonzeroPriceNoAnswer'] = self.nonzero_price_no_answer
        if self.nonzero_price_yes_answer is not None:
            result['NonzeroPriceYesAnswer'] = self.nonzero_price_yes_answer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonzeroPriceNoAnswer') is not None:
            self.nonzero_price_no_answer = m.get('NonzeroPriceNoAnswer')
        if m.get('NonzeroPriceYesAnswer') is not None:
            self.nonzero_price_yes_answer = m.get('NonzeroPriceYesAnswer')
        return self


class ListDialogueTemplateResponseBodyResultTemplateDetail(TeaModel):
    def __init__(self, first_dialogue_template=None, second_dialogue_template=None):
        self.first_dialogue_template = first_dialogue_template  # type: ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate
        self.second_dialogue_template = second_dialogue_template  # type: ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate

    def validate(self):
        if self.first_dialogue_template:
            self.first_dialogue_template.validate()
        if self.second_dialogue_template:
            self.second_dialogue_template.validate()

    def to_map(self):
        _map = super(ListDialogueTemplateResponseBodyResultTemplateDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_dialogue_template is not None:
            result['FirstDialogueTemplate'] = self.first_dialogue_template.to_map()
        if self.second_dialogue_template is not None:
            result['SecondDialogueTemplate'] = self.second_dialogue_template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirstDialogueTemplate') is not None:
            temp_model = ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate()
            self.first_dialogue_template = temp_model.from_map(m['FirstDialogueTemplate'])
        if m.get('SecondDialogueTemplate') is not None:
            temp_model = ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate()
            self.second_dialogue_template = temp_model.from_map(m['SecondDialogueTemplate'])
        return self


class ListDialogueTemplateResponseBodyResult(TeaModel):
    def __init__(self, template_detail=None, template_id=None, template_name=None, type=None):
        self.template_detail = template_detail  # type: ListDialogueTemplateResponseBodyResultTemplateDetail
        self.template_id = template_id  # type: long
        self.template_name = template_name  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.template_detail:
            self.template_detail.validate()

    def to_map(self):
        _map = super(ListDialogueTemplateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail.to_map()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            temp_model = ListDialogueTemplateResponseBodyResultTemplateDetail()
            self.template_detail = temp_model.from_map(m['TemplateDetail'])
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDialogueTemplateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListDialogueTemplateResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDialogueTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDialogueTemplateResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDialogueTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDialogueTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDialogueTemplateResponse, self).to_map()
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
            temp_model = ListDialogueTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelAlarmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelAlarmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelAlarmRequest(TeaModel):
    def __init__(self, hotel_id=None, rooms=None):
        self.hotel_id = hotel_id  # type: str
        self.rooms = rooms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.rooms is not None:
            result['Rooms'] = self.rooms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Rooms') is not None:
            self.rooms = m.get('Rooms')
        return self


class ListHotelAlarmShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, rooms_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.rooms_shrink = rooms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelAlarmShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.rooms_shrink is not None:
            result['Rooms'] = self.rooms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Rooms') is not None:
            self.rooms_shrink = m.get('Rooms')
        return self


class ListHotelAlarmResponseBodyResultScheduleInfoOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelAlarmResponseBodyResultScheduleInfoOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ListHotelAlarmResponseBodyResultScheduleInfoWeekly(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelAlarmResponseBodyResultScheduleInfoWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListHotelAlarmResponseBodyResultScheduleInfo(TeaModel):
    def __init__(self, once=None, type=None, weekly=None):
        self.once = once  # type: ListHotelAlarmResponseBodyResultScheduleInfoOnce
        # ONCE, WEEKLY
        self.type = type  # type: str
        self.weekly = weekly  # type: ListHotelAlarmResponseBodyResultScheduleInfoWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(ListHotelAlarmResponseBodyResultScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = ListHotelAlarmResponseBodyResultScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = ListHotelAlarmResponseBodyResultScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class ListHotelAlarmResponseBodyResult(TeaModel):
    def __init__(self, alarm_id=None, device_open_id=None, schedule_info=None, user_open_id=None):
        self.alarm_id = alarm_id  # type: long
        self.device_open_id = device_open_id  # type: str
        self.schedule_info = schedule_info  # type: ListHotelAlarmResponseBodyResultScheduleInfo
        self.user_open_id = user_open_id  # type: str

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(ListHotelAlarmResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('ScheduleInfo') is not None:
            temp_model = ListHotelAlarmResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class ListHotelAlarmResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListHotelAlarmResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelAlarmResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListHotelAlarmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelAlarmResponse, self).to_map()
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
            temp_model = ListHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelControlDeviceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelControlDeviceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelControlDeviceRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelControlDeviceRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListHotelControlDeviceRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: ListHotelControlDeviceRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListHotelControlDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = ListHotelControlDeviceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListHotelControlDeviceShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelControlDeviceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListHotelControlDeviceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelControlDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ListHotelControlDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelControlDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelControlDeviceResponse, self).to_map()
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
            temp_model = ListHotelControlDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelInfoResponseBodyResultAuthAccount(TeaModel):
    def __init__(self, user_name=None):
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelInfoResponseBodyResultAuthAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListHotelInfoResponseBodyResult(TeaModel):
    def __init__(self, auth_account=None, hotel_address=None, hotel_id=None, hotel_name=None):
        self.auth_account = auth_account  # type: list[ListHotelInfoResponseBodyResultAuthAccount]
        self.hotel_address = hotel_address  # type: str
        self.hotel_id = hotel_id  # type: str
        self.hotel_name = hotel_name  # type: str

    def validate(self):
        if self.auth_account:
            for k in self.auth_account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthAccount'] = []
        if self.auth_account is not None:
            for k in self.auth_account:
                result['AuthAccount'].append(k.to_map() if k else None)
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auth_account = []
        if m.get('AuthAccount') is not None:
            for k in m.get('AuthAccount'):
                temp_model = ListHotelInfoResponseBodyResultAuthAccount()
                self.auth_account.append(temp_model.from_map(k))
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        return self


class ListHotelInfoResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListHotelInfoResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListHotelInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelInfoResponse, self).to_map()
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
            temp_model = ListHotelInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelMessageTemplateHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelMessageTemplateHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelMessageTemplateResponseBodyResult(TeaModel):
    def __init__(self, audit_mark=None, audit_status=None, template_detail=None, template_id=None,
                 template_name=None):
        self.audit_mark = audit_mark  # type: str
        self.audit_status = audit_status  # type: str
        self.template_detail = template_detail  # type: str
        self.template_id = template_id  # type: long
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelMessageTemplateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_mark is not None:
            result['AuditMark'] = self.audit_mark
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditMark') is not None:
            self.audit_mark = m.get('AuditMark')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('TemplateDetail') is not None:
            self.template_detail = m.get('TemplateDetail')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListHotelMessageTemplateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListHotelMessageTemplateResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelMessageTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelMessageTemplateResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelMessageTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelMessageTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelMessageTemplateResponse, self).to_map()
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
            temp_model = ListHotelMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelOrderHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelOrderHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelOrderRequestPayloadPage(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelOrderRequestPayloadPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelOrderRequestPayload(TeaModel):
    def __init__(self, page=None):
        self.page = page  # type: ListHotelOrderRequestPayloadPage

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListHotelOrderRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListHotelOrderRequestPayloadPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListHotelOrderRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelOrderRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListHotelOrderRequest(TeaModel):
    def __init__(self, payload=None, user_info=None):
        self.payload = payload  # type: ListHotelOrderRequestPayload
        self.user_info = user_info  # type: ListHotelOrderRequestUserInfo

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListHotelOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = ListHotelOrderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListHotelOrderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListHotelOrderShrinkRequest(TeaModel):
    def __init__(self, payload_shrink=None, user_info_shrink=None):
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelOrderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListHotelOrderResponseBodyPage(TeaModel):
    def __init__(self, has_next=None, page_number=None, page_size=None, total=None, total_page=None):
        self.has_next = has_next  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelOrderResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelOrderResponseBodyResult(TeaModel):
    def __init__(self, apply_amt=None, gmt_create=None, order_no=None, quantity=None, room_no=None, status=None,
                 type=None, type_icon_url=None, type_name=None):
        self.apply_amt = apply_amt  # type: long
        self.gmt_create = gmt_create  # type: long
        self.order_no = order_no  # type: str
        self.quantity = quantity  # type: long
        self.room_no = room_no  # type: str
        self.status = status  # type: str
        self.type = type  # type: str
        self.type_icon_url = type_icon_url  # type: str
        self.type_name = type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelOrderResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_amt is not None:
            result['ApplyAmt'] = self.apply_amt
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.type_icon_url is not None:
            result['TypeIconUrl'] = self.type_icon_url
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyAmt') is not None:
            self.apply_amt = m.get('ApplyAmt')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeIconUrl') is not None:
            self.type_icon_url = m.get('TypeIconUrl')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListHotelOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, page=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.page = page  # type: ListHotelOrderResponseBodyPage
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListHotelOrderResponseBodyResult]

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListHotelOrderResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelOrderResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelOrderResponse, self).to_map()
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
            temp_model = ListHotelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelRoomsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelRoomsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelRoomsRequest(TeaModel):
    def __init__(self, hotel_id=None):
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelRoomsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ListHotelRoomsResponseBodyResult(TeaModel):
    def __init__(self, hotel_id=None, room_no=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelRoomsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ListHotelRoomsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListHotelRoomsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelRoomsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelRoomsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelRoomsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelRoomsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelRoomsResponse, self).to_map()
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
            temp_model = ListHotelRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelSceneBookItemsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneBookItemsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelSceneBookItemsRequestPage(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneBookItemsRequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelSceneBookItemsRequest(TeaModel):
    def __init__(self, hotel_id=None, page=None, type=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        self.page = page  # type: ListHotelSceneBookItemsRequestPage
        self.type = type  # type: str

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListHotelSceneBookItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Page') is not None:
            temp_model = ListHotelSceneBookItemsRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneBookItemsShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, page_shrink=None, type=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        self.page_shrink = page_shrink  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneBookItemsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneBookItemsResponseBodyResultPage(TeaModel):
    def __init__(self, has_next=None, page_number=None, page_size=None, total=None, total_page=None):
        self.has_next = has_next  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneBookItemsResponseBodyResultPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelSceneBookItemsResponseBodyResultSceneItemList(TeaModel):
    def __init__(self, icon=None, id=None, name=None, price=None, status=None, type=None, update_time=None):
        self.icon = icon  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.price = price  # type: long
        self.status = status  # type: str
        self.type = type  # type: str
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneBookItemsResponseBodyResultSceneItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListHotelSceneBookItemsResponseBodyResult(TeaModel):
    def __init__(self, page=None, scene_item_list=None):
        self.page = page  # type: ListHotelSceneBookItemsResponseBodyResultPage
        self.scene_item_list = scene_item_list  # type: list[ListHotelSceneBookItemsResponseBodyResultSceneItemList]

    def validate(self):
        if self.page:
            self.page.validate()
        if self.scene_item_list:
            for k in self.scene_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelSceneBookItemsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['SceneItemList'] = []
        if self.scene_item_list is not None:
            for k in self.scene_item_list:
                result['SceneItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListHotelSceneBookItemsResponseBodyResultPage()
            self.page = temp_model.from_map(m['Page'])
        self.scene_item_list = []
        if m.get('SceneItemList') is not None:
            for k in m.get('SceneItemList'):
                temp_model = ListHotelSceneBookItemsResponseBodyResultSceneItemList()
                self.scene_item_list.append(temp_model.from_map(k))
        return self


class ListHotelSceneBookItemsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ListHotelSceneBookItemsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListHotelSceneBookItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelSceneBookItemsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelSceneBookItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelSceneBookItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelSceneBookItemsResponse, self).to_map()
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
            temp_model = ListHotelSceneBookItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelSceneItemHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelSceneItemRequestPayload(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneItemRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListHotelSceneItemRequest(TeaModel):
    def __init__(self, payload=None, user_info=None):
        self.payload = payload  # type: ListHotelSceneItemRequestPayload
        self.user_info = user_info  # type: ListHotelSceneItemRequestUserInfo

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = ListHotelSceneItemRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListHotelSceneItemRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListHotelSceneItemShrinkRequest(TeaModel):
    def __init__(self, payload_shrink=None, user_info_shrink=None):
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListHotelSceneItemResponseBodyPage(TeaModel):
    def __init__(self, has_next=None, page_number=None, page_size=None, total=None, total_page=None):
        self.has_next = has_next  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelSceneItemResponseBodyResultSecondCategoryListItemList(TeaModel):
    def __init__(self, category=None, icon=None, id=None, name=None, price=None, residue_limit=None, status=None,
                 type=None):
        self.category = category  # type: str
        self.icon = icon  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.price = price  # type: long
        self.residue_limit = residue_limit  # type: long
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemResponseBodyResultSecondCategoryListItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.residue_limit is not None:
            result['ResidueLimit'] = self.residue_limit
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ResidueLimit') is not None:
            self.residue_limit = m.get('ResidueLimit')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneItemResponseBodyResultSecondCategoryList(TeaModel):
    def __init__(self, item_list=None, second_category_name=None):
        self.item_list = item_list  # type: list[ListHotelSceneItemResponseBodyResultSecondCategoryListItemList]
        self.second_category_name = second_category_name  # type: str

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemResponseBodyResultSecondCategoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = ListHotelSceneItemResponseBodyResultSecondCategoryListItemList()
                self.item_list.append(temp_model.from_map(k))
        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')
        return self


class ListHotelSceneItemResponseBodyResult(TeaModel):
    def __init__(self, second_category_list=None):
        self.second_category_list = second_category_list  # type: list[ListHotelSceneItemResponseBodyResultSecondCategoryList]

    def validate(self):
        if self.second_category_list:
            for k in self.second_category_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecondCategoryList'] = []
        if self.second_category_list is not None:
            for k in self.second_category_list:
                result['SecondCategoryList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.second_category_list = []
        if m.get('SecondCategoryList') is not None:
            for k in m.get('SecondCategoryList'):
                temp_model = ListHotelSceneItemResponseBodyResultSecondCategoryList()
                self.second_category_list.append(temp_model.from_map(k))
        return self


class ListHotelSceneItemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, page=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.page = page  # type: ListHotelSceneItemResponseBodyPage
        self.request_id = request_id  # type: str
        self.result = result  # type: ListHotelSceneItemResponseBodyResult

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListHotelSceneItemResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelSceneItemResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelSceneItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelSceneItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemResponse, self).to_map()
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
            temp_model = ListHotelSceneItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelSceneItemsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelSceneItemsRequestListHotelSceneReqPage(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemsRequestListHotelSceneReqPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelSceneItemsRequestListHotelSceneReq(TeaModel):
    def __init__(self, category=None, keywords=None, page=None, status=None, type=None):
        self.category = category  # type: str
        self.keywords = keywords  # type: str
        self.page = page  # type: ListHotelSceneItemsRequestListHotelSceneReqPage
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemsRequestListHotelSceneReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Page') is not None:
            temp_model = ListHotelSceneItemsRequestListHotelSceneReqPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneItemsRequest(TeaModel):
    def __init__(self, hotel_id=None, list_hotel_scene_req=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        # ListHotelSceneReq
        self.list_hotel_scene_req = list_hotel_scene_req  # type: ListHotelSceneItemsRequestListHotelSceneReq

    def validate(self):
        if self.list_hotel_scene_req:
            self.list_hotel_scene_req.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.list_hotel_scene_req is not None:
            result['ListHotelSceneReq'] = self.list_hotel_scene_req.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ListHotelSceneReq') is not None:
            temp_model = ListHotelSceneItemsRequestListHotelSceneReq()
            self.list_hotel_scene_req = temp_model.from_map(m['ListHotelSceneReq'])
        return self


class ListHotelSceneItemsShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, list_hotel_scene_req_shrink=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        # ListHotelSceneReq
        self.list_hotel_scene_req_shrink = list_hotel_scene_req_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.list_hotel_scene_req_shrink is not None:
            result['ListHotelSceneReq'] = self.list_hotel_scene_req_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ListHotelSceneReq') is not None:
            self.list_hotel_scene_req_shrink = m.get('ListHotelSceneReq')
        return self


class ListHotelSceneItemsResponseBodyResultPage(TeaModel):
    def __init__(self, has_next=None, page_number=None, page_size=None, total=None, total_page=None):
        self.has_next = has_next  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemsResponseBodyResultPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelSceneItemsResponseBodyResultSceneItemList(TeaModel):
    def __init__(self, beyond_limit_reply=None, category=None, delivery_method=None, icon=None, id=None,
                 limit_number=None, limit_switch=None, name=None, payment_method=None, price=None, robot_name=None, status=None,
                 type=None, update_time=None):
        self.beyond_limit_reply = beyond_limit_reply  # type: str
        self.category = category  # type: str
        self.delivery_method = delivery_method  # type: str
        self.icon = icon  # type: str
        # id
        self.id = id  # type: long
        self.limit_number = limit_number  # type: int
        self.limit_switch = limit_switch  # type: int
        self.name = name  # type: str
        self.payment_method = payment_method  # type: str
        self.price = price  # type: long
        self.robot_name = robot_name  # type: str
        self.status = status  # type: str
        self.type = type  # type: str
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelSceneItemsResponseBodyResultSceneItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beyond_limit_reply is not None:
            result['BeyondLimitReply'] = self.beyond_limit_reply
        if self.category is not None:
            result['Category'] = self.category
        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number
        if self.limit_switch is not None:
            result['LimitSwitch'] = self.limit_switch
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method
        if self.price is not None:
            result['Price'] = self.price
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeyondLimitReply') is not None:
            self.beyond_limit_reply = m.get('BeyondLimitReply')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')
        if m.get('LimitSwitch') is not None:
            self.limit_switch = m.get('LimitSwitch')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListHotelSceneItemsResponseBodyResult(TeaModel):
    def __init__(self, page=None, scene_item_list=None):
        self.page = page  # type: ListHotelSceneItemsResponseBodyResultPage
        self.scene_item_list = scene_item_list  # type: list[ListHotelSceneItemsResponseBodyResultSceneItemList]

    def validate(self):
        if self.page:
            self.page.validate()
        if self.scene_item_list:
            for k in self.scene_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['SceneItemList'] = []
        if self.scene_item_list is not None:
            for k in self.scene_item_list:
                result['SceneItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListHotelSceneItemsResponseBodyResultPage()
            self.page = temp_model.from_map(m['Page'])
        self.scene_item_list = []
        if m.get('SceneItemList') is not None:
            for k in m.get('SceneItemList'):
                temp_model = ListHotelSceneItemsResponseBodyResultSceneItemList()
                self.scene_item_list.append(temp_model.from_map(k))
        return self


class ListHotelSceneItemsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ListHotelSceneItemsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelSceneItemsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelSceneItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelSceneItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelSceneItemsResponse, self).to_map()
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
            temp_model = ListHotelSceneItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelServiceCategoryHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelServiceCategoryHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelServiceCategoryRequestPayload(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelServiceCategoryRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelServiceCategoryRequest(TeaModel):
    def __init__(self, payload=None):
        self.payload = payload  # type: ListHotelServiceCategoryRequestPayload

    def validate(self):
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super(ListHotelServiceCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = ListHotelServiceCategoryRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        return self


class ListHotelServiceCategoryShrinkRequest(TeaModel):
    def __init__(self, payload_shrink=None):
        self.payload_shrink = payload_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelServiceCategoryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        return self


class ListHotelServiceCategoryResponseBodyResult(TeaModel):
    def __init__(self, code=None, desc=None, icon=None, name=None, type=None):
        self.code = code  # type: str
        self.desc = desc  # type: str
        self.icon = icon  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelServiceCategoryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelServiceCategoryResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListHotelServiceCategoryResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotelServiceCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelServiceCategoryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelServiceCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelServiceCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelServiceCategoryResponse, self).to_map()
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
            temp_model = ListHotelServiceCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelsRequestPage(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelsRequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelsRequest(TeaModel):
    def __init__(self, page=None, status=None):
        self.page = page  # type: ListHotelsRequestPage
        self.status = status  # type: int

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListHotelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListHotelsRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListHotelsShrinkRequest(TeaModel):
    def __init__(self, page_shrink=None, status=None):
        self.page_shrink = page_shrink  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListHotelsResponseBodyResultHotelInfoList(TeaModel):
    def __init__(self, account_names=None, create_time=None, hotel_address=None, hotel_id=None, hotel_name=None,
                 industry_type=None, phone_number=None, related_product_name=None, room_num=None, status=None):
        self.account_names = account_names  # type: list[str]
        self.create_time = create_time  # type: long
        self.hotel_address = hotel_address  # type: str
        self.hotel_id = hotel_id  # type: str
        self.hotel_name = hotel_name  # type: str
        self.industry_type = industry_type  # type: str
        self.phone_number = phone_number  # type: str
        self.related_product_name = related_product_name  # type: str
        self.room_num = room_num  # type: int
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelsResponseBodyResultHotelInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_names is not None:
            result['AccountNames'] = self.account_names
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.industry_type is not None:
            result['IndustryType'] = self.industry_type
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_product_name is not None:
            result['RelatedProductName'] = self.related_product_name
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNames') is not None:
            self.account_names = m.get('AccountNames')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('IndustryType') is not None:
            self.industry_type = m.get('IndustryType')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedProductName') is not None:
            self.related_product_name = m.get('RelatedProductName')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListHotelsResponseBodyResultPage(TeaModel):
    def __init__(self, has_next=None, page_number=None, page_size=None, total=None, total_page=None):
        self.has_next = has_next  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotelsResponseBodyResultPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelsResponseBodyResult(TeaModel):
    def __init__(self, hotel_info_list=None, page=None):
        self.hotel_info_list = hotel_info_list  # type: list[ListHotelsResponseBodyResultHotelInfoList]
        self.page = page  # type: ListHotelsResponseBodyResultPage

    def validate(self):
        if self.hotel_info_list:
            for k in self.hotel_info_list:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListHotelsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotelInfoList'] = []
        if self.hotel_info_list is not None:
            for k in self.hotel_info_list:
                result['HotelInfoList'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hotel_info_list = []
        if m.get('HotelInfoList') is not None:
            for k in m.get('HotelInfoList'):
                temp_model = ListHotelsResponseBodyResultHotelInfoList()
                self.hotel_info_list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            temp_model = ListHotelsResponseBodyResultPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListHotelsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        self.result = result  # type: ListHotelsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListHotelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotelsResponse, self).to_map()
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
            temp_model = ListHotelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInfraredDeviceBrandsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInfraredDeviceBrandsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListInfraredDeviceBrandsRequest(TeaModel):
    def __init__(self, category=None, service_provider=None):
        self.category = category  # type: str
        self.service_provider = service_provider  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInfraredDeviceBrandsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        return self


class ListInfraredDeviceBrandsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, list[str]]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInfraredDeviceBrandsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListInfraredDeviceBrandsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInfraredDeviceBrandsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInfraredDeviceBrandsResponse, self).to_map()
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
            temp_model = ListInfraredDeviceBrandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInfraredRemoteControllersHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInfraredRemoteControllersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListInfraredRemoteControllersRequest(TeaModel):
    def __init__(self, brand=None, category=None, city=None, hotel_id=None, province=None, service_provider=None):
        self.brand = brand  # type: str
        self.category = category  # type: str
        self.city = city  # type: str
        self.hotel_id = hotel_id  # type: str
        self.province = province  # type: str
        self.service_provider = service_provider  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInfraredRemoteControllersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.category is not None:
            result['Category'] = self.category
        if self.city is not None:
            result['City'] = self.city
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.province is not None:
            result['Province'] = self.province
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        return self


class ListInfraredRemoteControllersResponseBodyResult(TeaModel):
    def __init__(self, index=None, rid=None, version=None):
        self.index = index  # type: int
        self.rid = rid  # type: long
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInfraredRemoteControllersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListInfraredRemoteControllersResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListInfraredRemoteControllersResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInfraredRemoteControllersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInfraredRemoteControllersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListInfraredRemoteControllersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInfraredRemoteControllersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInfraredRemoteControllersResponse, self).to_map()
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
            temp_model = ListInfraredRemoteControllersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSTBServiceProvidersHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSTBServiceProvidersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListSTBServiceProvidersRequest(TeaModel):
    def __init__(self, city=None, province=None):
        self.city = city  # type: str
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSTBServiceProvidersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class ListSTBServiceProvidersResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, list[str]]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSTBServiceProvidersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListSTBServiceProvidersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSTBServiceProvidersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSTBServiceProvidersResponse, self).to_map()
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
            temp_model = ListSTBServiceProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneCategoryHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSceneCategoryHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListSceneCategoryRequest(TeaModel):
    def __init__(self, hotel_id=None, type=None):
        # hotelId
        self.hotel_id = hotel_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSceneCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSceneCategoryResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSceneCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ListSceneCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSceneCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSceneCategoryResponse, self).to_map()
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
            temp_model = ListSceneCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListServiceQARequestPage(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceQARequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListServiceQARequest(TeaModel):
    def __init__(self, active=None, hotel_id=None, keyword=None, page=None):
        self.active = active  # type: bool
        self.hotel_id = hotel_id  # type: str
        self.keyword = keyword  # type: str
        self.page = page  # type: ListServiceQARequestPage

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListServiceQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            temp_model = ListServiceQARequestPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListServiceQAShrinkRequest(TeaModel):
    def __init__(self, active=None, hotel_id=None, keyword=None, page_shrink=None):
        self.active = active  # type: bool
        self.hotel_id = hotel_id  # type: str
        self.keyword = keyword  # type: str
        self.page_shrink = page_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceQAShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        return self


class ListServiceQAResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceQAResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListServiceQAResponseBodyResult(TeaModel):
    def __init__(self, active=None, answer=None, gmt_modified=None, question=None, service_qaid=None, templates=None):
        self.active = active  # type: bool
        self.answer = answer  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.question = question  # type: str
        self.service_qaid = service_qaid  # type: long
        self.templates = templates  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceQAResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.question is not None:
            result['Question'] = self.question
        if self.service_qaid is not None:
            result['ServiceQAId'] = self.service_qaid
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceQAId') is not None:
            self.service_qaid = m.get('ServiceQAId')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class ListServiceQAResponseBody(TeaModel):
    def __init__(self, message=None, page=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.page = page  # type: ListServiceQAResponseBodyPage
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListServiceQAResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListServiceQAResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListServiceQAResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListServiceQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceQAResponse, self).to_map()
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
            temp_model = ListServiceQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListTicketsRequestPage(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsRequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTicketsRequest(TeaModel):
    def __init__(self, end_time=None, hotel_id=None, is_desc=None, is_need_callback=None, is_need_charges=None,
                 page=None, room_no=None, sort_field=None, start_time=None, status=None, type=None):
        self.end_time = end_time  # type: str
        self.hotel_id = hotel_id  # type: str
        self.is_desc = is_desc  # type: bool
        self.is_need_callback = is_need_callback  # type: bool
        self.is_need_charges = is_need_charges  # type: bool
        self.page = page  # type: ListTicketsRequestPage
        self.room_no = room_no  # type: str
        self.sort_field = sort_field  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListTicketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.is_desc is not None:
            result['IsDesc'] = self.is_desc
        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback
        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('IsDesc') is not None:
            self.is_desc = m.get('IsDesc')
        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')
        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')
        if m.get('Page') is not None:
            temp_model = ListTicketsRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTicketsShrinkRequest(TeaModel):
    def __init__(self, end_time=None, hotel_id=None, is_desc=None, is_need_callback=None, is_need_charges=None,
                 page_shrink=None, room_no=None, sort_field=None, start_time=None, status=None, type=None):
        self.end_time = end_time  # type: str
        self.hotel_id = hotel_id  # type: str
        self.is_desc = is_desc  # type: bool
        self.is_need_callback = is_need_callback  # type: bool
        self.is_need_charges = is_need_charges  # type: bool
        self.page_shrink = page_shrink  # type: str
        self.room_no = room_no  # type: str
        self.sort_field = sort_field  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.is_desc is not None:
            result['IsDesc'] = self.is_desc
        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback
        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('IsDesc') is not None:
            self.is_desc = m.get('IsDesc')
        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')
        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTicketsResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTicketsResponseBodyResultDialogs(TeaModel):
    def __init__(self, answer=None, question=None):
        self.answer = answer  # type: str
        self.question = question  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTicketsResponseBodyResultDialogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.question is not None:
            result['Question'] = self.question
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        return self


class ListTicketsResponseBodyResult(TeaModel):
    def __init__(self, action=None, assigned_handler=None, charges_remark=None, complete_remark=None, dialogs=None,
                 gmt_called=None, gmt_create=None, gmt_delayed=None, gmt_modified=None, group_key=None, id=None,
                 is_accepted_charges=None, is_delayed=None, is_need_callback=None, is_need_charges=None, operations=None, remark=None,
                 room_no=None, status=None, type=None):
        self.action = action  # type: bool
        self.assigned_handler = assigned_handler  # type: str
        self.charges_remark = charges_remark  # type: str
        self.complete_remark = complete_remark  # type: str
        self.dialogs = dialogs  # type: list[ListTicketsResponseBodyResultDialogs]
        self.gmt_called = gmt_called  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_delayed = gmt_delayed  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.group_key = group_key  # type: str
        self.id = id  # type: long
        self.is_accepted_charges = is_accepted_charges  # type: bool
        self.is_delayed = is_delayed  # type: bool
        self.is_need_callback = is_need_callback  # type: bool
        self.is_need_charges = is_need_charges  # type: bool
        self.operations = operations  # type: list[dict[str, any]]
        self.remark = remark  # type: str
        self.room_no = room_no  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.dialogs:
            for k in self.dialogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTicketsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.assigned_handler is not None:
            result['AssignedHandler'] = self.assigned_handler
        if self.charges_remark is not None:
            result['ChargesRemark'] = self.charges_remark
        if self.complete_remark is not None:
            result['CompleteRemark'] = self.complete_remark
        result['Dialogs'] = []
        if self.dialogs is not None:
            for k in self.dialogs:
                result['Dialogs'].append(k.to_map() if k else None)
        if self.gmt_called is not None:
            result['GmtCalled'] = self.gmt_called
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_delayed is not None:
            result['GmtDelayed'] = self.gmt_delayed
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_key is not None:
            result['GroupKey'] = self.group_key
        if self.id is not None:
            result['Id'] = self.id
        if self.is_accepted_charges is not None:
            result['IsAcceptedCharges'] = self.is_accepted_charges
        if self.is_delayed is not None:
            result['IsDelayed'] = self.is_delayed
        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback
        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges
        if self.operations is not None:
            result['Operations'] = self.operations
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('AssignedHandler') is not None:
            self.assigned_handler = m.get('AssignedHandler')
        if m.get('ChargesRemark') is not None:
            self.charges_remark = m.get('ChargesRemark')
        if m.get('CompleteRemark') is not None:
            self.complete_remark = m.get('CompleteRemark')
        self.dialogs = []
        if m.get('Dialogs') is not None:
            for k in m.get('Dialogs'):
                temp_model = ListTicketsResponseBodyResultDialogs()
                self.dialogs.append(temp_model.from_map(k))
        if m.get('GmtCalled') is not None:
            self.gmt_called = m.get('GmtCalled')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtDelayed') is not None:
            self.gmt_delayed = m.get('GmtDelayed')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsAcceptedCharges') is not None:
            self.is_accepted_charges = m.get('IsAcceptedCharges')
        if m.get('IsDelayed') is not None:
            self.is_delayed = m.get('IsDelayed')
        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')
        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')
        if m.get('Operations') is not None:
            self.operations = m.get('Operations')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTicketsResponseBody(TeaModel):
    def __init__(self, message=None, page=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.page = page  # type: ListTicketsResponseBodyPage
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListTicketsResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTicketsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListTicketsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListTicketsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListTicketsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTicketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTicketsResponse, self).to_map()
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
            temp_model = ListTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageGetHotelRoomDevicesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageGetHotelRoomDevicesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PageGetHotelRoomDevicesRequest(TeaModel):
    def __init__(self, hotel_id=None, page_number=None, page_size=None):
        self.hotel_id = hotel_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageGetHotelRoomDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class PageGetHotelRoomDevicesResponseBodyPage(TeaModel):
    def __init__(self, end=None, has_next=None, page_number=None, page_size=None, start=None, total=None,
                 total_page=None):
        self.end = end  # type: int
        self.has_next = has_next  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start = start  # type: int
        self.total = total  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageGetHotelRoomDevicesResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start is not None:
            result['Start'] = self.start
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class PageGetHotelRoomDevicesResponseBodyResult(TeaModel):
    def __init__(self, firmware_version=None, hotel_id=None, mac=None, online_status=None, room_no=None, sn=None):
        self.firmware_version = firmware_version  # type: str
        self.hotel_id = hotel_id  # type: str
        self.mac = mac  # type: str
        self.online_status = online_status  # type: int
        self.room_no = room_no  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageGetHotelRoomDevicesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class PageGetHotelRoomDevicesResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, page=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.page = page  # type: PageGetHotelRoomDevicesResponseBodyPage
        self.request_id = request_id  # type: str
        self.result = result  # type: list[PageGetHotelRoomDevicesResponseBodyResult]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PageGetHotelRoomDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = PageGetHotelRoomDevicesResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = PageGetHotelRoomDevicesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class PageGetHotelRoomDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PageGetHotelRoomDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PageGetHotelRoomDevicesResponse, self).to_map()
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
            temp_model = PageGetHotelRoomDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushHotelMessageHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushHotelMessageHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushHotelMessageRequestPushHotelMessageReq(TeaModel):
    def __init__(self, hotel_id=None, param_map=None, room_no=None, template_id=None):
        self.hotel_id = hotel_id  # type: str
        self.param_map = param_map  # type: dict[str, str]
        self.room_no = room_no  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushHotelMessageRequestPushHotelMessageReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.param_map is not None:
            result['ParamMap'] = self.param_map
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ParamMap') is not None:
            self.param_map = m.get('ParamMap')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class PushHotelMessageRequest(TeaModel):
    def __init__(self, push_hotel_message_req=None):
        # pushHotelMessageReq
        self.push_hotel_message_req = push_hotel_message_req  # type: PushHotelMessageRequestPushHotelMessageReq

    def validate(self):
        if self.push_hotel_message_req:
            self.push_hotel_message_req.validate()

    def to_map(self):
        _map = super(PushHotelMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_hotel_message_req is not None:
            result['PushHotelMessageReq'] = self.push_hotel_message_req.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PushHotelMessageReq') is not None:
            temp_model = PushHotelMessageRequestPushHotelMessageReq()
            self.push_hotel_message_req = temp_model.from_map(m['PushHotelMessageReq'])
        return self


class PushHotelMessageShrinkRequest(TeaModel):
    def __init__(self, push_hotel_message_req_shrink=None):
        # pushHotelMessageReq
        self.push_hotel_message_req_shrink = push_hotel_message_req_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushHotelMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_hotel_message_req_shrink is not None:
            result['PushHotelMessageReq'] = self.push_hotel_message_req_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PushHotelMessageReq') is not None:
            self.push_hotel_message_req_shrink = m.get('PushHotelMessageReq')
        return self


class PushHotelMessageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushHotelMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class PushHotelMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushHotelMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushHotelMessageResponse, self).to_map()
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
            temp_model = PushHotelMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushWelcomeTextAndMusicHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushWelcomeTextAndMusicHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushWelcomeTextAndMusicRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no=None, template_variable=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str
        self.template_variable = template_variable  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushWelcomeTextAndMusicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.template_variable is not None:
            result['TemplateVariable'] = self.template_variable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('TemplateVariable') is not None:
            self.template_variable = m.get('TemplateVariable')
        return self


class PushWelcomeTextAndMusicShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no=None, template_variable_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str
        self.template_variable_shrink = template_variable_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushWelcomeTextAndMusicShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.template_variable_shrink is not None:
            result['TemplateVariable'] = self.template_variable_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('TemplateVariable') is not None:
            self.template_variable_shrink = m.get('TemplateVariable')
        return self


class PushWelcomeTextAndMusicResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushWelcomeTextAndMusicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class PushWelcomeTextAndMusicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushWelcomeTextAndMusicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushWelcomeTextAndMusicResponse, self).to_map()
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
            temp_model = PushWelcomeTextAndMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceStatusHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceStatusHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryDeviceStatusRequestPayloadLocationDevices(TeaModel):
    def __init__(self, device_number=None, device_type=None, location=None):
        self.device_number = device_number  # type: str
        self.device_type = device_type  # type: str
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceStatusRequestPayloadLocationDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class QueryDeviceStatusRequestPayload(TeaModel):
    def __init__(self, location_devices=None, properties=None):
        self.location_devices = location_devices  # type: list[QueryDeviceStatusRequestPayloadLocationDevices]
        self.properties = properties  # type: dict[str, str]

    def validate(self):
        if self.location_devices:
            for k in self.location_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDeviceStatusRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LocationDevices'] = []
        if self.location_devices is not None:
            for k in self.location_devices:
                result['LocationDevices'].append(k.to_map() if k else None)
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.location_devices = []
        if m.get('LocationDevices') is not None:
            for k in m.get('LocationDevices'):
                temp_model = QueryDeviceStatusRequestPayloadLocationDevices()
                self.location_devices.append(temp_model.from_map(k))
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class QueryDeviceStatusRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceStatusRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class QueryDeviceStatusRequest(TeaModel):
    def __init__(self, payload=None, user_info=None):
        self.payload = payload  # type: QueryDeviceStatusRequestPayload
        self.user_info = user_info  # type: QueryDeviceStatusRequestUserInfo

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(QueryDeviceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = QueryDeviceStatusRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = QueryDeviceStatusRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class QueryDeviceStatusShrinkRequest(TeaModel):
    def __init__(self, payload_shrink=None, user_info_shrink=None):
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class QueryDeviceStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class QueryDeviceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceStatusResponse, self).to_map()
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
            temp_model = QueryDeviceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHotelRoomDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotelRoomDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryHotelRoomDetailRequest(TeaModel):
    def __init__(self, hotel_id=None, mac=None, room_no=None, sn=None, uuid=None):
        self.hotel_id = hotel_id  # type: str
        self.mac = mac  # type: str
        self.room_no = room_no  # type: str
        # 设备sn信息
        # 注：若在mac uuid sn全都输入的情况下 按照输入正确的内容查询 若全输入都是正确的 则 按照 uuid > mac > sn 优先级查询
        # 传入mac uuid sn其中一个 则酒店id和房间号可不传
        self.sn = sn  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotelRoomDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryHotelRoomDetailResponseBodyResultAuthAccounts(TeaModel):
    def __init__(self, account_name=None, auth_time=None):
        self.account_name = account_name  # type: str
        self.auth_time = auth_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBodyResultAuthAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')
        return self


class QueryHotelRoomDetailResponseBodyResultDeviceInfos(TeaModel):
    def __init__(self, active_time=None, device_name=None, firmware_version=None, mac=None, online_status=None,
                 sn=None, uuid=None):
        self.active_time = active_time  # type: str
        self.device_name = device_name  # type: str
        self.firmware_version = firmware_version  # type: str
        self.mac = mac  # type: str
        self.online_status = online_status  # type: int
        self.sn = sn  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBodyResultDeviceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryHotelRoomDetailResponseBodyResultOtherService(TeaModel):
    def __init__(self, open_call=None, unhandle_tickets=None):
        self.open_call = open_call  # type: bool
        self.unhandle_tickets = unhandle_tickets  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBodyResultOtherService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_call is not None:
            result['OpenCall'] = self.open_call
        if self.unhandle_tickets is not None:
            result['UnhandleTickets'] = self.unhandle_tickets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenCall') is not None:
            self.open_call = m.get('OpenCall')
        if m.get('UnhandleTickets') is not None:
            self.unhandle_tickets = m.get('UnhandleTickets')
        return self


class QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos(TeaModel):
    def __init__(self, category_en_name=None, category_id=None, category_name=None, device_connect_type=None,
                 device_count=None, device_id=None, device_name=None, location_en_name=None, location_id=None,
                 location_name=None, product_key=None):
        self.category_en_name = category_en_name  # type: str
        self.category_id = category_id  # type: long
        self.category_name = category_name  # type: str
        self.device_connect_type = device_connect_type  # type: str
        self.device_count = device_count  # type: int
        self.device_id = device_id  # type: str
        self.device_name = device_name  # type: str
        self.location_en_name = location_en_name  # type: str
        self.location_id = location_id  # type: long
        self.location_name = location_name  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_en_name is not None:
            result['CategoryEnName'] = self.category_en_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.device_connect_type is not None:
            result['DeviceConnectType'] = self.device_connect_type
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.location_en_name is not None:
            result['LocationEnName'] = self.location_en_name
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryEnName') is not None:
            self.category_en_name = m.get('CategoryEnName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('DeviceConnectType') is not None:
            self.device_connect_type = m.get('DeviceConnectType')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('LocationEnName') is not None:
            self.location_en_name = m.get('LocationEnName')
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryHotelRoomDetailResponseBodyResultRoomControlInfo(TeaModel):
    def __init__(self, app_id=None, app_name=None, device_infos=None, rcu_url=None, template_id=None,
                 template_name=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.device_infos = device_infos  # type: list[QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos]
        self.rcu_url = rcu_url  # type: str
        self.template_id = template_id  # type: long
        self.template_name = template_name  # type: str

    def validate(self):
        if self.device_infos:
            for k in self.device_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBodyResultRoomControlInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k in self.device_infos:
                result['DeviceInfos'].append(k.to_map() if k else None)
        if self.rcu_url is not None:
            result['RcuUrl'] = self.rcu_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k in m.get('DeviceInfos'):
                temp_model = QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos()
                self.device_infos.append(temp_model.from_map(k))
        if m.get('RcuUrl') is not None:
            self.rcu_url = m.get('RcuUrl')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class QueryHotelRoomDetailResponseBodyResultRoomServiceInfo(TeaModel):
    def __init__(self, book_service_cnt=None, goods_service_cnt=None, repair_service_cnt=None,
                 room_service_cnt=None):
        self.book_service_cnt = book_service_cnt  # type: int
        self.goods_service_cnt = goods_service_cnt  # type: int
        self.repair_service_cnt = repair_service_cnt  # type: int
        self.room_service_cnt = room_service_cnt  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBodyResultRoomServiceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.book_service_cnt is not None:
            result['BookServiceCnt'] = self.book_service_cnt
        if self.goods_service_cnt is not None:
            result['GoodsServiceCnt'] = self.goods_service_cnt
        if self.repair_service_cnt is not None:
            result['RepairServiceCnt'] = self.repair_service_cnt
        if self.room_service_cnt is not None:
            result['RoomServiceCnt'] = self.room_service_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BookServiceCnt') is not None:
            self.book_service_cnt = m.get('BookServiceCnt')
        if m.get('GoodsServiceCnt') is not None:
            self.goods_service_cnt = m.get('GoodsServiceCnt')
        if m.get('RepairServiceCnt') is not None:
            self.repair_service_cnt = m.get('RepairServiceCnt')
        if m.get('RoomServiceCnt') is not None:
            self.room_service_cnt = m.get('RoomServiceCnt')
        return self


class QueryHotelRoomDetailResponseBodyResult(TeaModel):
    def __init__(self, auth_accounts=None, connect_type=None, creator_account_name=None, device_infos=None,
                 hotel_id=None, hotel_name=None, other_service=None, room_control_info=None, room_no=None,
                 room_service_info=None):
        self.auth_accounts = auth_accounts  # type: list[QueryHotelRoomDetailResponseBodyResultAuthAccounts]
        self.connect_type = connect_type  # type: str
        self.creator_account_name = creator_account_name  # type: str
        self.device_infos = device_infos  # type: list[QueryHotelRoomDetailResponseBodyResultDeviceInfos]
        self.hotel_id = hotel_id  # type: str
        self.hotel_name = hotel_name  # type: str
        self.other_service = other_service  # type: QueryHotelRoomDetailResponseBodyResultOtherService
        self.room_control_info = room_control_info  # type: QueryHotelRoomDetailResponseBodyResultRoomControlInfo
        self.room_no = room_no  # type: str
        self.room_service_info = room_service_info  # type: QueryHotelRoomDetailResponseBodyResultRoomServiceInfo

    def validate(self):
        if self.auth_accounts:
            for k in self.auth_accounts:
                if k:
                    k.validate()
        if self.device_infos:
            for k in self.device_infos:
                if k:
                    k.validate()
        if self.other_service:
            self.other_service.validate()
        if self.room_control_info:
            self.room_control_info.validate()
        if self.room_service_info:
            self.room_service_info.validate()

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthAccounts'] = []
        if self.auth_accounts is not None:
            for k in self.auth_accounts:
                result['AuthAccounts'].append(k.to_map() if k else None)
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.creator_account_name is not None:
            result['CreatorAccountName'] = self.creator_account_name
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k in self.device_infos:
                result['DeviceInfos'].append(k.to_map() if k else None)
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.other_service is not None:
            result['OtherService'] = self.other_service.to_map()
        if self.room_control_info is not None:
            result['RoomControlInfo'] = self.room_control_info.to_map()
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.room_service_info is not None:
            result['RoomServiceInfo'] = self.room_service_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auth_accounts = []
        if m.get('AuthAccounts') is not None:
            for k in m.get('AuthAccounts'):
                temp_model = QueryHotelRoomDetailResponseBodyResultAuthAccounts()
                self.auth_accounts.append(temp_model.from_map(k))
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('CreatorAccountName') is not None:
            self.creator_account_name = m.get('CreatorAccountName')
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k in m.get('DeviceInfos'):
                temp_model = QueryHotelRoomDetailResponseBodyResultDeviceInfos()
                self.device_infos.append(temp_model.from_map(k))
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('OtherService') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResultOtherService()
            self.other_service = temp_model.from_map(m['OtherService'])
        if m.get('RoomControlInfo') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResultRoomControlInfo()
            self.room_control_info = temp_model.from_map(m['RoomControlInfo'])
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('RoomServiceInfo') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResultRoomServiceInfo()
            self.room_service_info = temp_model.from_map(m['RoomServiceInfo'])
        return self


class QueryHotelRoomDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryHotelRoomDetailResponseBodyResult
        self.status_code = status_code  # type: int

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryHotelRoomDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryHotelRoomDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryHotelRoomDetailResponse, self).to_map()
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
            temp_model = QueryHotelRoomDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRoomControlDevicesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRoomControlDevicesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryRoomControlDevicesRequest(TeaModel):
    def __init__(self, hotel_id=None, room_no=None):
        self.hotel_id = hotel_id  # type: str
        self.room_no = room_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRoomControlDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList(TeaModel):
    def __init__(self, alias_list=None, category=None, device_index=None, device_name=None, device_status=None,
                 element_code=None, location=None):
        self.alias_list = alias_list  # type: list[str]
        self.category = category  # type: str
        self.device_index = device_index  # type: int
        self.device_name = device_name  # type: str
        self.device_status = device_status  # type: str
        self.element_code = element_code  # type: str
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.element_code is not None:
            result['ElementCode'] = self.element_code
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('ElementCode') is not None:
            self.element_code = m.get('ElementCode')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt(TeaModel):
    def __init__(self, switch_list=None):
        self.switch_list = switch_list  # type: list[QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList]

    def validate(self):
        if self.switch_list:
            for k in self.switch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SwitchList'] = []
        if self.switch_list is not None:
            for k in self.switch_list:
                result['SwitchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.switch_list = []
        if m.get('SwitchList') is not None:
            for k in m.get('SwitchList'):
                temp_model = QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k))
        return self


class QueryRoomControlDevicesResponseBodyResultDevices(TeaModel):
    def __init__(self, alias_list=None, connect_type=None, dn=None, device_name=None, device_status=None,
                 multi_key_switch_ext=None, name=None, number=None, pk=None):
        self.alias_list = alias_list  # type: list[str]
        self.connect_type = connect_type  # type: str
        self.dn = dn  # type: str
        self.device_name = device_name  # type: str
        self.device_status = device_status  # type: str
        self.multi_key_switch_ext = multi_key_switch_ext  # type: QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt
        self.name = name  # type: str
        self.number = number  # type: str
        self.pk = pk  # type: str

    def validate(self):
        if self.multi_key_switch_ext:
            self.multi_key_switch_ext.validate()

    def to_map(self):
        _map = super(QueryRoomControlDevicesResponseBodyResultDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.dn is not None:
            result['DN'] = self.dn
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.multi_key_switch_ext is not None:
            result['MultiKeySwitchExt'] = self.multi_key_switch_ext.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.pk is not None:
            result['PK'] = self.pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('DN') is not None:
            self.dn = m.get('DN')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('MultiKeySwitchExt') is not None:
            temp_model = QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt()
            self.multi_key_switch_ext = temp_model.from_map(m['MultiKeySwitchExt'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('PK') is not None:
            self.pk = m.get('PK')
        return self


class QueryRoomControlDevicesResponseBodyResult(TeaModel):
    def __init__(self, devices=None, location=None, location_name=None):
        self.devices = devices  # type: list[QueryRoomControlDevicesResponseBodyResultDevices]
        self.location = location  # type: str
        self.location_name = location_name  # type: str

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRoomControlDevicesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = QueryRoomControlDevicesResponseBodyResultDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        return self


class QueryRoomControlDevicesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryRoomControlDevicesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRoomControlDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryRoomControlDevicesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryRoomControlDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRoomControlDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRoomControlDevicesResponse, self).to_map()
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
            temp_model = QueryRoomControlDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySceneListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySceneListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QuerySceneListRequest(TeaModel):
    def __init__(self, hotel_id=None, scene_states=None, scene_types=None, template_info_ids=None):
        self.hotel_id = hotel_id  # type: str
        self.scene_states = scene_states  # type: list[int]
        self.scene_types = scene_types  # type: list[str]
        self.template_info_ids = template_info_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySceneListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_states is not None:
            result['SceneStates'] = self.scene_states
        if self.scene_types is not None:
            result['SceneTypes'] = self.scene_types
        if self.template_info_ids is not None:
            result['TemplateInfoIds'] = self.template_info_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneStates') is not None:
            self.scene_states = m.get('SceneStates')
        if m.get('SceneTypes') is not None:
            self.scene_types = m.get('SceneTypes')
        if m.get('TemplateInfoIds') is not None:
            self.template_info_ids = m.get('TemplateInfoIds')
        return self


class QuerySceneListShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, scene_states_shrink=None, scene_types_shrink=None,
                 template_info_ids_shrink=None):
        self.hotel_id = hotel_id  # type: str
        self.scene_states_shrink = scene_states_shrink  # type: str
        self.scene_types_shrink = scene_types_shrink  # type: str
        self.template_info_ids_shrink = template_info_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySceneListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_states_shrink is not None:
            result['SceneStates'] = self.scene_states_shrink
        if self.scene_types_shrink is not None:
            result['SceneTypes'] = self.scene_types_shrink
        if self.template_info_ids_shrink is not None:
            result['TemplateInfoIds'] = self.template_info_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneStates') is not None:
            self.scene_states_shrink = m.get('SceneStates')
        if m.get('SceneTypes') is not None:
            self.scene_types_shrink = m.get('SceneTypes')
        if m.get('TemplateInfoIds') is not None:
            self.template_info_ids_shrink = m.get('TemplateInfoIds')
        return self


class QuerySceneListResponseBodyResultsTemplateInfoDTOList(TeaModel):
    def __init__(self, description=None, id=None, name=None):
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySceneListResponseBodyResultsTemplateInfoDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QuerySceneListResponseBodyResults(TeaModel):
    def __init__(self, icon=None, scene_id=None, scene_name=None, scene_source=None, scene_state=None,
                 scene_type=None, template_info_dtolist=None, unavailable_reason=None):
        self.icon = icon  # type: str
        self.scene_id = scene_id  # type: str
        self.scene_name = scene_name  # type: str
        self.scene_source = scene_source  # type: str
        self.scene_state = scene_state  # type: int
        self.scene_type = scene_type  # type: str
        self.template_info_dtolist = template_info_dtolist  # type: list[QuerySceneListResponseBodyResultsTemplateInfoDTOList]
        self.unavailable_reason = unavailable_reason  # type: str

    def validate(self):
        if self.template_info_dtolist:
            for k in self.template_info_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySceneListResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.scene_source is not None:
            result['SceneSource'] = self.scene_source
        if self.scene_state is not None:
            result['SceneState'] = self.scene_state
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        result['TemplateInfoDTOList'] = []
        if self.template_info_dtolist is not None:
            for k in self.template_info_dtolist:
                result['TemplateInfoDTOList'].append(k.to_map() if k else None)
        if self.unavailable_reason is not None:
            result['UnavailableReason'] = self.unavailable_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SceneSource') is not None:
            self.scene_source = m.get('SceneSource')
        if m.get('SceneState') is not None:
            self.scene_state = m.get('SceneState')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        self.template_info_dtolist = []
        if m.get('TemplateInfoDTOList') is not None:
            for k in m.get('TemplateInfoDTOList'):
                temp_model = QuerySceneListResponseBodyResultsTemplateInfoDTOList()
                self.template_info_dtolist.append(temp_model.from_map(k))
        if m.get('UnavailableReason') is not None:
            self.unavailable_reason = m.get('UnavailableReason')
        return self


class QuerySceneListResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, results=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.results = results  # type: list[QuerySceneListResponseBodyResults]
        self.status_code = status_code  # type: int

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySceneListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = QuerySceneListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QuerySceneListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySceneListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySceneListResponse, self).to_map()
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
            temp_model = QuerySceneListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveChildAccountAuthHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveChildAccountAuthHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class RemoveChildAccountAuthRequest(TeaModel):
    def __init__(self, app_key=None, child_account_name=None, hotel_id=None, tb_open_id=None):
        self.app_key = app_key  # type: str
        self.child_account_name = child_account_name  # type: str
        self.hotel_id = hotel_id  # type: str
        self.tb_open_id = tb_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveChildAccountAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.child_account_name is not None:
            result['ChildAccountName'] = self.child_account_name
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ChildAccountName') is not None:
            self.child_account_name = m.get('ChildAccountName')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class RemoveChildAccountAuthResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveChildAccountAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class RemoveChildAccountAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveChildAccountAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveChildAccountAuthResponse, self).to_map()
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
            temp_model = RemoveChildAccountAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveHotelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveHotelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class RemoveHotelRequest(TeaModel):
    def __init__(self, app_key=None, hotel_id=None, tb_open_id=None):
        # appkey
        self.app_key = app_key  # type: str
        self.hotel_id = hotel_id  # type: str
        self.tb_open_id = tb_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveHotelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class RemoveHotelResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveHotelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class RemoveHotelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveHotelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveHotelResponse, self).to_map()
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
            temp_model = RemoveHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetWelcomeTextAndMusicHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetWelcomeTextAndMusicHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ResetWelcomeTextAndMusicRequest(TeaModel):
    def __init__(self, hotel_id=None):
        self.hotel_id = hotel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetWelcomeTextAndMusicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ResetWelcomeTextAndMusicResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetWelcomeTextAndMusicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ResetWelcomeTextAndMusicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetWelcomeTextAndMusicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetWelcomeTextAndMusicResponse, self).to_map()
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
            temp_model = ResetWelcomeTextAndMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RoomCheckOutHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RoomCheckOutHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class RoomCheckOutRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RoomCheckOutRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class RoomCheckOutRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RoomCheckOutRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class RoomCheckOutRequest(TeaModel):
    def __init__(self, device_info=None, user_info=None):
        self.device_info = device_info  # type: RoomCheckOutRequestDeviceInfo
        self.user_info = user_info  # type: RoomCheckOutRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(RoomCheckOutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = RoomCheckOutRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = RoomCheckOutRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class RoomCheckOutShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RoomCheckOutShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class RoomCheckOutResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RoomCheckOutResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RoomCheckOutResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RoomCheckOutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RoomCheckOutResponse, self).to_map()
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
            temp_model = RoomCheckOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitHotelOrderHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitHotelOrderHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SubmitHotelOrderRequestPayloadItemList(TeaModel):
    def __init__(self, item_id=None, quantity=None):
        self.item_id = item_id  # type: long
        self.quantity = quantity  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitHotelOrderRequestPayloadItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class SubmitHotelOrderRequestPayload(TeaModel):
    def __init__(self, item_list=None, type=None):
        self.item_list = item_list  # type: list[SubmitHotelOrderRequestPayloadItemList]
        self.type = type  # type: str

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SubmitHotelOrderRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = SubmitHotelOrderRequestPayloadItemList()
                self.item_list.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SubmitHotelOrderRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitHotelOrderRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SubmitHotelOrderRequest(TeaModel):
    def __init__(self, payload=None, user_info=None):
        self.payload = payload  # type: SubmitHotelOrderRequestPayload
        self.user_info = user_info  # type: SubmitHotelOrderRequestUserInfo

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(SubmitHotelOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = SubmitHotelOrderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = SubmitHotelOrderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SubmitHotelOrderShrinkRequest(TeaModel):
    def __init__(self, payload_shrink=None, user_info_shrink=None):
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitHotelOrderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SubmitHotelOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, status_code=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitHotelOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitHotelOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitHotelOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitHotelOrderResponse, self).to_map()
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
            temp_model = SubmitHotelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDeviceStatusWithAkHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDeviceStatusWithAkHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SyncDeviceStatusWithAkRequest(TeaModel):
    def __init__(self, category_cn_name=None, category_en_name=None, device_name=None, hotel_id=None, location=None,
                 location_cn_name=None, number=None, room_no=None, switch=None, fan_speed=None, mode=None, room_temperature=None,
                 temperature=None, value=None):
        self.category_cn_name = category_cn_name  # type: str
        self.category_en_name = category_en_name  # type: str
        self.device_name = device_name  # type: str
        self.hotel_id = hotel_id  # type: str
        self.location = location  # type: str
        self.location_cn_name = location_cn_name  # type: str
        self.number = number  # type: str
        self.room_no = room_no  # type: str
        self.switch = switch  # type: int
        self.fan_speed = fan_speed  # type: str
        self.mode = mode  # type: str
        self.room_temperature = room_temperature  # type: str
        self.temperature = temperature  # type: str
        self.value = value  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDeviceStatusWithAkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_cn_name is not None:
            result['CategoryCnName'] = self.category_cn_name
        if self.category_en_name is not None:
            result['CategoryEnName'] = self.category_en_name
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.location is not None:
            result['Location'] = self.location
        if self.location_cn_name is not None:
            result['LocationCnName'] = self.location_cn_name
        if self.number is not None:
            result['Number'] = self.number
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.switch is not None:
            result['Switch'] = self.switch
        if self.fan_speed is not None:
            result['fanSpeed'] = self.fan_speed
        if self.mode is not None:
            result['mode'] = self.mode
        if self.room_temperature is not None:
            result['roomTemperature'] = self.room_temperature
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryCnName') is not None:
            self.category_cn_name = m.get('CategoryCnName')
        if m.get('CategoryEnName') is not None:
            self.category_en_name = m.get('CategoryEnName')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationCnName') is not None:
            self.location_cn_name = m.get('LocationCnName')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        if m.get('fanSpeed') is not None:
            self.fan_speed = m.get('fanSpeed')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('roomTemperature') is not None:
            self.room_temperature = m.get('roomTemperature')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SyncDeviceStatusWithAkResponseBody(TeaModel):
    def __init__(self, message=None, result=None, status_code=None, request_id=None):
        self.message = message  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDeviceStatusWithAkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SyncDeviceStatusWithAkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SyncDeviceStatusWithAkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncDeviceStatusWithAkResponse, self).to_map()
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
            temp_model = SyncDeviceStatusWithAkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicInfoQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicInfoQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateBasicInfoQARequest(TeaModel):
    def __init__(self, check_in_time=None, check_out_time=None, hotel_address=None, hotel_id=None,
                 hotel_introduction=None, hotel_member=None, hotel_service=None, parking_expenses=None, parking_position=None,
                 phone_number=None, wifi_name=None, wifi_password=None):
        self.check_in_time = check_in_time  # type: str
        self.check_out_time = check_out_time  # type: str
        self.hotel_address = hotel_address  # type: str
        self.hotel_id = hotel_id  # type: str
        self.hotel_introduction = hotel_introduction  # type: str
        self.hotel_member = hotel_member  # type: str
        self.hotel_service = hotel_service  # type: str
        self.parking_expenses = parking_expenses  # type: str
        self.parking_position = parking_position  # type: str
        self.phone_number = phone_number  # type: str
        self.wifi_name = wifi_name  # type: str
        self.wifi_password = wifi_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicInfoQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in_time is not None:
            result['CheckInTime'] = self.check_in_time
        if self.check_out_time is not None:
            result['CheckOutTime'] = self.check_out_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_introduction is not None:
            result['HotelIntroduction'] = self.hotel_introduction
        if self.hotel_member is not None:
            result['HotelMember'] = self.hotel_member
        if self.hotel_service is not None:
            result['HotelService'] = self.hotel_service
        if self.parking_expenses is not None:
            result['ParkingExpenses'] = self.parking_expenses
        if self.parking_position is not None:
            result['ParkingPosition'] = self.parking_position
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.wifi_name is not None:
            result['WifiName'] = self.wifi_name
        if self.wifi_password is not None:
            result['WifiPassword'] = self.wifi_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckInTime') is not None:
            self.check_in_time = m.get('CheckInTime')
        if m.get('CheckOutTime') is not None:
            self.check_out_time = m.get('CheckOutTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelIntroduction') is not None:
            self.hotel_introduction = m.get('HotelIntroduction')
        if m.get('HotelMember') is not None:
            self.hotel_member = m.get('HotelMember')
        if m.get('HotelService') is not None:
            self.hotel_service = m.get('HotelService')
        if m.get('ParkingExpenses') is not None:
            self.parking_expenses = m.get('ParkingExpenses')
        if m.get('ParkingPosition') is not None:
            self.parking_position = m.get('ParkingPosition')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('WifiName') is not None:
            self.wifi_name = m.get('WifiName')
        if m.get('WifiPassword') is not None:
            self.wifi_password = m.get('WifiPassword')
        return self


class UpdateBasicInfoQAResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicInfoQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateBasicInfoQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBasicInfoQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBasicInfoQAResponse, self).to_map()
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
            temp_model = UpdateBasicInfoQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateCustomQARequest(TeaModel):
    def __init__(self, answers=None, custom_qaid=None, hotel_id=None, key_words=None, major_question=None,
                 supplementary_questions=None):
        self.answers = answers  # type: list[str]
        self.custom_qaid = custom_qaid  # type: str
        self.hotel_id = hotel_id  # type: str
        self.key_words = key_words  # type: list[str]
        self.major_question = major_question  # type: str
        self.supplementary_questions = supplementary_questions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.custom_qaid is not None:
            result['CustomQAId'] = self.custom_qaid
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('CustomQAId') is not None:
            self.custom_qaid = m.get('CustomQAId')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions = m.get('SupplementaryQuestions')
        return self


class UpdateCustomQAShrinkRequest(TeaModel):
    def __init__(self, answers_shrink=None, custom_qaid=None, hotel_id=None, key_words_shrink=None,
                 major_question=None, supplementary_questions_shrink=None):
        self.answers_shrink = answers_shrink  # type: str
        self.custom_qaid = custom_qaid  # type: str
        self.hotel_id = hotel_id  # type: str
        self.key_words_shrink = key_words_shrink  # type: str
        self.major_question = major_question  # type: str
        self.supplementary_questions_shrink = supplementary_questions_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomQAShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers_shrink is not None:
            result['Answers'] = self.answers_shrink
        if self.custom_qaid is not None:
            result['CustomQAId'] = self.custom_qaid
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words_shrink is not None:
            result['KeyWords'] = self.key_words_shrink
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions_shrink is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers_shrink = m.get('Answers')
        if m.get('CustomQAId') is not None:
            self.custom_qaid = m.get('CustomQAId')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words_shrink = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions_shrink = m.get('SupplementaryQuestions')
        return self


class UpdateCustomQAResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateCustomQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCustomQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomQAResponse, self).to_map()
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
            temp_model = UpdateCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelRequest(TeaModel):
    def __init__(self, app_key=None, est_open_time=None, hotel_address=None, hotel_email=None, hotel_id=None,
                 hotel_name=None, phone_number=None, related_pks=None, remark=None, room_num=None, tb_open_id=None):
        self.app_key = app_key  # type: str
        self.est_open_time = est_open_time  # type: str
        self.hotel_address = hotel_address  # type: str
        self.hotel_email = hotel_email  # type: str
        self.hotel_id = hotel_id  # type: str
        self.hotel_name = hotel_name  # type: str
        self.phone_number = phone_number  # type: str
        self.related_pks = related_pks  # type: list[str]
        self.remark = remark  # type: str
        self.room_num = room_num  # type: int
        self.tb_open_id = tb_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pks is not None:
            result['RelatedPks'] = self.related_pks
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPks') is not None:
            self.related_pks = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class UpdateHotelShrinkRequest(TeaModel):
    def __init__(self, app_key=None, est_open_time=None, hotel_address=None, hotel_email=None, hotel_id=None,
                 hotel_name=None, phone_number=None, related_pks_shrink=None, remark=None, room_num=None, tb_open_id=None):
        self.app_key = app_key  # type: str
        self.est_open_time = est_open_time  # type: str
        self.hotel_address = hotel_address  # type: str
        self.hotel_email = hotel_email  # type: str
        self.hotel_id = hotel_id  # type: str
        self.hotel_name = hotel_name  # type: str
        self.phone_number = phone_number  # type: str
        self.related_pks_shrink = related_pks_shrink  # type: str
        self.remark = remark  # type: str
        self.room_num = room_num  # type: int
        self.tb_open_id = tb_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pks_shrink is not None:
            result['RelatedPks'] = self.related_pks_shrink
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPks') is not None:
            self.related_pks_shrink = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class UpdateHotelResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateHotelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHotelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHotelResponse, self).to_map()
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
            temp_model = UpdateHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelAlarmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelAlarmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelAlarmRequestAlarms(TeaModel):
    def __init__(self, alarm_id=None, device_open_id=None, room_no=None, user_open_id=None):
        self.alarm_id = alarm_id  # type: long
        self.device_open_id = device_open_id  # type: str
        self.room_no = room_no  # type: str
        self.user_open_id = user_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelAlarmRequestAlarms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class UpdateHotelAlarmRequestScheduleInfoOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelAlarmRequestScheduleInfoOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class UpdateHotelAlarmRequestScheduleInfoWeekly(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelAlarmRequestScheduleInfoWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class UpdateHotelAlarmRequestScheduleInfo(TeaModel):
    def __init__(self, once=None, type=None, weekly=None):
        self.once = once  # type: UpdateHotelAlarmRequestScheduleInfoOnce
        # ONCE, WEEKLY
        self.type = type  # type: str
        self.weekly = weekly  # type: UpdateHotelAlarmRequestScheduleInfoWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(UpdateHotelAlarmRequestScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = UpdateHotelAlarmRequestScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = UpdateHotelAlarmRequestScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class UpdateHotelAlarmRequest(TeaModel):
    def __init__(self, alarms=None, hotel_id=None, schedule_info=None):
        self.alarms = alarms  # type: list[UpdateHotelAlarmRequestAlarms]
        self.hotel_id = hotel_id  # type: str
        self.schedule_info = schedule_info  # type: UpdateHotelAlarmRequestScheduleInfo

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(UpdateHotelAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = UpdateHotelAlarmRequestAlarms()
                self.alarms.append(temp_model.from_map(k))
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ScheduleInfo') is not None:
            temp_model = UpdateHotelAlarmRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        return self


class UpdateHotelAlarmShrinkRequest(TeaModel):
    def __init__(self, alarms_shrink=None, hotel_id=None, schedule_info_shrink=None):
        self.alarms_shrink = alarms_shrink  # type: str
        self.hotel_id = hotel_id  # type: str
        self.schedule_info_shrink = schedule_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelAlarmShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarms_shrink is not None:
            result['Alarms'] = self.alarms_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.schedule_info_shrink is not None:
            result['ScheduleInfo'] = self.schedule_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alarms') is not None:
            self.alarms_shrink = m.get('Alarms')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ScheduleInfo') is not None:
            self.schedule_info_shrink = m.get('ScheduleInfo')
        return self


class UpdateHotelAlarmResponseBody(TeaModel):
    def __init__(self, extentions=None, message=None, request_id=None, result=None, status_code=None):
        self.extentions = extentions  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: int
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateHotelAlarmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHotelAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHotelAlarmResponse, self).to_map()
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
            temp_model = UpdateHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelSceneBookItemHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneBookItemHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq(TeaModel):
    def __init__(self, icon=None, id=None, name=None, price=None):
        # icon
        self.icon = icon  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.price = price  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class UpdateHotelSceneBookItemRequest(TeaModel):
    def __init__(self, hotel_id=None, update_hotel_scene_book_req=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        # updateHotelSceneBookReq
        self.update_hotel_scene_book_req = update_hotel_scene_book_req  # type: UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq

    def validate(self):
        if self.update_hotel_scene_book_req:
            self.update_hotel_scene_book_req.validate()

    def to_map(self):
        _map = super(UpdateHotelSceneBookItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_book_req is not None:
            result['UpdateHotelSceneBookReq'] = self.update_hotel_scene_book_req.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneBookReq') is not None:
            temp_model = UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq()
            self.update_hotel_scene_book_req = temp_model.from_map(m['UpdateHotelSceneBookReq'])
        return self


class UpdateHotelSceneBookItemShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, update_hotel_scene_book_req_shrink=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        # updateHotelSceneBookReq
        self.update_hotel_scene_book_req_shrink = update_hotel_scene_book_req_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneBookItemShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_book_req_shrink is not None:
            result['UpdateHotelSceneBookReq'] = self.update_hotel_scene_book_req_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneBookReq') is not None:
            self.update_hotel_scene_book_req_shrink = m.get('UpdateHotelSceneBookReq')
        return self


class UpdateHotelSceneBookItemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneBookItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateHotelSceneBookItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHotelSceneBookItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHotelSceneBookItemResponse, self).to_map()
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
            temp_model = UpdateHotelSceneBookItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelSceneItemHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneItemHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq(TeaModel):
    def __init__(self, is_use_template_answer=None, operate_type=None):
        self.is_use_template_answer = is_use_template_answer  # type: bool
        self.operate_type = operate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_use_template_answer is not None:
            result['IsUseTemplateAnswer'] = self.is_use_template_answer
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsUseTemplateAnswer') is not None:
            self.is_use_template_answer = m.get('IsUseTemplateAnswer')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList(TeaModel):
    def __init__(self, dialogue_id=None, no_answer=None, no_answer_template=None, process=None, question=None,
                 service_id=None, yes_answer=None, yes_answer_template=None):
        self.dialogue_id = dialogue_id  # type: str
        self.no_answer = no_answer  # type: str
        self.no_answer_template = no_answer_template  # type: str
        self.process = process  # type: int
        self.question = question  # type: str
        # itemId
        self.service_id = service_id  # type: str
        self.yes_answer = yes_answer  # type: str
        self.yes_answer_template = yes_answer_template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id
        if self.no_answer is not None:
            result['NoAnswer'] = self.no_answer
        if self.no_answer_template is not None:
            result['NoAnswerTemplate'] = self.no_answer_template
        if self.process is not None:
            result['Process'] = self.process
        if self.question is not None:
            result['Question'] = self.question
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.yes_answer is not None:
            result['YesAnswer'] = self.yes_answer
        if self.yes_answer_template is not None:
            result['YesAnswerTemplate'] = self.yes_answer_template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')
        if m.get('NoAnswer') is not None:
            self.no_answer = m.get('NoAnswer')
        if m.get('NoAnswerTemplate') is not None:
            self.no_answer_template = m.get('NoAnswerTemplate')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('YesAnswer') is not None:
            self.yes_answer = m.get('YesAnswer')
        if m.get('YesAnswerTemplate') is not None:
            self.yes_answer_template = m.get('YesAnswerTemplate')
        return self


class UpdateHotelSceneItemRequestUpdateHotelSceneReq(TeaModel):
    def __init__(self, beyond_limit_reply=None, delivery_method=None, dialogue_list=None, icon=None, id=None,
                 limit_number=None, limit_switch=None, name=None, payment_method=None, price=None, robot_name=None, status=None):
        self.beyond_limit_reply = beyond_limit_reply  # type: str
        self.delivery_method = delivery_method  # type: str
        self.dialogue_list = dialogue_list  # type: list[UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList]
        # icon
        self.icon = icon  # type: str
        # itemID
        self.id = id  # type: long
        self.limit_number = limit_number  # type: long
        self.limit_switch = limit_switch  # type: int
        self.name = name  # type: str
        self.payment_method = payment_method  # type: str
        self.price = price  # type: long
        self.robot_name = robot_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateHotelSceneItemRequestUpdateHotelSceneReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beyond_limit_reply is not None:
            result['BeyondLimitReply'] = self.beyond_limit_reply
        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method
        result['DialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['DialogueList'].append(k.to_map() if k else None)
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number
        if self.limit_switch is not None:
            result['LimitSwitch'] = self.limit_switch
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method
        if self.price is not None:
            result['Price'] = self.price
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeyondLimitReply') is not None:
            self.beyond_limit_reply = m.get('BeyondLimitReply')
        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')
        self.dialogue_list = []
        if m.get('DialogueList') is not None:
            for k in m.get('DialogueList'):
                temp_model = UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')
        if m.get('LimitSwitch') is not None:
            self.limit_switch = m.get('LimitSwitch')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateHotelSceneItemRequest(TeaModel):
    def __init__(self, hotel_id=None, update_hotel_scene_operate_req=None, update_hotel_scene_req=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        # updateHotelSceneReq
        self.update_hotel_scene_operate_req = update_hotel_scene_operate_req  # type: UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq
        # UpdateHotelSceneReq
        self.update_hotel_scene_req = update_hotel_scene_req  # type: UpdateHotelSceneItemRequestUpdateHotelSceneReq

    def validate(self):
        if self.update_hotel_scene_operate_req:
            self.update_hotel_scene_operate_req.validate()
        if self.update_hotel_scene_req:
            self.update_hotel_scene_req.validate()

    def to_map(self):
        _map = super(UpdateHotelSceneItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_operate_req is not None:
            result['UpdateHotelSceneOperateReq'] = self.update_hotel_scene_operate_req.to_map()
        if self.update_hotel_scene_req is not None:
            result['UpdateHotelSceneReq'] = self.update_hotel_scene_req.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneOperateReq') is not None:
            temp_model = UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq()
            self.update_hotel_scene_operate_req = temp_model.from_map(m['UpdateHotelSceneOperateReq'])
        if m.get('UpdateHotelSceneReq') is not None:
            temp_model = UpdateHotelSceneItemRequestUpdateHotelSceneReq()
            self.update_hotel_scene_req = temp_model.from_map(m['UpdateHotelSceneReq'])
        return self


class UpdateHotelSceneItemShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, update_hotel_scene_operate_req_shrink=None,
                 update_hotel_scene_req_shrink=None):
        # hotelID
        self.hotel_id = hotel_id  # type: str
        # updateHotelSceneReq
        self.update_hotel_scene_operate_req_shrink = update_hotel_scene_operate_req_shrink  # type: str
        # UpdateHotelSceneReq
        self.update_hotel_scene_req_shrink = update_hotel_scene_req_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneItemShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_operate_req_shrink is not None:
            result['UpdateHotelSceneOperateReq'] = self.update_hotel_scene_operate_req_shrink
        if self.update_hotel_scene_req_shrink is not None:
            result['UpdateHotelSceneReq'] = self.update_hotel_scene_req_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneOperateReq') is not None:
            self.update_hotel_scene_operate_req_shrink = m.get('UpdateHotelSceneOperateReq')
        if m.get('UpdateHotelSceneReq') is not None:
            self.update_hotel_scene_req_shrink = m.get('UpdateHotelSceneReq')
        return self


class UpdateHotelSceneItemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotelSceneItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateHotelSceneItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHotelSceneItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHotelSceneItemResponse, self).to_map()
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
            temp_model = UpdateHotelSceneItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMessageTemplateHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMessageTemplateHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateMessageTemplateRequest(TeaModel):
    def __init__(self, template_detail=None, template_id=None, template_name=None):
        self.template_detail = template_detail  # type: str
        self.template_id = template_id  # type: long
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMessageTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            self.template_detail = m.get('TemplateDetail')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class UpdateMessageTemplateResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMessageTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateMessageTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMessageTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMessageTemplateResponse, self).to_map()
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
            temp_model = UpdateMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRcuSceneHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRcuSceneHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateRcuSceneRequestSceneRelationExtDTO(TeaModel):
    def __init__(self, corpus_list=None, description=None, icon=None, name=None):
        self.corpus_list = corpus_list  # type: list[str]
        self.description = description  # type: str
        self.icon = icon  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRcuSceneRequestSceneRelationExtDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateRcuSceneRequest(TeaModel):
    def __init__(self, hotel_id=None, scene_id=None, scene_relation_ext_dto=None):
        self.hotel_id = hotel_id  # type: str
        self.scene_id = scene_id  # type: str
        self.scene_relation_ext_dto = scene_relation_ext_dto  # type: UpdateRcuSceneRequestSceneRelationExtDTO

    def validate(self):
        if self.scene_relation_ext_dto:
            self.scene_relation_ext_dto.validate()

    def to_map(self):
        _map = super(UpdateRcuSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dto is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            temp_model = UpdateRcuSceneRequestSceneRelationExtDTO()
            self.scene_relation_ext_dto = temp_model.from_map(m['SceneRelationExtDTO'])
        return self


class UpdateRcuSceneShrinkRequest(TeaModel):
    def __init__(self, hotel_id=None, scene_id=None, scene_relation_ext_dtoshrink=None):
        self.hotel_id = hotel_id  # type: str
        self.scene_id = scene_id  # type: str
        self.scene_relation_ext_dtoshrink = scene_relation_ext_dtoshrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRcuSceneShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dtoshrink is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dtoshrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            self.scene_relation_ext_dtoshrink = m.get('SceneRelationExtDTO')
        return self


class UpdateRcuSceneResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRcuSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateRcuSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRcuSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRcuSceneResponse, self).to_map()
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
            temp_model = UpdateRcuSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceQAHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceQAHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateServiceQARequest(TeaModel):
    def __init__(self, answer=None, hotel_id=None, service_qaid=None, is_active=None):
        self.answer = answer  # type: str
        self.hotel_id = hotel_id  # type: str
        self.service_qaid = service_qaid  # type: long
        self.is_active = is_active  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.service_qaid is not None:
            result['ServiceQAId'] = self.service_qaid
        if self.is_active is not None:
            result['isActive'] = self.is_active
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ServiceQAId') is not None:
            self.service_qaid = m.get('ServiceQAId')
        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')
        return self


class UpdateServiceQAResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateServiceQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceQAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceQAResponse, self).to_map()
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
            temp_model = UpdateServiceQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTicketHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTicketHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateTicketRequest(TeaModel):
    def __init__(self, group_key=None, hotel_id=None, status=None):
        self.group_key = group_key  # type: str
        self.hotel_id = hotel_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_key is not None:
            result['GroupKey'] = self.group_key
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateTicketResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None, status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTicketResponse, self).to_map()
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
            temp_model = UpdateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


