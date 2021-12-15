# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DetectCardScreenshotRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectCardScreenshotRequest, self).to_map()
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


class DetectCardScreenshotAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(DetectCardScreenshotAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectCardScreenshotResponseBodyDataSpoofResultResultMap(TeaModel):
    def __init__(self, screen_score=None, screen_threshold=None):
        self.screen_score = screen_score  # type: float
        self.screen_threshold = screen_threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectCardScreenshotResponseBodyDataSpoofResultResultMap, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_score is not None:
            result['ScreenScore'] = self.screen_score
        if self.screen_threshold is not None:
            result['ScreenThreshold'] = self.screen_threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScreenScore') is not None:
            self.screen_score = m.get('ScreenScore')
        if m.get('ScreenThreshold') is not None:
            self.screen_threshold = m.get('ScreenThreshold')
        return self


class DetectCardScreenshotResponseBodyDataSpoofResult(TeaModel):
    def __init__(self, is_spoof=None, result_map=None):
        self.is_spoof = is_spoof  # type: bool
        self.result_map = result_map  # type: DetectCardScreenshotResponseBodyDataSpoofResultResultMap

    def validate(self):
        if self.result_map:
            self.result_map.validate()

    def to_map(self):
        _map = super(DetectCardScreenshotResponseBodyDataSpoofResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_spoof is not None:
            result['IsSpoof'] = self.is_spoof
        if self.result_map is not None:
            result['ResultMap'] = self.result_map.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSpoof') is not None:
            self.is_spoof = m.get('IsSpoof')
        if m.get('ResultMap') is not None:
            temp_model = DetectCardScreenshotResponseBodyDataSpoofResultResultMap()
            self.result_map = temp_model.from_map(m['ResultMap'])
        return self


class DetectCardScreenshotResponseBodyData(TeaModel):
    def __init__(self, is_blur=None, is_card=None, spoof_result=None):
        self.is_blur = is_blur  # type: bool
        self.is_card = is_card  # type: bool
        self.spoof_result = spoof_result  # type: DetectCardScreenshotResponseBodyDataSpoofResult

    def validate(self):
        if self.spoof_result:
            self.spoof_result.validate()

    def to_map(self):
        _map = super(DetectCardScreenshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_blur is not None:
            result['IsBlur'] = self.is_blur
        if self.is_card is not None:
            result['IsCard'] = self.is_card
        if self.spoof_result is not None:
            result['SpoofResult'] = self.spoof_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBlur') is not None:
            self.is_blur = m.get('IsBlur')
        if m.get('IsCard') is not None:
            self.is_card = m.get('IsCard')
        if m.get('SpoofResult') is not None:
            temp_model = DetectCardScreenshotResponseBodyDataSpoofResult()
            self.spoof_result = temp_model.from_map(m['SpoofResult'])
        return self


class DetectCardScreenshotResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DetectCardScreenshotResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DetectCardScreenshotResponseBody, self).to_map()
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
            temp_model = DetectCardScreenshotResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectCardScreenshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectCardScreenshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectCardScreenshotResponse, self).to_map()
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
            temp_model = DetectCardScreenshotResponseBody()
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


class RecognizeAccountPageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAccountPageRequest, self).to_map()
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


class RecognizeAccountPageAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeAccountPageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeAccountPageResponseBodyDataInvalidStampAreas(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAccountPageResponseBodyDataInvalidStampAreas, self).to_map()
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


class RecognizeAccountPageResponseBodyDataOtherStampAreas(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAccountPageResponseBodyDataOtherStampAreas, self).to_map()
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


class RecognizeAccountPageResponseBodyDataRegisterStampAreas(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAccountPageResponseBodyDataRegisterStampAreas, self).to_map()
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


class RecognizeAccountPageResponseBodyDataTitleArea(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAccountPageResponseBodyDataTitleArea, self).to_map()
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


class RecognizeAccountPageResponseBodyDataUndertakeStampAreas(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAccountPageResponseBodyDataUndertakeStampAreas, self).to_map()
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


class RecognizeAccountPageResponseBodyData(TeaModel):
    def __init__(self, angle=None, birth_date=None, birth_place=None, gender=None, idnumber=None,
                 invalid_stamp_areas=None, name=None, nationality=None, native_place=None, other_stamp_areas=None,
                 register_stamp_areas=None, relation=None, title_area=None, undertake_stamp_areas=None):
        self.angle = angle  # type: float
        self.birth_date = birth_date  # type: str
        self.birth_place = birth_place  # type: str
        self.gender = gender  # type: str
        self.idnumber = idnumber  # type: str
        self.invalid_stamp_areas = invalid_stamp_areas  # type: list[RecognizeAccountPageResponseBodyDataInvalidStampAreas]
        self.name = name  # type: str
        self.nationality = nationality  # type: str
        self.native_place = native_place  # type: str
        self.other_stamp_areas = other_stamp_areas  # type: list[RecognizeAccountPageResponseBodyDataOtherStampAreas]
        self.register_stamp_areas = register_stamp_areas  # type: list[RecognizeAccountPageResponseBodyDataRegisterStampAreas]
        self.relation = relation  # type: str
        self.title_area = title_area  # type: RecognizeAccountPageResponseBodyDataTitleArea
        self.undertake_stamp_areas = undertake_stamp_areas  # type: list[RecognizeAccountPageResponseBodyDataUndertakeStampAreas]

    def validate(self):
        if self.invalid_stamp_areas:
            for k in self.invalid_stamp_areas:
                if k:
                    k.validate()
        if self.other_stamp_areas:
            for k in self.other_stamp_areas:
                if k:
                    k.validate()
        if self.register_stamp_areas:
            for k in self.register_stamp_areas:
                if k:
                    k.validate()
        if self.title_area:
            self.title_area.validate()
        if self.undertake_stamp_areas:
            for k in self.undertake_stamp_areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAccountPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.birth_place is not None:
            result['BirthPlace'] = self.birth_place
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.idnumber is not None:
            result['IDNumber'] = self.idnumber
        result['InvalidStampAreas'] = []
        if self.invalid_stamp_areas is not None:
            for k in self.invalid_stamp_areas:
                result['InvalidStampAreas'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.native_place is not None:
            result['NativePlace'] = self.native_place
        result['OtherStampAreas'] = []
        if self.other_stamp_areas is not None:
            for k in self.other_stamp_areas:
                result['OtherStampAreas'].append(k.to_map() if k else None)
        result['RegisterStampAreas'] = []
        if self.register_stamp_areas is not None:
            for k in self.register_stamp_areas:
                result['RegisterStampAreas'].append(k.to_map() if k else None)
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.title_area is not None:
            result['TitleArea'] = self.title_area.to_map()
        result['UndertakeStampAreas'] = []
        if self.undertake_stamp_areas is not None:
            for k in self.undertake_stamp_areas:
                result['UndertakeStampAreas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('BirthPlace') is not None:
            self.birth_place = m.get('BirthPlace')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('IDNumber') is not None:
            self.idnumber = m.get('IDNumber')
        self.invalid_stamp_areas = []
        if m.get('InvalidStampAreas') is not None:
            for k in m.get('InvalidStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataInvalidStampAreas()
                self.invalid_stamp_areas.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('NativePlace') is not None:
            self.native_place = m.get('NativePlace')
        self.other_stamp_areas = []
        if m.get('OtherStampAreas') is not None:
            for k in m.get('OtherStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataOtherStampAreas()
                self.other_stamp_areas.append(temp_model.from_map(k))
        self.register_stamp_areas = []
        if m.get('RegisterStampAreas') is not None:
            for k in m.get('RegisterStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataRegisterStampAreas()
                self.register_stamp_areas.append(temp_model.from_map(k))
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('TitleArea') is not None:
            temp_model = RecognizeAccountPageResponseBodyDataTitleArea()
            self.title_area = temp_model.from_map(m['TitleArea'])
        self.undertake_stamp_areas = []
        if m.get('UndertakeStampAreas') is not None:
            for k in m.get('UndertakeStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataUndertakeStampAreas()
                self.undertake_stamp_areas.append(temp_model.from_map(k))
        return self


class RecognizeAccountPageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeAccountPageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeAccountPageResponseBody, self).to_map()
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
            temp_model = RecognizeAccountPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeAccountPageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeAccountPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeAccountPageResponse, self).to_map()
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
            temp_model = RecognizeAccountPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankCardRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankCardRequest, self).to_map()
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


class RecognizeBankCardAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeBankCardAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeBankCardResponseBodyData(TeaModel):
    def __init__(self, bank_name=None, card_number=None, valid_date=None):
        self.bank_name = bank_name  # type: str
        self.card_number = card_number  # type: str
        self.valid_date = valid_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankCardResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bank_name is not None:
            result['BankName'] = self.bank_name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BankName') is not None:
            self.bank_name = m.get('BankName')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class RecognizeBankCardResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeBankCardResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeBankCardResponseBody, self).to_map()
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
            temp_model = RecognizeBankCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeBankCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBankCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBankCardResponse, self).to_map()
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
            temp_model = RecognizeBankCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessCardRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessCardRequest, self).to_map()
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


class RecognizeBusinessCardAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeBusinessCardAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeBusinessCardResponseBodyData(TeaModel):
    def __init__(self, addresses=None, cell_phone_numbers=None, companies=None, departments=None, emails=None,
                 name=None, office_phone_numbers=None, titles=None):
        self.addresses = addresses  # type: list[str]
        self.cell_phone_numbers = cell_phone_numbers  # type: list[str]
        self.companies = companies  # type: list[str]
        self.departments = departments  # type: list[str]
        self.emails = emails  # type: list[str]
        self.name = name  # type: str
        self.office_phone_numbers = office_phone_numbers  # type: list[str]
        self.titles = titles  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessCardResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.cell_phone_numbers is not None:
            result['CellPhoneNumbers'] = self.cell_phone_numbers
        if self.companies is not None:
            result['Companies'] = self.companies
        if self.departments is not None:
            result['Departments'] = self.departments
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.name is not None:
            result['Name'] = self.name
        if self.office_phone_numbers is not None:
            result['OfficePhoneNumbers'] = self.office_phone_numbers
        if self.titles is not None:
            result['Titles'] = self.titles
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('CellPhoneNumbers') is not None:
            self.cell_phone_numbers = m.get('CellPhoneNumbers')
        if m.get('Companies') is not None:
            self.companies = m.get('Companies')
        if m.get('Departments') is not None:
            self.departments = m.get('Departments')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfficePhoneNumbers') is not None:
            self.office_phone_numbers = m.get('OfficePhoneNumbers')
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        return self


class RecognizeBusinessCardResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeBusinessCardResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeBusinessCardResponseBody, self).to_map()
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
            temp_model = RecognizeBusinessCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeBusinessCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBusinessCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBusinessCardResponse, self).to_map()
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
            temp_model = RecognizeBusinessCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessLicenseRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseRequest, self).to_map()
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


class RecognizeBusinessLicenseAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeBusinessLicenseAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeBusinessLicenseResponseBodyDataEmblem(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBodyDataEmblem, self).to_map()
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


class RecognizeBusinessLicenseResponseBodyDataQRCode(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBodyDataQRCode, self).to_map()
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


class RecognizeBusinessLicenseResponseBodyDataStamp(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBodyDataStamp, self).to_map()
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


class RecognizeBusinessLicenseResponseBodyDataTitle(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBodyDataTitle, self).to_map()
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


class RecognizeBusinessLicenseResponseBodyData(TeaModel):
    def __init__(self, address=None, angle=None, business=None, capital=None, emblem=None, establish_date=None,
                 legal_person=None, name=None, qrcode=None, register_number=None, stamp=None, title=None, type=None,
                 valid_period=None):
        self.address = address  # type: str
        self.angle = angle  # type: float
        self.business = business  # type: str
        self.capital = capital  # type: str
        self.emblem = emblem  # type: RecognizeBusinessLicenseResponseBodyDataEmblem
        self.establish_date = establish_date  # type: str
        self.legal_person = legal_person  # type: str
        self.name = name  # type: str
        self.qrcode = qrcode  # type: RecognizeBusinessLicenseResponseBodyDataQRCode
        self.register_number = register_number  # type: str
        self.stamp = stamp  # type: RecognizeBusinessLicenseResponseBodyDataStamp
        self.title = title  # type: RecognizeBusinessLicenseResponseBodyDataTitle
        self.type = type  # type: str
        self.valid_period = valid_period  # type: str

    def validate(self):
        if self.emblem:
            self.emblem.validate()
        if self.qrcode:
            self.qrcode.validate()
        if self.stamp:
            self.stamp.validate()
        if self.title:
            self.title.validate()

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.business is not None:
            result['Business'] = self.business
        if self.capital is not None:
            result['Capital'] = self.capital
        if self.emblem is not None:
            result['Emblem'] = self.emblem.to_map()
        if self.establish_date is not None:
            result['EstablishDate'] = self.establish_date
        if self.legal_person is not None:
            result['LegalPerson'] = self.legal_person
        if self.name is not None:
            result['Name'] = self.name
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode.to_map()
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.stamp is not None:
            result['Stamp'] = self.stamp.to_map()
        if self.title is not None:
            result['Title'] = self.title.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.valid_period is not None:
            result['ValidPeriod'] = self.valid_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Capital') is not None:
            self.capital = m.get('Capital')
        if m.get('Emblem') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataEmblem()
            self.emblem = temp_model.from_map(m['Emblem'])
        if m.get('EstablishDate') is not None:
            self.establish_date = m.get('EstablishDate')
        if m.get('LegalPerson') is not None:
            self.legal_person = m.get('LegalPerson')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QRCode') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataQRCode()
            self.qrcode = temp_model.from_map(m['QRCode'])
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Stamp') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataStamp()
            self.stamp = temp_model.from_map(m['Stamp'])
        if m.get('Title') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataTitle()
            self.title = temp_model.from_map(m['Title'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidPeriod') is not None:
            self.valid_period = m.get('ValidPeriod')
        return self


class RecognizeBusinessLicenseResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeBusinessLicenseResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBody, self).to_map()
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
            temp_model = RecognizeBusinessLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeBusinessLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeBusinessLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponse, self).to_map()
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
            temp_model = RecognizeBusinessLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCharacterRequest(TeaModel):
    def __init__(self, image_url=None, min_height=None, output_probability=None):
        self.image_url = image_url  # type: str
        self.min_height = min_height  # type: int
        self.output_probability = output_probability  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCharacterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.output_probability is not None:
            result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')
        if m.get('OutputProbability') is not None:
            self.output_probability = m.get('OutputProbability')
        return self


class RecognizeCharacterAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, min_height=None, output_probability=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.min_height = min_height  # type: int
        self.output_probability = output_probability  # type: bool

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeCharacterAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.output_probability is not None:
            result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')
        if m.get('OutputProbability') is not None:
            self.output_probability = m.get('OutputProbability')
        return self


class RecognizeCharacterResponseBodyDataResultsTextRectangles(TeaModel):
    def __init__(self, angle=None, height=None, left=None, top=None, width=None):
        self.angle = angle  # type: int
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCharacterResponseBodyDataResultsTextRectangles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
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
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeCharacterResponseBodyDataResults(TeaModel):
    def __init__(self, probability=None, text=None, text_rectangles=None):
        self.probability = probability  # type: float
        self.text = text  # type: str
        self.text_rectangles = text_rectangles  # type: RecognizeCharacterResponseBodyDataResultsTextRectangles

    def validate(self):
        if self.text_rectangles:
            self.text_rectangles.validate()

    def to_map(self):
        _map = super(RecognizeCharacterResponseBodyDataResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.probability is not None:
            result['Probability'] = self.probability
        if self.text is not None:
            result['Text'] = self.text
        if self.text_rectangles is not None:
            result['TextRectangles'] = self.text_rectangles.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextRectangles') is not None:
            temp_model = RecognizeCharacterResponseBodyDataResultsTextRectangles()
            self.text_rectangles = temp_model.from_map(m['TextRectangles'])
        return self


class RecognizeCharacterResponseBodyData(TeaModel):
    def __init__(self, results=None):
        self.results = results  # type: list[RecognizeCharacterResponseBodyDataResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeCharacterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeCharacterResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class RecognizeCharacterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeCharacterResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeCharacterResponseBody, self).to_map()
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
            temp_model = RecognizeCharacterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeCharacterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeCharacterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCharacterResponse, self).to_map()
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
            temp_model = RecognizeCharacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeChinapassportRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeChinapassportRequest, self).to_map()
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


class RecognizeChinapassportAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeChinapassportAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeChinapassportResponseBodyData(TeaModel):
    def __init__(self, authority=None, birth_date=None, birth_day=None, birth_place=None, birth_place_raw=None,
                 country=None, expiry_date=None, expiry_day=None, issue_date=None, issue_place=None, issue_place_raw=None,
                 line_one=None, line_zero=None, name=None, name_chinese=None, name_chinese_raw=None, passport_no=None,
                 person_id=None, sex=None, source_country=None, success=None, type=None):
        self.authority = authority  # type: str
        self.birth_date = birth_date  # type: str
        self.birth_day = birth_day  # type: str
        self.birth_place = birth_place  # type: str
        self.birth_place_raw = birth_place_raw  # type: str
        self.country = country  # type: str
        self.expiry_date = expiry_date  # type: str
        self.expiry_day = expiry_day  # type: str
        self.issue_date = issue_date  # type: str
        self.issue_place = issue_place  # type: str
        self.issue_place_raw = issue_place_raw  # type: str
        self.line_one = line_one  # type: str
        self.line_zero = line_zero  # type: str
        self.name = name  # type: str
        self.name_chinese = name_chinese  # type: str
        self.name_chinese_raw = name_chinese_raw  # type: str
        self.passport_no = passport_no  # type: str
        self.person_id = person_id  # type: str
        self.sex = sex  # type: str
        self.source_country = source_country  # type: str
        self.success = success  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeChinapassportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.birth_day is not None:
            result['BirthDay'] = self.birth_day
        if self.birth_place is not None:
            result['BirthPlace'] = self.birth_place
        if self.birth_place_raw is not None:
            result['BirthPlaceRaw'] = self.birth_place_raw
        if self.country is not None:
            result['Country'] = self.country
        if self.expiry_date is not None:
            result['ExpiryDate'] = self.expiry_date
        if self.expiry_day is not None:
            result['ExpiryDay'] = self.expiry_day
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.issue_place is not None:
            result['IssuePlace'] = self.issue_place
        if self.issue_place_raw is not None:
            result['IssuePlaceRaw'] = self.issue_place_raw
        if self.line_one is not None:
            result['LineOne'] = self.line_one
        if self.line_zero is not None:
            result['LineZero'] = self.line_zero
        if self.name is not None:
            result['Name'] = self.name
        if self.name_chinese is not None:
            result['NameChinese'] = self.name_chinese
        if self.name_chinese_raw is not None:
            result['NameChineseRaw'] = self.name_chinese_raw
        if self.passport_no is not None:
            result['PassportNo'] = self.passport_no
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.source_country is not None:
            result['SourceCountry'] = self.source_country
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('BirthDay') is not None:
            self.birth_day = m.get('BirthDay')
        if m.get('BirthPlace') is not None:
            self.birth_place = m.get('BirthPlace')
        if m.get('BirthPlaceRaw') is not None:
            self.birth_place_raw = m.get('BirthPlaceRaw')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ExpiryDate') is not None:
            self.expiry_date = m.get('ExpiryDate')
        if m.get('ExpiryDay') is not None:
            self.expiry_day = m.get('ExpiryDay')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('IssuePlace') is not None:
            self.issue_place = m.get('IssuePlace')
        if m.get('IssuePlaceRaw') is not None:
            self.issue_place_raw = m.get('IssuePlaceRaw')
        if m.get('LineOne') is not None:
            self.line_one = m.get('LineOne')
        if m.get('LineZero') is not None:
            self.line_zero = m.get('LineZero')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameChinese') is not None:
            self.name_chinese = m.get('NameChinese')
        if m.get('NameChineseRaw') is not None:
            self.name_chinese_raw = m.get('NameChineseRaw')
        if m.get('PassportNo') is not None:
            self.passport_no = m.get('PassportNo')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('SourceCountry') is not None:
            self.source_country = m.get('SourceCountry')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeChinapassportResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeChinapassportResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeChinapassportResponseBody, self).to_map()
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
            temp_model = RecognizeChinapassportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeChinapassportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeChinapassportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeChinapassportResponse, self).to_map()
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
            temp_model = RecognizeChinapassportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDriverLicenseRequest(TeaModel):
    def __init__(self, image_url=None, side=None):
        self.image_url = image_url  # type: str
        self.side = side  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDriverLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDriverLicenseAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, side=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.side = side  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeDriverLicenseAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDriverLicenseResponseBodyDataBackResult(TeaModel):
    def __init__(self, archive_number=None, card_number=None, name=None, record=None):
        self.archive_number = archive_number  # type: str
        self.card_number = card_number  # type: str
        self.name = name  # type: str
        self.record = record  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDriverLicenseResponseBodyDataBackResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_number is not None:
            result['ArchiveNumber'] = self.archive_number
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.name is not None:
            result['Name'] = self.name
        if self.record is not None:
            result['Record'] = self.record
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchiveNumber') is not None:
            self.archive_number = m.get('ArchiveNumber')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        return self


class RecognizeDriverLicenseResponseBodyDataFaceResult(TeaModel):
    def __init__(self, address=None, end_date=None, gender=None, issue_date=None, issue_unit=None,
                 license_number=None, name=None, start_date=None, vehicle_type=None):
        self.address = address  # type: str
        self.end_date = end_date  # type: str
        self.gender = gender  # type: str
        self.issue_date = issue_date  # type: str
        self.issue_unit = issue_unit  # type: str
        self.license_number = license_number  # type: str
        self.name = name  # type: str
        self.start_date = start_date  # type: str
        self.vehicle_type = vehicle_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDriverLicenseResponseBodyDataFaceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.issue_unit is not None:
            result['IssueUnit'] = self.issue_unit
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.name is not None:
            result['Name'] = self.name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('IssueUnit') is not None:
            self.issue_unit = m.get('IssueUnit')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        return self


class RecognizeDriverLicenseResponseBodyData(TeaModel):
    def __init__(self, back_result=None, face_result=None):
        self.back_result = back_result  # type: RecognizeDriverLicenseResponseBodyDataBackResult
        self.face_result = face_result  # type: RecognizeDriverLicenseResponseBodyDataFaceResult

    def validate(self):
        if self.back_result:
            self.back_result.validate()
        if self.face_result:
            self.face_result.validate()

    def to_map(self):
        _map = super(RecognizeDriverLicenseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        if self.face_result is not None:
            result['FaceResult'] = self.face_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackResult') is not None:
            temp_model = RecognizeDriverLicenseResponseBodyDataBackResult()
            self.back_result = temp_model.from_map(m['BackResult'])
        if m.get('FaceResult') is not None:
            temp_model = RecognizeDriverLicenseResponseBodyDataFaceResult()
            self.face_result = temp_model.from_map(m['FaceResult'])
        return self


class RecognizeDriverLicenseResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeDriverLicenseResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeDriverLicenseResponseBody, self).to_map()
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
            temp_model = RecognizeDriverLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeDriverLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeDriverLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeDriverLicenseResponse, self).to_map()
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
            temp_model = RecognizeDriverLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDrivingLicenseRequest(TeaModel):
    def __init__(self, image_url=None, side=None):
        self.image_url = image_url  # type: str
        self.side = side  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDrivingLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDrivingLicenseAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, side=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.side = side  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeDrivingLicenseAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDrivingLicenseResponseBodyDataBackResult(TeaModel):
    def __init__(self, approved_load=None, approved_passenger_capacity=None, energy_type=None, file_number=None,
                 gross_mass=None, inspection_record=None, overall_dimension=None, plate_number=None, traction_mass=None,
                 unladen_mass=None):
        self.approved_load = approved_load  # type: str
        self.approved_passenger_capacity = approved_passenger_capacity  # type: str
        self.energy_type = energy_type  # type: str
        self.file_number = file_number  # type: str
        self.gross_mass = gross_mass  # type: str
        self.inspection_record = inspection_record  # type: str
        self.overall_dimension = overall_dimension  # type: str
        self.plate_number = plate_number  # type: str
        self.traction_mass = traction_mass  # type: str
        self.unladen_mass = unladen_mass  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponseBodyDataBackResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approved_load is not None:
            result['ApprovedLoad'] = self.approved_load
        if self.approved_passenger_capacity is not None:
            result['ApprovedPassengerCapacity'] = self.approved_passenger_capacity
        if self.energy_type is not None:
            result['EnergyType'] = self.energy_type
        if self.file_number is not None:
            result['FileNumber'] = self.file_number
        if self.gross_mass is not None:
            result['GrossMass'] = self.gross_mass
        if self.inspection_record is not None:
            result['InspectionRecord'] = self.inspection_record
        if self.overall_dimension is not None:
            result['OverallDimension'] = self.overall_dimension
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.traction_mass is not None:
            result['TractionMass'] = self.traction_mass
        if self.unladen_mass is not None:
            result['UnladenMass'] = self.unladen_mass
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovedLoad') is not None:
            self.approved_load = m.get('ApprovedLoad')
        if m.get('ApprovedPassengerCapacity') is not None:
            self.approved_passenger_capacity = m.get('ApprovedPassengerCapacity')
        if m.get('EnergyType') is not None:
            self.energy_type = m.get('EnergyType')
        if m.get('FileNumber') is not None:
            self.file_number = m.get('FileNumber')
        if m.get('GrossMass') is not None:
            self.gross_mass = m.get('GrossMass')
        if m.get('InspectionRecord') is not None:
            self.inspection_record = m.get('InspectionRecord')
        if m.get('OverallDimension') is not None:
            self.overall_dimension = m.get('OverallDimension')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('TractionMass') is not None:
            self.traction_mass = m.get('TractionMass')
        if m.get('UnladenMass') is not None:
            self.unladen_mass = m.get('UnladenMass')
        return self


class RecognizeDrivingLicenseResponseBodyDataFaceResult(TeaModel):
    def __init__(self, address=None, engine_number=None, issue_date=None, model=None, owner=None, plate_number=None,
                 register_date=None, use_character=None, vehicle_type=None, vin=None):
        self.address = address  # type: str
        self.engine_number = engine_number  # type: str
        self.issue_date = issue_date  # type: str
        self.model = model  # type: str
        self.owner = owner  # type: str
        self.plate_number = plate_number  # type: str
        self.register_date = register_date  # type: str
        self.use_character = use_character  # type: str
        self.vehicle_type = vehicle_type  # type: str
        self.vin = vin  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponseBodyDataFaceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.engine_number is not None:
            result['EngineNumber'] = self.engine_number
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.model is not None:
            result['Model'] = self.model
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.register_date is not None:
            result['RegisterDate'] = self.register_date
        if self.use_character is not None:
            result['UseCharacter'] = self.use_character
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.vin is not None:
            result['Vin'] = self.vin
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngineNumber') is not None:
            self.engine_number = m.get('EngineNumber')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('RegisterDate') is not None:
            self.register_date = m.get('RegisterDate')
        if m.get('UseCharacter') is not None:
            self.use_character = m.get('UseCharacter')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('Vin') is not None:
            self.vin = m.get('Vin')
        return self


class RecognizeDrivingLicenseResponseBodyData(TeaModel):
    def __init__(self, back_result=None, face_result=None):
        self.back_result = back_result  # type: RecognizeDrivingLicenseResponseBodyDataBackResult
        self.face_result = face_result  # type: RecognizeDrivingLicenseResponseBodyDataFaceResult

    def validate(self):
        if self.back_result:
            self.back_result.validate()
        if self.face_result:
            self.face_result.validate()

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        if self.face_result is not None:
            result['FaceResult'] = self.face_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackResult') is not None:
            temp_model = RecognizeDrivingLicenseResponseBodyDataBackResult()
            self.back_result = temp_model.from_map(m['BackResult'])
        if m.get('FaceResult') is not None:
            temp_model = RecognizeDrivingLicenseResponseBodyDataFaceResult()
            self.face_result = temp_model.from_map(m['FaceResult'])
        return self


class RecognizeDrivingLicenseResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeDrivingLicenseResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponseBody, self).to_map()
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
            temp_model = RecognizeDrivingLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeDrivingLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeDrivingLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponse, self).to_map()
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
            temp_model = RecognizeDrivingLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeIdentityCardRequest(TeaModel):
    def __init__(self, image_url=None, side=None):
        self.image_url = image_url  # type: str
        self.side = side  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdentityCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeIdentityCardAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, side=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.side = side  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeIdentityCardAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeIdentityCardResponseBodyDataBackResult(TeaModel):
    def __init__(self, end_date=None, issue=None, start_date=None):
        self.end_date = end_date  # type: str
        self.issue = issue  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyDataBackResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.issue is not None:
            result['Issue'] = self.issue
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Issue') is not None:
            self.issue = m.get('Issue')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultCardAreas(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyDataFrontResultCardAreas, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize(TeaModel):
    def __init__(self, height=None, width=None):
        self.height = height  # type: float
        self.width = width  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle(TeaModel):
    def __init__(self, angle=None, center=None, size=None):
        self.angle = angle  # type: float
        self.center = center  # type: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter
        self.size = size  # type: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize

    def validate(self):
        if self.center:
            self.center.validate()
        if self.size:
            self.size.validate()

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        if self.size is not None:
            result['Size'] = self.size.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Center') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter()
            self.center = temp_model.from_map(m['Center'])
        if m.get('Size') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize()
            self.size = temp_model.from_map(m['Size'])
        return self


class RecognizeIdentityCardResponseBodyDataFrontResult(TeaModel):
    def __init__(self, address=None, birth_date=None, card_areas=None, face_rect_vertices=None, face_rectangle=None,
                 gender=None, idnumber=None, name=None, nationality=None):
        self.address = address  # type: str
        self.birth_date = birth_date  # type: str
        self.card_areas = card_areas  # type: list[RecognizeIdentityCardResponseBodyDataFrontResultCardAreas]
        self.face_rect_vertices = face_rect_vertices  # type: list[RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices]
        self.face_rectangle = face_rectangle  # type: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle
        self.gender = gender  # type: str
        self.idnumber = idnumber  # type: str
        self.name = name  # type: str
        self.nationality = nationality  # type: str

    def validate(self):
        if self.card_areas:
            for k in self.card_areas:
                if k:
                    k.validate()
        if self.face_rect_vertices:
            for k in self.face_rect_vertices:
                if k:
                    k.validate()
        if self.face_rectangle:
            self.face_rectangle.validate()

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyDataFrontResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        result['CardAreas'] = []
        if self.card_areas is not None:
            for k in self.card_areas:
                result['CardAreas'].append(k.to_map() if k else None)
        result['FaceRectVertices'] = []
        if self.face_rect_vertices is not None:
            for k in self.face_rect_vertices:
                result['FaceRectVertices'].append(k.to_map() if k else None)
        if self.face_rectangle is not None:
            result['FaceRectangle'] = self.face_rectangle.to_map()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.idnumber is not None:
            result['IDNumber'] = self.idnumber
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        self.card_areas = []
        if m.get('CardAreas') is not None:
            for k in m.get('CardAreas'):
                temp_model = RecognizeIdentityCardResponseBodyDataFrontResultCardAreas()
                self.card_areas.append(temp_model.from_map(k))
        self.face_rect_vertices = []
        if m.get('FaceRectVertices') is not None:
            for k in m.get('FaceRectVertices'):
                temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices()
                self.face_rect_vertices.append(temp_model.from_map(k))
        if m.get('FaceRectangle') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle()
            self.face_rectangle = temp_model.from_map(m['FaceRectangle'])
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('IDNumber') is not None:
            self.idnumber = m.get('IDNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        return self


class RecognizeIdentityCardResponseBodyData(TeaModel):
    def __init__(self, back_result=None, front_result=None):
        self.back_result = back_result  # type: RecognizeIdentityCardResponseBodyDataBackResult
        self.front_result = front_result  # type: RecognizeIdentityCardResponseBodyDataFrontResult

    def validate(self):
        if self.back_result:
            self.back_result.validate()
        if self.front_result:
            self.front_result.validate()

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        if self.front_result is not None:
            result['FrontResult'] = self.front_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackResult') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataBackResult()
            self.back_result = temp_model.from_map(m['BackResult'])
        if m.get('FrontResult') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResult()
            self.front_result = temp_model.from_map(m['FrontResult'])
        return self


class RecognizeIdentityCardResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeIdentityCardResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeIdentityCardResponseBody, self).to_map()
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
            temp_model = RecognizeIdentityCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeIdentityCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeIdentityCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeIdentityCardResponse, self).to_map()
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
            temp_model = RecognizeIdentityCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeLicensePlateRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeLicensePlateRequest, self).to_map()
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


class RecognizeLicensePlateAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeLicensePlateAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeLicensePlateResponseBodyDataPlatesPositions(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeLicensePlateResponseBodyDataPlatesPositions, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeLicensePlateResponseBodyDataPlatesRoi(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h  # type: int
        self.w = w  # type: int
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeLicensePlateResponseBodyDataPlatesRoi, self).to_map()
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


class RecognizeLicensePlateResponseBodyDataPlates(TeaModel):
    def __init__(self, confidence=None, plate_number=None, plate_type=None, plate_type_confidence=None,
                 positions=None, roi=None):
        self.confidence = confidence  # type: float
        self.plate_number = plate_number  # type: str
        self.plate_type = plate_type  # type: str
        self.plate_type_confidence = plate_type_confidence  # type: float
        self.positions = positions  # type: list[RecognizeLicensePlateResponseBodyDataPlatesPositions]
        self.roi = roi  # type: RecognizeLicensePlateResponseBodyDataPlatesRoi

    def validate(self):
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()
        if self.roi:
            self.roi.validate()

    def to_map(self):
        _map = super(RecognizeLicensePlateResponseBodyDataPlates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.plate_type is not None:
            result['PlateType'] = self.plate_type
        if self.plate_type_confidence is not None:
            result['PlateTypeConfidence'] = self.plate_type_confidence
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('PlateType') is not None:
            self.plate_type = m.get('PlateType')
        if m.get('PlateTypeConfidence') is not None:
            self.plate_type_confidence = m.get('PlateTypeConfidence')
        self.positions = []
        if m.get('Positions') is not None:
            for k in m.get('Positions'):
                temp_model = RecognizeLicensePlateResponseBodyDataPlatesPositions()
                self.positions.append(temp_model.from_map(k))
        if m.get('Roi') is not None:
            temp_model = RecognizeLicensePlateResponseBodyDataPlatesRoi()
            self.roi = temp_model.from_map(m['Roi'])
        return self


class RecognizeLicensePlateResponseBodyData(TeaModel):
    def __init__(self, plates=None):
        self.plates = plates  # type: list[RecognizeLicensePlateResponseBodyDataPlates]

    def validate(self):
        if self.plates:
            for k in self.plates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeLicensePlateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Plates'] = []
        if self.plates is not None:
            for k in self.plates:
                result['Plates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.plates = []
        if m.get('Plates') is not None:
            for k in m.get('Plates'):
                temp_model = RecognizeLicensePlateResponseBodyDataPlates()
                self.plates.append(temp_model.from_map(k))
        return self


class RecognizeLicensePlateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeLicensePlateResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeLicensePlateResponseBody, self).to_map()
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
            temp_model = RecognizeLicensePlateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeLicensePlateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeLicensePlateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeLicensePlateResponse, self).to_map()
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
            temp_model = RecognizeLicensePlateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePassportMRZRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePassportMRZRequest, self).to_map()
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


class RecognizePassportMRZAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizePassportMRZAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizePassportMRZResponseBodyDataRegions(TeaModel):
    def __init__(self, band_boxes=None, content=None, detection_score=None, name=None, recognition_score=None):
        self.band_boxes = band_boxes  # type: list[float]
        self.content = content  # type: str
        self.detection_score = detection_score  # type: float
        self.name = name  # type: str
        self.recognition_score = recognition_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePassportMRZResponseBodyDataRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_boxes is not None:
            result['BandBoxes'] = self.band_boxes
        if self.content is not None:
            result['Content'] = self.content
        if self.detection_score is not None:
            result['DetectionScore'] = self.detection_score
        if self.name is not None:
            result['Name'] = self.name
        if self.recognition_score is not None:
            result['RecognitionScore'] = self.recognition_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandBoxes') is not None:
            self.band_boxes = m.get('BandBoxes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DetectionScore') is not None:
            self.detection_score = m.get('DetectionScore')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecognitionScore') is not None:
            self.recognition_score = m.get('RecognitionScore')
        return self


class RecognizePassportMRZResponseBodyData(TeaModel):
    def __init__(self, regions=None):
        self.regions = regions  # type: list[RecognizePassportMRZResponseBodyDataRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizePassportMRZResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = RecognizePassportMRZResponseBodyDataRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class RecognizePassportMRZResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizePassportMRZResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizePassportMRZResponseBody, self).to_map()
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
            temp_model = RecognizePassportMRZResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizePassportMRZResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizePassportMRZResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizePassportMRZResponse, self).to_map()
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
            temp_model = RecognizePassportMRZResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePdfRequest(TeaModel):
    def __init__(self, file_url=None):
        # A short description of struct
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePdfRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        return self


class RecognizePdfAdvanceRequest(TeaModel):
    def __init__(self, file_urlobject=None):
        self.file_urlobject = file_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')

    def to_map(self):
        _map = super(RecognizePdfAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_urlobject is not None:
            result['FileURLObject'] = self.file_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURLObject') is not None:
            self.file_urlobject = m.get('FileURLObject')
        return self


class RecognizePdfResponseBodyDataWordsInfoPositions(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePdfResponseBodyDataWordsInfoPositions, self).to_map()
        if _map is not None:
            return _map

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


class RecognizePdfResponseBodyDataWordsInfo(TeaModel):
    def __init__(self, angle=None, height=None, positions=None, width=None, word=None, x=None, y=None):
        self.angle = angle  # type: long
        self.height = height  # type: long
        self.positions = positions  # type: list[RecognizePdfResponseBodyDataWordsInfoPositions]
        self.width = width  # type: long
        self.word = word  # type: str
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizePdfResponseBodyDataWordsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.height is not None:
            result['Height'] = self.height
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        if self.word is not None:
            result['Word'] = self.word
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        self.positions = []
        if m.get('Positions') is not None:
            for k in m.get('Positions'):
                temp_model = RecognizePdfResponseBodyDataWordsInfoPositions()
                self.positions.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizePdfResponseBodyData(TeaModel):
    def __init__(self, angle=None, height=None, org_height=None, org_width=None, page_index=None, width=None,
                 words_info=None):
        self.angle = angle  # type: long
        self.height = height  # type: long
        self.org_height = org_height  # type: long
        self.org_width = org_width  # type: long
        self.page_index = page_index  # type: long
        self.width = width  # type: long
        self.words_info = words_info  # type: list[RecognizePdfResponseBodyDataWordsInfo]

    def validate(self):
        if self.words_info:
            for k in self.words_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizePdfResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.height is not None:
            result['Height'] = self.height
        if self.org_height is not None:
            result['OrgHeight'] = self.org_height
        if self.org_width is not None:
            result['OrgWidth'] = self.org_width
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.width is not None:
            result['Width'] = self.width
        result['WordsInfo'] = []
        if self.words_info is not None:
            for k in self.words_info:
                result['WordsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OrgHeight') is not None:
            self.org_height = m.get('OrgHeight')
        if m.get('OrgWidth') is not None:
            self.org_width = m.get('OrgWidth')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        self.words_info = []
        if m.get('WordsInfo') is not None:
            for k in m.get('WordsInfo'):
                temp_model = RecognizePdfResponseBodyDataWordsInfo()
                self.words_info.append(temp_model.from_map(k))
        return self


class RecognizePdfResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizePdfResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizePdfResponseBody, self).to_map()
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
            temp_model = RecognizePdfResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizePdfResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizePdfResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizePdfResponse, self).to_map()
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
            temp_model = RecognizePdfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePoiNameRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePoiNameRequest, self).to_map()
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


class RecognizePoiNameAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizePoiNameAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizePoiNameResponseBodyDataSignboardsTexts(TeaModel):
    def __init__(self, label=None, points=None, score=None, tag=None, type=None):
        self.label = label  # type: str
        self.points = points  # type: list[int]
        self.score = score  # type: float
        self.tag = tag  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePoiNameResponseBodyDataSignboardsTexts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.points is not None:
            result['Points'] = self.points
        if self.score is not None:
            result['Score'] = self.score
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizePoiNameResponseBodyDataSignboards(TeaModel):
    def __init__(self, texts=None):
        self.texts = texts  # type: list[RecognizePoiNameResponseBodyDataSignboardsTexts]

    def validate(self):
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizePoiNameResponseBodyDataSignboards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = RecognizePoiNameResponseBodyDataSignboardsTexts()
                self.texts.append(temp_model.from_map(k))
        return self


class RecognizePoiNameResponseBodyDataSummary(TeaModel):
    def __init__(self, brand=None, score=None):
        self.brand = brand  # type: str
        self.score = score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePoiNameResponseBodyDataSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class RecognizePoiNameResponseBodyData(TeaModel):
    def __init__(self, signboards=None, summary=None):
        self.signboards = signboards  # type: list[RecognizePoiNameResponseBodyDataSignboards]
        self.summary = summary  # type: RecognizePoiNameResponseBodyDataSummary

    def validate(self):
        if self.signboards:
            for k in self.signboards:
                if k:
                    k.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        _map = super(RecognizePoiNameResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Signboards'] = []
        if self.signboards is not None:
            for k in self.signboards:
                result['Signboards'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.signboards = []
        if m.get('Signboards') is not None:
            for k in m.get('Signboards'):
                temp_model = RecognizePoiNameResponseBodyDataSignboards()
                self.signboards.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            temp_model = RecognizePoiNameResponseBodyDataSummary()
            self.summary = temp_model.from_map(m['Summary'])
        return self


class RecognizePoiNameResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizePoiNameResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizePoiNameResponseBody, self).to_map()
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
            temp_model = RecognizePoiNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizePoiNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizePoiNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizePoiNameResponse, self).to_map()
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
            temp_model = RecognizePoiNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQrCodeRequestTasks(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQrCodeRequestTasks, self).to_map()
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


class RecognizeQrCodeRequest(TeaModel):
    def __init__(self, tasks=None):
        self.tasks = tasks  # type: list[RecognizeQrCodeRequestTasks]

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeQrCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = RecognizeQrCodeRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class RecognizeQrCodeResponseBodyDataElementsResults(TeaModel):
    def __init__(self, label=None, qr_codes_data=None, rate=None, suggestion=None):
        self.label = label  # type: str
        self.qr_codes_data = qr_codes_data  # type: list[str]
        self.rate = rate  # type: float
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQrCodeResponseBodyDataElementsResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.qr_codes_data is not None:
            result['QrCodesData'] = self.qr_codes_data
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('QrCodesData') is not None:
            self.qr_codes_data = m.get('QrCodesData')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class RecognizeQrCodeResponseBodyDataElements(TeaModel):
    def __init__(self, image_url=None, results=None, task_id=None):
        self.image_url = image_url  # type: str
        self.results = results  # type: list[RecognizeQrCodeResponseBodyDataElementsResults]
        self.task_id = task_id  # type: str

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeQrCodeResponseBodyDataElements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeQrCodeResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RecognizeQrCodeResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[RecognizeQrCodeResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeQrCodeResponseBodyData, self).to_map()
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
                temp_model = RecognizeQrCodeResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeQrCodeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeQrCodeResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeQrCodeResponseBody, self).to_map()
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
            temp_model = RecognizeQrCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeQrCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeQrCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeQrCodeResponse, self).to_map()
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
            temp_model = RecognizeQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQuotaInvoiceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceRequest, self).to_map()
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


class RecognizeQuotaInvoiceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeQuotaInvoiceResponseBodyDataContent(TeaModel):
    def __init__(self, invoice_amount=None, invoice_code=None, invoice_details=None, invoice_no=None,
                 sum_amount=None):
        self.invoice_amount = invoice_amount  # type: str
        self.invoice_code = invoice_code  # type: str
        self.invoice_details = invoice_details  # type: str
        self.invoice_no = invoice_no  # type: str
        self.sum_amount = sum_amount  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponseBodyDataContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_details is not None:
            result['InvoiceDetails'] = self.invoice_details
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.sum_amount is not None:
            result['SumAmount'] = self.sum_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDetails') is not None:
            self.invoice_details = m.get('InvoiceDetails')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('SumAmount') is not None:
            self.sum_amount = m.get('SumAmount')
        return self


class RecognizeQuotaInvoiceResponseBodyDataKeyValueInfosValuePositions(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponseBodyDataKeyValueInfosValuePositions, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeQuotaInvoiceResponseBodyDataKeyValueInfos(TeaModel):
    def __init__(self, key=None, value=None, value_positions=None, value_score=None):
        self.key = key  # type: str
        self.value = value  # type: str
        self.value_positions = value_positions  # type: list[RecognizeQuotaInvoiceResponseBodyDataKeyValueInfosValuePositions]
        self.value_score = value_score  # type: float

    def validate(self):
        if self.value_positions:
            for k in self.value_positions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponseBodyDataKeyValueInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        result['ValuePositions'] = []
        if self.value_positions is not None:
            for k in self.value_positions:
                result['ValuePositions'].append(k.to_map() if k else None)
        if self.value_score is not None:
            result['ValueScore'] = self.value_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        self.value_positions = []
        if m.get('ValuePositions') is not None:
            for k in m.get('ValuePositions'):
                temp_model = RecognizeQuotaInvoiceResponseBodyDataKeyValueInfosValuePositions()
                self.value_positions.append(temp_model.from_map(k))
        if m.get('ValueScore') is not None:
            self.value_score = m.get('ValueScore')
        return self


class RecognizeQuotaInvoiceResponseBodyData(TeaModel):
    def __init__(self, angle=None, content=None, height=None, key_value_infos=None, org_height=None, org_width=None,
                 width=None):
        self.angle = angle  # type: long
        self.content = content  # type: RecognizeQuotaInvoiceResponseBodyDataContent
        self.height = height  # type: long
        self.key_value_infos = key_value_infos  # type: list[RecognizeQuotaInvoiceResponseBodyDataKeyValueInfos]
        self.org_height = org_height  # type: long
        self.org_width = org_width  # type: long
        self.width = width  # type: long

    def validate(self):
        if self.content:
            self.content.validate()
        if self.key_value_infos:
            for k in self.key_value_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.height is not None:
            result['Height'] = self.height
        result['KeyValueInfos'] = []
        if self.key_value_infos is not None:
            for k in self.key_value_infos:
                result['KeyValueInfos'].append(k.to_map() if k else None)
        if self.org_height is not None:
            result['OrgHeight'] = self.org_height
        if self.org_width is not None:
            result['OrgWidth'] = self.org_width
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Content') is not None:
            temp_model = RecognizeQuotaInvoiceResponseBodyDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Height') is not None:
            self.height = m.get('Height')
        self.key_value_infos = []
        if m.get('KeyValueInfos') is not None:
            for k in m.get('KeyValueInfos'):
                temp_model = RecognizeQuotaInvoiceResponseBodyDataKeyValueInfos()
                self.key_value_infos.append(temp_model.from_map(k))
        if m.get('OrgHeight') is not None:
            self.org_height = m.get('OrgHeight')
        if m.get('OrgWidth') is not None:
            self.org_width = m.get('OrgWidth')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeQuotaInvoiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeQuotaInvoiceResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponseBody, self).to_map()
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
            temp_model = RecognizeQuotaInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeQuotaInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeQuotaInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponse, self).to_map()
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
            temp_model = RecognizeQuotaInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeStampRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeStampRequest, self).to_map()
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


class RecognizeStampAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeStampAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeStampResponseBodyDataResultsGeneralText(TeaModel):
    def __init__(self, confidence=None, content=None):
        self.confidence = confidence  # type: float
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeStampResponseBodyDataResultsGeneralText, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class RecognizeStampResponseBodyDataResultsRoi(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeStampResponseBodyDataResultsRoi, self).to_map()
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


class RecognizeStampResponseBodyDataResultsText(TeaModel):
    def __init__(self, confidence=None, content=None):
        self.confidence = confidence  # type: float
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeStampResponseBodyDataResultsText, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class RecognizeStampResponseBodyDataResults(TeaModel):
    def __init__(self, general_text=None, roi=None, text=None):
        self.general_text = general_text  # type: list[RecognizeStampResponseBodyDataResultsGeneralText]
        self.roi = roi  # type: RecognizeStampResponseBodyDataResultsRoi
        self.text = text  # type: RecognizeStampResponseBodyDataResultsText

    def validate(self):
        if self.general_text:
            for k in self.general_text:
                if k:
                    k.validate()
        if self.roi:
            self.roi.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super(RecognizeStampResponseBodyDataResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GeneralText'] = []
        if self.general_text is not None:
            for k in self.general_text:
                result['GeneralText'].append(k.to_map() if k else None)
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        if self.text is not None:
            result['Text'] = self.text.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.general_text = []
        if m.get('GeneralText') is not None:
            for k in m.get('GeneralText'):
                temp_model = RecognizeStampResponseBodyDataResultsGeneralText()
                self.general_text.append(temp_model.from_map(k))
        if m.get('Roi') is not None:
            temp_model = RecognizeStampResponseBodyDataResultsRoi()
            self.roi = temp_model.from_map(m['Roi'])
        if m.get('Text') is not None:
            temp_model = RecognizeStampResponseBodyDataResultsText()
            self.text = temp_model.from_map(m['Text'])
        return self


class RecognizeStampResponseBodyData(TeaModel):
    def __init__(self, results=None):
        self.results = results  # type: list[RecognizeStampResponseBodyDataResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeStampResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeStampResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class RecognizeStampResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeStampResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeStampResponseBody, self).to_map()
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
            temp_model = RecognizeStampResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeStampResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeStampResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeStampResponse, self).to_map()
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
            temp_model = RecognizeStampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTableRequest(TeaModel):
    def __init__(self, assure_direction=None, has_line=None, image_url=None, output_format=None,
                 skip_detection=None, use_finance_model=None):
        self.assure_direction = assure_direction  # type: bool
        self.has_line = has_line  # type: bool
        self.image_url = image_url  # type: str
        self.output_format = output_format  # type: str
        self.skip_detection = skip_detection  # type: bool
        self.use_finance_model = use_finance_model  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assure_direction is not None:
            result['AssureDirection'] = self.assure_direction
        if self.has_line is not None:
            result['HasLine'] = self.has_line
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.skip_detection is not None:
            result['SkipDetection'] = self.skip_detection
        if self.use_finance_model is not None:
            result['UseFinanceModel'] = self.use_finance_model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssureDirection') is not None:
            self.assure_direction = m.get('AssureDirection')
        if m.get('HasLine') is not None:
            self.has_line = m.get('HasLine')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('SkipDetection') is not None:
            self.skip_detection = m.get('SkipDetection')
        if m.get('UseFinanceModel') is not None:
            self.use_finance_model = m.get('UseFinanceModel')
        return self


class RecognizeTableAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, assure_direction=None, has_line=None, output_format=None,
                 skip_detection=None, use_finance_model=None):
        self.image_urlobject = image_urlobject  # type: READABLE
        self.assure_direction = assure_direction  # type: bool
        self.has_line = has_line  # type: bool
        self.output_format = output_format  # type: str
        self.skip_detection = skip_detection  # type: bool
        self.use_finance_model = use_finance_model  # type: bool

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeTableAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.assure_direction is not None:
            result['AssureDirection'] = self.assure_direction
        if self.has_line is not None:
            result['HasLine'] = self.has_line
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.skip_detection is not None:
            result['SkipDetection'] = self.skip_detection
        if self.use_finance_model is not None:
            result['UseFinanceModel'] = self.use_finance_model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('AssureDirection') is not None:
            self.assure_direction = m.get('AssureDirection')
        if m.get('HasLine') is not None:
            self.has_line = m.get('HasLine')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('SkipDetection') is not None:
            self.skip_detection = m.get('SkipDetection')
        if m.get('UseFinanceModel') is not None:
            self.use_finance_model = m.get('UseFinanceModel')
        return self


class RecognizeTableResponseBodyDataTablesTableRowsTableColumns(TeaModel):
    def __init__(self, end_column=None, end_row=None, height=None, start_column=None, start_row=None, texts=None,
                 width=None):
        self.end_column = end_column  # type: int
        self.end_row = end_row  # type: int
        self.height = height  # type: int
        self.start_column = start_column  # type: int
        self.start_row = start_row  # type: int
        self.texts = texts  # type: list[str]
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTableResponseBodyDataTablesTableRowsTableColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_column is not None:
            result['EndColumn'] = self.end_column
        if self.end_row is not None:
            result['EndRow'] = self.end_row
        if self.height is not None:
            result['Height'] = self.height
        if self.start_column is not None:
            result['StartColumn'] = self.start_column
        if self.start_row is not None:
            result['StartRow'] = self.start_row
        if self.texts is not None:
            result['Texts'] = self.texts
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndColumn') is not None:
            self.end_column = m.get('EndColumn')
        if m.get('EndRow') is not None:
            self.end_row = m.get('EndRow')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('StartColumn') is not None:
            self.start_column = m.get('StartColumn')
        if m.get('StartRow') is not None:
            self.start_row = m.get('StartRow')
        if m.get('Texts') is not None:
            self.texts = m.get('Texts')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeTableResponseBodyDataTablesTableRows(TeaModel):
    def __init__(self, table_columns=None):
        self.table_columns = table_columns  # type: list[RecognizeTableResponseBodyDataTablesTableRowsTableColumns]

    def validate(self):
        if self.table_columns:
            for k in self.table_columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTableResponseBodyDataTablesTableRows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TableColumns'] = []
        if self.table_columns is not None:
            for k in self.table_columns:
                result['TableColumns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table_columns = []
        if m.get('TableColumns') is not None:
            for k in m.get('TableColumns'):
                temp_model = RecognizeTableResponseBodyDataTablesTableRowsTableColumns()
                self.table_columns.append(temp_model.from_map(k))
        return self


class RecognizeTableResponseBodyDataTables(TeaModel):
    def __init__(self, head=None, table_rows=None, tail=None):
        self.head = head  # type: list[str]
        self.table_rows = table_rows  # type: list[RecognizeTableResponseBodyDataTablesTableRows]
        self.tail = tail  # type: list[str]

    def validate(self):
        if self.table_rows:
            for k in self.table_rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTableResponseBodyDataTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.head is not None:
            result['Head'] = self.head
        result['TableRows'] = []
        if self.table_rows is not None:
            for k in self.table_rows:
                result['TableRows'].append(k.to_map() if k else None)
        if self.tail is not None:
            result['Tail'] = self.tail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Head') is not None:
            self.head = m.get('Head')
        self.table_rows = []
        if m.get('TableRows') is not None:
            for k in m.get('TableRows'):
                temp_model = RecognizeTableResponseBodyDataTablesTableRows()
                self.table_rows.append(temp_model.from_map(k))
        if m.get('Tail') is not None:
            self.tail = m.get('Tail')
        return self


class RecognizeTableResponseBodyData(TeaModel):
    def __init__(self, file_content=None, tables=None):
        self.file_content = file_content  # type: str
        self.tables = tables  # type: list[RecognizeTableResponseBodyDataTables]

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTableResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_content is not None:
            result['FileContent'] = self.file_content
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = RecognizeTableResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class RecognizeTableResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeTableResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeTableResponseBody, self).to_map()
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
            temp_model = RecognizeTableResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeTableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTableResponse, self).to_map()
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
            temp_model = RecognizeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTakeoutOrderRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTakeoutOrderRequest, self).to_map()
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


class RecognizeTakeoutOrderAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeTakeoutOrderAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTakeoutOrderResponseBodyDataElements(TeaModel):
    def __init__(self, boxes=None, name=None, score=None, value=None):
        self.boxes = boxes  # type: list[int]
        self.name = name  # type: str
        self.score = score  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTakeoutOrderResponseBodyDataElements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RecognizeTakeoutOrderResponseBodyData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements  # type: list[RecognizeTakeoutOrderResponseBodyDataElements]

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTakeoutOrderResponseBodyData, self).to_map()
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
                temp_model = RecognizeTakeoutOrderResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeTakeoutOrderResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeTakeoutOrderResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeTakeoutOrderResponseBody, self).to_map()
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
            temp_model = RecognizeTakeoutOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeTakeoutOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTakeoutOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTakeoutOrderResponse, self).to_map()
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
            temp_model = RecognizeTakeoutOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTaxiInvoiceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceRequest, self).to_map()
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


class RecognizeTaxiInvoiceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h  # type: float
        self.w = w  # type: float
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi, self).to_map()
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


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize(TeaModel):
    def __init__(self, h=None, w=None):
        self.h = h  # type: float
        self.w = w  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi(TeaModel):
    def __init__(self, angle=None, center=None, size=None):
        self.angle = angle  # type: float
        self.center = center  # type: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter
        self.size = size  # type: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize

    def validate(self):
        if self.center:
            self.center.validate()
        if self.size:
            self.size.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        if self.size is not None:
            result['Size'] = self.size.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Center') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter()
            self.center = temp_model.from_map(m['Center'])
        if m.get('Size') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize()
            self.size = temp_model.from_map(m['Size'])
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItems(TeaModel):
    def __init__(self, item_roi=None, text=None):
        self.item_roi = item_roi  # type: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi
        self.text = text  # type: str

    def validate(self):
        if self.item_roi:
            self.item_roi.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBodyDataInvoicesItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_roi is not None:
            result['ItemRoi'] = self.item_roi.to_map()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemRoi') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi()
            self.item_roi = temp_model.from_map(m['ItemRoi'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoices(TeaModel):
    def __init__(self, invoice_roi=None, items=None, rotate_type=None):
        self.invoice_roi = invoice_roi  # type: RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi
        self.items = items  # type: list[RecognizeTaxiInvoiceResponseBodyDataInvoicesItems]
        self.rotate_type = rotate_type  # type: int

    def validate(self):
        if self.invoice_roi:
            self.invoice_roi.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBodyDataInvoices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoice_roi is not None:
            result['InvoiceRoi'] = self.invoice_roi.to_map()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.rotate_type is not None:
            result['RotateType'] = self.rotate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvoiceRoi') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi()
            self.invoice_roi = temp_model.from_map(m['InvoiceRoi'])
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RotateType') is not None:
            self.rotate_type = m.get('RotateType')
        return self


class RecognizeTaxiInvoiceResponseBodyData(TeaModel):
    def __init__(self, invoices=None):
        self.invoices = invoices  # type: list[RecognizeTaxiInvoiceResponseBodyDataInvoices]

    def validate(self):
        if self.invoices:
            for k in self.invoices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Invoices'] = []
        if self.invoices is not None:
            for k in self.invoices:
                result['Invoices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invoices = []
        if m.get('Invoices') is not None:
            for k in m.get('Invoices'):
                temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoices()
                self.invoices.append(temp_model.from_map(k))
        return self


class RecognizeTaxiInvoiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeTaxiInvoiceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBody, self).to_map()
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
            temp_model = RecognizeTaxiInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeTaxiInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTaxiInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponse, self).to_map()
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
            temp_model = RecognizeTaxiInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTicketInvoiceRequest(TeaModel):
    def __init__(self, image_url=None):
        # A short description of struct
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTicketInvoiceRequest, self).to_map()
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


class RecognizeTicketInvoiceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeTicketInvoiceAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTicketInvoiceResponseBodyDataResultsContent(TeaModel):
    def __init__(self, anti_fake_code=None, invoice_code=None, invoice_date=None, invoice_number=None,
                 payee_name=None, payee_register_no=None, payer_name=None, payer_register_no=None, sum_amount=None):
        self.anti_fake_code = anti_fake_code  # type: str
        self.invoice_code = invoice_code  # type: str
        self.invoice_date = invoice_date  # type: str
        self.invoice_number = invoice_number  # type: str
        self.payee_name = payee_name  # type: str
        self.payee_register_no = payee_register_no  # type: str
        self.payer_name = payer_name  # type: str
        self.payer_register_no = payer_register_no  # type: str
        self.sum_amount = sum_amount  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponseBodyDataResultsContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_fake_code is not None:
            result['AntiFakeCode'] = self.anti_fake_code
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_number is not None:
            result['InvoiceNumber'] = self.invoice_number
        if self.payee_name is not None:
            result['PayeeName'] = self.payee_name
        if self.payee_register_no is not None:
            result['PayeeRegisterNo'] = self.payee_register_no
        if self.payer_name is not None:
            result['PayerName'] = self.payer_name
        if self.payer_register_no is not None:
            result['PayerRegisterNo'] = self.payer_register_no
        if self.sum_amount is not None:
            result['SumAmount'] = self.sum_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AntiFakeCode') is not None:
            self.anti_fake_code = m.get('AntiFakeCode')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceNumber') is not None:
            self.invoice_number = m.get('InvoiceNumber')
        if m.get('PayeeName') is not None:
            self.payee_name = m.get('PayeeName')
        if m.get('PayeeRegisterNo') is not None:
            self.payee_register_no = m.get('PayeeRegisterNo')
        if m.get('PayerName') is not None:
            self.payer_name = m.get('PayerName')
        if m.get('PayerRegisterNo') is not None:
            self.payer_register_no = m.get('PayerRegisterNo')
        if m.get('SumAmount') is not None:
            self.sum_amount = m.get('SumAmount')
        return self


class RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfosValuePositions(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfosValuePositions, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfos(TeaModel):
    def __init__(self, key=None, value=None, value_positions=None, value_score=None):
        self.key = key  # type: str
        self.value = value  # type: str
        self.value_positions = value_positions  # type: list[RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfosValuePositions]
        self.value_score = value_score  # type: float

    def validate(self):
        if self.value_positions:
            for k in self.value_positions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        result['ValuePositions'] = []
        if self.value_positions is not None:
            for k in self.value_positions:
                result['ValuePositions'].append(k.to_map() if k else None)
        if self.value_score is not None:
            result['ValueScore'] = self.value_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        self.value_positions = []
        if m.get('ValuePositions') is not None:
            for k in m.get('ValuePositions'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfosValuePositions()
                self.value_positions.append(temp_model.from_map(k))
        if m.get('ValueScore') is not None:
            self.value_score = m.get('ValueScore')
        return self


class RecognizeTicketInvoiceResponseBodyDataResultsSliceRectangle(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponseBodyDataResultsSliceRectangle, self).to_map()
        if _map is not None:
            return _map

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


class RecognizeTicketInvoiceResponseBodyDataResults(TeaModel):
    def __init__(self, content=None, index=None, key_value_infos=None, slice_rectangle=None, type=None):
        self.content = content  # type: RecognizeTicketInvoiceResponseBodyDataResultsContent
        self.index = index  # type: long
        self.key_value_infos = key_value_infos  # type: list[RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfos]
        self.slice_rectangle = slice_rectangle  # type: list[RecognizeTicketInvoiceResponseBodyDataResultsSliceRectangle]
        self.type = type  # type: str

    def validate(self):
        if self.content:
            self.content.validate()
        if self.key_value_infos:
            for k in self.key_value_infos:
                if k:
                    k.validate()
        if self.slice_rectangle:
            for k in self.slice_rectangle:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponseBodyDataResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.index is not None:
            result['Index'] = self.index
        result['KeyValueInfos'] = []
        if self.key_value_infos is not None:
            for k in self.key_value_infos:
                result['KeyValueInfos'].append(k.to_map() if k else None)
        result['SliceRectangle'] = []
        if self.slice_rectangle is not None:
            for k in self.slice_rectangle:
                result['SliceRectangle'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = RecognizeTicketInvoiceResponseBodyDataResultsContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.key_value_infos = []
        if m.get('KeyValueInfos') is not None:
            for k in m.get('KeyValueInfos'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfos()
                self.key_value_infos.append(temp_model.from_map(k))
        self.slice_rectangle = []
        if m.get('SliceRectangle') is not None:
            for k in m.get('SliceRectangle'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResultsSliceRectangle()
                self.slice_rectangle.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeTicketInvoiceResponseBodyData(TeaModel):
    def __init__(self, count=None, height=None, org_height=None, org_width=None, results=None, width=None):
        self.count = count  # type: long
        self.height = height  # type: long
        self.org_height = org_height  # type: long
        self.org_width = org_width  # type: long
        self.results = results  # type: list[RecognizeTicketInvoiceResponseBodyDataResults]
        self.width = width  # type: long

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.height is not None:
            result['Height'] = self.height
        if self.org_height is not None:
            result['OrgHeight'] = self.org_height
        if self.org_width is not None:
            result['OrgWidth'] = self.org_width
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OrgHeight') is not None:
            self.org_height = m.get('OrgHeight')
        if m.get('OrgWidth') is not None:
            self.org_width = m.get('OrgWidth')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeTicketInvoiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeTicketInvoiceResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponseBody, self).to_map()
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
            temp_model = RecognizeTicketInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeTicketInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTicketInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTicketInvoiceResponse, self).to_map()
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
            temp_model = RecognizeTicketInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTrainTicketRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTrainTicketRequest, self).to_map()
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


class RecognizeTrainTicketAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeTrainTicketAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTrainTicketResponseBodyData(TeaModel):
    def __init__(self, date=None, departure_station=None, destination=None, level=None, name=None, number=None,
                 price=None, seat=None):
        self.date = date  # type: str
        self.departure_station = departure_station  # type: str
        self.destination = destination  # type: str
        self.level = level  # type: str
        self.name = name  # type: str
        self.number = number  # type: str
        self.price = price  # type: float
        self.seat = seat  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTrainTicketResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.departure_station is not None:
            result['DepartureStation'] = self.departure_station
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.price is not None:
            result['Price'] = self.price
        if self.seat is not None:
            result['Seat'] = self.seat
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DepartureStation') is not None:
            self.departure_station = m.get('DepartureStation')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Seat') is not None:
            self.seat = m.get('Seat')
        return self


class RecognizeTrainTicketResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeTrainTicketResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeTrainTicketResponseBody, self).to_map()
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
            temp_model = RecognizeTrainTicketResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeTrainTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeTrainTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTrainTicketResponse, self).to_map()
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
            temp_model = RecognizeTrainTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVATInvoiceRequest(TeaModel):
    def __init__(self, file_type=None, file_url=None):
        self.file_type = file_type  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVATInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        return self


class RecognizeVATInvoiceAdvanceRequest(TeaModel):
    def __init__(self, file_urlobject=None, file_type=None):
        self.file_urlobject = file_urlobject  # type: READABLE
        self.file_type = file_type  # type: str

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')

    def to_map(self):
        _map = super(RecognizeVATInvoiceAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_urlobject is not None:
            result['FileURLObject'] = self.file_urlobject
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURLObject') is not None:
            self.file_urlobject = m.get('FileURLObject')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class RecognizeVATInvoiceResponseBodyDataBox(TeaModel):
    def __init__(self, checkers=None, clerks=None, invoice_amounts=None, invoice_codes=None, invoice_dates=None,
                 invoice_fake_codes=None, invoice_noes=None, payee_addresses=None, payee_bank_names=None, payee_names=None,
                 payee_register_noes=None, payees=None, payer_addresses=None, payer_bank_names=None, payer_names=None,
                 payer_register_noes=None, sum_amounts=None, tax_amounts=None, without_tax_amounts=None):
        self.checkers = checkers  # type: list[float]
        self.clerks = clerks  # type: list[float]
        self.invoice_amounts = invoice_amounts  # type: list[float]
        self.invoice_codes = invoice_codes  # type: list[float]
        self.invoice_dates = invoice_dates  # type: list[float]
        self.invoice_fake_codes = invoice_fake_codes  # type: list[float]
        self.invoice_noes = invoice_noes  # type: list[float]
        self.payee_addresses = payee_addresses  # type: list[float]
        self.payee_bank_names = payee_bank_names  # type: list[float]
        self.payee_names = payee_names  # type: list[float]
        self.payee_register_noes = payee_register_noes  # type: list[float]
        self.payees = payees  # type: list[float]
        self.payer_addresses = payer_addresses  # type: list[float]
        self.payer_bank_names = payer_bank_names  # type: list[float]
        self.payer_names = payer_names  # type: list[float]
        self.payer_register_noes = payer_register_noes  # type: list[float]
        self.sum_amounts = sum_amounts  # type: list[float]
        self.tax_amounts = tax_amounts  # type: list[float]
        self.without_tax_amounts = without_tax_amounts  # type: list[float]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVATInvoiceResponseBodyDataBox, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkers is not None:
            result['Checkers'] = self.checkers
        if self.clerks is not None:
            result['Clerks'] = self.clerks
        if self.invoice_amounts is not None:
            result['InvoiceAmounts'] = self.invoice_amounts
        if self.invoice_codes is not None:
            result['InvoiceCodes'] = self.invoice_codes
        if self.invoice_dates is not None:
            result['InvoiceDates'] = self.invoice_dates
        if self.invoice_fake_codes is not None:
            result['InvoiceFakeCodes'] = self.invoice_fake_codes
        if self.invoice_noes is not None:
            result['InvoiceNoes'] = self.invoice_noes
        if self.payee_addresses is not None:
            result['PayeeAddresses'] = self.payee_addresses
        if self.payee_bank_names is not None:
            result['PayeeBankNames'] = self.payee_bank_names
        if self.payee_names is not None:
            result['PayeeNames'] = self.payee_names
        if self.payee_register_noes is not None:
            result['PayeeRegisterNoes'] = self.payee_register_noes
        if self.payees is not None:
            result['Payees'] = self.payees
        if self.payer_addresses is not None:
            result['PayerAddresses'] = self.payer_addresses
        if self.payer_bank_names is not None:
            result['PayerBankNames'] = self.payer_bank_names
        if self.payer_names is not None:
            result['PayerNames'] = self.payer_names
        if self.payer_register_noes is not None:
            result['PayerRegisterNoes'] = self.payer_register_noes
        if self.sum_amounts is not None:
            result['SumAmounts'] = self.sum_amounts
        if self.tax_amounts is not None:
            result['TaxAmounts'] = self.tax_amounts
        if self.without_tax_amounts is not None:
            result['WithoutTaxAmounts'] = self.without_tax_amounts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Checkers') is not None:
            self.checkers = m.get('Checkers')
        if m.get('Clerks') is not None:
            self.clerks = m.get('Clerks')
        if m.get('InvoiceAmounts') is not None:
            self.invoice_amounts = m.get('InvoiceAmounts')
        if m.get('InvoiceCodes') is not None:
            self.invoice_codes = m.get('InvoiceCodes')
        if m.get('InvoiceDates') is not None:
            self.invoice_dates = m.get('InvoiceDates')
        if m.get('InvoiceFakeCodes') is not None:
            self.invoice_fake_codes = m.get('InvoiceFakeCodes')
        if m.get('InvoiceNoes') is not None:
            self.invoice_noes = m.get('InvoiceNoes')
        if m.get('PayeeAddresses') is not None:
            self.payee_addresses = m.get('PayeeAddresses')
        if m.get('PayeeBankNames') is not None:
            self.payee_bank_names = m.get('PayeeBankNames')
        if m.get('PayeeNames') is not None:
            self.payee_names = m.get('PayeeNames')
        if m.get('PayeeRegisterNoes') is not None:
            self.payee_register_noes = m.get('PayeeRegisterNoes')
        if m.get('Payees') is not None:
            self.payees = m.get('Payees')
        if m.get('PayerAddresses') is not None:
            self.payer_addresses = m.get('PayerAddresses')
        if m.get('PayerBankNames') is not None:
            self.payer_bank_names = m.get('PayerBankNames')
        if m.get('PayerNames') is not None:
            self.payer_names = m.get('PayerNames')
        if m.get('PayerRegisterNoes') is not None:
            self.payer_register_noes = m.get('PayerRegisterNoes')
        if m.get('SumAmounts') is not None:
            self.sum_amounts = m.get('SumAmounts')
        if m.get('TaxAmounts') is not None:
            self.tax_amounts = m.get('TaxAmounts')
        if m.get('WithoutTaxAmounts') is not None:
            self.without_tax_amounts = m.get('WithoutTaxAmounts')
        return self


class RecognizeVATInvoiceResponseBodyDataContent(TeaModel):
    def __init__(self, anti_fake_code=None, checker=None, clerk=None, invoice_amount=None, invoice_code=None,
                 invoice_date=None, invoice_no=None, payee=None, payee_address=None, payee_bank_name=None, payee_name=None,
                 payee_register_no=None, payer_address=None, payer_bank_name=None, payer_name=None, payer_register_no=None,
                 sum_amount=None, tax_amount=None, without_tax_amount=None):
        self.anti_fake_code = anti_fake_code  # type: str
        self.checker = checker  # type: str
        self.clerk = clerk  # type: str
        self.invoice_amount = invoice_amount  # type: str
        self.invoice_code = invoice_code  # type: str
        self.invoice_date = invoice_date  # type: str
        self.invoice_no = invoice_no  # type: str
        self.payee = payee  # type: str
        self.payee_address = payee_address  # type: str
        self.payee_bank_name = payee_bank_name  # type: str
        self.payee_name = payee_name  # type: str
        self.payee_register_no = payee_register_no  # type: str
        self.payer_address = payer_address  # type: str
        self.payer_bank_name = payer_bank_name  # type: str
        self.payer_name = payer_name  # type: str
        self.payer_register_no = payer_register_no  # type: str
        self.sum_amount = sum_amount  # type: str
        self.tax_amount = tax_amount  # type: str
        self.without_tax_amount = without_tax_amount  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVATInvoiceResponseBodyDataContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_fake_code is not None:
            result['AntiFakeCode'] = self.anti_fake_code
        if self.checker is not None:
            result['Checker'] = self.checker
        if self.clerk is not None:
            result['Clerk'] = self.clerk
        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.payee is not None:
            result['Payee'] = self.payee
        if self.payee_address is not None:
            result['PayeeAddress'] = self.payee_address
        if self.payee_bank_name is not None:
            result['PayeeBankName'] = self.payee_bank_name
        if self.payee_name is not None:
            result['PayeeName'] = self.payee_name
        if self.payee_register_no is not None:
            result['PayeeRegisterNo'] = self.payee_register_no
        if self.payer_address is not None:
            result['PayerAddress'] = self.payer_address
        if self.payer_bank_name is not None:
            result['PayerBankName'] = self.payer_bank_name
        if self.payer_name is not None:
            result['PayerName'] = self.payer_name
        if self.payer_register_no is not None:
            result['PayerRegisterNo'] = self.payer_register_no
        if self.sum_amount is not None:
            result['SumAmount'] = self.sum_amount
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.without_tax_amount is not None:
            result['WithoutTaxAmount'] = self.without_tax_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AntiFakeCode') is not None:
            self.anti_fake_code = m.get('AntiFakeCode')
        if m.get('Checker') is not None:
            self.checker = m.get('Checker')
        if m.get('Clerk') is not None:
            self.clerk = m.get('Clerk')
        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('Payee') is not None:
            self.payee = m.get('Payee')
        if m.get('PayeeAddress') is not None:
            self.payee_address = m.get('PayeeAddress')
        if m.get('PayeeBankName') is not None:
            self.payee_bank_name = m.get('PayeeBankName')
        if m.get('PayeeName') is not None:
            self.payee_name = m.get('PayeeName')
        if m.get('PayeeRegisterNo') is not None:
            self.payee_register_no = m.get('PayeeRegisterNo')
        if m.get('PayerAddress') is not None:
            self.payer_address = m.get('PayerAddress')
        if m.get('PayerBankName') is not None:
            self.payer_bank_name = m.get('PayerBankName')
        if m.get('PayerName') is not None:
            self.payer_name = m.get('PayerName')
        if m.get('PayerRegisterNo') is not None:
            self.payer_register_no = m.get('PayerRegisterNo')
        if m.get('SumAmount') is not None:
            self.sum_amount = m.get('SumAmount')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('WithoutTaxAmount') is not None:
            self.without_tax_amount = m.get('WithoutTaxAmount')
        return self


class RecognizeVATInvoiceResponseBodyData(TeaModel):
    def __init__(self, box=None, content=None):
        self.box = box  # type: RecognizeVATInvoiceResponseBodyDataBox
        self.content = content  # type: RecognizeVATInvoiceResponseBodyDataContent

    def validate(self):
        if self.box:
            self.box.validate()
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(RecognizeVATInvoiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box.to_map()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Box') is not None:
            temp_model = RecognizeVATInvoiceResponseBodyDataBox()
            self.box = temp_model.from_map(m['Box'])
        if m.get('Content') is not None:
            temp_model = RecognizeVATInvoiceResponseBodyDataContent()
            self.content = temp_model.from_map(m['Content'])
        return self


class RecognizeVATInvoiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeVATInvoiceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeVATInvoiceResponseBody, self).to_map()
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
            temp_model = RecognizeVATInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVATInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeVATInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVATInvoiceResponse, self).to_map()
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
            temp_model = RecognizeVATInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVINCodeRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVINCodeRequest, self).to_map()
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


class RecognizeVINCodeAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeVINCodeAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVINCodeResponseBodyData(TeaModel):
    def __init__(self, vin_code=None):
        self.vin_code = vin_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVINCodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vin_code is not None:
            result['VinCode'] = self.vin_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VinCode') is not None:
            self.vin_code = m.get('VinCode')
        return self


class RecognizeVINCodeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeVINCodeResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeVINCodeResponseBody, self).to_map()
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
            temp_model = RecognizeVINCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVINCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeVINCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVINCodeResponse, self).to_map()
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
            temp_model = RecognizeVINCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVerificationcodeRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVerificationcodeRequest, self).to_map()
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


class RecognizeVerificationcodeAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: READABLE

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super(RecognizeVerificationcodeAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVerificationcodeResponseBodyData(TeaModel):
    def __init__(self, content=None):
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVerificationcodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class RecognizeVerificationcodeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeVerificationcodeResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeVerificationcodeResponseBody, self).to_map()
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
            temp_model = RecognizeVerificationcodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVerificationcodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeVerificationcodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVerificationcodeResponse, self).to_map()
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
            temp_model = RecognizeVerificationcodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVideoCharacterRequest(TeaModel):
    def __init__(self, video_url=None):
        # 视频文件地址
        self.video_url = video_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVideoCharacterRequest, self).to_map()
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


class RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles(TeaModel):
    def __init__(self, angle=None, height=None, left=None, top=None, width=None):
        # 文字区域角度，角度范围[0, 360]
        self.angle = angle  # type: long
        # 文字区域高度
        self.height = height  # type: long
        # 文字区域左上角x坐标
        self.left = left  # type: long
        # 文字区域左上角y坐标
        self.top = top  # type: long
        # 文字区域宽度
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
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
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeVideoCharacterResponseBodyDataFramesElements(TeaModel):
    def __init__(self, score=None, text=None, text_rectangles=None):
        # 文字区域概率，概率值的范围为[0.0, 1.0]
        self.score = score  # type: float
        # 文字内容
        self.text = text  # type: str
        self.text_rectangles = text_rectangles  # type: list[RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles]

    def validate(self):
        if self.text_rectangles:
            for k in self.text_rectangles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeVideoCharacterResponseBodyDataFramesElements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        result['TextRectangles'] = []
        if self.text_rectangles is not None:
            for k in self.text_rectangles:
                result['TextRectangles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.text_rectangles = []
        if m.get('TextRectangles') is not None:
            for k in m.get('TextRectangles'):
                temp_model = RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles()
                self.text_rectangles.append(temp_model.from_map(k))
        return self


class RecognizeVideoCharacterResponseBodyDataFrames(TeaModel):
    def __init__(self, elements=None, timestamp=None):
        self.elements = elements  # type: list[RecognizeVideoCharacterResponseBodyDataFramesElements]
        # 帧时间戳时间戳，单位秒。
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeVideoCharacterResponseBodyDataFrames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeVideoCharacterResponseBodyDataFramesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class RecognizeVideoCharacterResponseBodyData(TeaModel):
    def __init__(self, frames=None, height=None, input_file=None, width=None):
        # 视频帧的集合，空信息的帧不列出。
        self.frames = frames  # type: list[RecognizeVideoCharacterResponseBodyDataFrames]
        self.height = height  # type: long
        # 对应的输入OSS文件 (格式oss://{bucketName}/{object})
        self.input_file = input_file  # type: str
        self.width = width  # type: long

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeVideoCharacterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = RecognizeVideoCharacterResponseBodyDataFrames()
                self.frames.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeVideoCharacterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RecognizeVideoCharacterResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeVideoCharacterResponseBody, self).to_map()
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
            temp_model = RecognizeVideoCharacterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVideoCharacterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecognizeVideoCharacterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVideoCharacterResponse, self).to_map()
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
            temp_model = RecognizeVideoCharacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrimDocumentRequest(TeaModel):
    def __init__(self, file_type=None, file_url=None, output_type=None):
        self.file_type = file_type  # type: str
        self.file_url = file_url  # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrimDocumentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class TrimDocumentAdvanceRequest(TeaModel):
    def __init__(self, file_urlobject=None, file_type=None, output_type=None):
        self.file_urlobject = file_urlobject  # type: READABLE
        self.file_type = file_type  # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')

    def to_map(self):
        _map = super(TrimDocumentAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_urlobject is not None:
            result['FileURLObject'] = self.file_urlobject
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURLObject') is not None:
            self.file_urlobject = m.get('FileURLObject')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class TrimDocumentResponseBodyData(TeaModel):
    def __init__(self, content=None):
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrimDocumentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class TrimDocumentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: TrimDocumentResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TrimDocumentResponseBody, self).to_map()
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
            temp_model = TrimDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TrimDocumentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TrimDocumentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TrimDocumentResponse, self).to_map()
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
            temp_model = TrimDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


