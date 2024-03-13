# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AbstractEcommerceVideoRequest(TeaModel):
    def __init__(self, duration=None, height=None, video_url=None, width=None):
        self.duration = duration  # type: float
        self.height = height  # type: int
        self.video_url = video_url  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbstractEcommerceVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.height is not None:
            result['Height'] = self.height
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class AbstractEcommerceVideoAdvanceRequest(TeaModel):
    def __init__(self, duration=None, height=None, video_url_object=None, width=None):
        self.duration = duration  # type: float
        self.height = height  # type: int
        self.video_url_object = video_url_object  # type: READABLE
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbstractEcommerceVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.height is not None:
            result['Height'] = self.height
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class AbstractEcommerceVideoResponseBodyData(TeaModel):
    def __init__(self, video_cover_url=None, video_url=None):
        self.video_cover_url = video_cover_url  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbstractEcommerceVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoCoverUrl') is not None:
            self.video_cover_url = m.get('VideoCoverUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AbstractEcommerceVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: AbstractEcommerceVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AbstractEcommerceVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AbstractEcommerceVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbstractEcommerceVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AbstractEcommerceVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AbstractEcommerceVideoResponse, self).to_map()
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
            temp_model = AbstractEcommerceVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbstractFilmVideoRequest(TeaModel):
    def __init__(self, length=None, video_url=None):
        self.length = length  # type: int
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbstractFilmVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.length is not None:
            result['Length'] = self.length
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AbstractFilmVideoAdvanceRequest(TeaModel):
    def __init__(self, length=None, video_url_object=None):
        self.length = length  # type: int
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbstractFilmVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.length is not None:
            result['Length'] = self.length
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class AbstractFilmVideoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbstractFilmVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AbstractFilmVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: AbstractFilmVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AbstractFilmVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AbstractFilmVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbstractFilmVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AbstractFilmVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AbstractFilmVideoResponse, self).to_map()
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
            temp_model = AbstractFilmVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceVideoTemplateRequest(TeaModel):
    def __init__(self, video_scene=None, video_url=None):
        self.video_scene = video_scene  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceVideoTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_scene is not None:
            result['VideoScene'] = self.video_scene
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoScene') is not None:
            self.video_scene = m.get('VideoScene')
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class AddFaceVideoTemplateAdvanceRequest(TeaModel):
    def __init__(self, video_scene=None, video_urlobject=None):
        self.video_scene = video_scene  # type: str
        self.video_urlobject = video_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceVideoTemplateAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_scene is not None:
            result['VideoScene'] = self.video_scene
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoScene') is not None:
            self.video_scene = m.get('VideoScene')
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        return self


class AddFaceVideoTemplateResponseBodyDateFaceInfos(TeaModel):
    def __init__(self, template_face_id=None, template_face_url=None):
        self.template_face_id = template_face_id  # type: str
        self.template_face_url = template_face_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceVideoTemplateResponseBodyDateFaceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        if self.template_face_url is not None:
            result['TemplateFaceURL'] = self.template_face_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        if m.get('TemplateFaceURL') is not None:
            self.template_face_url = m.get('TemplateFaceURL')
        return self


class AddFaceVideoTemplateResponseBodyDate(TeaModel):
    def __init__(self, face_infos=None, template_id=None):
        self.face_infos = face_infos  # type: list[AddFaceVideoTemplateResponseBodyDateFaceInfos]
        self.template_id = template_id  # type: str

    def validate(self):
        if self.face_infos:
            for k in self.face_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddFaceVideoTemplateResponseBodyDate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaceInfos'] = []
        if self.face_infos is not None:
            for k in self.face_infos:
                result['FaceInfos'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.face_infos = []
        if m.get('FaceInfos') is not None:
            for k in m.get('FaceInfos'):
                temp_model = AddFaceVideoTemplateResponseBodyDateFaceInfos()
                self.face_infos.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class AddFaceVideoTemplateResponseBody(TeaModel):
    def __init__(self, date=None, message=None, request_id=None):
        self.date = date  # type: AddFaceVideoTemplateResponseBodyDate
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super(AddFaceVideoTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            temp_model = AddFaceVideoTemplateResponseBodyDate()
            self.date = temp_model.from_map(m['Date'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddFaceVideoTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceVideoTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceVideoTemplateResponse, self).to_map()
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
            temp_model = AddFaceVideoTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AdjustVideoColorRequest(TeaModel):
    def __init__(self, mode=None, video_bitrate=None, video_codec=None, video_format=None, video_url=None):
        self.mode = mode  # type: str
        self.video_bitrate = video_bitrate  # type: long
        self.video_codec = video_codec  # type: str
        self.video_format = video_format  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdjustVideoColorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AdjustVideoColorAdvanceRequest(TeaModel):
    def __init__(self, mode=None, video_bitrate=None, video_codec=None, video_format=None, video_url_object=None):
        self.mode = mode  # type: str
        self.video_bitrate = video_bitrate  # type: long
        self.video_codec = video_codec  # type: str
        self.video_format = video_format  # type: str
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdjustVideoColorAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class AdjustVideoColorResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdjustVideoColorResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AdjustVideoColorResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: AdjustVideoColorResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AdjustVideoColorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AdjustVideoColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AdjustVideoColorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AdjustVideoColorResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AdjustVideoColorResponse, self).to_map()
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
            temp_model = AdjustVideoColorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeVideoSizeRequest(TeaModel):
    def __init__(self, b=None, crop_type=None, fill_type=None, g=None, height=None, r=None, tightness=None,
                 video_url=None, width=None):
        self.b = b  # type: int
        self.crop_type = crop_type  # type: str
        self.fill_type = fill_type  # type: str
        self.g = g  # type: int
        self.height = height  # type: int
        self.r = r  # type: int
        self.tightness = tightness  # type: float
        self.video_url = video_url  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeVideoSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.b is not None:
            result['B'] = self.b
        if self.crop_type is not None:
            result['CropType'] = self.crop_type
        if self.fill_type is not None:
            result['FillType'] = self.fill_type
        if self.g is not None:
            result['G'] = self.g
        if self.height is not None:
            result['Height'] = self.height
        if self.r is not None:
            result['R'] = self.r
        if self.tightness is not None:
            result['Tightness'] = self.tightness
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')
        if m.get('CropType') is not None:
            self.crop_type = m.get('CropType')
        if m.get('FillType') is not None:
            self.fill_type = m.get('FillType')
        if m.get('G') is not None:
            self.g = m.get('G')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('R') is not None:
            self.r = m.get('R')
        if m.get('Tightness') is not None:
            self.tightness = m.get('Tightness')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ChangeVideoSizeAdvanceRequest(TeaModel):
    def __init__(self, b=None, crop_type=None, fill_type=None, g=None, height=None, r=None, tightness=None,
                 video_url_object=None, width=None):
        self.b = b  # type: int
        self.crop_type = crop_type  # type: str
        self.fill_type = fill_type  # type: str
        self.g = g  # type: int
        self.height = height  # type: int
        self.r = r  # type: int
        self.tightness = tightness  # type: float
        self.video_url_object = video_url_object  # type: READABLE
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeVideoSizeAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.b is not None:
            result['B'] = self.b
        if self.crop_type is not None:
            result['CropType'] = self.crop_type
        if self.fill_type is not None:
            result['FillType'] = self.fill_type
        if self.g is not None:
            result['G'] = self.g
        if self.height is not None:
            result['Height'] = self.height
        if self.r is not None:
            result['R'] = self.r
        if self.tightness is not None:
            result['Tightness'] = self.tightness
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')
        if m.get('CropType') is not None:
            self.crop_type = m.get('CropType')
        if m.get('FillType') is not None:
            self.fill_type = m.get('FillType')
        if m.get('G') is not None:
            self.g = m.get('G')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('R') is not None:
            self.r = m.get('R')
        if m.get('Tightness') is not None:
            self.tightness = m.get('Tightness')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ChangeVideoSizeResponseBodyData(TeaModel):
    def __init__(self, video_cover_url=None, video_url=None):
        self.video_cover_url = video_cover_url  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeVideoSizeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoCoverUrl') is not None:
            self.video_cover_url = m.get('VideoCoverUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ChangeVideoSizeResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: ChangeVideoSizeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeVideoSizeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ChangeVideoSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeVideoSizeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeVideoSizeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeVideoSizeResponse, self).to_map()
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
            temp_model = ChangeVideoSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertHdrVideoRequest(TeaModel):
    def __init__(self, bitrate=None, hdrformat=None, max_illuminance=None, video_url=None):
        self.bitrate = bitrate  # type: int
        self.hdrformat = hdrformat  # type: str
        self.max_illuminance = max_illuminance  # type: int
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertHdrVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class ConvertHdrVideoAdvanceRequest(TeaModel):
    def __init__(self, bitrate=None, hdrformat=None, max_illuminance=None, video_urlobject=None):
        self.bitrate = bitrate  # type: int
        self.hdrformat = hdrformat  # type: str
        self.max_illuminance = max_illuminance  # type: int
        self.video_urlobject = video_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertHdrVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        return self


class ConvertHdrVideoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertHdrVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class ConvertHdrVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: ConvertHdrVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ConvertHdrVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ConvertHdrVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConvertHdrVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConvertHdrVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConvertHdrVideoResponse, self).to_map()
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
            temp_model = ConvertHdrVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceVideoTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceVideoTemplateRequest, self).to_map()
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


class DeleteFaceVideoTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceVideoTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFaceVideoTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFaceVideoTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFaceVideoTemplateResponse, self).to_map()
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
            temp_model = DeleteFaceVideoTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhancePortraitVideoRequest(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhancePortraitVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EnhancePortraitVideoAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None):
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhancePortraitVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class EnhancePortraitVideoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhancePortraitVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EnhancePortraitVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: EnhancePortraitVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EnhancePortraitVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = EnhancePortraitVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnhancePortraitVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnhancePortraitVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnhancePortraitVideoResponse, self).to_map()
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
            temp_model = EnhancePortraitVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhanceVideoQualityRequest(TeaModel):
    def __init__(self, bitrate=None, frame_rate=None, hdrformat=None, max_illuminance=None, out_put_height=None,
                 out_put_width=None, video_url=None):
        self.bitrate = bitrate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.hdrformat = hdrformat  # type: str
        self.max_illuminance = max_illuminance  # type: int
        self.out_put_height = out_put_height  # type: int
        self.out_put_width = out_put_width  # type: int
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhanceVideoQualityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.out_put_height is not None:
            result['OutPutHeight'] = self.out_put_height
        if self.out_put_width is not None:
            result['OutPutWidth'] = self.out_put_width
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('OutPutHeight') is not None:
            self.out_put_height = m.get('OutPutHeight')
        if m.get('OutPutWidth') is not None:
            self.out_put_width = m.get('OutPutWidth')
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class EnhanceVideoQualityAdvanceRequest(TeaModel):
    def __init__(self, bitrate=None, frame_rate=None, hdrformat=None, max_illuminance=None, out_put_height=None,
                 out_put_width=None, video_urlobject=None):
        self.bitrate = bitrate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.hdrformat = hdrformat  # type: str
        self.max_illuminance = max_illuminance  # type: int
        self.out_put_height = out_put_height  # type: int
        self.out_put_width = out_put_width  # type: int
        self.video_urlobject = video_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhanceVideoQualityAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.out_put_height is not None:
            result['OutPutHeight'] = self.out_put_height
        if self.out_put_width is not None:
            result['OutPutWidth'] = self.out_put_width
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('OutPutHeight') is not None:
            self.out_put_height = m.get('OutPutHeight')
        if m.get('OutPutWidth') is not None:
            self.out_put_width = m.get('OutPutWidth')
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        return self


class EnhanceVideoQualityResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhanceVideoQualityResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class EnhanceVideoQualityResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: EnhanceVideoQualityResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EnhanceVideoQualityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = EnhanceVideoQualityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnhanceVideoQualityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnhanceVideoQualityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnhanceVideoQualityResponse, self).to_map()
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
            temp_model = EnhanceVideoQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EraseVideoLogoRequestBoxes(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h  # type: float
        self.w = w  # type: float
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseVideoLogoRequestBoxes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class EraseVideoLogoRequest(TeaModel):
    def __init__(self, boxes=None, video_url=None):
        self.boxes = boxes  # type: list[EraseVideoLogoRequestBoxes]
        self.video_url = video_url  # type: str

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EraseVideoLogoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = EraseVideoLogoRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseVideoLogoAdvanceRequestBoxes(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h  # type: float
        self.w = w  # type: float
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseVideoLogoAdvanceRequestBoxes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class EraseVideoLogoAdvanceRequest(TeaModel):
    def __init__(self, boxes=None, video_url_object=None):
        self.boxes = boxes  # type: list[EraseVideoLogoAdvanceRequestBoxes]
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EraseVideoLogoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = EraseVideoLogoAdvanceRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class EraseVideoLogoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseVideoLogoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseVideoLogoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: EraseVideoLogoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EraseVideoLogoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = EraseVideoLogoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EraseVideoLogoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EraseVideoLogoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EraseVideoLogoResponse, self).to_map()
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
            temp_model = EraseVideoLogoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EraseVideoSubtitlesRequest(TeaModel):
    def __init__(self, bh=None, bw=None, bx=None, by=None, video_url=None):
        self.bh = bh  # type: float
        self.bw = bw  # type: float
        self.bx = bx  # type: float
        self.by = by  # type: float
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseVideoSubtitlesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bh is not None:
            result['BH'] = self.bh
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseVideoSubtitlesAdvanceRequest(TeaModel):
    def __init__(self, bh=None, bw=None, bx=None, by=None, video_url_object=None):
        self.bh = bh  # type: float
        self.bw = bw  # type: float
        self.bx = bx  # type: float
        self.by = by  # type: float
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseVideoSubtitlesAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bh is not None:
            result['BH'] = self.bh
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class EraseVideoSubtitlesResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseVideoSubtitlesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseVideoSubtitlesResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: EraseVideoSubtitlesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EraseVideoSubtitlesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = EraseVideoSubtitlesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EraseVideoSubtitlesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EraseVideoSubtitlesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EraseVideoSubtitlesResponse, self).to_map()
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
            temp_model = EraseVideoSubtitlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateHumanAnimeStyleVideoRequest(TeaModel):
    def __init__(self, cartoon_style=None, video_url=None):
        self.cartoon_style = cartoon_style  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateHumanAnimeStyleVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cartoon_style is not None:
            result['CartoonStyle'] = self.cartoon_style
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CartoonStyle') is not None:
            self.cartoon_style = m.get('CartoonStyle')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GenerateHumanAnimeStyleVideoAdvanceRequest(TeaModel):
    def __init__(self, cartoon_style=None, video_url_object=None):
        self.cartoon_style = cartoon_style  # type: str
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateHumanAnimeStyleVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cartoon_style is not None:
            result['CartoonStyle'] = self.cartoon_style
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CartoonStyle') is not None:
            self.cartoon_style = m.get('CartoonStyle')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class GenerateHumanAnimeStyleVideoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateHumanAnimeStyleVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GenerateHumanAnimeStyleVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateHumanAnimeStyleVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateHumanAnimeStyleVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateHumanAnimeStyleVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateHumanAnimeStyleVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateHumanAnimeStyleVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateHumanAnimeStyleVideoResponse, self).to_map()
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
            temp_model = GenerateHumanAnimeStyleVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVideoRequestFileList(TeaModel):
    def __init__(self, file_name=None, file_url=None, type=None):
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoRequestFileList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GenerateVideoRequest(TeaModel):
    def __init__(self, duration=None, duration_adaption=None, file_list=None, height=None, mute=None,
                 puzzle_effect=None, scene=None, smart_effect=None, style=None, transition_style=None, width=None):
        self.duration = duration  # type: float
        self.duration_adaption = duration_adaption  # type: bool
        # 1
        self.file_list = file_list  # type: list[GenerateVideoRequestFileList]
        self.height = height  # type: int
        self.mute = mute  # type: bool
        self.puzzle_effect = puzzle_effect  # type: bool
        self.scene = scene  # type: str
        self.smart_effect = smart_effect  # type: bool
        self.style = style  # type: str
        self.transition_style = transition_style  # type: str
        self.width = width  # type: int

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.duration_adaption is not None:
            result['DurationAdaption'] = self.duration_adaption
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.puzzle_effect is not None:
            result['PuzzleEffect'] = self.puzzle_effect
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.smart_effect is not None:
            result['SmartEffect'] = self.smart_effect
        if self.style is not None:
            result['Style'] = self.style
        if self.transition_style is not None:
            result['TransitionStyle'] = self.transition_style
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DurationAdaption') is not None:
            self.duration_adaption = m.get('DurationAdaption')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = GenerateVideoRequestFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('PuzzleEffect') is not None:
            self.puzzle_effect = m.get('PuzzleEffect')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SmartEffect') is not None:
            self.smart_effect = m.get('SmartEffect')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('TransitionStyle') is not None:
            self.transition_style = m.get('TransitionStyle')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GenerateVideoAdvanceRequestFileList(TeaModel):
    def __init__(self, file_name=None, file_url_object=None, type=None):
        self.file_name = file_name  # type: str
        self.file_url_object = file_url_object  # type: READABLE
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoAdvanceRequestFileList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GenerateVideoAdvanceRequest(TeaModel):
    def __init__(self, duration=None, duration_adaption=None, file_list=None, height=None, mute=None,
                 puzzle_effect=None, scene=None, smart_effect=None, style=None, transition_style=None, width=None):
        self.duration = duration  # type: float
        self.duration_adaption = duration_adaption  # type: bool
        # 1
        self.file_list = file_list  # type: list[GenerateVideoAdvanceRequestFileList]
        self.height = height  # type: int
        self.mute = mute  # type: bool
        self.puzzle_effect = puzzle_effect  # type: bool
        self.scene = scene  # type: str
        self.smart_effect = smart_effect  # type: bool
        self.style = style  # type: str
        self.transition_style = transition_style  # type: str
        self.width = width  # type: int

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.duration_adaption is not None:
            result['DurationAdaption'] = self.duration_adaption
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.puzzle_effect is not None:
            result['PuzzleEffect'] = self.puzzle_effect
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.smart_effect is not None:
            result['SmartEffect'] = self.smart_effect
        if self.style is not None:
            result['Style'] = self.style
        if self.transition_style is not None:
            result['TransitionStyle'] = self.transition_style
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DurationAdaption') is not None:
            self.duration_adaption = m.get('DurationAdaption')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = GenerateVideoAdvanceRequestFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('PuzzleEffect') is not None:
            self.puzzle_effect = m.get('PuzzleEffect')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SmartEffect') is not None:
            self.smart_effect = m.get('SmartEffect')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('TransitionStyle') is not None:
            self.transition_style = m.get('TransitionStyle')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GenerateVideoResponseBodyData(TeaModel):
    def __init__(self, video_cover_url=None, video_url=None):
        self.video_cover_url = video_cover_url  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoCoverUrl') is not None:
            self.video_cover_url = m.get('VideoCoverUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GenerateVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateVideoResponse, self).to_map()
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
            temp_model = GenerateVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncJobResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(self, error_code=None, error_message=None, job_id=None, result=None, status=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.job_id = job_id  # type: str
        self.result = result  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncJobResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetAsyncJobResultResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAsyncJobResultResponseBody, self).to_map()
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
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAsyncJobResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncJobResultResponse, self).to_map()
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InterpolateVideoFrameRequest(TeaModel):
    def __init__(self, bitrate=None, frame_rate=None, video_url=None):
        self.bitrate = bitrate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InterpolateVideoFrameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class InterpolateVideoFrameAdvanceRequest(TeaModel):
    def __init__(self, bitrate=None, frame_rate=None, video_urlobject=None):
        self.bitrate = bitrate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.video_urlobject = video_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(InterpolateVideoFrameAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        return self


class InterpolateVideoFrameResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InterpolateVideoFrameResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class InterpolateVideoFrameResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: InterpolateVideoFrameResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InterpolateVideoFrameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = InterpolateVideoFrameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InterpolateVideoFrameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InterpolateVideoFrameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InterpolateVideoFrameResponse, self).to_map()
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
            temp_model = InterpolateVideoFrameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeVideoFaceRequest(TeaModel):
    def __init__(self, add_watermark=None, enhance=None, reference_url=None, video_url=None, watermark_type=None):
        self.add_watermark = add_watermark  # type: bool
        self.enhance = enhance  # type: bool
        self.reference_url = reference_url  # type: str
        self.video_url = video_url  # type: str
        self.watermark_type = watermark_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeVideoFaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_watermark is not None:
            result['AddWatermark'] = self.add_watermark
        if self.enhance is not None:
            result['Enhance'] = self.enhance
        if self.reference_url is not None:
            result['ReferenceURL'] = self.reference_url
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddWatermark') is not None:
            self.add_watermark = m.get('AddWatermark')
        if m.get('Enhance') is not None:
            self.enhance = m.get('Enhance')
        if m.get('ReferenceURL') is not None:
            self.reference_url = m.get('ReferenceURL')
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class MergeVideoFaceAdvanceRequest(TeaModel):
    def __init__(self, add_watermark=None, enhance=None, reference_urlobject=None, video_urlobject=None,
                 watermark_type=None):
        self.add_watermark = add_watermark  # type: bool
        self.enhance = enhance  # type: bool
        self.reference_urlobject = reference_urlobject  # type: READABLE
        self.video_urlobject = video_urlobject  # type: READABLE
        self.watermark_type = watermark_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeVideoFaceAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_watermark is not None:
            result['AddWatermark'] = self.add_watermark
        if self.enhance is not None:
            result['Enhance'] = self.enhance
        if self.reference_urlobject is not None:
            result['ReferenceURL'] = self.reference_urlobject
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddWatermark') is not None:
            self.add_watermark = m.get('AddWatermark')
        if m.get('Enhance') is not None:
            self.enhance = m.get('Enhance')
        if m.get('ReferenceURL') is not None:
            self.reference_urlobject = m.get('ReferenceURL')
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class MergeVideoFaceResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeVideoFaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class MergeVideoFaceResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: MergeVideoFaceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MergeVideoFaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = MergeVideoFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MergeVideoFaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MergeVideoFaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MergeVideoFaceResponse, self).to_map()
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
            temp_model = MergeVideoFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeVideoModelFaceRequestMergeInfos(TeaModel):
    def __init__(self, image_url=None, template_face_id=None, template_face_url=None):
        self.image_url = image_url  # type: str
        self.template_face_id = template_face_id  # type: str
        self.template_face_url = template_face_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeVideoModelFaceRequestMergeInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        if self.template_face_url is not None:
            result['TemplateFaceURL'] = self.template_face_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        if m.get('TemplateFaceURL') is not None:
            self.template_face_url = m.get('TemplateFaceURL')
        return self


class MergeVideoModelFaceRequest(TeaModel):
    def __init__(self, add_watermark=None, enhance=None, face_image_url=None, merge_infos=None, template_id=None,
                 watermark_type=None):
        self.add_watermark = add_watermark  # type: bool
        self.enhance = enhance  # type: bool
        self.face_image_url = face_image_url  # type: str
        self.merge_infos = merge_infos  # type: list[MergeVideoModelFaceRequestMergeInfos]
        self.template_id = template_id  # type: str
        self.watermark_type = watermark_type  # type: str

    def validate(self):
        if self.merge_infos:
            for k in self.merge_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MergeVideoModelFaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_watermark is not None:
            result['AddWatermark'] = self.add_watermark
        if self.enhance is not None:
            result['Enhance'] = self.enhance
        if self.face_image_url is not None:
            result['FaceImageURL'] = self.face_image_url
        result['MergeInfos'] = []
        if self.merge_infos is not None:
            for k in self.merge_infos:
                result['MergeInfos'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddWatermark') is not None:
            self.add_watermark = m.get('AddWatermark')
        if m.get('Enhance') is not None:
            self.enhance = m.get('Enhance')
        if m.get('FaceImageURL') is not None:
            self.face_image_url = m.get('FaceImageURL')
        self.merge_infos = []
        if m.get('MergeInfos') is not None:
            for k in m.get('MergeInfos'):
                temp_model = MergeVideoModelFaceRequestMergeInfos()
                self.merge_infos.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class MergeVideoModelFaceAdvanceRequestMergeInfos(TeaModel):
    def __init__(self, image_url=None, template_face_id=None, template_face_url=None):
        self.image_url = image_url  # type: str
        self.template_face_id = template_face_id  # type: str
        self.template_face_url = template_face_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeVideoModelFaceAdvanceRequestMergeInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        if self.template_face_url is not None:
            result['TemplateFaceURL'] = self.template_face_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        if m.get('TemplateFaceURL') is not None:
            self.template_face_url = m.get('TemplateFaceURL')
        return self


class MergeVideoModelFaceAdvanceRequest(TeaModel):
    def __init__(self, add_watermark=None, enhance=None, face_image_urlobject=None, merge_infos=None,
                 template_id=None, watermark_type=None):
        self.add_watermark = add_watermark  # type: bool
        self.enhance = enhance  # type: bool
        self.face_image_urlobject = face_image_urlobject  # type: READABLE
        self.merge_infos = merge_infos  # type: list[MergeVideoModelFaceAdvanceRequestMergeInfos]
        self.template_id = template_id  # type: str
        self.watermark_type = watermark_type  # type: str

    def validate(self):
        if self.merge_infos:
            for k in self.merge_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MergeVideoModelFaceAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_watermark is not None:
            result['AddWatermark'] = self.add_watermark
        if self.enhance is not None:
            result['Enhance'] = self.enhance
        if self.face_image_urlobject is not None:
            result['FaceImageURL'] = self.face_image_urlobject
        result['MergeInfos'] = []
        if self.merge_infos is not None:
            for k in self.merge_infos:
                result['MergeInfos'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddWatermark') is not None:
            self.add_watermark = m.get('AddWatermark')
        if m.get('Enhance') is not None:
            self.enhance = m.get('Enhance')
        if m.get('FaceImageURL') is not None:
            self.face_image_urlobject = m.get('FaceImageURL')
        self.merge_infos = []
        if m.get('MergeInfos') is not None:
            for k in m.get('MergeInfos'):
                temp_model = MergeVideoModelFaceAdvanceRequestMergeInfos()
                self.merge_infos.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class MergeVideoModelFaceResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeVideoModelFaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class MergeVideoModelFaceResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: MergeVideoModelFaceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MergeVideoModelFaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = MergeVideoModelFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MergeVideoModelFaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MergeVideoModelFaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MergeVideoModelFaceResponse, self).to_map()
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
            temp_model = MergeVideoModelFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceVideoTemplateRequest(TeaModel):
    def __init__(self, page_no=None, page_size=None, template_id=None):
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceVideoTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryFaceVideoTemplateResponseBodyDataElementsFaceInfos(TeaModel):
    def __init__(self, template_face_id=None, template_face_url=None):
        self.template_face_id = template_face_id  # type: str
        self.template_face_url = template_face_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceVideoTemplateResponseBodyDataElementsFaceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        if self.template_face_url is not None:
            result['TemplateFaceURL'] = self.template_face_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        if m.get('TemplateFaceURL') is not None:
            self.template_face_url = m.get('TemplateFaceURL')
        return self


class QueryFaceVideoTemplateResponseBodyDataElements(TeaModel):
    def __init__(self, create_time=None, face_infos=None, template_id=None, template_url=None, update_time=None,
                 user_id=None):
        self.create_time = create_time  # type: str
        self.face_infos = face_infos  # type: list[QueryFaceVideoTemplateResponseBodyDataElementsFaceInfos]
        self.template_id = template_id  # type: str
        self.template_url = template_url  # type: str
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.face_infos:
            for k in self.face_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceVideoTemplateResponseBodyDataElements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['FaceInfos'] = []
        if self.face_infos is not None:
            for k in self.face_infos:
                result['FaceInfos'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.face_infos = []
        if m.get('FaceInfos') is not None:
            for k in m.get('FaceInfos'):
                temp_model = QueryFaceVideoTemplateResponseBodyDataElementsFaceInfos()
                self.face_infos.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceVideoTemplateResponseBodyData(TeaModel):
    def __init__(self, elements=None, total=None):
        self.elements = elements  # type: list[QueryFaceVideoTemplateResponseBodyDataElements]
        self.total = total  # type: long

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceVideoTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = QueryFaceVideoTemplateResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceVideoTemplateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryFaceVideoTemplateResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceVideoTemplateResponseBody, self).to_map()
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
            temp_model = QueryFaceVideoTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryFaceVideoTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceVideoTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceVideoTemplateResponse, self).to_map()
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
            temp_model = QueryFaceVideoTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReduceVideoNoiseRequest(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReduceVideoNoiseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ReduceVideoNoiseAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None):
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReduceVideoNoiseAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class ReduceVideoNoiseResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReduceVideoNoiseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ReduceVideoNoiseResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: ReduceVideoNoiseResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ReduceVideoNoiseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ReduceVideoNoiseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReduceVideoNoiseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReduceVideoNoiseResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReduceVideoNoiseResponse, self).to_map()
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
            temp_model = ReduceVideoNoiseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuperResolveVideoRequest(TeaModel):
    def __init__(self, bit_rate=None, video_url=None):
        self.bit_rate = bit_rate  # type: int
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuperResolveVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class SuperResolveVideoAdvanceRequest(TeaModel):
    def __init__(self, bit_rate=None, video_url_object=None):
        self.bit_rate = bit_rate  # type: int
        self.video_url_object = video_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuperResolveVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class SuperResolveVideoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuperResolveVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class SuperResolveVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: SuperResolveVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SuperResolveVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SuperResolveVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SuperResolveVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SuperResolveVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SuperResolveVideoResponse, self).to_map()
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
            temp_model = SuperResolveVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ToneSdrVideoRequest(TeaModel):
    def __init__(self, bitrate=None, recolor_model=None, video_url=None):
        self.bitrate = bitrate  # type: int
        self.recolor_model = recolor_model  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ToneSdrVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.recolor_model is not None:
            result['RecolorModel'] = self.recolor_model
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('RecolorModel') is not None:
            self.recolor_model = m.get('RecolorModel')
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class ToneSdrVideoAdvanceRequest(TeaModel):
    def __init__(self, bitrate=None, recolor_model=None, video_urlobject=None):
        self.bitrate = bitrate  # type: int
        self.recolor_model = recolor_model  # type: str
        self.video_urlobject = video_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ToneSdrVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.recolor_model is not None:
            result['RecolorModel'] = self.recolor_model
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('RecolorModel') is not None:
            self.recolor_model = m.get('RecolorModel')
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        return self


class ToneSdrVideoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ToneSdrVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class ToneSdrVideoResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: ToneSdrVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ToneSdrVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ToneSdrVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ToneSdrVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ToneSdrVideoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ToneSdrVideoResponse, self).to_map()
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
            temp_model = ToneSdrVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


