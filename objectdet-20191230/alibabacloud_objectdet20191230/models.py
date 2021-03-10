# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class ClassifyVehicleInsuranceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ClassifyVehicleInsuranceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class ClassifyVehicleInsuranceResponseBodyDataLabels(TeaModel):
    def __init__(self, score=None, name=None):
        self.score = score  # type: float
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ClassifyVehicleInsuranceResponseBodyData(TeaModel):
    def __init__(self, labels=None, threshold=None):
        self.labels = labels  # type: list[ClassifyVehicleInsuranceResponseBodyDataLabels]
        self.threshold = threshold  # type: float

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ClassifyVehicleInsuranceResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ClassifyVehicleInsuranceResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: ClassifyVehicleInsuranceResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ClassifyVehicleInsuranceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ClassifyVehicleInsuranceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ClassifyVehicleInsuranceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ClassifyVehicleInsuranceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectIPCObjectRequest(TeaModel):
    def __init__(self, image_url=None):
        # 图片URL地址
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectIPCObjectResponseBodyDataElements(TeaModel):
    def __init__(self, type=None, score=None, box=None, target_rate=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.score = score  # type: float
        self.box = box  # type: list[long]
        self.target_rate = target_rate  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.score is not None:
            result['Score'] = self.score
        if self.box is not None:
            result['Box'] = self.box
        if self.target_rate is not None:
            result['TargetRate'] = self.target_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('TargetRate') is not None:
            self.target_rate = m.get('TargetRate')
        return self


class DetectIPCObjectResponseBodyData(TeaModel):
    def __init__(self, elements=None, width=None, height=None):
        self.elements = elements  # type: list[DetectIPCObjectResponseBodyDataElements]
        self.width = width  # type: long
        self.height = height  # type: long

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectIPCObjectResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectIPCObjectResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectIPCObjectResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectIPCObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectIPCObjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectIPCObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectIPCObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectMainBodyRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectMainBodyAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectMainBodyResponseBodyDataLocation(TeaModel):
    def __init__(self, width=None, height=None, y=None, x=None):
        self.width = width  # type: int
        self.height = height  # type: int
        self.y = y  # type: int
        self.x = x  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DetectMainBodyResponseBodyData(TeaModel):
    def __init__(self, location=None):
        self.location = location  # type: DetectMainBodyResponseBodyDataLocation

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = DetectMainBodyResponseBodyDataLocation()
            self.location = temp_model.from_map(m['Location'])
        return self


class DetectMainBodyResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectMainBodyResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectMainBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectMainBodyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectMainBodyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectMainBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectObjectRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectObjectAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectObjectResponseBodyDataElements(TeaModel):
    def __init__(self, type=None, boxes=None, score=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.boxes = boxes  # type: list[int]
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DetectObjectResponseBodyData(TeaModel):
    def __init__(self, elements=None, width=None, height=None):
        self.elements = elements  # type: list[DetectObjectResponseBodyDataElements]
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectObjectResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectObjectResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectObjectResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectObjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectTransparentImageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectTransparentImageAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectTransparentImageResponseBodyDataElements(TeaModel):
    def __init__(self, transparent_image=None):
        self.transparent_image = transparent_image  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transparent_image is not None:
            result['TransparentImage'] = self.transparent_image
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransparentImage') is not None:
            self.transparent_image = m.get('TransparentImage')
        return self


class DetectTransparentImageResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[DetectTransparentImageResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DetectTransparentImageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectTransparentImageResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectTransparentImageResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectTransparentImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectTransparentImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectTransparentImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectTransparentImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVehicleRequest(TeaModel):
    def __init__(self, image_type=None, image_url=None):
        self.image_type = image_type  # type: int
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectVehicleAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, image_type=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.image_type = image_type  # type: int

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class DetectVehicleResponseBodyDataDetectObjectInfoList(TeaModel):
    def __init__(self, type=None, boxes=None, score=None, id=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.boxes = boxes  # type: list[int]
        self.score = score  # type: float
        self.id = id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DetectVehicleResponseBodyData(TeaModel):
    def __init__(self, detect_object_info_list=None, width=None, height=None):
        self.detect_object_info_list = detect_object_info_list  # type: list[DetectVehicleResponseBodyDataDetectObjectInfoList]
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        if self.detect_object_info_list:
            for k in self.detect_object_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DetectObjectInfoList'] = []
        if self.detect_object_info_list is not None:
            for k in self.detect_object_info_list:
                result['DetectObjectInfoList'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detect_object_info_list = []
        if m.get('DetectObjectInfoList') is not None:
            for k in m.get('DetectObjectInfoList'):
                temp_model = DetectVehicleResponseBodyDataDetectObjectInfoList()
                self.detect_object_info_list.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectVehicleResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectVehicleResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectVehicleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectVehicleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectVehicleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectVehicleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVehicleICongestionRequestRoadRegionsRoadRegionPoint(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DetectVehicleICongestionRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(self, point=None):
        self.point = point  # type: DetectVehicleICongestionRequestRoadRegionsRoadRegionPoint

    def validate(self):
        if self.point:
            self.point.validate()

    def to_map(self):
        result = dict()
        if self.point is not None:
            result['Point'] = self.point.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Point') is not None:
            temp_model = DetectVehicleICongestionRequestRoadRegionsRoadRegionPoint()
            self.point = temp_model.from_map(m['Point'])
        return self


class DetectVehicleICongestionRequestRoadRegions(TeaModel):
    def __init__(self, road_region=None):
        self.road_region = road_region  # type: list[DetectVehicleICongestionRequestRoadRegionsRoadRegion]

    def validate(self):
        if self.road_region:
            for k in self.road_region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RoadRegion'] = []
        if self.road_region is not None:
            for k in self.road_region:
                result['RoadRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.road_region = []
        if m.get('RoadRegion') is not None:
            for k in m.get('RoadRegion'):
                temp_model = DetectVehicleICongestionRequestRoadRegionsRoadRegion()
                self.road_region.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionRequestPreRegionIntersectFeatures(TeaModel):
    def __init__(self, features=None):
        self.features = features  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.features is not None:
            result['Features'] = self.features
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')
        return self


class DetectVehicleICongestionRequest(TeaModel):
    def __init__(self, image_url=None, road_regions=None, pre_region_intersect_features=None):
        # A short description of struct
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode
        self.road_regions = road_regions  # type: list[DetectVehicleICongestionRequestRoadRegions]
        self.pre_region_intersect_features = pre_region_intersect_features  # type: list[DetectVehicleICongestionRequestPreRegionIntersectFeatures]

    def validate(self):
        if self.road_regions:
            for k in self.road_regions:
                if k:
                    k.validate()
        if self.pre_region_intersect_features:
            for k in self.pre_region_intersect_features:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        result['PreRegionIntersectFeatures'] = []
        if self.pre_region_intersect_features is not None:
            for k in self.pre_region_intersect_features:
                result['PreRegionIntersectFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.road_regions = []
        if m.get('RoadRegions') is not None:
            for k in m.get('RoadRegions'):
                temp_model = DetectVehicleICongestionRequestRoadRegions()
                self.road_regions.append(temp_model.from_map(k))
        self.pre_region_intersect_features = []
        if m.get('PreRegionIntersectFeatures') is not None:
            for k in m.get('PreRegionIntersectFeatures'):
                temp_model = DetectVehicleICongestionRequestPreRegionIntersectFeatures()
                self.pre_region_intersect_features.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionShrinkRequest(TeaModel):
    def __init__(self, image_url=None, road_regions_shrink=None, pre_region_intersect_features_shrink=None):
        # A short description of struct
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode
        self.road_regions_shrink = TeaConverter.to_unicode(road_regions_shrink)  # type: unicode
        self.pre_region_intersect_features_shrink = TeaConverter.to_unicode(pre_region_intersect_features_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.road_regions_shrink is not None:
            result['RoadRegions'] = self.road_regions_shrink
        if self.pre_region_intersect_features_shrink is not None:
            result['PreRegionIntersectFeatures'] = self.pre_region_intersect_features_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('RoadRegions') is not None:
            self.road_regions_shrink = m.get('RoadRegions')
        if m.get('PreRegionIntersectFeatures') is not None:
            self.pre_region_intersect_features_shrink = m.get('PreRegionIntersectFeatures')
        return self


class DetectVehicleICongestionResponseBodyDataElementsBoxes(TeaModel):
    def __init__(self, left=None, top=None, right=None, bottom=None):
        self.left = left  # type: long
        self.top = top  # type: long
        self.right = right  # type: long
        self.bottom = bottom  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.right is not None:
            result['Right'] = self.right
        if self.bottom is not None:
            result['Bottom'] = self.bottom
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Right') is not None:
            self.right = m.get('Right')
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')
        return self


class DetectVehicleICongestionResponseBodyDataElements(TeaModel):
    def __init__(self, boxes=None, score=None, type_name=None):
        self.boxes = boxes  # type: list[DetectVehicleICongestionResponseBodyDataElementsBoxes]
        self.score = score  # type: float
        self.type_name = TeaConverter.to_unicode(type_name)  # type: unicode

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = DetectVehicleICongestionResponseBodyDataElementsBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class DetectVehicleICongestionResponseBodyDataRegionIntersectFeatures(TeaModel):
    def __init__(self, features=None):
        self.features = features  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.features is not None:
            result['Features'] = self.features
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')
        return self


class DetectVehicleICongestionResponseBodyDataRegionIntersectMatched(TeaModel):
    def __init__(self, ids=None):
        self.ids = ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DetectVehicleICongestionResponseBodyDataRegionIntersects(TeaModel):
    def __init__(self, ids=None):
        self.ids = ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DetectVehicleICongestionResponseBodyData(TeaModel):
    def __init__(self, elements=None, region_intersect_features=None, region_intersect_matched=None,
                 region_intersects=None):
        self.elements = elements  # type: list[DetectVehicleICongestionResponseBodyDataElements]
        self.region_intersect_features = region_intersect_features  # type: list[DetectVehicleICongestionResponseBodyDataRegionIntersectFeatures]
        self.region_intersect_matched = region_intersect_matched  # type: list[DetectVehicleICongestionResponseBodyDataRegionIntersectMatched]
        self.region_intersects = region_intersects  # type: list[DetectVehicleICongestionResponseBodyDataRegionIntersects]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        if self.region_intersect_features:
            for k in self.region_intersect_features:
                if k:
                    k.validate()
        if self.region_intersect_matched:
            for k in self.region_intersect_matched:
                if k:
                    k.validate()
        if self.region_intersects:
            for k in self.region_intersects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        result['RegionIntersectFeatures'] = []
        if self.region_intersect_features is not None:
            for k in self.region_intersect_features:
                result['RegionIntersectFeatures'].append(k.to_map() if k else None)
        result['RegionIntersectMatched'] = []
        if self.region_intersect_matched is not None:
            for k in self.region_intersect_matched:
                result['RegionIntersectMatched'].append(k.to_map() if k else None)
        result['RegionIntersects'] = []
        if self.region_intersects is not None:
            for k in self.region_intersects:
                result['RegionIntersects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectVehicleICongestionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        self.region_intersect_features = []
        if m.get('RegionIntersectFeatures') is not None:
            for k in m.get('RegionIntersectFeatures'):
                temp_model = DetectVehicleICongestionResponseBodyDataRegionIntersectFeatures()
                self.region_intersect_features.append(temp_model.from_map(k))
        self.region_intersect_matched = []
        if m.get('RegionIntersectMatched') is not None:
            for k in m.get('RegionIntersectMatched'):
                temp_model = DetectVehicleICongestionResponseBodyDataRegionIntersectMatched()
                self.region_intersect_matched.append(temp_model.from_map(k))
        self.region_intersects = []
        if m.get('RegionIntersects') is not None:
            for k in m.get('RegionIntersects'):
                temp_model = DetectVehicleICongestionResponseBodyDataRegionIntersects()
                self.region_intersects.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectVehicleICongestionResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectVehicleICongestionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectVehicleICongestionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectVehicleICongestionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectVehicleICongestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DetectVehicleIllegalParkingRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(self, point=None):
        self.point = point  # type: DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint

    def validate(self):
        if self.point:
            self.point.validate()

    def to_map(self):
        result = dict()
        if self.point is not None:
            result['Point'] = self.point.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Point') is not None:
            temp_model = DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint()
            self.point = temp_model.from_map(m['Point'])
        return self


class DetectVehicleIllegalParkingRequestRoadRegions(TeaModel):
    def __init__(self, road_region=None):
        self.road_region = road_region  # type: list[DetectVehicleIllegalParkingRequestRoadRegionsRoadRegion]

    def validate(self):
        if self.road_region:
            for k in self.road_region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RoadRegion'] = []
        if self.road_region is not None:
            for k in self.road_region:
                result['RoadRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.road_region = []
        if m.get('RoadRegion') is not None:
            for k in m.get('RoadRegion'):
                temp_model = DetectVehicleIllegalParkingRequestRoadRegionsRoadRegion()
                self.road_region.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingRequest(TeaModel):
    def __init__(self, image_url=None, road_regions=None):
        # A short description of struct
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode
        self.road_regions = road_regions  # type: list[DetectVehicleIllegalParkingRequestRoadRegions]

    def validate(self):
        if self.road_regions:
            for k in self.road_regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.road_regions = []
        if m.get('RoadRegions') is not None:
            for k in m.get('RoadRegions'):
                temp_model = DetectVehicleIllegalParkingRequestRoadRegions()
                self.road_regions.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingShrinkRequest(TeaModel):
    def __init__(self, image_url=None, road_regions_shrink=None):
        # A short description of struct
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode
        self.road_regions_shrink = TeaConverter.to_unicode(road_regions_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.road_regions_shrink is not None:
            result['RoadRegions'] = self.road_regions_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('RoadRegions') is not None:
            self.road_regions_shrink = m.get('RoadRegions')
        return self


class DetectVehicleIllegalParkingResponseBodyDataElementsBoxes(TeaModel):
    def __init__(self, left=None, top=None, right=None, bottom=None):
        self.left = left  # type: long
        self.top = top  # type: long
        self.right = right  # type: long
        self.bottom = bottom  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.right is not None:
            result['Right'] = self.right
        if self.bottom is not None:
            result['Bottom'] = self.bottom
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Right') is not None:
            self.right = m.get('Right')
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')
        return self


class DetectVehicleIllegalParkingResponseBodyDataElements(TeaModel):
    def __init__(self, boxes=None, score=None, type_name=None):
        self.boxes = boxes  # type: list[DetectVehicleIllegalParkingResponseBodyDataElementsBoxes]
        self.score = score  # type: float
        self.type_name = TeaConverter.to_unicode(type_name)  # type: unicode

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = DetectVehicleIllegalParkingResponseBodyDataElementsBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class DetectVehicleIllegalParkingResponseBodyDataRegionIntersects(TeaModel):
    def __init__(self, ids=None):
        self.ids = ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DetectVehicleIllegalParkingResponseBodyData(TeaModel):
    def __init__(self, elements=None, region_intersects=None):
        self.elements = elements  # type: list[DetectVehicleIllegalParkingResponseBodyDataElements]
        self.region_intersects = region_intersects  # type: list[DetectVehicleIllegalParkingResponseBodyDataRegionIntersects]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        if self.region_intersects:
            for k in self.region_intersects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        result['RegionIntersects'] = []
        if self.region_intersects is not None:
            for k in self.region_intersects:
                result['RegionIntersects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectVehicleIllegalParkingResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        self.region_intersects = []
        if m.get('RegionIntersects') is not None:
            for k in m.get('RegionIntersects'):
                temp_model = DetectVehicleIllegalParkingResponseBodyDataRegionIntersects()
                self.region_intersects.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectVehicleIllegalParkingResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectVehicleIllegalParkingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectVehicleIllegalParkingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectVehicleIllegalParkingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectVehicleIllegalParkingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectWhiteBaseImageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectWhiteBaseImageAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectWhiteBaseImageResponseBodyDataElements(TeaModel):
    def __init__(self, white_base=None):
        self.white_base = white_base  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.white_base is not None:
            result['WhiteBase'] = self.white_base
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WhiteBase') is not None:
            self.white_base = m.get('WhiteBase')
        return self


class DetectWhiteBaseImageResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[DetectWhiteBaseImageResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DetectWhiteBaseImageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectWhiteBaseImageResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: DetectWhiteBaseImageResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectWhiteBaseImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectWhiteBaseImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetectWhiteBaseImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectWhiteBaseImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVehicleRepairPlanRequestDamageImageList(TeaModel):
    def __init__(self, create_time_stamp=None, image_url=None):
        self.create_time_stamp = TeaConverter.to_unicode(create_time_stamp)  # type: unicode
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class GenerateVehicleRepairPlanRequest(TeaModel):
    def __init__(self, damage_image_list=None):
        self.damage_image_list = damage_image_list  # type: list[GenerateVehicleRepairPlanRequestDamageImageList]

    def validate(self):
        if self.damage_image_list:
            for k in self.damage_image_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DamageImageList'] = []
        if self.damage_image_list is not None:
            for k in self.damage_image_list:
                result['DamageImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.damage_image_list = []
        if m.get('DamageImageList') is not None:
            for k in m.get('DamageImageList'):
                temp_model = GenerateVehicleRepairPlanRequestDamageImageList()
                self.damage_image_list.append(temp_model.from_map(k))
        return self


class GenerateVehicleRepairPlanResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GenerateVehicleRepairPlanResponseBody(TeaModel):
    def __init__(self, http_code=None, request_id=None, data=None, error_message=None, code=None, success=None):
        self.http_code = http_code  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GenerateVehicleRepairPlanResponseBodyData
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GenerateVehicleRepairPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateVehicleRepairPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GenerateVehicleRepairPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GenerateVehicleRepairPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVehicleRepairPlanRequest(TeaModel):
    def __init__(self, task_id=None, car_number_image=None, vin_code_image=None):
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.car_number_image = TeaConverter.to_unicode(car_number_image)  # type: unicode
        self.vin_code_image = TeaConverter.to_unicode(vin_code_image)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.car_number_image is not None:
            result['CarNumberImage'] = self.car_number_image
        if self.vin_code_image is not None:
            result['VinCodeImage'] = self.vin_code_image
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CarNumberImage') is not None:
            self.car_number_image = m.get('CarNumberImage')
        if m.get('VinCodeImage') is not None:
            self.vin_code_image = m.get('VinCodeImage')
        return self


class GetVehicleRepairPlanResponseBodyDataRepairParts(TeaModel):
    def __init__(self, relation_type=None, parts_std_code=None, part_name_match=None, repair_fee=None,
                 out_standard_parts_name=None, parts_std_name=None, repair_type_name=None, repair_type=None, oe_match=None,
                 out_standard_parts_id=None, garage_type=None):
        self.relation_type = TeaConverter.to_unicode(relation_type)  # type: unicode
        self.parts_std_code = TeaConverter.to_unicode(parts_std_code)  # type: unicode
        self.part_name_match = part_name_match  # type: bool
        self.repair_fee = TeaConverter.to_unicode(repair_fee)  # type: unicode
        self.out_standard_parts_name = TeaConverter.to_unicode(out_standard_parts_name)  # type: unicode
        self.parts_std_name = TeaConverter.to_unicode(parts_std_name)  # type: unicode
        self.repair_type_name = TeaConverter.to_unicode(repair_type_name)  # type: unicode
        self.repair_type = TeaConverter.to_unicode(repair_type)  # type: unicode
        self.oe_match = oe_match  # type: bool
        self.out_standard_parts_id = TeaConverter.to_unicode(out_standard_parts_id)  # type: unicode
        self.garage_type = TeaConverter.to_unicode(garage_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.parts_std_code is not None:
            result['PartsStdCode'] = self.parts_std_code
        if self.part_name_match is not None:
            result['PartNameMatch'] = self.part_name_match
        if self.repair_fee is not None:
            result['RepairFee'] = self.repair_fee
        if self.out_standard_parts_name is not None:
            result['OutStandardPartsName'] = self.out_standard_parts_name
        if self.parts_std_name is not None:
            result['PartsStdName'] = self.parts_std_name
        if self.repair_type_name is not None:
            result['RepairTypeName'] = self.repair_type_name
        if self.repair_type is not None:
            result['RepairType'] = self.repair_type
        if self.oe_match is not None:
            result['OeMatch'] = self.oe_match
        if self.out_standard_parts_id is not None:
            result['OutStandardPartsId'] = self.out_standard_parts_id
        if self.garage_type is not None:
            result['GarageType'] = self.garage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('PartsStdCode') is not None:
            self.parts_std_code = m.get('PartsStdCode')
        if m.get('PartNameMatch') is not None:
            self.part_name_match = m.get('PartNameMatch')
        if m.get('RepairFee') is not None:
            self.repair_fee = m.get('RepairFee')
        if m.get('OutStandardPartsName') is not None:
            self.out_standard_parts_name = m.get('OutStandardPartsName')
        if m.get('PartsStdName') is not None:
            self.parts_std_name = m.get('PartsStdName')
        if m.get('RepairTypeName') is not None:
            self.repair_type_name = m.get('RepairTypeName')
        if m.get('RepairType') is not None:
            self.repair_type = m.get('RepairType')
        if m.get('OeMatch') is not None:
            self.oe_match = m.get('OeMatch')
        if m.get('OutStandardPartsId') is not None:
            self.out_standard_parts_id = m.get('OutStandardPartsId')
        if m.get('GarageType') is not None:
            self.garage_type = m.get('GarageType')
        return self


class GetVehicleRepairPlanResponseBodyData(TeaModel):
    def __init__(self, repair_parts=None, frame_no=None):
        self.repair_parts = repair_parts  # type: list[GetVehicleRepairPlanResponseBodyDataRepairParts]
        self.frame_no = TeaConverter.to_unicode(frame_no)  # type: unicode

    def validate(self):
        if self.repair_parts:
            for k in self.repair_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RepairParts'] = []
        if self.repair_parts is not None:
            for k in self.repair_parts:
                result['RepairParts'].append(k.to_map() if k else None)
        if self.frame_no is not None:
            result['FrameNo'] = self.frame_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.repair_parts = []
        if m.get('RepairParts') is not None:
            for k in m.get('RepairParts'):
                temp_model = GetVehicleRepairPlanResponseBodyDataRepairParts()
                self.repair_parts.append(temp_model.from_map(k))
        if m.get('FrameNo') is not None:
            self.frame_no = m.get('FrameNo')
        return self


class GetVehicleRepairPlanResponseBody(TeaModel):
    def __init__(self, http_code=None, request_id=None, data=None, error_message=None, code=None, success=None):
        self.http_code = http_code  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetVehicleRepairPlanResponseBodyData
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetVehicleRepairPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVehicleRepairPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetVehicleRepairPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetVehicleRepairPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleDamageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeVehicleDamageAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVehicleDamageResponseBodyDataElements(TeaModel):
    def __init__(self, type=None, scores=None, boxes=None, score=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.scores = scores  # type: list[float]
        self.boxes = boxes  # type: list[int]
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.scores is not None:
            result['Scores'] = self.scores
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Scores') is not None:
            self.scores = m.get('Scores')
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class RecognizeVehicleDamageResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[RecognizeVehicleDamageResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = RecognizeVehicleDamageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeVehicleDamageResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: RecognizeVehicleDamageResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeVehicleDamageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVehicleDamageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RecognizeVehicleDamageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeVehicleDamageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleDashboardRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeVehicleDashboardAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVehicleDashboardResponseBodyDataElements(TeaModel):
    def __init__(self, boxes=None, score=None, label=None, class_name=None):
        self.boxes = boxes  # type: list[float]
        self.score = score  # type: float
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.class_name = TeaConverter.to_unicode(class_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        if self.label is not None:
            result['Label'] = self.label
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        return self


class RecognizeVehicleDashboardResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[RecognizeVehicleDashboardResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = RecognizeVehicleDashboardResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeVehicleDashboardResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: RecognizeVehicleDashboardResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeVehicleDashboardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVehicleDashboardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RecognizeVehicleDashboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeVehicleDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehiclePartsRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeVehiclePartsAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVehiclePartsResponseBodyDataElements(TeaModel):
    def __init__(self, type=None, boxes=None, score=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.boxes = boxes  # type: list[int]
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class RecognizeVehiclePartsResponseBodyData(TeaModel):
    def __init__(self, elements=None, origin_shapes=None):
        self.elements = elements  # type: list[RecognizeVehiclePartsResponseBodyDataElements]
        self.origin_shapes = origin_shapes  # type: list[int]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.origin_shapes is not None:
            result['OriginShapes'] = self.origin_shapes
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeVehiclePartsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('OriginShapes') is not None:
            self.origin_shapes = m.get('OriginShapes')
        return self


class RecognizeVehiclePartsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: RecognizeVehiclePartsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeVehiclePartsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVehiclePartsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RecognizeVehiclePartsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeVehiclePartsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


