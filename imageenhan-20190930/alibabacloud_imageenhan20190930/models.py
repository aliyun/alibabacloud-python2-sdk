# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AssessCompositionRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessCompositionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessCompositionAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessCompositionAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class AssessCompositionResponseBodyData(TeaModel):
    def __init__(self, score=None):
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessCompositionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class AssessCompositionResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AssessCompositionResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AssessCompositionResponseBody, self).to_map()
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
            temp_model = AssessCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssessCompositionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssessCompositionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssessCompositionResponse, self).to_map()
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
            temp_model = AssessCompositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssessExposureRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessExposureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessExposureAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessExposureAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class AssessExposureResponseBodyData(TeaModel):
    def __init__(self, exposure=None):
        self.exposure = exposure  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessExposureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        return self


class AssessExposureResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AssessExposureResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AssessExposureResponseBody, self).to_map()
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
            temp_model = AssessExposureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssessExposureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssessExposureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssessExposureResponse, self).to_map()
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
            temp_model = AssessExposureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssessSharpnessRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessSharpnessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessSharpnessAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessSharpnessAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class AssessSharpnessResponseBodyData(TeaModel):
    def __init__(self, sharpness=None):
        self.sharpness = sharpness  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssessSharpnessResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sharpness is not None:
            result['Sharpness'] = self.sharpness
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Sharpness') is not None:
            self.sharpness = m.get('Sharpness')
        return self


class AssessSharpnessResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AssessSharpnessResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AssessSharpnessResponseBody, self).to_map()
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
            temp_model = AssessSharpnessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssessSharpnessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssessSharpnessResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssessSharpnessResponse, self).to_map()
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
            temp_model = AssessSharpnessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeImageSizeRequest(TeaModel):
    def __init__(self, height=None, url=None, width=None):
        self.height = height  # type: int
        self.url = url  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeImageSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ChangeImageSizeAdvanceRequest(TeaModel):
    def __init__(self, height=None, url_object=None, width=None):
        self.height = height  # type: int
        self.url_object = url_object  # type: READABLE
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeImageSizeAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.url_object is not None:
            result['Url'] = self.url_object
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ChangeImageSizeResponseBodyDataRetainLocation(TeaModel):
    def __init__(self, height=None, width=None, x=None, y=None):
        self.height = height  # type: int
        self.width = width  # type: int
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeImageSizeResponseBodyDataRetainLocation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class ChangeImageSizeResponseBodyData(TeaModel):
    def __init__(self, retain_location=None, url=None):
        self.retain_location = retain_location  # type: ChangeImageSizeResponseBodyDataRetainLocation
        self.url = url  # type: str

    def validate(self):
        if self.retain_location:
            self.retain_location.validate()

    def to_map(self):
        _map = super(ChangeImageSizeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.retain_location is not None:
            result['RetainLocation'] = self.retain_location.to_map()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RetainLocation') is not None:
            temp_model = ChangeImageSizeResponseBodyDataRetainLocation()
            self.retain_location = temp_model.from_map(m['RetainLocation'])
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeImageSizeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ChangeImageSizeResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeImageSizeResponseBody, self).to_map()
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
            temp_model = ChangeImageSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeImageSizeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeImageSizeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeImageSizeResponse, self).to_map()
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
            temp_model = ChangeImageSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ColorizeImageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ColorizeImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ColorizeImageAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ColorizeImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class ColorizeImageResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ColorizeImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ColorizeImageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ColorizeImageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ColorizeImageResponseBody, self).to_map()
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
            temp_model = ColorizeImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ColorizeImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ColorizeImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ColorizeImageResponse, self).to_map()
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
            temp_model = ColorizeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhanceImageColorRequest(TeaModel):
    def __init__(self, image_url=None, mode=None, output_format=None):
        self.image_url = image_url  # type: str
        self.mode = mode  # type: str
        self.output_format = output_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhanceImageColorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        return self


class EnhanceImageColorAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, mode=None, output_format=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.mode = mode  # type: str
        self.output_format = output_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhanceImageColorAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        return self


class EnhanceImageColorResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnhanceImageColorResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class EnhanceImageColorResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: EnhanceImageColorResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EnhanceImageColorResponseBody, self).to_map()
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
            temp_model = EnhanceImageColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnhanceImageColorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnhanceImageColorResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnhanceImageColorResponse, self).to_map()
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
            temp_model = EnhanceImageColorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ErasePersonRequest(TeaModel):
    def __init__(self, image_url=None, user_mask=None):
        self.image_url = image_url  # type: str
        self.user_mask = user_mask  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ErasePersonRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.user_mask is not None:
            result['UserMask'] = self.user_mask
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('UserMask') is not None:
            self.user_mask = m.get('UserMask')
        return self


class ErasePersonAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, user_mask_object=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.user_mask_object = user_mask_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ErasePersonAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.user_mask_object is not None:
            result['UserMask'] = self.user_mask_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('UserMask') is not None:
            self.user_mask_object = m.get('UserMask')
        return self


class ErasePersonResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ErasePersonResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class ErasePersonResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ErasePersonResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ErasePersonResponseBody, self).to_map()
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
            temp_model = ErasePersonResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ErasePersonResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ErasePersonResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ErasePersonResponse, self).to_map()
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
            temp_model = ErasePersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtendImageStyleRequest(TeaModel):
    def __init__(self, major_url=None, style_url=None):
        self.major_url = major_url  # type: str
        self.style_url = style_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendImageStyleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        return self


class ExtendImageStyleAdvanceRequest(TeaModel):
    def __init__(self, major_url_object=None, style_url_object=None):
        self.major_url_object = major_url_object  # type: READABLE
        self.style_url_object = style_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendImageStyleAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.major_url_object is not None:
            result['MajorUrl'] = self.major_url_object
        if self.style_url_object is not None:
            result['StyleUrl'] = self.style_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MajorUrl') is not None:
            self.major_url_object = m.get('MajorUrl')
        if m.get('StyleUrl') is not None:
            self.style_url_object = m.get('StyleUrl')
        return self


class ExtendImageStyleResponseBodyData(TeaModel):
    def __init__(self, major_url=None, url=None):
        self.major_url = major_url  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendImageStyleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExtendImageStyleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ExtendImageStyleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExtendImageStyleResponseBody, self).to_map()
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
            temp_model = ExtendImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtendImageStyleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExtendImageStyleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtendImageStyleResponse, self).to_map()
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
            temp_model = ExtendImageStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCartoonizedImageRequest(TeaModel):
    def __init__(self, image_type=None, image_url=None, index=None):
        self.image_type = image_type  # type: str
        self.image_url = image_url  # type: str
        self.index = index  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateCartoonizedImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.index is not None:
            result['Index'] = self.index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        return self


class GenerateCartoonizedImageAdvanceRequest(TeaModel):
    def __init__(self, image_type=None, image_url_object=None, index=None):
        self.image_type = image_type  # type: str
        self.image_url_object = image_url_object  # type: READABLE
        self.index = index  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateCartoonizedImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.index is not None:
            result['Index'] = self.index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        return self


class GenerateCartoonizedImageResponseBodyData(TeaModel):
    def __init__(self, result_url=None):
        self.result_url = result_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateCartoonizedImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class GenerateCartoonizedImageResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateCartoonizedImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateCartoonizedImageResponseBody, self).to_map()
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
            temp_model = GenerateCartoonizedImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateCartoonizedImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateCartoonizedImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateCartoonizedImageResponse, self).to_map()
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
            temp_model = GenerateCartoonizedImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDynamicImageRequest(TeaModel):
    def __init__(self, operation=None, url=None):
        self.operation = operation  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDynamicImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GenerateDynamicImageAdvanceRequest(TeaModel):
    def __init__(self, operation=None, url_object=None):
        self.operation = operation  # type: str
        self.url_object = url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDynamicImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class GenerateDynamicImageResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDynamicImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GenerateDynamicImageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GenerateDynamicImageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateDynamicImageResponseBody, self).to_map()
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
            temp_model = GenerateDynamicImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateDynamicImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateDynamicImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateDynamicImageResponse, self).to_map()
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
            temp_model = GenerateDynamicImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateImageWithTextRequest(TeaModel):
    def __init__(self, number=None, resolution=None, text=None):
        self.number = number  # type: int
        self.resolution = resolution  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageWithTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GenerateImageWithTextResponseBodyData(TeaModel):
    def __init__(self, image_urls=None):
        self.image_urls = image_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageWithTextResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class GenerateImageWithTextResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateImageWithTextResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateImageWithTextResponseBody, self).to_map()
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
            temp_model = GenerateImageWithTextResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateImageWithTextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateImageWithTextResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateImageWithTextResponse, self).to_map()
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
            temp_model = GenerateImageWithTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateImageWithTextAndImageRequest(TeaModel):
    def __init__(self, aspect_ratio_mode=None, number=None, ref_image_url=None, resolution=None, similarity=None,
                 text=None):
        self.aspect_ratio_mode = aspect_ratio_mode  # type: str
        self.number = number  # type: int
        self.ref_image_url = ref_image_url  # type: str
        self.resolution = resolution  # type: str
        self.similarity = similarity  # type: float
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageWithTextAndImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio_mode is not None:
            result['AspectRatioMode'] = self.aspect_ratio_mode
        if self.number is not None:
            result['Number'] = self.number
        if self.ref_image_url is not None:
            result['RefImageUrl'] = self.ref_image_url
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AspectRatioMode') is not None:
            self.aspect_ratio_mode = m.get('AspectRatioMode')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RefImageUrl') is not None:
            self.ref_image_url = m.get('RefImageUrl')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GenerateImageWithTextAndImageAdvanceRequest(TeaModel):
    def __init__(self, aspect_ratio_mode=None, number=None, ref_image_url_object=None, resolution=None,
                 similarity=None, text=None):
        self.aspect_ratio_mode = aspect_ratio_mode  # type: str
        self.number = number  # type: int
        self.ref_image_url_object = ref_image_url_object  # type: READABLE
        self.resolution = resolution  # type: str
        self.similarity = similarity  # type: float
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageWithTextAndImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio_mode is not None:
            result['AspectRatioMode'] = self.aspect_ratio_mode
        if self.number is not None:
            result['Number'] = self.number
        if self.ref_image_url_object is not None:
            result['RefImageUrl'] = self.ref_image_url_object
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AspectRatioMode') is not None:
            self.aspect_ratio_mode = m.get('AspectRatioMode')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RefImageUrl') is not None:
            self.ref_image_url_object = m.get('RefImageUrl')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GenerateImageWithTextAndImageResponseBodyData(TeaModel):
    def __init__(self, image_urls=None):
        self.image_urls = image_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageWithTextAndImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class GenerateImageWithTextAndImageResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateImageWithTextAndImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateImageWithTextAndImageResponseBody, self).to_map()
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
            temp_model = GenerateImageWithTextAndImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateImageWithTextAndImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateImageWithTextAndImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateImageWithTextAndImageResponse, self).to_map()
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
            temp_model = GenerateImageWithTextAndImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateSuperResolutionImageRequest(TeaModel):
    def __init__(self, image_url=None, output_format=None, output_quality=None, scale=None, user_data=None):
        self.image_url = image_url  # type: str
        self.output_format = output_format  # type: str
        self.output_quality = output_quality  # type: int
        self.scale = scale  # type: int
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateSuperResolutionImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.output_quality is not None:
            result['OutputQuality'] = self.output_quality
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('OutputQuality') is not None:
            self.output_quality = m.get('OutputQuality')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GenerateSuperResolutionImageAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None, output_format=None, output_quality=None, scale=None, user_data=None):
        self.image_url_object = image_url_object  # type: READABLE
        self.output_format = output_format  # type: str
        self.output_quality = output_quality  # type: int
        self.scale = scale  # type: int
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateSuperResolutionImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.output_quality is not None:
            result['OutputQuality'] = self.output_quality
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('OutputQuality') is not None:
            self.output_quality = m.get('OutputQuality')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GenerateSuperResolutionImageResponseBodyData(TeaModel):
    def __init__(self, result_url=None):
        self.result_url = result_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateSuperResolutionImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class GenerateSuperResolutionImageResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateSuperResolutionImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateSuperResolutionImageResponseBody, self).to_map()
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
            temp_model = GenerateSuperResolutionImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateSuperResolutionImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateSuperResolutionImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateSuperResolutionImageResponse, self).to_map()
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
            temp_model = GenerateSuperResolutionImageResponseBody()
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


class ImageBlindCharacterWatermarkRequest(TeaModel):
    def __init__(self, function_type=None, origin_image_url=None, output_file_type=None, quality_factor=None,
                 text=None, watermark_image_url=None):
        self.function_type = function_type  # type: str
        self.origin_image_url = origin_image_url  # type: str
        self.output_file_type = output_file_type  # type: str
        self.quality_factor = quality_factor  # type: int
        self.text = text  # type: str
        self.watermark_image_url = watermark_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageBlindCharacterWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.text is not None:
            result['Text'] = self.text
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindCharacterWatermarkAdvanceRequest(TeaModel):
    def __init__(self, function_type=None, origin_image_urlobject=None, output_file_type=None, quality_factor=None,
                 text=None, watermark_image_urlobject=None):
        self.function_type = function_type  # type: str
        self.origin_image_urlobject = origin_image_urlobject  # type: READABLE
        self.output_file_type = output_file_type  # type: str
        self.quality_factor = quality_factor  # type: int
        self.text = text  # type: str
        self.watermark_image_urlobject = watermark_image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageBlindCharacterWatermarkAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.origin_image_urlobject is not None:
            result['OriginImageURL'] = self.origin_image_urlobject
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.text is not None:
            result['Text'] = self.text
        if self.watermark_image_urlobject is not None:
            result['WatermarkImageURL'] = self.watermark_image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('OriginImageURL') is not None:
            self.origin_image_urlobject = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_urlobject = m.get('WatermarkImageURL')
        return self


class ImageBlindCharacterWatermarkResponseBodyData(TeaModel):
    def __init__(self, text_image_url=None, watermark_image_url=None):
        self.text_image_url = text_image_url  # type: str
        self.watermark_image_url = watermark_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageBlindCharacterWatermarkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text_image_url is not None:
            result['TextImageURL'] = self.text_image_url
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TextImageURL') is not None:
            self.text_image_url = m.get('TextImageURL')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindCharacterWatermarkResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ImageBlindCharacterWatermarkResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImageBlindCharacterWatermarkResponseBody, self).to_map()
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
            temp_model = ImageBlindCharacterWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageBlindCharacterWatermarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImageBlindCharacterWatermarkResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImageBlindCharacterWatermarkResponse, self).to_map()
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
            temp_model = ImageBlindCharacterWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageBlindPicWatermarkRequest(TeaModel):
    def __init__(self, function_type=None, logo_url=None, origin_image_url=None, output_file_type=None,
                 quality_factor=None, watermark_image_url=None):
        self.function_type = function_type  # type: str
        self.logo_url = logo_url  # type: str
        self.origin_image_url = origin_image_url  # type: str
        self.output_file_type = output_file_type  # type: str
        self.quality_factor = quality_factor  # type: int
        self.watermark_image_url = watermark_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageBlindPicWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.logo_url is not None:
            result['LogoURL'] = self.logo_url
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('LogoURL') is not None:
            self.logo_url = m.get('LogoURL')
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindPicWatermarkAdvanceRequest(TeaModel):
    def __init__(self, function_type=None, logo_urlobject=None, origin_image_urlobject=None, output_file_type=None,
                 quality_factor=None, watermark_image_urlobject=None):
        self.function_type = function_type  # type: str
        self.logo_urlobject = logo_urlobject  # type: READABLE
        self.origin_image_urlobject = origin_image_urlobject  # type: READABLE
        self.output_file_type = output_file_type  # type: str
        self.quality_factor = quality_factor  # type: int
        self.watermark_image_urlobject = watermark_image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageBlindPicWatermarkAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.logo_urlobject is not None:
            result['LogoURL'] = self.logo_urlobject
        if self.origin_image_urlobject is not None:
            result['OriginImageURL'] = self.origin_image_urlobject
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.watermark_image_urlobject is not None:
            result['WatermarkImageURL'] = self.watermark_image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('LogoURL') is not None:
            self.logo_urlobject = m.get('LogoURL')
        if m.get('OriginImageURL') is not None:
            self.origin_image_urlobject = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_urlobject = m.get('WatermarkImageURL')
        return self


class ImageBlindPicWatermarkResponseBodyData(TeaModel):
    def __init__(self, logo_url=None, watermark_image_url=None):
        self.logo_url = logo_url  # type: str
        self.watermark_image_url = watermark_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageBlindPicWatermarkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_url is not None:
            result['LogoURL'] = self.logo_url
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogoURL') is not None:
            self.logo_url = m.get('LogoURL')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindPicWatermarkResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ImageBlindPicWatermarkResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImageBlindPicWatermarkResponseBody, self).to_map()
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
            temp_model = ImageBlindPicWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageBlindPicWatermarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImageBlindPicWatermarkResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImageBlindPicWatermarkResponse, self).to_map()
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
            temp_model = ImageBlindPicWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImitatePhotoStyleRequest(TeaModel):
    def __init__(self, image_url=None, style_url=None):
        self.image_url = image_url  # type: str
        self.style_url = style_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImitatePhotoStyleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        return self


class ImitatePhotoStyleAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, style_url_object=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.style_url_object = style_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImitatePhotoStyleAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.style_url_object is not None:
            result['StyleUrl'] = self.style_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('StyleUrl') is not None:
            self.style_url_object = m.get('StyleUrl')
        return self


class ImitatePhotoStyleResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImitatePhotoStyleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ImitatePhotoStyleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ImitatePhotoStyleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImitatePhotoStyleResponseBody, self).to_map()
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
            temp_model = ImitatePhotoStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImitatePhotoStyleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImitatePhotoStyleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImitatePhotoStyleResponse, self).to_map()
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
            temp_model = ImitatePhotoStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IntelligentCompositionRequest(TeaModel):
    def __init__(self, image_url=None, num_boxes=None):
        self.image_url = image_url  # type: str
        self.num_boxes = num_boxes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(IntelligentCompositionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.num_boxes is not None:
            result['NumBoxes'] = self.num_boxes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('NumBoxes') is not None:
            self.num_boxes = m.get('NumBoxes')
        return self


class IntelligentCompositionAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, num_boxes=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.num_boxes = num_boxes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(IntelligentCompositionAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.num_boxes is not None:
            result['NumBoxes'] = self.num_boxes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('NumBoxes') is not None:
            self.num_boxes = m.get('NumBoxes')
        return self


class IntelligentCompositionResponseBodyDataElements(TeaModel):
    def __init__(self, max_x=None, max_y=None, min_x=None, min_y=None, score=None):
        self.max_x = max_x  # type: int
        self.max_y = max_y  # type: int
        self.min_x = min_x  # type: int
        self.min_y = min_y  # type: int
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(IntelligentCompositionResponseBodyDataElements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_x is not None:
            result['MaxX'] = self.max_x
        if self.max_y is not None:
            result['MaxY'] = self.max_y
        if self.min_x is not None:
            result['MinX'] = self.min_x
        if self.min_y is not None:
            result['MinY'] = self.min_y
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxX') is not None:
            self.max_x = m.get('MaxX')
        if m.get('MaxY') is not None:
            self.max_y = m.get('MaxY')
        if m.get('MinX') is not None:
            self.min_x = m.get('MinX')
        if m.get('MinY') is not None:
            self.min_y = m.get('MinY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class IntelligentCompositionResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[IntelligentCompositionResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(IntelligentCompositionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = IntelligentCompositionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class IntelligentCompositionResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: IntelligentCompositionResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(IntelligentCompositionResponseBody, self).to_map()
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
            temp_model = IntelligentCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IntelligentCompositionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IntelligentCompositionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IntelligentCompositionResponse, self).to_map()
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
            temp_model = IntelligentCompositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeSuperResolutionImageRequest(TeaModel):
    def __init__(self, mode=None, output_format=None, output_quality=None, upscale_factor=None, url=None):
        self.mode = mode  # type: str
        self.output_format = output_format  # type: str
        self.output_quality = output_quality  # type: long
        self.upscale_factor = upscale_factor  # type: long
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeSuperResolutionImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.output_quality is not None:
            result['OutputQuality'] = self.output_quality
        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('OutputQuality') is not None:
            self.output_quality = m.get('OutputQuality')
        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class MakeSuperResolutionImageAdvanceRequest(TeaModel):
    def __init__(self, mode=None, output_format=None, output_quality=None, upscale_factor=None, url_object=None):
        self.mode = mode  # type: str
        self.output_format = output_format  # type: str
        self.output_quality = output_quality  # type: long
        self.upscale_factor = upscale_factor  # type: long
        self.url_object = url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeSuperResolutionImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.output_quality is not None:
            result['OutputQuality'] = self.output_quality
        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('OutputQuality') is not None:
            self.output_quality = m.get('OutputQuality')
        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class MakeSuperResolutionImageResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeSuperResolutionImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class MakeSuperResolutionImageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: MakeSuperResolutionImageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MakeSuperResolutionImageResponseBody, self).to_map()
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
            temp_model = MakeSuperResolutionImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MakeSuperResolutionImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MakeSuperResolutionImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MakeSuperResolutionImageResponse, self).to_map()
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
            temp_model = MakeSuperResolutionImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecolorHDImageRequestColorTemplate(TeaModel):
    def __init__(self, color=None):
        self.color = color  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecolorHDImageRequestColorTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorHDImageRequest(TeaModel):
    def __init__(self, color_count=None, color_template=None, degree=None, mode=None, ref_url=None, url=None):
        self.color_count = color_count  # type: int
        # 1
        self.color_template = color_template  # type: list[RecolorHDImageRequestColorTemplate]
        self.degree = degree  # type: str
        self.mode = mode  # type: str
        self.ref_url = ref_url  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecolorHDImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.degree is not None:
            result['Degree'] = self.degree
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorHDImageRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecolorHDImageAdvanceRequestColorTemplate(TeaModel):
    def __init__(self, color=None):
        self.color = color  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecolorHDImageAdvanceRequestColorTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorHDImageAdvanceRequest(TeaModel):
    def __init__(self, color_count=None, color_template=None, degree=None, mode=None, ref_url_object=None,
                 url_object=None):
        self.color_count = color_count  # type: int
        # 1
        self.color_template = color_template  # type: list[RecolorHDImageAdvanceRequestColorTemplate]
        self.degree = degree  # type: str
        self.mode = mode  # type: str
        self.ref_url_object = ref_url_object  # type: READABLE
        self.url_object = url_object  # type: READABLE

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecolorHDImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.degree is not None:
            result['Degree'] = self.degree
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url_object is not None:
            result['RefUrl'] = self.ref_url_object
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorHDImageAdvanceRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url_object = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class RecolorHDImageResponseBodyData(TeaModel):
    def __init__(self, image_list=None):
        # 1
        self.image_list = image_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecolorHDImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_list is not None:
            result['ImageList'] = self.image_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')
        return self


class RecolorHDImageResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: RecolorHDImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecolorHDImageResponseBody, self).to_map()
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
            temp_model = RecolorHDImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecolorHDImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecolorHDImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecolorHDImageResponse, self).to_map()
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
            temp_model = RecolorHDImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecolorImageRequestColorTemplate(TeaModel):
    def __init__(self, color=None):
        self.color = color  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecolorImageRequestColorTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorImageRequest(TeaModel):
    def __init__(self, color_count=None, color_template=None, mode=None, ref_url=None, url=None):
        self.color_count = color_count  # type: int
        # 1
        self.color_template = color_template  # type: list[RecolorImageRequestColorTemplate]
        self.mode = mode  # type: str
        self.ref_url = ref_url  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecolorImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorImageRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecolorImageAdvanceRequestColorTemplate(TeaModel):
    def __init__(self, color=None):
        self.color = color  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecolorImageAdvanceRequestColorTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorImageAdvanceRequest(TeaModel):
    def __init__(self, color_count=None, color_template=None, mode=None, ref_url_object=None, url_object=None):
        self.color_count = color_count  # type: int
        # 1
        self.color_template = color_template  # type: list[RecolorImageAdvanceRequestColorTemplate]
        self.mode = mode  # type: str
        self.ref_url_object = ref_url_object  # type: READABLE
        self.url_object = url_object  # type: READABLE

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecolorImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url_object is not None:
            result['RefUrl'] = self.ref_url_object
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorImageAdvanceRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url_object = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class RecolorImageResponseBodyData(TeaModel):
    def __init__(self, image_list=None):
        # 1
        self.image_list = image_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecolorImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_list is not None:
            result['ImageList'] = self.image_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')
        return self


class RecolorImageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecolorImageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecolorImageResponseBody, self).to_map()
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
            temp_model = RecolorImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecolorImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecolorImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecolorImageResponse, self).to_map()
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
            temp_model = RecolorImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageSubtitlesRequest(TeaModel):
    def __init__(self, bh=None, bw=None, bx=None, by=None, image_url=None):
        self.bh = bh  # type: float
        self.bw = bw  # type: float
        self.bx = bx  # type: float
        self.by = by  # type: float
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageSubtitlesRequest, self).to_map()
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
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
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
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageSubtitlesAdvanceRequest(TeaModel):
    def __init__(self, bh=None, bw=None, bx=None, by=None, image_urlobject=None):
        self.bh = bh  # type: float
        self.bw = bw  # type: float
        self.bx = bx  # type: float
        self.by = by  # type: float
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageSubtitlesAdvanceRequest, self).to_map()
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
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
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
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RemoveImageSubtitlesResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageSubtitlesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageSubtitlesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RemoveImageSubtitlesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RemoveImageSubtitlesResponseBody, self).to_map()
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
            temp_model = RemoveImageSubtitlesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveImageSubtitlesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveImageSubtitlesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveImageSubtitlesResponse, self).to_map()
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
            temp_model = RemoveImageSubtitlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageWatermarkRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageWatermarkAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageWatermarkAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RemoveImageWatermarkResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageWatermarkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageWatermarkResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RemoveImageWatermarkResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RemoveImageWatermarkResponseBody, self).to_map()
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
            temp_model = RemoveImageWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveImageWatermarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveImageWatermarkResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveImageWatermarkResponse, self).to_map()
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
            temp_model = RemoveImageWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


