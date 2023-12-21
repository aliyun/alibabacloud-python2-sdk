# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AuthUserRequest(TeaModel):
    def __init__(self, jwt_token=None):
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class AuthUserResponseBodyData(TeaModel):
    def __init__(self, jwt_token=None, type=None):
        self.jwt_token = jwt_token  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AuthUserResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: AuthUserResponseBodyData
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AuthUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = AuthUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthUserResponse, self).to_map()
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
            temp_model = AuthUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDigitalHumanProjectRequest(TeaModel):
    def __init__(self, audio_id=None, audio_url=None, background_id=None, background_url=None, content=None,
                 foreground_id=None, foreground_url=None, human_layer_style=None, intro=None, jwt_token=None, mode=None,
                 model_id=None, output_config=None, title=None, tts_voice_id=None, watermark_image_url=None,
                 watermark_style=None):
        self.audio_id = audio_id  # type: str
        self.audio_url = audio_url  # type: str
        self.background_id = background_id  # type: str
        self.background_url = background_url  # type: str
        self.content = content  # type: str
        self.foreground_id = foreground_id  # type: str
        self.foreground_url = foreground_url  # type: str
        self.human_layer_style = human_layer_style  # type: str
        self.intro = intro  # type: str
        self.jwt_token = jwt_token  # type: str
        self.mode = mode  # type: str
        self.model_id = model_id  # type: str
        self.output_config = output_config  # type: str
        self.title = title  # type: str
        self.tts_voice_id = tts_voice_id  # type: str
        self.watermark_image_url = watermark_image_url  # type: str
        self.watermark_style = watermark_style  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDigitalHumanProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.background_id is not None:
            result['BackgroundId'] = self.background_id
        if self.background_url is not None:
            result['BackgroundUrl'] = self.background_url
        if self.content is not None:
            result['Content'] = self.content
        if self.foreground_id is not None:
            result['ForegroundId'] = self.foreground_id
        if self.foreground_url is not None:
            result['ForegroundUrl'] = self.foreground_url
        if self.human_layer_style is not None:
            result['HumanLayerStyle'] = self.human_layer_style
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.title is not None:
            result['Title'] = self.title
        if self.tts_voice_id is not None:
            result['TtsVoiceId'] = self.tts_voice_id
        if self.watermark_image_url is not None:
            result['WatermarkImageUrl'] = self.watermark_image_url
        if self.watermark_style is not None:
            result['WatermarkStyle'] = self.watermark_style
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('BackgroundId') is not None:
            self.background_id = m.get('BackgroundId')
        if m.get('BackgroundUrl') is not None:
            self.background_url = m.get('BackgroundUrl')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ForegroundId') is not None:
            self.foreground_id = m.get('ForegroundId')
        if m.get('ForegroundUrl') is not None:
            self.foreground_url = m.get('ForegroundUrl')
        if m.get('HumanLayerStyle') is not None:
            self.human_layer_style = m.get('HumanLayerStyle')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TtsVoiceId') is not None:
            self.tts_voice_id = m.get('TtsVoiceId')
        if m.get('WatermarkImageUrl') is not None:
            self.watermark_image_url = m.get('WatermarkImageUrl')
        if m.get('WatermarkStyle') is not None:
            self.watermark_style = m.get('WatermarkStyle')
        return self


class CreateDigitalHumanProjectResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDigitalHumanProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateDigitalHumanProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateDigitalHumanProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateDigitalHumanProjectResponseBody, self).to_map()
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
            temp_model = CreateDigitalHumanProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDigitalHumanProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDigitalHumanProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDigitalHumanProjectResponse, self).to_map()
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
            temp_model = CreateDigitalHumanProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLivePortraitProjectRequest(TeaModel):
    def __init__(self, audio_id=None, audio_url=None, content=None, image_id=None, image_url=None, intro=None,
                 jwt_token=None, light_model=None, mode=None, output_config=None, title=None, tts_voice_id=None,
                 watermark_image_url=None, watermark_style=None):
        self.audio_id = audio_id  # type: str
        self.audio_url = audio_url  # type: str
        self.content = content  # type: str
        self.image_id = image_id  # type: str
        self.image_url = image_url  # type: str
        self.intro = intro  # type: str
        self.jwt_token = jwt_token  # type: str
        self.light_model = light_model  # type: bool
        self.mode = mode  # type: str
        self.output_config = output_config  # type: str
        self.title = title  # type: str
        self.tts_voice_id = tts_voice_id  # type: str
        self.watermark_image_url = watermark_image_url  # type: str
        self.watermark_style = watermark_style  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLivePortraitProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.content is not None:
            result['Content'] = self.content
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.light_model is not None:
            result['LightModel'] = self.light_model
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.title is not None:
            result['Title'] = self.title
        if self.tts_voice_id is not None:
            result['TtsVoiceId'] = self.tts_voice_id
        if self.watermark_image_url is not None:
            result['WatermarkImageUrl'] = self.watermark_image_url
        if self.watermark_style is not None:
            result['WatermarkStyle'] = self.watermark_style
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('LightModel') is not None:
            self.light_model = m.get('LightModel')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TtsVoiceId') is not None:
            self.tts_voice_id = m.get('TtsVoiceId')
        if m.get('WatermarkImageUrl') is not None:
            self.watermark_image_url = m.get('WatermarkImageUrl')
        if m.get('WatermarkStyle') is not None:
            self.watermark_style = m.get('WatermarkStyle')
        return self


class CreateLivePortraitProjectResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLivePortraitProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateLivePortraitProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateLivePortraitProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateLivePortraitProjectResponseBody, self).to_map()
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
            temp_model = CreateLivePortraitProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLivePortraitProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLivePortraitProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLivePortraitProjectResponse, self).to_map()
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
            temp_model = CreateLivePortraitProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMapDataRequest(TeaModel):
    def __init__(self, app_id=None, jwt_token=None):
        self.app_id = app_id  # type: str
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMapDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GetMapDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: list[dict[str, any]]
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMapDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            self.data = m.get('Data')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMapDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMapDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMapDataResponse, self).to_map()
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
            temp_model = GetMapDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMapPublishDataRequest(TeaModel):
    def __init__(self, app_id=None, jwt_token=None):
        self.app_id = app_id  # type: str
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMapPublishDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GetMapPublishDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: list[dict[str, any]]
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMapPublishDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            self.data = m.get('Data')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMapPublishDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMapPublishDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMapPublishDataResponse, self).to_map()
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
            temp_model = GetMapPublishDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitLocateRequest(TeaModel):
    def __init__(self, jwt_token=None, params=None):
        self.jwt_token = jwt_token  # type: str
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitLocateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class InitLocateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitLocateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            self.data = m.get('Data')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InitLocateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitLocateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitLocateResponse, self).to_map()
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
            temp_model = InitLocateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDigitalHumanMaterialsRequest(TeaModel):
    def __init__(self, current=None, jwt_token=None, only_personal_materials=None, size=None, types=None):
        self.current = current  # type: int
        self.jwt_token = jwt_token  # type: str
        self.only_personal_materials = only_personal_materials  # type: bool
        self.size = size  # type: int
        self.types = types  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDigitalHumanMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.only_personal_materials is not None:
            result['OnlyPersonalMaterials'] = self.only_personal_materials
        if self.size is not None:
            result['Size'] = self.size
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('OnlyPersonalMaterials') is not None:
            self.only_personal_materials = m.get('OnlyPersonalMaterials')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class ListDigitalHumanMaterialsResponseBodyDataComponents(TeaModel):
    def __init__(self, ext=None, file_url=None, files=None, id=None, name=None, type=None):
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.files = files  # type: dict[str, any]
        self.id = id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDigitalHumanMaterialsResponseBodyDataComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.files is not None:
            result['Files'] = self.files
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Files') is not None:
            self.files = m.get('Files')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDigitalHumanMaterialsResponseBodyData(TeaModel):
    def __init__(self, components=None, ext=None, file_url=None, files=None, id=None, name=None, type=None):
        self.components = components  # type: list[ListDigitalHumanMaterialsResponseBodyDataComponents]
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.files = files  # type: dict[str, any]
        self.id = id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDigitalHumanMaterialsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.files is not None:
            result['Files'] = self.files
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ListDigitalHumanMaterialsResponseBodyDataComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Files') is not None:
            self.files = m.get('Files')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDigitalHumanMaterialsResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[ListDigitalHumanMaterialsResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDigitalHumanMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDigitalHumanMaterialsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDigitalHumanMaterialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDigitalHumanMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDigitalHumanMaterialsResponse, self).to_map()
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
            temp_model = ListDigitalHumanMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLocationServiceRequest(TeaModel):
    def __init__(self, current=None, jwt_token=None, size=None, sort=None, sort_field=None):
        self.current = current  # type: int
        self.jwt_token = jwt_token  # type: str
        self.size = size  # type: int
        self.sort = sort  # type: str
        self.sort_field = sort_field  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLocationServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        return self


class ListLocationServiceResponseBodyData(TeaModel):
    def __init__(self, app_id=None, expire_time=None, gmt_create=None, gmt_modified=None, id=None, name=None,
                 note=None, qps=None, start_time=None, status=None, svc_state=None):
        self.app_id = app_id  # type: str
        self.expire_time = expire_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.note = note  # type: str
        self.qps = qps  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.svc_state = svc_state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLocationServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.svc_state is not None:
            result['SvcState'] = self.svc_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SvcState') is not None:
            self.svc_state = m.get('SvcState')
        return self


class ListLocationServiceResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, error_name=None, http_code=None, message=None, pages=None,
                 request_id=None, size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[ListLocationServiceResponseBodyData]
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLocationServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListLocationServiceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListLocationServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLocationServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLocationServiceResponse, self).to_map()
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
            temp_model = ListLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LivePortraitFaceDetectRequest(TeaModel):
    def __init__(self, image_url=None, jwt_token=None):
        self.image_url = image_url  # type: str
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LivePortraitFaceDetectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class LivePortraitFaceDetectResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: int
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LivePortraitFaceDetectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class LivePortraitFaceDetectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: LivePortraitFaceDetectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(LivePortraitFaceDetectResponseBody, self).to_map()
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
            temp_model = LivePortraitFaceDetectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LivePortraitFaceDetectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LivePortraitFaceDetectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LivePortraitFaceDetectResponse, self).to_map()
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
            temp_model = LivePortraitFaceDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LocateRequest(TeaModel):
    def __init__(self, image=None, jwt_token=None, params=None):
        self.image = image  # type: str
        self.jwt_token = jwt_token  # type: str
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LocateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class LocateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(LocateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            self.data = m.get('Data')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LocateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LocateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LocateResponse, self).to_map()
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
            temp_model = LocateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoginModelScopeRequest(TeaModel):
    def __init__(self, emp_id=None, emp_name=None, token=None, type=None):
        self.emp_id = emp_id  # type: str
        self.emp_name = emp_name  # type: str
        self.token = token  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginModelScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emp_id is not None:
            result['EmpId'] = self.emp_id
        if self.emp_name is not None:
            result['EmpName'] = self.emp_name
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmpId') is not None:
            self.emp_id = m.get('EmpId')
        if m.get('EmpName') is not None:
            self.emp_name = m.get('EmpName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class LoginModelScopeResponseBodyData(TeaModel):
    def __init__(self, email=None, jwt_token=None, nickname=None, uid=None):
        self.email = email  # type: str
        self.jwt_token = jwt_token  # type: str
        self.nickname = nickname  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginModelScopeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class LoginModelScopeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: LoginModelScopeResponseBodyData
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(LoginModelScopeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = LoginModelScopeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LoginModelScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LoginModelScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LoginModelScopeResponse, self).to_map()
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
            temp_model = LoginModelScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBatchQueryObjectGenerationProjectStatusRequest(TeaModel):
    def __init__(self, jwt_token=None, project_ids=None):
        self.jwt_token = jwt_token  # type: str
        self.project_ids = project_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBatchQueryObjectGenerationProjectStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class PopBatchQueryObjectGenerationProjectStatusResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBatchQueryObjectGenerationProjectStatusResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        return self


class PopBatchQueryObjectGenerationProjectStatusResponseBodyData(TeaModel):
    def __init__(self, biz_usage=None, dataset=None, id=None, status=None):
        self.biz_usage = biz_usage  # type: str
        self.dataset = dataset  # type: PopBatchQueryObjectGenerationProjectStatusResponseBodyDataDataset
        self.id = id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopBatchQueryObjectGenerationProjectStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Dataset') is not None:
            temp_model = PopBatchQueryObjectGenerationProjectStatusResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopBatchQueryObjectGenerationProjectStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[PopBatchQueryObjectGenerationProjectStatusResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopBatchQueryObjectGenerationProjectStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopBatchQueryObjectGenerationProjectStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopBatchQueryObjectGenerationProjectStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBatchQueryObjectGenerationProjectStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBatchQueryObjectGenerationProjectStatusResponse, self).to_map()
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
            temp_model = PopBatchQueryObjectGenerationProjectStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBatchQueryObjectProjectStatusRequest(TeaModel):
    def __init__(self, jwt_token=None, project_ids=None):
        self.jwt_token = jwt_token  # type: str
        self.project_ids = project_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBatchQueryObjectProjectStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class PopBatchQueryObjectProjectStatusResponseBodyData(TeaModel):
    def __init__(self, check_status=None, id=None, status=None):
        self.check_status = check_status  # type: str
        self.id = id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBatchQueryObjectProjectStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopBatchQueryObjectProjectStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: list[PopBatchQueryObjectProjectStatusResponseBodyData]
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopBatchQueryObjectProjectStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopBatchQueryObjectProjectStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopBatchQueryObjectProjectStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBatchQueryObjectProjectStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBatchQueryObjectProjectStatusResponse, self).to_map()
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
            temp_model = PopBatchQueryObjectProjectStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildFeatureToAvatarProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildFeatureToAvatarProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopBuildFeatureToAvatarProjectResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildFeatureToAvatarProjectResponseBody, self).to_map()
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


class PopBuildFeatureToAvatarProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBuildFeatureToAvatarProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBuildFeatureToAvatarProjectResponse, self).to_map()
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
            temp_model = PopBuildFeatureToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildLivePortraitModelScopeProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildLivePortraitModelScopeProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopBuildLivePortraitModelScopeProjectResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildLivePortraitModelScopeProjectResponseBody, self).to_map()
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


class PopBuildLivePortraitModelScopeProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBuildLivePortraitModelScopeProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBuildLivePortraitModelScopeProjectResponse, self).to_map()
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
            temp_model = PopBuildLivePortraitModelScopeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildObjectGenerationProjectRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildObjectGenerationProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopBuildObjectGenerationProjectResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildObjectGenerationProjectResponseBody, self).to_map()
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


class PopBuildObjectGenerationProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBuildObjectGenerationProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBuildObjectGenerationProjectResponse, self).to_map()
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
            temp_model = PopBuildObjectGenerationProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildObjectProjectRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildObjectProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopBuildObjectProjectResponseBody(TeaModel):
    def __init__(self, code=None, error_name=None, http_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildObjectProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopBuildObjectProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBuildObjectProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBuildObjectProjectResponse, self).to_map()
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
            temp_model = PopBuildObjectProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildPakRenderProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildPakRenderProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopBuildPakRenderProjectResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildPakRenderProjectResponseBody, self).to_map()
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


class PopBuildPakRenderProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBuildPakRenderProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBuildPakRenderProjectResponse, self).to_map()
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
            temp_model = PopBuildPakRenderProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopBuildTextToAvatarProjectRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildTextToAvatarProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopBuildTextToAvatarProjectResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopBuildTextToAvatarProjectResponseBody, self).to_map()
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


class PopBuildTextToAvatarProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopBuildTextToAvatarProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopBuildTextToAvatarProjectResponse, self).to_map()
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
            temp_model = PopBuildTextToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateFeatureToAvatarProjectRequest(TeaModel):
    def __init__(self, ext_info=None, intro=None, title=None):
        self.ext_info = ext_info  # type: str
        self.intro = intro  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateFeatureToAvatarProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreateFeatureToAvatarProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, id=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateFeatureToAvatarProjectResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopCreateFeatureToAvatarProjectResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateFeatureToAvatarProjectResponseBodyDataDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopCreateFeatureToAvatarProjectResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_code=None,
                 error_message=None, glb_model_url=None, id=None, model_url=None, modified_time=None, origin_result_url=None,
                 oss_key=None, policy=None, pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.id = id  # type: long
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopCreateFeatureToAvatarProjectResponseBodyDataDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopCreateFeatureToAvatarProjectResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopCreateFeatureToAvatarProjectResponseBodyData(TeaModel):
    def __init__(self, biz_usage=None, build_detail=None, check_status=None, create_mode=None, create_time=None,
                 dataset=None, deleted=None, ext=None, id=None, intro=None, material_cover_url=None, modified_time=None,
                 status=None, title=None, type=None):
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopCreateFeatureToAvatarProjectResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.dataset = dataset  # type: PopCreateFeatureToAvatarProjectResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopCreateFeatureToAvatarProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateFeatureToAvatarProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopCreateFeatureToAvatarProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopCreateFeatureToAvatarProjectResponseBody, self).to_map()
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
            temp_model = PopCreateFeatureToAvatarProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreateFeatureToAvatarProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopCreateFeatureToAvatarProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopCreateFeatureToAvatarProjectResponse, self).to_map()
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
            temp_model = PopCreateFeatureToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateLivePortraitModelScopeProjectRequest(TeaModel):
    def __init__(self, ext_info=None, intro=None, title=None):
        self.ext_info = ext_info  # type: str
        self.intro = intro  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateLivePortraitModelScopeProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreateLivePortraitModelScopeProjectResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateLivePortraitModelScopeProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class PopCreateLivePortraitModelScopeProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopCreateLivePortraitModelScopeProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopCreateLivePortraitModelScopeProjectResponseBody, self).to_map()
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
            temp_model = PopCreateLivePortraitModelScopeProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreateLivePortraitModelScopeProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopCreateLivePortraitModelScopeProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopCreateLivePortraitModelScopeProjectResponse, self).to_map()
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
            temp_model = PopCreateLivePortraitModelScopeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateMaterialRequest(TeaModel):
    def __init__(self, check_status=None, ext=None, intro=None, jwt_token=None, list_status=None, name=None,
                 oss_key=None, type=None):
        self.check_status = check_status  # type: str
        self.ext = ext  # type: str
        self.intro = intro  # type: str
        self.jwt_token = jwt_token  # type: str
        self.list_status = list_status  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateMaterialResponseBodyData(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateMaterialResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateMaterialResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopCreateMaterialResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopCreateMaterialResponseBody, self).to_map()
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
            temp_model = PopCreateMaterialResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreateMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopCreateMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopCreateMaterialResponse, self).to_map()
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
            temp_model = PopCreateMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateObjectGenerationProjectRequest(TeaModel):
    def __init__(self, biz_usage=None, ext_info=None, intro=None, jwt_token=None, title=None):
        self.biz_usage = biz_usage  # type: str
        self.ext_info = ext_info  # type: str
        self.intro = intro  # type: str
        self.jwt_token = jwt_token  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectGenerationProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreateObjectGenerationProjectResponseBodyData(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectGenerationProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class PopCreateObjectGenerationProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopCreateObjectGenerationProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopCreateObjectGenerationProjectResponseBody, self).to_map()
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
            temp_model = PopCreateObjectGenerationProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreateObjectGenerationProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopCreateObjectGenerationProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopCreateObjectGenerationProjectResponse, self).to_map()
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
            temp_model = PopCreateObjectGenerationProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateObjectProjectRequest(TeaModel):
    def __init__(self, auto_build=None, biz_usage=None, custom_source=None, dependencies=None, foreign_uid=None,
                 intro=None, jwt_token=None, mode=None, recommend_status=None, title=None):
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.custom_source = custom_source  # type: str
        self.dependencies = dependencies  # type: str
        self.foreign_uid = foreign_uid  # type: str
        self.intro = intro  # type: str
        self.jwt_token = jwt_token  # type: str
        self.mode = mode  # type: str
        self.recommend_status = recommend_status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.foreign_uid is not None:
            result['ForeignUid'] = self.foreign_uid
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.recommend_status is not None:
            result['RecommendStatus'] = self.recommend_status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('ForeignUid') is not None:
            self.foreign_uid = m.get('ForeignUid')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RecommendStatus') is not None:
            self.recommend_status = m.get('RecommendStatus')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreateObjectProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, modified_time=None, running_time=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopCreateObjectProjectResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopCreateObjectProjectResponseBodyDataDatasetToken(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, dir=None, expiration=None, host=None,
                 security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.dir = dir  # type: str
        self.expiration = expiration  # type: str
        self.host = host  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataDatasetToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.host is not None:
            result['Host'] = self.host
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PopCreateObjectProjectResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_message=None,
                 glb_model_url=None, model_url=None, modified_time=None, origin_result_url=None, oss_key=None, policy=None,
                 pose_url=None, preview_url=None, token=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopCreateObjectProjectResponseBodyDataDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str
        self.token = token  # type: PopCreateObjectProjectResponseBodyDataDatasetToken

    def validate(self):
        if self.policy:
            self.policy.validate()
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Token') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataDatasetToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class PopCreateObjectProjectResponseBodyDataSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, modified_time=None, name=None, oss_key=None,
                 type=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateObjectProjectResponseBodyDataSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopCreateObjectProjectResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopCreateObjectProjectResponseBodyDataSourceToken(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, dir=None, expiration=None, host=None,
                 security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.dir = dir  # type: str
        self.expiration = expiration  # type: str
        self.host = host  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataSourceToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.host is not None:
            result['Host'] = self.host
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PopCreateObjectProjectResponseBodyDataSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, modified_time=None, oss_key=None, policy=None,
                 source_files=None, token=None):
        self.clothes = clothes  # type: list[PopCreateObjectProjectResponseBodyDataSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopCreateObjectProjectResponseBodyDataSourcePolicy
        self.source_files = source_files  # type: list[PopCreateObjectProjectResponseBodyDataSourceSourceFiles]
        self.token = token  # type: PopCreateObjectProjectResponseBodyDataSourceToken

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopCreateObjectProjectResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopCreateObjectProjectResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataSourceToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class PopCreateObjectProjectResponseBodyData(TeaModel):
    def __init__(self, audit_status=None, auto_build=None, biz_usage=None, build_detail=None, check_status=None,
                 create_mode=None, create_time=None, custom_source=None, dataset=None, deleted=None, dependencies=None, ext=None,
                 id=None, intro=None, modified_time=None, recommend_status=None, source=None, status=None, title=None,
                 type=None):
        self.audit_status = audit_status  # type: str
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopCreateObjectProjectResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.custom_source = custom_source  # type: str
        self.dataset = dataset  # type: PopCreateObjectProjectResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.modified_time = modified_time  # type: str
        self.recommend_status = recommend_status  # type: str
        self.source = source  # type: PopCreateObjectProjectResponseBodyDataSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.recommend_status is not None:
            result['RecommendStatus'] = self.recommend_status
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dataset') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RecommendStatus') is not None:
            self.recommend_status = m.get('RecommendStatus')
        if m.get('Source') is not None:
            temp_model = PopCreateObjectProjectResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateObjectProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: PopCreateObjectProjectResponseBodyData
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopCreateObjectProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = PopCreateObjectProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreateObjectProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopCreateObjectProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopCreateObjectProjectResponse, self).to_map()
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
            temp_model = PopCreateObjectProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreatePakRenderProjectRequest(TeaModel):
    def __init__(self, ext_info=None, intro=None, title=None):
        self.ext_info = ext_info  # type: str
        self.intro = intro  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreatePakRenderProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreatePakRenderProjectResponseBodyData(TeaModel):
    def __init__(self, auto_build=None, biz_usage=None, check_status=None, create_mode=None, create_time=None,
                 deleted=None, dependencies=None, ext=None, id=None, intro=None, material_cover_url=None, modified_time=None,
                 status=None, title=None, type=None):
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreatePakRenderProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreatePakRenderProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopCreatePakRenderProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopCreatePakRenderProjectResponseBody, self).to_map()
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
            temp_model = PopCreatePakRenderProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreatePakRenderProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopCreatePakRenderProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopCreatePakRenderProjectResponse, self).to_map()
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
            temp_model = PopCreatePakRenderProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopCreateTextToAvatarProjectRequest(TeaModel):
    def __init__(self, ext_info=None, intro=None, jwt_token=None, title=None):
        self.ext_info = ext_info  # type: str
        self.intro = intro  # type: str
        self.jwt_token = jwt_token  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateTextToAvatarProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopCreateTextToAvatarProjectResponseBodyData(TeaModel):
    def __init__(self, auto_build=None, biz_usage=None, check_status=None, create_mode=None, create_time=None,
                 deleted=None, dependencies=None, ext=None, id=None, intro=None, material_cover_url=None, modified_time=None,
                 status=None, title=None, type=None):
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopCreateTextToAvatarProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopCreateTextToAvatarProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopCreateTextToAvatarProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopCreateTextToAvatarProjectResponseBody, self).to_map()
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
            temp_model = PopCreateTextToAvatarProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopCreateTextToAvatarProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopCreateTextToAvatarProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopCreateTextToAvatarProjectResponse, self).to_map()
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
            temp_model = PopCreateTextToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopDeleteMaterialRequest(TeaModel):
    def __init__(self, jwt_token=None, material_id=None):
        self.jwt_token = jwt_token  # type: str
        self.material_id = material_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopDeleteMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        return self


class PopDeleteMaterialResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopDeleteMaterialResponseBody, self).to_map()
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


class PopDeleteMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopDeleteMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopDeleteMaterialResponse, self).to_map()
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
            temp_model = PopDeleteMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopGetAITryOnJobRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None, with_material=None, with_result=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str
        self.with_material = with_material  # type: bool
        self.with_result = with_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.with_material is not None:
            result['WithMaterial'] = self.with_material
        if self.with_result is not None:
            result['WithResult'] = self.with_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WithMaterial') is not None:
            self.with_material = m.get('WithMaterial')
        if m.get('WithResult') is not None:
            self.with_result = m.get('WithResult')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, id=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_code=None,
                 error_message=None, glb_model_url=None, id=None, model_url=None, modified_time=None, origin_result_url=None,
                 oss_key=None, policy=None, pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.id = id  # type: long
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopGetAITryOnJobResponseBodyDataDummyProjectInfoDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkuProps(TeaModel):
    def __init__(self, name=None, options=None):
        self.name = name  # type: str
        self.options = options  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkuProps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkus(TeaModel):
    def __init__(self, color=None, cover=None, size=None, status=None):
        self.color = color  # type: str
        self.cover = cover  # type: str
        self.size = size  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.cover is not None:
            result['Cover'] = self.cover
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Cover') is not None:
            self.cover = m.get('Cover')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, id=None, modified_time=None, name=None,
                 oss_key=None, part=None, size=None, sku_props=None, skus=None, status=None, type=None, version=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.part = part  # type: str
        self.size = size  # type: str
        self.sku_props = sku_props  # type: list[PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkuProps]
        self.skus = skus  # type: list[PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkus]
        self.status = status  # type: dict[str, str]
        self.type = type  # type: str
        self.version = version  # type: int

    def validate(self):
        if self.sku_props:
            for k in self.sku_props:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.part is not None:
            result['Part'] = self.part
        if self.size is not None:
            result['Size'] = self.size
        result['SkuProps'] = []
        if self.sku_props is not None:
            for k in self.sku_props:
                result['SkuProps'].append(k.to_map() if k else None)
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.sku_props = []
        if m.get('SkuProps') is not None:
            for k in m.get('SkuProps'):
                temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkuProps()
                self.sku_props.append(temp_model.from_map(k))
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothesSkus()
                self.skus.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None, id=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceToken(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, dir=None, expiration=None, host=None,
                 security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.dir = dir  # type: str
        self.expiration = expiration  # type: str
        self.host = host  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.host is not None:
            result['Host'] = self.host
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfoSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, id=None, modified_time=None, oss_key=None,
                 policy=None, source_files=None, token=None):
        self.clothes = clothes  # type: list[PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourcePolicy
        self.source_files = source_files  # type: list[PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceSourceFiles]
        self.token = token  # type: PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceToken

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfoSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoSourceToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class PopGetAITryOnJobResponseBodyDataDummyProjectInfo(TeaModel):
    def __init__(self, audit_status=None, auto_build=None, biz_usage=None, build_detail=None, check_status=None,
                 create_mode=None, create_time=None, custom_source=None, dataset=None, deleted=None, dependencies=None, ext=None,
                 id=None, intro=None, material_cover_url=None, modified_time=None, source=None, status=None, title=None,
                 type=None):
        self.audit_status = audit_status  # type: str
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopGetAITryOnJobResponseBodyDataDummyProjectInfoBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.custom_source = custom_source  # type: str
        self.dataset = dataset  # type: PopGetAITryOnJobResponseBodyDataDummyProjectInfoDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.source = source  # type: PopGetAITryOnJobResponseBodyDataDummyProjectInfoSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataDummyProjectInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dataset') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfoSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopGetAITryOnJobResponseBodyDataMaterialInfoBottoms(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataMaterialInfoBottoms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopGetAITryOnJobResponseBodyDataMaterialInfoModel(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataMaterialInfoModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopGetAITryOnJobResponseBodyDataMaterialInfoSuit(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataMaterialInfoSuit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopGetAITryOnJobResponseBodyDataMaterialInfoTops(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataMaterialInfoTops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopGetAITryOnJobResponseBodyDataMaterialInfo(TeaModel):
    def __init__(self, bottoms=None, clothing_type=None, model=None, shoe_type=None, suit=None, tops=None):
        self.bottoms = bottoms  # type: PopGetAITryOnJobResponseBodyDataMaterialInfoBottoms
        self.clothing_type = clothing_type  # type: str
        self.model = model  # type: PopGetAITryOnJobResponseBodyDataMaterialInfoModel
        self.shoe_type = shoe_type  # type: str
        self.suit = suit  # type: PopGetAITryOnJobResponseBodyDataMaterialInfoSuit
        self.tops = tops  # type: PopGetAITryOnJobResponseBodyDataMaterialInfoTops

    def validate(self):
        if self.bottoms:
            self.bottoms.validate()
        if self.model:
            self.model.validate()
        if self.suit:
            self.suit.validate()
        if self.tops:
            self.tops.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bottoms is not None:
            result['Bottoms'] = self.bottoms.to_map()
        if self.clothing_type is not None:
            result['ClothingType'] = self.clothing_type
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.shoe_type is not None:
            result['ShoeType'] = self.shoe_type
        if self.suit is not None:
            result['Suit'] = self.suit.to_map()
        if self.tops is not None:
            result['Tops'] = self.tops.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bottoms') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataMaterialInfoBottoms()
            self.bottoms = temp_model.from_map(m['Bottoms'])
        if m.get('ClothingType') is not None:
            self.clothing_type = m.get('ClothingType')
        if m.get('Model') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataMaterialInfoModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('ShoeType') is not None:
            self.shoe_type = m.get('ShoeType')
        if m.get('Suit') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataMaterialInfoSuit()
            self.suit = temp_model.from_map(m['Suit'])
        if m.get('Tops') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataMaterialInfoTops()
            self.tops = temp_model.from_map(m['Tops'])
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksFeedback(TeaModel):
    def __init__(self, dislike_tags=None, other_reason=None, project_id=None, rating=None):
        self.dislike_tags = dislike_tags  # type: list[int]
        self.other_reason = other_reason  # type: str
        self.project_id = project_id  # type: long
        self.rating = rating  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksFeedback, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dislike_tags is not None:
            result['DislikeTags'] = self.dislike_tags
        if self.other_reason is not None:
            result['OtherReason'] = self.other_reason
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.rating is not None:
            result['Rating'] = self.rating
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DislikeTags') is not None:
            self.dislike_tags = m.get('DislikeTags')
        if m.get('OtherReason') is not None:
            self.other_reason = m.get('OtherReason')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, id=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_code=None,
                 error_message=None, glb_model_url=None, id=None, model_url=None, modified_time=None, origin_result_url=None,
                 oss_key=None, policy=None, pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.id = id  # type: long
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps(TeaModel):
    def __init__(self, name=None, options=None):
        self.name = name  # type: str
        self.options = options  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus(TeaModel):
    def __init__(self, color=None, cover=None, size=None, status=None):
        self.color = color  # type: str
        self.cover = cover  # type: str
        self.size = size  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.cover is not None:
            result['Cover'] = self.cover
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Cover') is not None:
            self.cover = m.get('Cover')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, id=None, modified_time=None, name=None,
                 oss_key=None, part=None, size=None, sku_props=None, skus=None, status=None, type=None, version=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.part = part  # type: str
        self.size = size  # type: str
        self.sku_props = sku_props  # type: list[PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps]
        self.skus = skus  # type: list[PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus]
        self.status = status  # type: dict[str, str]
        self.type = type  # type: str
        self.version = version  # type: int

    def validate(self):
        if self.sku_props:
            for k in self.sku_props:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.part is not None:
            result['Part'] = self.part
        if self.size is not None:
            result['Size'] = self.size
        result['SkuProps'] = []
        if self.sku_props is not None:
            for k in self.sku_props:
                result['SkuProps'].append(k.to_map() if k else None)
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.sku_props = []
        if m.get('SkuProps') is not None:
            for k in m.get('SkuProps'):
                temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps()
                self.sku_props.append(temp_model.from_map(k))
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus()
                self.skus.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None, id=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceToken(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, dir=None, expiration=None, host=None,
                 security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.dir = dir  # type: str
        self.expiration = expiration  # type: str
        self.host = host  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.host is not None:
            result['Host'] = self.host
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, id=None, modified_time=None, oss_key=None,
                 policy=None, source_files=None, token=None):
        self.clothes = clothes  # type: list[PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourcePolicy
        self.source_files = source_files  # type: list[PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles]
        self.token = token  # type: PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceToken

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSourceToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfo(TeaModel):
    def __init__(self, audit_status=None, auto_build=None, biz_usage=None, build_detail=None, check_status=None,
                 create_mode=None, create_time=None, custom_source=None, dataset=None, deleted=None, dependencies=None, ext=None,
                 id=None, intro=None, material_cover_url=None, modified_time=None, source=None, status=None, title=None,
                 type=None):
        self.audit_status = audit_status  # type: str
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.custom_source = custom_source  # type: str
        self.dataset = dataset  # type: PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.source = source  # type: PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dataset') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfoSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopGetAITryOnJobResponseBodyDataSubTasks(TeaModel):
    def __init__(self, feedback=None, sub_project_info=None):
        self.feedback = feedback  # type: PopGetAITryOnJobResponseBodyDataSubTasksFeedback
        self.sub_project_info = sub_project_info  # type: PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfo

    def validate(self):
        if self.feedback:
            self.feedback.validate()
        if self.sub_project_info:
            self.sub_project_info.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyDataSubTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback.to_map()
        if self.sub_project_info is not None:
            result['SubProjectInfo'] = self.sub_project_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksFeedback()
            self.feedback = temp_model.from_map(m['Feedback'])
        if m.get('SubProjectInfo') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataSubTasksSubProjectInfo()
            self.sub_project_info = temp_model.from_map(m['SubProjectInfo'])
        return self


class PopGetAITryOnJobResponseBodyData(TeaModel):
    def __init__(self, dummy_project_info=None, material_info=None, sub_tasks=None):
        self.dummy_project_info = dummy_project_info  # type: PopGetAITryOnJobResponseBodyDataDummyProjectInfo
        self.material_info = material_info  # type: PopGetAITryOnJobResponseBodyDataMaterialInfo
        self.sub_tasks = sub_tasks  # type: list[PopGetAITryOnJobResponseBodyDataSubTasks]

    def validate(self):
        if self.dummy_project_info:
            self.dummy_project_info.validate()
        if self.material_info:
            self.material_info.validate()
        if self.sub_tasks:
            for k in self.sub_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dummy_project_info is not None:
            result['DummyProjectInfo'] = self.dummy_project_info.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k in self.sub_tasks:
                result['SubTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DummyProjectInfo') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataDummyProjectInfo()
            self.dummy_project_info = temp_model.from_map(m['DummyProjectInfo'])
        if m.get('MaterialInfo') is not None:
            temp_model = PopGetAITryOnJobResponseBodyDataMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k in m.get('SubTasks'):
                temp_model = PopGetAITryOnJobResponseBodyDataSubTasks()
                self.sub_tasks.append(temp_model.from_map(k))
        return self


class PopGetAITryOnJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopGetAITryOnJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponseBody, self).to_map()
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
            temp_model = PopGetAITryOnJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopGetAITryOnJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopGetAITryOnJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopGetAITryOnJobResponse, self).to_map()
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
            temp_model = PopGetAITryOnJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListAITryOnJobsRequest(TeaModel):
    def __init__(self, current=None, jwt_token=None, size=None):
        self.current = current  # type: int
        self.jwt_token = jwt_token  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, id=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_code=None,
                 error_message=None, glb_model_url=None, id=None, model_url=None, modified_time=None, origin_result_url=None,
                 oss_key=None, policy=None, pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.id = id  # type: long
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListAITryOnJobsResponseBodyDataDummyProjectInfoDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkuProps(TeaModel):
    def __init__(self, name=None, options=None):
        self.name = name  # type: str
        self.options = options  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkuProps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkus(TeaModel):
    def __init__(self, color=None, cover=None, size=None, status=None):
        self.color = color  # type: str
        self.cover = cover  # type: str
        self.size = size  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.cover is not None:
            result['Cover'] = self.cover
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Cover') is not None:
            self.cover = m.get('Cover')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, id=None, modified_time=None, name=None,
                 oss_key=None, part=None, size=None, sku_props=None, skus=None, status=None, type=None, version=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.part = part  # type: str
        self.size = size  # type: str
        self.sku_props = sku_props  # type: list[PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkuProps]
        self.skus = skus  # type: list[PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkus]
        self.status = status  # type: dict[str, str]
        self.type = type  # type: str
        self.version = version  # type: int

    def validate(self):
        if self.sku_props:
            for k in self.sku_props:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.part is not None:
            result['Part'] = self.part
        if self.size is not None:
            result['Size'] = self.size
        result['SkuProps'] = []
        if self.sku_props is not None:
            for k in self.sku_props:
                result['SkuProps'].append(k.to_map() if k else None)
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.sku_props = []
        if m.get('SkuProps') is not None:
            for k in m.get('SkuProps'):
                temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkuProps()
                self.sku_props.append(temp_model.from_map(k))
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothesSkus()
                self.skus.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None, id=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceToken(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, dir=None, expiration=None, host=None,
                 security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.dir = dir  # type: str
        self.expiration = expiration  # type: str
        self.host = host  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.host is not None:
            result['Host'] = self.host
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfoSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, id=None, modified_time=None, oss_key=None,
                 policy=None, source_files=None, token=None):
        self.clothes = clothes  # type: list[PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourcePolicy
        self.source_files = source_files  # type: list[PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceSourceFiles]
        self.token = token  # type: PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceToken

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfoSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoSourceToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class PopListAITryOnJobsResponseBodyDataDummyProjectInfo(TeaModel):
    def __init__(self, audit_status=None, auto_build=None, biz_usage=None, build_detail=None, check_status=None,
                 create_mode=None, create_time=None, custom_source=None, dataset=None, deleted=None, dependencies=None, ext=None,
                 id=None, intro=None, material_cover_url=None, modified_time=None, source=None, status=None, title=None,
                 type=None):
        self.audit_status = audit_status  # type: str
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopListAITryOnJobsResponseBodyDataDummyProjectInfoBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.custom_source = custom_source  # type: str
        self.dataset = dataset  # type: PopListAITryOnJobsResponseBodyDataDummyProjectInfoDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.source = source  # type: PopListAITryOnJobsResponseBodyDataDummyProjectInfoSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataDummyProjectInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dataset') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfoSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListAITryOnJobsResponseBodyDataMaterialInfoBottoms(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataMaterialInfoBottoms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListAITryOnJobsResponseBodyDataMaterialInfoModel(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataMaterialInfoModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListAITryOnJobsResponseBodyDataMaterialInfoSuit(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataMaterialInfoSuit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListAITryOnJobsResponseBodyDataMaterialInfoTops(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: long
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataMaterialInfoTops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListAITryOnJobsResponseBodyDataMaterialInfo(TeaModel):
    def __init__(self, bottoms=None, clothing_type=None, model=None, shoe_type=None, suit=None, tops=None):
        self.bottoms = bottoms  # type: PopListAITryOnJobsResponseBodyDataMaterialInfoBottoms
        self.clothing_type = clothing_type  # type: str
        self.model = model  # type: PopListAITryOnJobsResponseBodyDataMaterialInfoModel
        self.shoe_type = shoe_type  # type: str
        self.suit = suit  # type: PopListAITryOnJobsResponseBodyDataMaterialInfoSuit
        self.tops = tops  # type: PopListAITryOnJobsResponseBodyDataMaterialInfoTops

    def validate(self):
        if self.bottoms:
            self.bottoms.validate()
        if self.model:
            self.model.validate()
        if self.suit:
            self.suit.validate()
        if self.tops:
            self.tops.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bottoms is not None:
            result['Bottoms'] = self.bottoms.to_map()
        if self.clothing_type is not None:
            result['ClothingType'] = self.clothing_type
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.shoe_type is not None:
            result['ShoeType'] = self.shoe_type
        if self.suit is not None:
            result['Suit'] = self.suit.to_map()
        if self.tops is not None:
            result['Tops'] = self.tops.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bottoms') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataMaterialInfoBottoms()
            self.bottoms = temp_model.from_map(m['Bottoms'])
        if m.get('ClothingType') is not None:
            self.clothing_type = m.get('ClothingType')
        if m.get('Model') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataMaterialInfoModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('ShoeType') is not None:
            self.shoe_type = m.get('ShoeType')
        if m.get('Suit') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataMaterialInfoSuit()
            self.suit = temp_model.from_map(m['Suit'])
        if m.get('Tops') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataMaterialInfoTops()
            self.tops = temp_model.from_map(m['Tops'])
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksFeedback(TeaModel):
    def __init__(self, dislike_tags=None, other_reason=None, project_id=None, rating=None):
        self.dislike_tags = dislike_tags  # type: list[int]
        self.other_reason = other_reason  # type: str
        self.project_id = project_id  # type: long
        self.rating = rating  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksFeedback, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dislike_tags is not None:
            result['DislikeTags'] = self.dislike_tags
        if self.other_reason is not None:
            result['OtherReason'] = self.other_reason
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.rating is not None:
            result['Rating'] = self.rating
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DislikeTags') is not None:
            self.dislike_tags = m.get('DislikeTags')
        if m.get('OtherReason') is not None:
            self.other_reason = m.get('OtherReason')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, id=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_code=None,
                 error_message=None, glb_model_url=None, id=None, model_url=None, modified_time=None, origin_result_url=None,
                 oss_key=None, policy=None, pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.id = id  # type: long
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps(TeaModel):
    def __init__(self, name=None, options=None):
        self.name = name  # type: str
        self.options = options  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus(TeaModel):
    def __init__(self, color=None, cover=None, size=None, status=None):
        self.color = color  # type: str
        self.cover = cover  # type: str
        self.size = size  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.cover is not None:
            result['Cover'] = self.cover
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Cover') is not None:
            self.cover = m.get('Cover')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, id=None, modified_time=None, name=None,
                 oss_key=None, part=None, size=None, sku_props=None, skus=None, status=None, type=None, version=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.part = part  # type: str
        self.size = size  # type: str
        self.sku_props = sku_props  # type: list[PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps]
        self.skus = skus  # type: list[PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus]
        self.status = status  # type: dict[str, str]
        self.type = type  # type: str
        self.version = version  # type: int

    def validate(self):
        if self.sku_props:
            for k in self.sku_props:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.part is not None:
            result['Part'] = self.part
        if self.size is not None:
            result['Size'] = self.size
        result['SkuProps'] = []
        if self.sku_props is not None:
            for k in self.sku_props:
                result['SkuProps'].append(k.to_map() if k else None)
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Part') is not None:
            self.part = m.get('Part')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.sku_props = []
        if m.get('SkuProps') is not None:
            for k in m.get('SkuProps'):
                temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkuProps()
                self.sku_props.append(temp_model.from_map(k))
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothesSkus()
                self.skus.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None, id=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceToken(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, dir=None, expiration=None, host=None,
                 security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.dir = dir  # type: str
        self.expiration = expiration  # type: str
        self.host = host  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.host is not None:
            result['Host'] = self.host
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, id=None, modified_time=None, oss_key=None,
                 policy=None, source_files=None, token=None):
        self.clothes = clothes  # type: list[PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourcePolicy
        self.source_files = source_files  # type: list[PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles]
        self.token = token  # type: PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceToken

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSourceToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfo(TeaModel):
    def __init__(self, audit_status=None, auto_build=None, biz_usage=None, build_detail=None, check_status=None,
                 create_mode=None, create_time=None, custom_source=None, dataset=None, deleted=None, dependencies=None, ext=None,
                 id=None, intro=None, material_cover_url=None, modified_time=None, source=None, status=None, title=None,
                 type=None):
        self.audit_status = audit_status  # type: str
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.custom_source = custom_source  # type: str
        self.dataset = dataset  # type: PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.source = source  # type: PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dataset') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfoSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListAITryOnJobsResponseBodyDataSubTasks(TeaModel):
    def __init__(self, feedback=None, sub_project_info=None):
        self.feedback = feedback  # type: PopListAITryOnJobsResponseBodyDataSubTasksFeedback
        self.sub_project_info = sub_project_info  # type: PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfo

    def validate(self):
        if self.feedback:
            self.feedback.validate()
        if self.sub_project_info:
            self.sub_project_info.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyDataSubTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback.to_map()
        if self.sub_project_info is not None:
            result['SubProjectInfo'] = self.sub_project_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksFeedback()
            self.feedback = temp_model.from_map(m['Feedback'])
        if m.get('SubProjectInfo') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataSubTasksSubProjectInfo()
            self.sub_project_info = temp_model.from_map(m['SubProjectInfo'])
        return self


class PopListAITryOnJobsResponseBodyData(TeaModel):
    def __init__(self, dummy_project_info=None, material_info=None, sub_tasks=None):
        self.dummy_project_info = dummy_project_info  # type: PopListAITryOnJobsResponseBodyDataDummyProjectInfo
        self.material_info = material_info  # type: PopListAITryOnJobsResponseBodyDataMaterialInfo
        self.sub_tasks = sub_tasks  # type: list[PopListAITryOnJobsResponseBodyDataSubTasks]

    def validate(self):
        if self.dummy_project_info:
            self.dummy_project_info.validate()
        if self.material_info:
            self.material_info.validate()
        if self.sub_tasks:
            for k in self.sub_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dummy_project_info is not None:
            result['DummyProjectInfo'] = self.dummy_project_info.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k in self.sub_tasks:
                result['SubTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DummyProjectInfo') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataDummyProjectInfo()
            self.dummy_project_info = temp_model.from_map(m['DummyProjectInfo'])
        if m.get('MaterialInfo') is not None:
            temp_model = PopListAITryOnJobsResponseBodyDataMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k in m.get('SubTasks'):
                temp_model = PopListAITryOnJobsResponseBodyDataSubTasks()
                self.sub_tasks.append(temp_model.from_map(k))
        return self


class PopListAITryOnJobsResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListAITryOnJobsResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListAITryOnJobsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListAITryOnJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListAITryOnJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListAITryOnJobsResponse, self).to_map()
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
            temp_model = PopListAITryOnJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListCommonMaterialsAllRequest(TeaModel):
    def __init__(self, current=None, jwt_token=None, list_status=None, name=None, size=None, tags=None, type=None):
        self.current = current  # type: int
        self.jwt_token = jwt_token  # type: str
        self.list_status = list_status  # type: str
        self.name = name  # type: str
        self.size = size  # type: int
        self.tags = tags  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListCommonMaterialsAllRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListCommonMaterialsAllResponseBodyData(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, create_time=None, deleted=None, ext=None,
                 file_url=None, id=None, intro=None, list_status=None, modified_time=None, name=None, oss_key=None,
                 preview_url=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.preview_url = preview_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListCommonMaterialsAllResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListCommonMaterialsAllResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[PopListCommonMaterialsAllResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListCommonMaterialsAllResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListCommonMaterialsAllResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopListCommonMaterialsAllResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListCommonMaterialsAllResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListCommonMaterialsAllResponse, self).to_map()
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
            temp_model = PopListCommonMaterialsAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListFeatureToAvatarMaterialsRequest(TeaModel):
    def __init__(self, current=None, list_status=None, size=None, tags=None):
        self.current = current  # type: int
        self.list_status = list_status  # type: str
        self.size = size  # type: int
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListFeatureToAvatarMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.size is not None:
            result['Size'] = self.size
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class PopListFeatureToAvatarMaterialsResponseBodyData(TeaModel):
    def __init__(self, check_status=None, common=None, cover_url=None, deleted=None, ext=None, file_url=None, id=None,
                 intro=None, list_status=None, name=None, type=None):
        self.check_status = check_status  # type: str
        self.common = common  # type: bool
        self.cover_url = cover_url  # type: str
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.list_status = list_status  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListFeatureToAvatarMaterialsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.common is not None:
            result['Common'] = self.common
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListFeatureToAvatarMaterialsResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListFeatureToAvatarMaterialsResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListFeatureToAvatarMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListFeatureToAvatarMaterialsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListFeatureToAvatarMaterialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListFeatureToAvatarMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListFeatureToAvatarMaterialsResponse, self).to_map()
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
            temp_model = PopListFeatureToAvatarMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListFeatureToAvatarProjectRequest(TeaModel):
    def __init__(self, current=None, size=None, sort_field=None, status=None, title=None):
        self.current = current  # type: int
        self.size = size  # type: int
        self.sort_field = sort_field  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListFeatureToAvatarProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopListFeatureToAvatarProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListFeatureToAvatarProjectResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListFeatureToAvatarProjectResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListFeatureToAvatarProjectResponseBodyDataDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListFeatureToAvatarProjectResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_code=None,
                 error_message=None, glb_model_url=None, model_url=None, modified_time=None, origin_result_url=None, oss_key=None,
                 policy=None, pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListFeatureToAvatarProjectResponseBodyDataDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopListFeatureToAvatarProjectResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListFeatureToAvatarProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopListFeatureToAvatarProjectResponseBodyData(TeaModel):
    def __init__(self, biz_usage=None, build_detail=None, check_status=None, create_mode=None, create_time=None,
                 dataset=None, deleted=None, ext=None, id=None, intro=None, material_cover_url=None, modified_time=None,
                 status=None, title=None, type=None):
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopListFeatureToAvatarProjectResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.dataset = dataset  # type: PopListFeatureToAvatarProjectResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopListFeatureToAvatarProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListFeatureToAvatarProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopListFeatureToAvatarProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListFeatureToAvatarProjectResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListFeatureToAvatarProjectResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListFeatureToAvatarProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListFeatureToAvatarProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListFeatureToAvatarProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListFeatureToAvatarProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListFeatureToAvatarProjectResponse, self).to_map()
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
            temp_model = PopListFeatureToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListLivePortraitModelScopeMaterialsRequest(TeaModel):
    def __init__(self, current=None, size=None, types=None):
        self.current = current  # type: int
        self.size = size  # type: int
        self.types = types  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListLivePortraitModelScopeMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class PopListLivePortraitModelScopeMaterialsResponseBodyData(TeaModel):
    def __init__(self, cover_url=None, ext=None, file_url=None, id=None, intro=None, name=None, type=None):
        self.cover_url = cover_url  # type: str
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListLivePortraitModelScopeMaterialsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListLivePortraitModelScopeMaterialsResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListLivePortraitModelScopeMaterialsResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListLivePortraitModelScopeMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListLivePortraitModelScopeMaterialsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListLivePortraitModelScopeMaterialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListLivePortraitModelScopeMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListLivePortraitModelScopeMaterialsResponse, self).to_map()
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
            temp_model = PopListLivePortraitModelScopeMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListObjectCaseRequest(TeaModel):
    def __init__(self, current=None, jwt_token=None, size=None):
        self.current = current  # type: int
        self.jwt_token = jwt_token  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectCaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class PopListObjectCaseResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, modified_time=None, running_time=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListObjectCaseResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyDataDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListObjectCaseResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_message=None,
                 glb_model_url=None, model_url=None, modified_time=None, origin_result_url=None, oss_key=None, policy=None,
                 pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListObjectCaseResponseBodyDataDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListObjectCaseResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopListObjectCaseResponseBodyDataSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, modified_time=None, name=None, oss_key=None,
                 type=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyDataSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListObjectCaseResponseBodyDataSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyDataSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListObjectCaseResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyDataSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopListObjectCaseResponseBodyDataSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, modified_time=None, oss_key=None, policy=None,
                 source_files=None):
        self.clothes = clothes  # type: list[PopListObjectCaseResponseBodyDataSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListObjectCaseResponseBodyDataSourcePolicy
        self.source_files = source_files  # type: list[PopListObjectCaseResponseBodyDataSourceSourceFiles]

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopListObjectCaseResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListObjectCaseResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopListObjectCaseResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        return self


class PopListObjectCaseResponseBodyData(TeaModel):
    def __init__(self, audit_status=None, auto_build=None, biz_usage=None, build_detail=None, check_status=None,
                 create_mode=None, create_time=None, custom_source=None, dataset=None, deleted=None, dependencies=None, ext=None,
                 id=None, intro=None, modified_time=None, source=None, status=None, title=None, type=None):
        self.audit_status = audit_status  # type: str
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopListObjectCaseResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.custom_source = custom_source  # type: str
        self.dataset = dataset  # type: PopListObjectCaseResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.modified_time = modified_time  # type: str
        self.source = source  # type: PopListObjectCaseResponseBodyDataSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopListObjectCaseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListObjectCaseResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dataset') is not None:
            temp_model = PopListObjectCaseResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopListObjectCaseResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListObjectCaseResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, error_name=None, http_code=None, message=None, pages=None,
                 request_id=None, size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListObjectCaseResponseBodyData]
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListObjectCaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListObjectCaseResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListObjectCaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListObjectCaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListObjectCaseResponse, self).to_map()
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
            temp_model = PopListObjectCaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListObjectGenerationProjectRequest(TeaModel):
    def __init__(self, current=None, jwt_token=None, size=None):
        self.current = current  # type: int
        self.jwt_token = jwt_token  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectGenerationProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class PopListObjectGenerationProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, error_message=None, estimated_duration=None, running_time=None,
                 submit_time=None):
        self.completed_time = completed_time  # type: str
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.running_time = running_time  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectGenerationProjectResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListObjectGenerationProjectResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectGenerationProjectResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        return self


class PopListObjectGenerationProjectResponseBodyData(TeaModel):
    def __init__(self, biz_usage=None, build_detail=None, dataset=None, ext=None, id=None, intro=None, status=None,
                 title=None):
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopListObjectGenerationProjectResponseBodyDataBuildDetail
        self.dataset = dataset  # type: PopListObjectGenerationProjectResponseBodyDataDataset
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopListObjectGenerationProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListObjectGenerationProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('Dataset') is not None:
            temp_model = PopListObjectGenerationProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopListObjectGenerationProjectResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListObjectGenerationProjectResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListObjectGenerationProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListObjectGenerationProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListObjectGenerationProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListObjectGenerationProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListObjectGenerationProjectResponse, self).to_map()
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
            temp_model = PopListObjectGenerationProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListObjectProjectRequest(TeaModel):
    def __init__(self, audit_status=None, current=None, custom_source=None, jwt_token=None, size=None,
                 sort_field=None, status=None, title=None, with_source=None):
        self.audit_status = audit_status  # type: str
        self.current = current  # type: int
        self.custom_source = custom_source  # type: str
        self.jwt_token = jwt_token  # type: str
        self.size = size  # type: int
        self.sort_field = sort_field  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.with_source = with_source  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.current is not None:
            result['Current'] = self.current
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.with_source is not None:
            result['WithSource'] = self.with_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WithSource') is not None:
            self.with_source = m.get('WithSource')
        return self


class PopListObjectProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, modified_time=None, running_time=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListObjectProjectResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyDataDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListObjectProjectResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_message=None,
                 glb_model_url=None, model_url=None, modified_time=None, origin_result_url=None, oss_key=None, policy=None,
                 pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListObjectProjectResponseBodyDataDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListObjectProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopListObjectProjectResponseBodyDataSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, modified_time=None, name=None, oss_key=None,
                 type=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyDataSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListObjectProjectResponseBodyDataSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyDataSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListObjectProjectResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyDataSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopListObjectProjectResponseBodyDataSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, modified_time=None, oss_key=None, policy=None,
                 source_files=None):
        self.clothes = clothes  # type: list[PopListObjectProjectResponseBodyDataSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListObjectProjectResponseBodyDataSourcePolicy
        self.source_files = source_files  # type: list[PopListObjectProjectResponseBodyDataSourceSourceFiles]

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopListObjectProjectResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListObjectProjectResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopListObjectProjectResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        return self


class PopListObjectProjectResponseBodyData(TeaModel):
    def __init__(self, audit_status=None, auto_build=None, biz_usage=None, build_detail=None, check_status=None,
                 create_mode=None, create_time=None, custom_source=None, dataset=None, deleted=None, dependencies=None, ext=None,
                 id=None, intro=None, modified_time=None, source=None, status=None, title=None, type=None):
        self.audit_status = audit_status  # type: str
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopListObjectProjectResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.custom_source = custom_source  # type: str
        self.dataset = dataset  # type: PopListObjectProjectResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.modified_time = modified_time  # type: str
        self.source = source  # type: PopListObjectProjectResponseBodyDataSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopListObjectProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_source is not None:
            result['CustomSource'] = self.custom_source
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListObjectProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomSource') is not None:
            self.custom_source = m.get('CustomSource')
        if m.get('Dataset') is not None:
            temp_model = PopListObjectProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopListObjectProjectResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListObjectProjectResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, error_name=None, http_code=None, message=None, pages=None,
                 request_id=None, size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListObjectProjectResponseBodyData]
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListObjectProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListObjectProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListObjectProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListObjectProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListObjectProjectResponse, self).to_map()
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
            temp_model = PopListObjectProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListPakRenderExpressionRequest(TeaModel):
    def __init__(self, current=None, list_status=None, size=None):
        self.current = current  # type: int
        self.list_status = list_status  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListPakRenderExpressionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class PopListPakRenderExpressionResponseBodyData(TeaModel):
    def __init__(self, cover_url=None, ext=None, file_url=None, id=None, intro=None, name=None):
        self.cover_url = cover_url  # type: str
        self.ext = ext  # type: str
        self.file_url = file_url  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListPakRenderExpressionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PopListPakRenderExpressionResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListPakRenderExpressionResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListPakRenderExpressionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListPakRenderExpressionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListPakRenderExpressionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListPakRenderExpressionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListPakRenderExpressionResponse, self).to_map()
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
            temp_model = PopListPakRenderExpressionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopListTextToAvatarProjectRequest(TeaModel):
    def __init__(self, current=None, jwt_token=None, size=None, sort_field=None, status=None, title=None):
        self.current = current  # type: int
        self.jwt_token = jwt_token  # type: str
        self.size = size  # type: int
        self.sort_field = sort_field  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListTextToAvatarProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.size is not None:
            result['Size'] = self.size
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopListTextToAvatarProjectResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListTextToAvatarProjectResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopListTextToAvatarProjectResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopListTextToAvatarProjectResponseBodyDataDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopListTextToAvatarProjectResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, create_time=None, deleted=None, error_code=None, error_message=None,
                 modified_time=None, oss_key=None, policy=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopListTextToAvatarProjectResponseBodyDataDatasetPolicy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopListTextToAvatarProjectResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopListTextToAvatarProjectResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class PopListTextToAvatarProjectResponseBodyData(TeaModel):
    def __init__(self, auto_build=None, biz_usage=None, build_detail=None, check_status=None, create_mode=None,
                 create_time=None, dataset=None, deleted=None, dependencies=None, ext=None, id=None, intro=None,
                 material_cover_url=None, modified_time=None, status=None, title=None, type=None):
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopListTextToAvatarProjectResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.dataset = dataset  # type: PopListTextToAvatarProjectResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopListTextToAvatarProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopListTextToAvatarProjectResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopListTextToAvatarProjectResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopListTextToAvatarProjectResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, message=None, pages=None, request_id=None, size=None,
                 success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[PopListTextToAvatarProjectResponseBodyData]
        self.message = message  # type: str
        self.pages = pages  # type: int
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopListTextToAvatarProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopListTextToAvatarProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PopListTextToAvatarProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopListTextToAvatarProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopListTextToAvatarProjectResponse, self).to_map()
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
            temp_model = PopListTextToAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopObjectProjectDetailRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectProjectDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopObjectProjectDetailResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, modified_time=None, running_time=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopObjectProjectDetailResponseBodyDataDatasetPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyDataDatasetPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopObjectProjectDetailResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_message=None,
                 glb_model_url=None, model_url=None, modified_time=None, origin_result_url=None, oss_key=None, policy=None,
                 pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopObjectProjectDetailResponseBodyDataDatasetPolicy
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataDatasetPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopObjectProjectDetailResponseBodyDataSourceClothes(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, modified_time=None, name=None, oss_key=None,
                 type=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyDataSourceClothes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopObjectProjectDetailResponseBodyDataSourcePolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyDataSourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopObjectProjectDetailResponseBodyDataSourceSourceFiles(TeaModel):
    def __init__(self, cover_url=None, create_time=None, deleted=None, file_name=None, filesize=None,
                 modified_time=None, oss_key=None, type=None, url=None):
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.file_name = file_name  # type: str
        self.filesize = filesize  # type: long
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyDataSourceSourceFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PopObjectProjectDetailResponseBodyDataSource(TeaModel):
    def __init__(self, clothes=None, create_time=None, deleted=None, modified_time=None, oss_key=None, policy=None,
                 source_files=None):
        self.clothes = clothes  # type: list[PopObjectProjectDetailResponseBodyDataSourceClothes]
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.modified_time = modified_time  # type: str
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopObjectProjectDetailResponseBodyDataSourcePolicy
        self.source_files = source_files  # type: list[PopObjectProjectDetailResponseBodyDataSourceSourceFiles]

    def validate(self):
        if self.clothes:
            for k in self.clothes:
                if k:
                    k.validate()
        if self.policy:
            self.policy.validate()
        if self.source_files:
            for k in self.source_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clothes'] = []
        if self.clothes is not None:
            for k in self.clothes:
                result['Clothes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        result['SourceFiles'] = []
        if self.source_files is not None:
            for k in self.source_files:
                result['SourceFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clothes = []
        if m.get('Clothes') is not None:
            for k in m.get('Clothes'):
                temp_model = PopObjectProjectDetailResponseBodyDataSourceClothes()
                self.clothes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataSourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        self.source_files = []
        if m.get('SourceFiles') is not None:
            for k in m.get('SourceFiles'):
                temp_model = PopObjectProjectDetailResponseBodyDataSourceSourceFiles()
                self.source_files.append(temp_model.from_map(k))
        return self


class PopObjectProjectDetailResponseBodyData(TeaModel):
    def __init__(self, auto_build=None, biz_usage=None, build_detail=None, check_status=None, create_mode=None,
                 create_time=None, dataset=None, deleted=None, dependencies=None, ext=None, id=None, intro=None,
                 modified_time=None, source=None, status=None, title=None, type=None):
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopObjectProjectDetailResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.dataset = dataset  # type: PopObjectProjectDetailResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.modified_time = modified_time  # type: str
        self.source = source  # type: PopObjectProjectDetailResponseBodyDataSource
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            temp_model = PopObjectProjectDetailResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopObjectProjectDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_name=None, http_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: PopObjectProjectDetailResponseBodyData
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopObjectProjectDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = PopObjectProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopObjectProjectDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopObjectProjectDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopObjectProjectDetailResponse, self).to_map()
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
            temp_model = PopObjectProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopObjectRetrievalRequest(TeaModel):
    def __init__(self, content=None, jwt_token=None, source_type=None, top_k=None):
        self.content = content  # type: str
        self.jwt_token = jwt_token  # type: str
        self.source_type = source_type  # type: str
        self.top_k = top_k  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectRetrievalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.top_k is not None:
            result['TopK'] = self.top_k
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        return self


class PopObjectRetrievalResponseBodyData(TeaModel):
    def __init__(self, cover_url=None, glb_url=None, id=None, model_url=None, preview_url=None, title=None):
        self.cover_url = cover_url  # type: str
        self.glb_url = glb_url  # type: str
        self.id = id  # type: str
        self.model_url = model_url  # type: str
        self.preview_url = preview_url  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectRetrievalResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.glb_url is not None:
            result['GlbUrl'] = self.glb_url
        if self.id is not None:
            result['Id'] = self.id
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('GlbUrl') is not None:
            self.glb_url = m.get('GlbUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopObjectRetrievalResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[PopObjectRetrievalResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PopObjectRetrievalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PopObjectRetrievalResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopObjectRetrievalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopObjectRetrievalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopObjectRetrievalResponse, self).to_map()
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
            temp_model = PopObjectRetrievalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopObjectRetrievalUploadDataRequest(TeaModel):
    def __init__(self, jwt_token=None):
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectRetrievalUploadDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class PopObjectRetrievalUploadDataResponseBodyData(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopObjectRetrievalUploadDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopObjectRetrievalUploadDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopObjectRetrievalUploadDataResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopObjectRetrievalUploadDataResponseBody, self).to_map()
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
            temp_model = PopObjectRetrievalUploadDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopObjectRetrievalUploadDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopObjectRetrievalUploadDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopObjectRetrievalUploadDataResponse, self).to_map()
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
            temp_model = PopObjectRetrievalUploadDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopQueryAvatarProjectDetailRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryAvatarProjectDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopQueryAvatarProjectDetailResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, create_time=None, deleted=None, error_message=None,
                 estimated_duration=None, modified_time=None, running_time=None, status=None, submit_time=None):
        self.completed_time = completed_time  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.modified_time = modified_time  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryAvatarProjectDetailResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopQueryAvatarProjectDetailResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, cover_url=None, create_time=None, deleted=None, error_code=None,
                 error_message=None, glb_model_url=None, model_url=None, modified_time=None, origin_result_url=None, oss_key=None,
                 pose_url=None, preview_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.cover_url = cover_url  # type: str
        self.create_time = create_time  # type: str
        self.deleted = deleted  # type: bool
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.glb_model_url = glb_model_url  # type: str
        self.model_url = model_url  # type: str
        self.modified_time = modified_time  # type: str
        self.origin_result_url = origin_result_url  # type: str
        self.oss_key = oss_key  # type: str
        self.pose_url = pose_url  # type: str
        self.preview_url = preview_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryAvatarProjectDetailResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.glb_model_url is not None:
            result['GlbModelUrl'] = self.glb_model_url
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.origin_result_url is not None:
            result['OriginResultUrl'] = self.origin_result_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.pose_url is not None:
            result['PoseUrl'] = self.pose_url
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GlbModelUrl') is not None:
            self.glb_model_url = m.get('GlbModelUrl')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OriginResultUrl') is not None:
            self.origin_result_url = m.get('OriginResultUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PoseUrl') is not None:
            self.pose_url = m.get('PoseUrl')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PopQueryAvatarProjectDetailResponseBodyData(TeaModel):
    def __init__(self, auto_build=None, biz_usage=None, build_detail=None, check_status=None, create_mode=None,
                 create_time=None, dataset=None, deleted=None, dependencies=None, ext=None, id=None, intro=None,
                 material_cover_url=None, modified_time=None, status=None, title=None, type=None):
        self.auto_build = auto_build  # type: bool
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopQueryAvatarProjectDetailResponseBodyDataBuildDetail
        self.check_status = check_status  # type: str
        self.create_mode = create_mode  # type: str
        self.create_time = create_time  # type: str
        self.dataset = dataset  # type: PopQueryAvatarProjectDetailResponseBodyDataDataset
        self.deleted = deleted  # type: bool
        self.dependencies = dependencies  # type: str
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopQueryAvatarProjectDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopQueryAvatarProjectDetailResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopQueryAvatarProjectDetailResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopQueryAvatarProjectDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopQueryAvatarProjectDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopQueryAvatarProjectDetailResponseBody, self).to_map()
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
            temp_model = PopQueryAvatarProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopQueryAvatarProjectDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopQueryAvatarProjectDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopQueryAvatarProjectDetailResponse, self).to_map()
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
            temp_model = PopQueryAvatarProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopQueryLatestAvatarProjectDetailByUserRequest(TeaModel):
    def __init__(self, jwt_token=None):
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryLatestAvatarProjectDetailByUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class PopQueryLatestAvatarProjectDetailByUserResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, running_time=None, status=None):
        self.running_time = running_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryLatestAvatarProjectDetailByUserResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PopQueryLatestAvatarProjectDetailByUserResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, error_code=None, error_message=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryLatestAvatarProjectDetailByUserResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class PopQueryLatestAvatarProjectDetailByUserResponseBodyData(TeaModel):
    def __init__(self, biz_usage=None, build_detail=None, create_time=None, dataset=None, ext=None, id=None,
                 intro=None, status=None, title=None):
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopQueryLatestAvatarProjectDetailByUserResponseBodyDataBuildDetail
        self.create_time = create_time  # type: str
        self.dataset = dataset  # type: PopQueryLatestAvatarProjectDetailByUserResponseBodyDataDataset
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopQueryLatestAvatarProjectDetailByUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopQueryLatestAvatarProjectDetailByUserResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dataset') is not None:
            temp_model = PopQueryLatestAvatarProjectDetailByUserResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopQueryLatestAvatarProjectDetailByUserResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopQueryLatestAvatarProjectDetailByUserResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopQueryLatestAvatarProjectDetailByUserResponseBody, self).to_map()
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
            temp_model = PopQueryLatestAvatarProjectDetailByUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopQueryLatestAvatarProjectDetailByUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopQueryLatestAvatarProjectDetailByUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopQueryLatestAvatarProjectDetailByUserResponse, self).to_map()
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
            temp_model = PopQueryLatestAvatarProjectDetailByUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopQueryLivePortraitModelScopeProjectDetailRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryLivePortraitModelScopeProjectDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopQueryLivePortraitModelScopeProjectDetailResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None, error_code=None, error_message=None):
        self.build_result_url = build_result_url  # type: dict[str, any]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryLivePortraitModelScopeProjectDetailResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class PopQueryLivePortraitModelScopeProjectDetailResponseBodyData(TeaModel):
    def __init__(self, biz_usage=None, dataset=None, ext=None, id=None, intro=None, material_cover_url=None,
                 status=None, title=None, type=None):
        self.biz_usage = biz_usage  # type: str
        self.dataset = dataset  # type: PopQueryLivePortraitModelScopeProjectDetailResponseBodyDataDataset
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.material_cover_url = material_cover_url  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopQueryLivePortraitModelScopeProjectDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.material_cover_url is not None:
            result['MaterialCoverUrl'] = self.material_cover_url
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('Dataset') is not None:
            temp_model = PopQueryLivePortraitModelScopeProjectDetailResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('MaterialCoverUrl') is not None:
            self.material_cover_url = m.get('MaterialCoverUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PopQueryLivePortraitModelScopeProjectDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopQueryLivePortraitModelScopeProjectDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopQueryLivePortraitModelScopeProjectDetailResponseBody, self).to_map()
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
            temp_model = PopQueryLivePortraitModelScopeProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopQueryLivePortraitModelScopeProjectDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopQueryLivePortraitModelScopeProjectDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopQueryLivePortraitModelScopeProjectDetailResponse, self).to_map()
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
            temp_model = PopQueryLivePortraitModelScopeProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopQueryObjectGenerationProjectDetailRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryObjectGenerationProjectDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopQueryObjectGenerationProjectDetailResponseBodyDataBuildDetail(TeaModel):
    def __init__(self, completed_time=None, error_message=None, estimated_duration=None, running_time=None,
                 submit_time=None):
        self.completed_time = completed_time  # type: str
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: long
        self.running_time = running_time  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryObjectGenerationProjectDetailResponseBodyDataBuildDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class PopQueryObjectGenerationProjectDetailResponseBodyDataDataset(TeaModel):
    def __init__(self, build_result_url=None):
        self.build_result_url = build_result_url  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopQueryObjectGenerationProjectDetailResponseBodyDataDataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_result_url is not None:
            result['BuildResultUrl'] = self.build_result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildResultUrl') is not None:
            self.build_result_url = m.get('BuildResultUrl')
        return self


class PopQueryObjectGenerationProjectDetailResponseBodyData(TeaModel):
    def __init__(self, biz_usage=None, build_detail=None, dataset=None, ext=None, id=None, intro=None, status=None,
                 title=None):
        self.biz_usage = biz_usage  # type: str
        self.build_detail = build_detail  # type: PopQueryObjectGenerationProjectDetailResponseBodyDataBuildDetail
        self.dataset = dataset  # type: PopQueryObjectGenerationProjectDetailResponseBodyDataDataset
        self.ext = ext  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.build_detail:
            self.build_detail.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(PopQueryObjectGenerationProjectDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_usage is not None:
            result['BizUsage'] = self.biz_usage
        if self.build_detail is not None:
            result['BuildDetail'] = self.build_detail.to_map()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizUsage') is not None:
            self.biz_usage = m.get('BizUsage')
        if m.get('BuildDetail') is not None:
            temp_model = PopQueryObjectGenerationProjectDetailResponseBodyDataBuildDetail()
            self.build_detail = temp_model.from_map(m['BuildDetail'])
        if m.get('Dataset') is not None:
            temp_model = PopQueryObjectGenerationProjectDetailResponseBodyDataDataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PopQueryObjectGenerationProjectDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopQueryObjectGenerationProjectDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopQueryObjectGenerationProjectDetailResponseBody, self).to_map()
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
            temp_model = PopQueryObjectGenerationProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopQueryObjectGenerationProjectDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopQueryObjectGenerationProjectDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopQueryObjectGenerationProjectDetailResponse, self).to_map()
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
            temp_model = PopQueryObjectGenerationProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopRetryAITryOnTaskRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopRetryAITryOnTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopRetryAITryOnTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopRetryAITryOnTaskResponseBody, self).to_map()
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


class PopRetryAITryOnTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopRetryAITryOnTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopRetryAITryOnTaskResponse, self).to_map()
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
            temp_model = PopRetryAITryOnTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopSubmitAITryOnJobRequest(TeaModel):
    def __init__(self, bottoms_id=None, clothing_type=None, jwt_token=None, model_id=None, shoe_type=None,
                 suit_id=None, tops_id=None):
        self.bottoms_id = bottoms_id  # type: str
        self.clothing_type = clothing_type  # type: str
        self.jwt_token = jwt_token  # type: str
        self.model_id = model_id  # type: str
        self.shoe_type = shoe_type  # type: str
        self.suit_id = suit_id  # type: str
        self.tops_id = tops_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopSubmitAITryOnJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bottoms_id is not None:
            result['BottomsId'] = self.bottoms_id
        if self.clothing_type is not None:
            result['ClothingType'] = self.clothing_type
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.shoe_type is not None:
            result['ShoeType'] = self.shoe_type
        if self.suit_id is not None:
            result['SuitId'] = self.suit_id
        if self.tops_id is not None:
            result['TopsId'] = self.tops_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BottomsId') is not None:
            self.bottoms_id = m.get('BottomsId')
        if m.get('ClothingType') is not None:
            self.clothing_type = m.get('ClothingType')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ShoeType') is not None:
            self.shoe_type = m.get('ShoeType')
        if m.get('SuitId') is not None:
            self.suit_id = m.get('SuitId')
        if m.get('TopsId') is not None:
            self.tops_id = m.get('TopsId')
        return self


class PopSubmitAITryOnJobResponseBodyData(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopSubmitAITryOnJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PopSubmitAITryOnJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopSubmitAITryOnJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopSubmitAITryOnJobResponseBody, self).to_map()
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
            temp_model = PopSubmitAITryOnJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopSubmitAITryOnJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopSubmitAITryOnJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopSubmitAITryOnJobResponse, self).to_map()
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
            temp_model = PopSubmitAITryOnJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopUploadMaterialRequest(TeaModel):
    def __init__(self, jwt_token=None):
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopUploadMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class PopUploadMaterialResponseBodyDataPolicy(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopUploadMaterialResponseBodyDataPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class PopUploadMaterialResponseBodyData(TeaModel):
    def __init__(self, oss_key=None, policy=None):
        self.oss_key = oss_key  # type: str
        self.policy = policy  # type: PopUploadMaterialResponseBodyDataPolicy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(PopUploadMaterialResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Policy') is not None:
            temp_model = PopUploadMaterialResponseBodyDataPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class PopUploadMaterialResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PopUploadMaterialResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PopUploadMaterialResponseBody, self).to_map()
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
            temp_model = PopUploadMaterialResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopUploadMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopUploadMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopUploadMaterialResponse, self).to_map()
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
            temp_model = PopUploadMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PopVideoSaveSourceRequest(TeaModel):
    def __init__(self, jwt_token=None, project_id=None, source_type=None):
        self.jwt_token = jwt_token  # type: str
        self.project_id = project_id  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopVideoSaveSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class PopVideoSaveSourceResponseBody(TeaModel):
    def __init__(self, code=None, error_name=None, http_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PopVideoSaveSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PopVideoSaveSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PopVideoSaveSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PopVideoSaveSourceResponse, self).to_map()
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
            temp_model = PopVideoSaveSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDigitalHumanProjectRequest(TeaModel):
    def __init__(self, ids=None, jwt_token=None):
        self.ids = ids  # type: str
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDigitalHumanProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class QueryDigitalHumanProjectResponseBodyData(TeaModel):
    def __init__(self, error_code=None, error_message=None, estimated_duration=None, file_url=None, id=None,
                 intro=None, running_time=None, status=None, subtitle_url=None, title=None, video_length=None,
                 waiting_time=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.estimated_duration = estimated_duration  # type: int
        self.file_url = file_url  # type: str
        self.id = id  # type: str
        self.intro = intro  # type: str
        self.running_time = running_time  # type: str
        self.status = status  # type: str
        self.subtitle_url = subtitle_url  # type: str
        self.title = title  # type: str
        self.video_length = video_length  # type: int
        self.waiting_time = waiting_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDigitalHumanProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.estimated_duration is not None:
            result['EstimatedDuration'] = self.estimated_duration
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.intro is not None:
            result['Intro'] = self.intro
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.subtitle_url is not None:
            result['SubtitleUrl'] = self.subtitle_url
        if self.title is not None:
            result['Title'] = self.title
        if self.video_length is not None:
            result['VideoLength'] = self.video_length
        if self.waiting_time is not None:
            result['WaitingTime'] = self.waiting_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EstimatedDuration') is not None:
            self.estimated_duration = m.get('EstimatedDuration')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubtitleUrl') is not None:
            self.subtitle_url = m.get('SubtitleUrl')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoLength') is not None:
            self.video_length = m.get('VideoLength')
        if m.get('WaitingTime') is not None:
            self.waiting_time = m.get('WaitingTime')
        return self


class QueryDigitalHumanProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[QueryDigitalHumanProjectResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDigitalHumanProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDigitalHumanProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDigitalHumanProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDigitalHumanProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDigitalHumanProjectResponse, self).to_map()
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
            temp_model = QueryDigitalHumanProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLongTtsResultRequest(TeaModel):
    def __init__(self, job_id=None, jwt_token=None):
        self.job_id = job_id  # type: str
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLongTtsResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class QueryLongTtsResultResponseBodyData(TeaModel):
    def __init__(self, audio_url=None, duration=None, status=None):
        self.audio_url = audio_url  # type: str
        self.duration = duration  # type: float
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLongTtsResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryLongTtsResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryLongTtsResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryLongTtsResultResponseBody, self).to_map()
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
            temp_model = QueryLongTtsResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLongTtsResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryLongTtsResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryLongTtsResultResponse, self).to_map()
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
            temp_model = QueryLongTtsResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitLongTtsTaskRequest(TeaModel):
    def __init__(self, content=None, jwt_token=None, tts_voice_id=None):
        self.content = content  # type: str
        self.jwt_token = jwt_token  # type: str
        self.tts_voice_id = tts_voice_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitLongTtsTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        if self.tts_voice_id is not None:
            result['TtsVoiceId'] = self.tts_voice_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        if m.get('TtsVoiceId') is not None:
            self.tts_voice_id = m.get('TtsVoiceId')
        return self


class SubmitLongTtsTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitLongTtsTaskResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitLongTtsTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitLongTtsTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitLongTtsTaskResponse, self).to_map()
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
            temp_model = SubmitLongTtsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserEmailRequest(TeaModel):
    def __init__(self, email=None, jwt_token=None):
        self.email = email  # type: str
        self.jwt_token = jwt_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class UpdateUserEmailResponseBody(TeaModel):
    def __init__(self, code=None, error_name=None, http_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_name = error_name  # type: str
        self.http_code = http_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserEmailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserEmailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserEmailResponse, self).to_map()
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
            temp_model = UpdateUserEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


