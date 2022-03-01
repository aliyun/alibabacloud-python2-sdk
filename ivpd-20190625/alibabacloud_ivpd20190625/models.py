# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


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


class ChangeImageSizeResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeImageSizeResponseBodyData, self).to_map()
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


class ChangeImageSizeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: ChangeImageSizeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeImageSizeResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChangeImageSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeImageSizeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeImageSizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeImageSizeResponse, self).to_map()
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
            temp_model = ChangeImageSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSegmentBodyJobRequestDataList(TeaModel):
    def __init__(self, data_id=None, image_url=None):
        self.data_id = data_id  # type: str
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSegmentBodyJobRequestDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class CreateSegmentBodyJobRequest(TeaModel):
    def __init__(self, data_list=None, job_id=None, time_to_live=None):
        self.data_list = data_list  # type: list[CreateSegmentBodyJobRequestDataList]
        self.job_id = job_id  # type: str
        self.time_to_live = time_to_live  # type: int

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSegmentBodyJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.time_to_live is not None:
            result['TimeToLive'] = self.time_to_live
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = CreateSegmentBodyJobRequestDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TimeToLive') is not None:
            self.time_to_live = m.get('TimeToLive')
        return self


class CreateSegmentBodyJobResponseBodyDataResultListResultData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSegmentBodyJobResponseBodyDataResultListResultData, self).to_map()
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


class CreateSegmentBodyJobResponseBodyDataResultList(TeaModel):
    def __init__(self, code=None, data_id=None, message=None, result_data=None, success=None):
        self.code = code  # type: str
        self.data_id = data_id  # type: str
        self.message = message  # type: str
        self.result_data = result_data  # type: CreateSegmentBodyJobResponseBodyDataResultListResultData
        self.success = success  # type: bool

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        _map = super(CreateSegmentBodyJobResponseBodyDataResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.message is not None:
            result['Message'] = self.message
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ResultData') is not None:
            temp_model = CreateSegmentBodyJobResponseBodyDataResultListResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSegmentBodyJobResponseBodyData(TeaModel):
    def __init__(self, batch_size=None, completed=None, job_id=None, progress=None, result_list=None, status=None,
                 total_used_time=None):
        self.batch_size = batch_size  # type: int
        self.completed = completed  # type: bool
        self.job_id = job_id  # type: str
        self.progress = progress  # type: int
        self.result_list = result_list  # type: list[CreateSegmentBodyJobResponseBodyDataResultList]
        self.status = status  # type: str
        self.total_used_time = total_used_time  # type: long

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSegmentBodyJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = CreateSegmentBodyJobResponseBodyDataResultList()
                self.result_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        return self


class CreateSegmentBodyJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateSegmentBodyJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSegmentBodyJobResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSegmentBodyJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSegmentBodyJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSegmentBodyJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSegmentBodyJobResponse, self).to_map()
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
            temp_model = CreateSegmentBodyJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageElementsRequest(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageElementsRequest, self).to_map()
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


class DetectImageElementsResponseBodyDataElements(TeaModel):
    def __init__(self, height=None, score=None, type=None, width=None, x=None, y=None):
        self.height = height  # type: int
        self.score = score  # type: float
        self.type = type  # type: str
        self.width = width  # type: int
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageElementsResponseBodyDataElements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
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
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DetectImageElementsResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[DetectImageElementsResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageElementsResponseBodyData, self).to_map()
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
                temp_model = DetectImageElementsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectImageElementsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: DetectImageElementsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DetectImageElementsResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DetectImageElementsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageElementsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectImageElementsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageElementsResponse, self).to_map()
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
            temp_model = DetectImageElementsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EraseLogoInVideoRequestBoxes(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h  # type: float
        self.w = w  # type: float
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseLogoInVideoRequestBoxes, self).to_map()
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


class EraseLogoInVideoRequest(TeaModel):
    def __init__(self, boxes=None, job_id=None, video_url=None):
        self.boxes = boxes  # type: list[EraseLogoInVideoRequestBoxes]
        self.job_id = job_id  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EraseLogoInVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = EraseLogoInVideoRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseLogoInVideoResponseBodyData(TeaModel):
    def __init__(self, job_id=None, video_url=None):
        self.job_id = job_id  # type: str
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EraseLogoInVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseLogoInVideoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: EraseLogoInVideoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EraseLogoInVideoResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = EraseLogoInVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EraseLogoInVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EraseLogoInVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EraseLogoInVideoResponse, self).to_map()
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
            temp_model = EraseLogoInVideoResponseBody()
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: ExtendImageStyleResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExtendImageStyleResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ExtendImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtendImageStyleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExtendImageStyleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtendImageStyleResponse, self).to_map()
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
            temp_model = ExtendImageStyleResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAsyncJobResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncJobResultResponse, self).to_map()
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncResultRequest, self).to_map()
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


class GetAsyncResultResponseBodyData(TeaModel):
    def __init__(self, batch_size=None, code=None, completed=None, finish=None, message=None, progress=None,
                 result=None, status=None, total_used_time=None):
        self.batch_size = batch_size  # type: str
        self.code = code  # type: str
        self.completed = completed  # type: bool
        self.finish = finish  # type: bool
        self.message = message  # type: str
        self.progress = progress  # type: float
        self.result = result  # type: dict[str, any]
        self.status = status  # type: str
        self.total_used_time = total_used_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.finish is not None:
            result['Finish'] = self.finish
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Finish') is not None:
            self.finish = m.get('Finish')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        return self


class GetAsyncResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetAsyncResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAsyncResultResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAsyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAsyncResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAsyncResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncResultResponse, self).to_map()
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
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobResultRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResultRequest, self).to_map()
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


class GetJobResultResponseBodyData(TeaModel):
    def __init__(self, batch_size=None, completed=None, finish=None, message=None, progress=None, result_list=None,
                 status=None, total_used_time=None):
        self.batch_size = batch_size  # type: str
        self.completed = completed  # type: bool
        self.finish = finish  # type: bool
        self.message = message  # type: str
        self.progress = progress  # type: float
        self.result_list = result_list  # type: list[dict[str, any]]
        self.status = status  # type: str
        self.total_used_time = total_used_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.finish is not None:
            result['Finish'] = self.finish
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result_list is not None:
            result['ResultList'] = self.result_list
        if self.status is not None:
            result['Status'] = self.status
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Finish') is not None:
            self.finish = m.get('Finish')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ResultList') is not None:
            self.result_list = m.get('ResultList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        return self


class GetJobResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetJobResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetJobResultResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetJobResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobResultResponse, self).to_map()
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
            temp_model = GetJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobStatusRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobStatusRequest, self).to_map()
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


class GetJobStatusResponseBodyData(TeaModel):
    def __init__(self, batch_size=None, completed=None, finish=None, message=None, progress=None, status=None,
                 time_to_live=None, total_used_time=None):
        self.batch_size = batch_size  # type: str
        self.completed = completed  # type: bool
        self.finish = finish  # type: bool
        self.message = message  # type: str
        self.progress = progress  # type: float
        self.status = status  # type: str
        self.time_to_live = time_to_live  # type: int
        self.total_used_time = total_used_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.finish is not None:
            result['Finish'] = self.finish
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.time_to_live is not None:
            result['TimeToLive'] = self.time_to_live
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Finish') is not None:
            self.finish = m.get('Finish')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeToLive') is not None:
            self.time_to_live = m.get('TimeToLive')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        return self


class GetJobStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetJobStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetJobStatusResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetJobStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobStatusResponse, self).to_map()
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
            temp_model = GetJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserBucketConfigResponseBodyData(TeaModel):
    def __init__(self, bucket=None, region=None, region_name=None):
        self.bucket = bucket  # type: str
        self.region = region  # type: str
        self.region_name = region_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserBucketConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.region is not None:
            result['Region'] = self.region
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class GetUserBucketConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetUserBucketConfigResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserBucketConfigResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetUserBucketConfigResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserBucketConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserBucketConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserBucketConfigResponse, self).to_map()
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
            temp_model = GetUserBucketConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HighlightGameVideoRequest(TeaModel):
    def __init__(self, async=None, video_url=None):
        self.async = async  # type: bool
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HighlightGameVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async is not None:
            result['Async'] = self.async
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async = m.get('Async')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class HighlightGameVideoAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, async=None):
        self.video_url_object = video_url_object  # type: READABLE
        self.async = async  # type: bool

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        _map = super(HighlightGameVideoAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async is not None:
            result['Async'] = self.async
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async = m.get('Async')
        return self


class HighlightGameVideoResponseBodyDataGameList(TeaModel):
    def __init__(self, end=None, game_info=None, id=None, start=None):
        self.end = end  # type: float
        self.game_info = game_info  # type: dict[str, any]
        self.id = id  # type: str
        self.start = start  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(HighlightGameVideoResponseBodyDataGameList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.game_info is not None:
            result['GameInfo'] = self.game_info
        if self.id is not None:
            result['Id'] = self.id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('GameInfo') is not None:
            self.game_info = m.get('GameInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class HighlightGameVideoResponseBodyDataHighlightList(TeaModel):
    def __init__(self, end=None, start=None):
        self.end = end  # type: float
        self.start = start  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(HighlightGameVideoResponseBodyDataHighlightList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class HighlightGameVideoResponseBodyData(TeaModel):
    def __init__(self, game_list=None, highlight_list=None):
        self.game_list = game_list  # type: list[HighlightGameVideoResponseBodyDataGameList]
        self.highlight_list = highlight_list  # type: list[HighlightGameVideoResponseBodyDataHighlightList]

    def validate(self):
        if self.game_list:
            for k in self.game_list:
                if k:
                    k.validate()
        if self.highlight_list:
            for k in self.highlight_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(HighlightGameVideoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GameList'] = []
        if self.game_list is not None:
            for k in self.game_list:
                result['GameList'].append(k.to_map() if k else None)
        result['HighlightList'] = []
        if self.highlight_list is not None:
            for k in self.highlight_list:
                result['HighlightList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.game_list = []
        if m.get('GameList') is not None:
            for k in m.get('GameList'):
                temp_model = HighlightGameVideoResponseBodyDataGameList()
                self.game_list.append(temp_model.from_map(k))
        self.highlight_list = []
        if m.get('HighlightList') is not None:
            for k in m.get('HighlightList'):
                temp_model = HighlightGameVideoResponseBodyDataHighlightList()
                self.highlight_list.append(temp_model.from_map(k))
        return self


class HighlightGameVideoResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: HighlightGameVideoResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(HighlightGameVideoResponseBody, self).to_map()
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
            temp_model = HighlightGameVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HighlightGameVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HighlightGameVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HighlightGameVideoResponse, self).to_map()
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
            temp_model = HighlightGameVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPackageDesignModelTypesResponseBodyDataModelTypeListElements(TeaModel):
    def __init__(self, side_name=None):
        self.side_name = side_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPackageDesignModelTypesResponseBodyDataModelTypeListElements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.side_name is not None:
            result['SideName'] = self.side_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SideName') is not None:
            self.side_name = m.get('SideName')
        return self


class ListPackageDesignModelTypesResponseBodyDataModelTypeList(TeaModel):
    def __init__(self, elements=None, model_type=None):
        self.elements = elements  # type: list[ListPackageDesignModelTypesResponseBodyDataModelTypeListElements]
        self.model_type = model_type  # type: str

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPackageDesignModelTypesResponseBodyDataModelTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ListPackageDesignModelTypesResponseBodyDataModelTypeListElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        return self


class ListPackageDesignModelTypesResponseBodyData(TeaModel):
    def __init__(self, model_type_list=None):
        self.model_type_list = model_type_list  # type: list[ListPackageDesignModelTypesResponseBodyDataModelTypeList]

    def validate(self):
        if self.model_type_list:
            for k in self.model_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPackageDesignModelTypesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModelTypeList'] = []
        if self.model_type_list is not None:
            for k in self.model_type_list:
                result['ModelTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.model_type_list = []
        if m.get('ModelTypeList') is not None:
            for k in m.get('ModelTypeList'):
                temp_model = ListPackageDesignModelTypesResponseBodyDataModelTypeList()
                self.model_type_list.append(temp_model.from_map(k))
        return self


class ListPackageDesignModelTypesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListPackageDesignModelTypesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListPackageDesignModelTypesResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListPackageDesignModelTypesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPackageDesignModelTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPackageDesignModelTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPackageDesignModelTypesResponse, self).to_map()
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
            temp_model = ListPackageDesignModelTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserBucketsRequestData(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserBucketsRequestData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserBucketsRequest(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[ListUserBucketsRequestData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserBucketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserBucketsRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class ListUserBucketsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserBucketsResponseBody, self).to_map()
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
        return self


class ListUserBucketsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserBucketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserBucketsResponse, self).to_map()
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
            temp_model = ListUserBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeSuperResolutionImageRequest(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeSuperResolutionImageRequest, self).to_map()
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: MakeSuperResolutionImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MakeSuperResolutionImageResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MakeSuperResolutionImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MakeSuperResolutionImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MakeSuperResolutionImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MakeSuperResolutionImageResponse, self).to_map()
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
            temp_model = MakeSuperResolutionImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageColorRequest(TeaModel):
    def __init__(self, color_count=None, url=None):
        self.color_count = color_count  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeImageColorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecognizeImageColorResponseBodyDataColorTemplateList(TeaModel):
    def __init__(self, color=None, label=None, percentage=None):
        self.color = color  # type: str
        self.label = label  # type: str
        self.percentage = percentage  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeImageColorResponseBodyDataColorTemplateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.label is not None:
            result['Label'] = self.label
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        return self


class RecognizeImageColorResponseBodyData(TeaModel):
    def __init__(self, color_template_list=None):
        self.color_template_list = color_template_list  # type: list[RecognizeImageColorResponseBodyDataColorTemplateList]

    def validate(self):
        if self.color_template_list:
            for k in self.color_template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeImageColorResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ColorTemplateList'] = []
        if self.color_template_list is not None:
            for k in self.color_template_list:
                result['ColorTemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.color_template_list = []
        if m.get('ColorTemplateList') is not None:
            for k in m.get('ColorTemplateList'):
                temp_model = RecognizeImageColorResponseBodyDataColorTemplateList()
                self.color_template_list.append(temp_model.from_map(k))
        return self


class RecognizeImageColorResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: RecognizeImageColorResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeImageColorResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RecognizeImageColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeImageColorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeImageColorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeImageColorResponse, self).to_map()
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
            temp_model = RecognizeImageColorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageStyleRequest(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeImageStyleRequest, self).to_map()
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


class RecognizeImageStyleResponseBodyData(TeaModel):
    def __init__(self, styles=None):
        self.styles = styles  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeImageStyleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.styles is not None:
            result['Styles'] = self.styles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        return self


class RecognizeImageStyleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: RecognizeImageStyleResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeImageStyleResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RecognizeImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeImageStyleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeImageStyleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeImageStyleResponse, self).to_map()
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
            temp_model = RecognizeImageStyleResponseBody()
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


class RecolorImageResponseBodyData(TeaModel):
    def __init__(self, image_list=None):
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
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: RecolorImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecolorImageResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RecolorImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecolorImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecolorImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecolorImageResponse, self).to_map()
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
            temp_model = RecolorImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentBodyRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SegmentBodyRequest, self).to_map()
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


class SegmentBodyResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SegmentBodyResponseBodyData, self).to_map()
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


class SegmentBodyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SegmentBodyResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SegmentBodyResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SegmentBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SegmentBodyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SegmentBodyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SegmentBodyResponse, self).to_map()
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
            temp_model = SegmentBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentCommodityRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SegmentCommodityRequest, self).to_map()
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


class SegmentCommodityResponseBodyData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SegmentCommodityResponseBodyData, self).to_map()
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


class SegmentCommodityResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: SegmentCommodityResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SegmentCommodityResponseBody, self).to_map()
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
            temp_model = SegmentCommodityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SegmentCommodityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SegmentCommodityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SegmentCommodityResponse, self).to_map()
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
            temp_model = SegmentCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentImageRequest(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SegmentImageRequest, self).to_map()
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


class SegmentImageResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SegmentImageResponseBodyData, self).to_map()
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


class SegmentImageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: SegmentImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SegmentImageResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SegmentImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SegmentImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SegmentImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SegmentImageResponse, self).to_map()
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
            temp_model = SegmentImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserBucketConfigRequestData(TeaModel):
    def __init__(self, bucket=None, region=None):
        self.bucket = bucket  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserBucketConfigRequestData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class UpdateUserBucketConfigRequest(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[UpdateUserBucketConfigRequestData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserBucketConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = UpdateUserBucketConfigRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class UpdateUserBucketConfigResponseBodyData(TeaModel):
    def __init__(self, bucket=None, region=None, region_name=None):
        self.bucket = bucket  # type: str
        self.region = region  # type: str
        self.region_name = region_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserBucketConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.region is not None:
            result['Region'] = self.region
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class UpdateUserBucketConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[UpdateUserBucketConfigResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserBucketConfigResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = UpdateUserBucketConfigResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserBucketConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserBucketConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserBucketConfigResponse, self).to_map()
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
            temp_model = UpdateUserBucketConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


