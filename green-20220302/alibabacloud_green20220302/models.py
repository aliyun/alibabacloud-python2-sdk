# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeFileModerationResultRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileModerationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult(TeaModel):
    def __init__(self, confidence=None, label=None):
        self.confidence = confidence  # type: float
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h  # type: int
        self.w = w  # type: int
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation, self).to_map()
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


class DescribeFileModerationResultResponseBodyDataPageResultImageResult(TeaModel):
    def __init__(self, description=None, label_result=None, location=None, service=None):
        self.description = description  # type: str
        self.label_result = label_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult]
        self.location = location  # type: DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation
        self.service = service  # type: str

    def validate(self):
        if self.label_result:
            for k in self.label_result:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageResultImageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['LabelResult'] = []
        if self.label_result is not None:
            for k in self.label_result:
                result['LabelResult'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.label_result = []
        if m.get('LabelResult') is not None:
            for k in m.get('LabelResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult()
                self.label_result.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultTextResult(TeaModel):
    def __init__(self, description=None, labels=None, risk_tips=None, risk_words=None, service=None, text=None,
                 text_segment=None):
        self.description = description  # type: str
        self.labels = labels  # type: str
        self.risk_tips = risk_tips  # type: str
        self.risk_words = risk_words  # type: str
        self.service = service  # type: str
        self.text = text  # type: str
        self.text_segment = text_segment  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageResultTextResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.service is not None:
            result['Service'] = self.service
        if self.text is not None:
            result['Text'] = self.text
        if self.text_segment is not None:
            result['TextSegment'] = self.text_segment
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextSegment') is not None:
            self.text_segment = m.get('TextSegment')
        return self


class DescribeFileModerationResultResponseBodyDataPageResult(TeaModel):
    def __init__(self, image_result=None, image_url=None, page_num=None, text_result=None, text_url=None):
        self.image_result = image_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResultImageResult]
        self.image_url = image_url  # type: str
        self.page_num = page_num  # type: int
        self.text_result = text_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResultTextResult]
        self.text_url = text_url  # type: str

    def validate(self):
        if self.image_result:
            for k in self.image_result:
                if k:
                    k.validate()
        if self.text_result:
            for k in self.text_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageResult'] = []
        if self.image_result is not None:
            for k in self.image_result:
                result['ImageResult'].append(k.to_map() if k else None)
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        result['TextResult'] = []
        if self.text_result is not None:
            for k in self.text_result:
                result['TextResult'].append(k.to_map() if k else None)
        if self.text_url is not None:
            result['TextUrl'] = self.text_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.image_result = []
        if m.get('ImageResult') is not None:
            for k in m.get('ImageResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResultImageResult()
                self.image_result.append(temp_model.from_map(k))
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        self.text_result = []
        if m.get('TextResult') is not None:
            for k in m.get('TextResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResultTextResult()
                self.text_result.append(temp_model.from_map(k))
        if m.get('TextUrl') is not None:
            self.text_url = m.get('TextUrl')
        return self


class DescribeFileModerationResultResponseBodyData(TeaModel):
    def __init__(self, data_id=None, doc_type=None, page_result=None, url=None):
        self.data_id = data_id  # type: str
        self.doc_type = doc_type  # type: str
        self.page_result = page_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResult]
        self.url = url  # type: str

    def validate(self):
        if self.page_result:
            for k in self.page_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        result['PageResult'] = []
        if self.page_result is not None:
            for k in self.page_result:
                result['PageResult'].append(k.to_map() if k else None)
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        self.page_result = []
        if m.get('PageResult') is not None:
            for k in m.get('PageResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResult()
                self.page_result.append(temp_model.from_map(k))
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeFileModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeFileModerationResultResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBody, self).to_map()
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
            temp_model = DescribeFileModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFileModerationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFileModerationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponse, self).to_map()
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
            temp_model = DescribeFileModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageModerationResultRequest(TeaModel):
    def __init__(self, req_id=None):
        self.req_id = req_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageModerationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeImageModerationResultResponseBodyDataResult(TeaModel):
    def __init__(self, confidence=None, label=None):
        self.confidence = confidence  # type: float
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageModerationResultResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeImageModerationResultResponseBodyData(TeaModel):
    def __init__(self, data_id=None, frame=None, frame_num=None, req_id=None, result=None):
        self.data_id = data_id  # type: str
        self.frame = frame  # type: str
        self.frame_num = frame_num  # type: int
        self.req_id = req_id  # type: str
        self.result = result  # type: list[DescribeImageModerationResultResponseBodyDataResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageModerationResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.frame is not None:
            result['Frame'] = self.frame
        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Frame') is not None:
            self.frame = m.get('Frame')
        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeImageModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeImageModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeImageModerationResultResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeImageModerationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeImageModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageModerationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeImageModerationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageModerationResultResponse, self).to_map()
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
            temp_model = DescribeImageModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageResultExtRequest(TeaModel):
    def __init__(self, info_type=None, req_id=None):
        self.info_type = info_type  # type: str
        self.req_id = req_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageResultExtRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info_type is not None:
            result['InfoType'] = self.info_type
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeImageResultExtResponseBodyDataCustomImage(TeaModel):
    def __init__(self, image_id=None, lib_id=None, lib_name=None):
        # 图片ID。
        self.image_id = image_id  # type: str
        # 图库ID。
        self.lib_id = lib_id  # type: str
        # 图库名。
        self.lib_name = lib_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageResultExtResponseBodyDataCustomImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        return self


class DescribeImageResultExtResponseBodyDataPublicFigure(TeaModel):
    def __init__(self, figure_id=None):
        # 人物ID。
        self.figure_id = figure_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageResultExtResponseBodyDataPublicFigure, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class DescribeImageResultExtResponseBodyDataTextInImage(TeaModel):
    def __init__(self, ocr_datas=None, risk_words=None):
        self.ocr_datas = ocr_datas  # type: list[str]
        self.risk_words = risk_words  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageResultExtResponseBodyDataTextInImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocr_datas is not None:
            result['OcrDatas'] = self.ocr_datas
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OcrDatas') is not None:
            self.ocr_datas = m.get('OcrDatas')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        return self


class DescribeImageResultExtResponseBodyData(TeaModel):
    def __init__(self, custom_image=None, public_figure=None, text_in_image=None):
        self.custom_image = custom_image  # type: list[DescribeImageResultExtResponseBodyDataCustomImage]
        self.public_figure = public_figure  # type: list[DescribeImageResultExtResponseBodyDataPublicFigure]
        self.text_in_image = text_in_image  # type: DescribeImageResultExtResponseBodyDataTextInImage

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.public_figure:
            for k in self.public_figure:
                if k:
                    k.validate()
        if self.text_in_image:
            self.text_in_image.validate()

    def to_map(self):
        _map = super(DescribeImageResultExtResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k in self.custom_image:
                result['CustomImage'].append(k.to_map() if k else None)
        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k in self.public_figure:
                result['PublicFigure'].append(k.to_map() if k else None)
        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = DescribeImageResultExtResponseBodyDataCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = DescribeImageResultExtResponseBodyDataPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        if m.get('TextInImage') is not None:
            temp_model = DescribeImageResultExtResponseBodyDataTextInImage()
            self.text_in_image = temp_model.from_map(m['TextInImage'])
        return self


class DescribeImageResultExtResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeImageResultExtResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeImageResultExtResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeImageResultExtResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageResultExtResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeImageResultExtResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageResultExtResponse, self).to_map()
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
            temp_model = DescribeImageResultExtResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadTokenResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, bucket_name=None, expiration=None,
                 file_name_prefix=None, oss_internal_end_point=None, oss_internet_end_point=None, security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.bucket_name = bucket_name  # type: str
        self.expiration = expiration  # type: int
        self.file_name_prefix = file_name_prefix  # type: str
        self.oss_internal_end_point = oss_internal_end_point  # type: str
        self.oss_internet_end_point = oss_internet_end_point  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUploadTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix
        if self.oss_internal_end_point is not None:
            result['OssInternalEndPoint'] = self.oss_internal_end_point
        if self.oss_internet_end_point is not None:
            result['OssInternetEndPoint'] = self.oss_internet_end_point
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')
        if m.get('OssInternalEndPoint') is not None:
            self.oss_internal_end_point = m.get('OssInternalEndPoint')
        if m.get('OssInternetEndPoint') is not None:
            self.oss_internet_end_point = m.get('OssInternetEndPoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUploadTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeUploadTokenResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeUploadTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeUploadTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUploadTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUploadTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUploadTokenResponse, self).to_map()
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
            temp_model = DescribeUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUrlModerationResultRequest(TeaModel):
    def __init__(self, req_id=None):
        self.req_id = req_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUrlModerationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeUrlModerationResultResponseBodyDataExtraInfo(TeaModel):
    def __init__(self, icp_no=None, icp_type=None):
        self.icp_no = icp_no  # type: str
        self.icp_type = icp_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUrlModerationResultResponseBodyDataExtraInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icp_no is not None:
            result['IcpNo'] = self.icp_no
        if self.icp_type is not None:
            result['IcpType'] = self.icp_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IcpNo') is not None:
            self.icp_no = m.get('IcpNo')
        if m.get('IcpType') is not None:
            self.icp_type = m.get('IcpType')
        return self


class DescribeUrlModerationResultResponseBodyDataResult(TeaModel):
    def __init__(self, confidence=None, label=None):
        self.confidence = confidence  # type: float
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUrlModerationResultResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeUrlModerationResultResponseBodyData(TeaModel):
    def __init__(self, data_id=None, extra_info=None, req_id=None, result=None):
        self.data_id = data_id  # type: str
        self.extra_info = extra_info  # type: DescribeUrlModerationResultResponseBodyDataExtraInfo
        self.req_id = req_id  # type: str
        self.result = result  # type: list[DescribeUrlModerationResultResponseBodyDataResult]

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUrlModerationResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ExtraInfo') is not None:
            temp_model = DescribeUrlModerationResultResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeUrlModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeUrlModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeUrlModerationResultResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeUrlModerationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeUrlModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUrlModerationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUrlModerationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUrlModerationResultResponse, self).to_map()
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
            temp_model = DescribeUrlModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FileModerationRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FileModerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class FileModerationResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FileModerationResponseBodyData, self).to_map()
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


class FileModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: FileModerationResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FileModerationResponseBody, self).to_map()
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
            temp_model = FileModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FileModerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FileModerationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FileModerationResponse, self).to_map()
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
            temp_model = FileModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageAsyncModerationRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageAsyncModerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ImageAsyncModerationResponseBodyData(TeaModel):
    def __init__(self, data_id=None, req_id=None):
        self.data_id = data_id  # type: str
        self.req_id = req_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageAsyncModerationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class ImageAsyncModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: ImageAsyncModerationResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImageAsyncModerationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ImageAsyncModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageAsyncModerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImageAsyncModerationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImageAsyncModerationResponse, self).to_map()
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
            temp_model = ImageAsyncModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageModerationRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ImageModerationResponseBodyDataResult(TeaModel):
    def __init__(self, confidence=None, label=None):
        self.confidence = confidence  # type: float
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ImageModerationResponseBodyData(TeaModel):
    def __init__(self, data_id=None, result=None):
        self.data_id = data_id  # type: str
        self.result = result  # type: list[ImageModerationResponseBodyDataResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ImageModerationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        return self


class ImageModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: ImageModerationResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ImageModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageModerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImageModerationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImageModerationResponse, self).to_map()
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
            temp_model = ImageModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TextModerationRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TextModerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class TextModerationResponseBodyData(TeaModel):
    def __init__(self, account_id=None, device_id=None, labels=None, reason=None):
        self.account_id = account_id  # type: str
        self.device_id = device_id  # type: str
        self.labels = labels  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TextModerationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.labels is not None:
            result['labels'] = self.labels
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class TextModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: TextModerationResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TextModerationResponseBody, self).to_map()
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
            temp_model = TextModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TextModerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TextModerationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TextModerationResponse, self).to_map()
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
            temp_model = TextModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TextModerationPlusRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TextModerationPlusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class TextModerationPlusResponseBodyDataAdvice(TeaModel):
    def __init__(self, answer=None):
        self.answer = answer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TextModerationPlusResponseBodyDataAdvice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        return self


class TextModerationPlusResponseBodyDataResultCustomizedHit(TeaModel):
    def __init__(self, key_words=None, lib_name=None):
        self.key_words = key_words  # type: str
        self.lib_name = lib_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TextModerationPlusResponseBodyDataResultCustomizedHit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        return self


class TextModerationPlusResponseBodyDataResult(TeaModel):
    def __init__(self, confidence=None, customized_hit=None, label=None, risk_words=None):
        self.confidence = confidence  # type: float
        self.customized_hit = customized_hit  # type: list[TextModerationPlusResponseBodyDataResultCustomizedHit]
        self.label = label  # type: str
        self.risk_words = risk_words  # type: str

    def validate(self):
        if self.customized_hit:
            for k in self.customized_hit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TextModerationPlusResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        result['CustomizedHit'] = []
        if self.customized_hit is not None:
            for k in self.customized_hit:
                result['CustomizedHit'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        self.customized_hit = []
        if m.get('CustomizedHit') is not None:
            for k in m.get('CustomizedHit'):
                temp_model = TextModerationPlusResponseBodyDataResultCustomizedHit()
                self.customized_hit.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        return self


class TextModerationPlusResponseBodyData(TeaModel):
    def __init__(self, advice=None, result=None, score=None):
        self.advice = advice  # type: list[TextModerationPlusResponseBodyDataAdvice]
        self.result = result  # type: list[TextModerationPlusResponseBodyDataResult]
        self.score = score  # type: float

    def validate(self):
        if self.advice:
            for k in self.advice:
                if k:
                    k.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TextModerationPlusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Advice'] = []
        if self.advice is not None:
            for k in self.advice:
                result['Advice'].append(k.to_map() if k else None)
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.advice = []
        if m.get('Advice') is not None:
            for k in m.get('Advice'):
                temp_model = TextModerationPlusResponseBodyDataAdvice()
                self.advice.append(temp_model.from_map(k))
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = TextModerationPlusResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class TextModerationPlusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: TextModerationPlusResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TextModerationPlusResponseBody, self).to_map()
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
            temp_model = TextModerationPlusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TextModerationPlusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TextModerationPlusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TextModerationPlusResponse, self).to_map()
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
            temp_model = TextModerationPlusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UrlAsyncModerationRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UrlAsyncModerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class UrlAsyncModerationResponseBodyData(TeaModel):
    def __init__(self, data_id=None, req_id=None):
        self.data_id = data_id  # type: str
        self.req_id = req_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UrlAsyncModerationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class UrlAsyncModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: UrlAsyncModerationResponseBodyData
        self.msg = msg  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UrlAsyncModerationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UrlAsyncModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UrlAsyncModerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UrlAsyncModerationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UrlAsyncModerationResponse, self).to_map()
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
            temp_model = UrlAsyncModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResponseBodyData, self).to_map()
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


class VideoModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: VideoModerationResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(VideoModerationResponseBody, self).to_map()
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
            temp_model = VideoModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VideoModerationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VideoModerationResponse, self).to_map()
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
            temp_model = VideoModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationCancelRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationCancelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationCancelResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationCancelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationCancelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VideoModerationCancelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VideoModerationCancelResponse, self).to_map()
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
            temp_model = VideoModerationCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationResultRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationResultResponseBodyDataAudioResultAudioSummarys(TeaModel):
    def __init__(self, label=None, label_sum=None):
        self.label = label  # type: str
        self.label_sum = label_sum  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataAudioResultAudioSummarys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')
        return self


class VideoModerationResultResponseBodyDataAudioResultSliceDetails(TeaModel):
    def __init__(self, end_time=None, end_timestamp=None, extend=None, labels=None, risk_tips=None, risk_words=None,
                 score=None, start_time=None, start_timestamp=None, text=None, url=None):
        self.end_time = end_time  # type: long
        self.end_timestamp = end_timestamp  # type: long
        self.extend = extend  # type: str
        self.labels = labels  # type: str
        self.risk_tips = risk_tips  # type: str
        self.risk_words = risk_words  # type: str
        self.score = score  # type: float
        self.start_time = start_time  # type: long
        self.start_timestamp = start_timestamp  # type: long
        self.text = text  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataAudioResultSliceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.score is not None:
            result['Score'] = self.score
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.text is not None:
            result['Text'] = self.text
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VideoModerationResultResponseBodyDataAudioResult(TeaModel):
    def __init__(self, audio_summarys=None, slice_details=None):
        self.audio_summarys = audio_summarys  # type: list[VideoModerationResultResponseBodyDataAudioResultAudioSummarys]
        self.slice_details = slice_details  # type: list[VideoModerationResultResponseBodyDataAudioResultSliceDetails]

    def validate(self):
        if self.audio_summarys:
            for k in self.audio_summarys:
                if k:
                    k.validate()
        if self.slice_details:
            for k in self.slice_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataAudioResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioSummarys'] = []
        if self.audio_summarys is not None:
            for k in self.audio_summarys:
                result['AudioSummarys'].append(k.to_map() if k else None)
        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k in self.slice_details:
                result['SliceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.audio_summarys = []
        if m.get('AudioSummarys') is not None:
            for k in m.get('AudioSummarys'):
                temp_model = VideoModerationResultResponseBodyDataAudioResultAudioSummarys()
                self.audio_summarys.append(temp_model.from_map(k))
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VideoModerationResultResponseBodyDataAudioResultSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyDataFrameResultFrameSummarys(TeaModel):
    def __init__(self, label=None, label_sum=None):
        self.label = label  # type: str
        self.label_sum = label_sum  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFrameSummarys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResultsResult(TeaModel):
    def __init__(self, confidence=None, label=None):
        self.confidence = confidence  # type: float
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFramesResultsResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResults(TeaModel):
    def __init__(self, result=None, service=None):
        self.result = result  # type: list[VideoModerationResultResponseBodyDataFrameResultFramesResultsResult]
        self.service = service  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFramesResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class VideoModerationResultResponseBodyDataFrameResultFrames(TeaModel):
    def __init__(self, offset=None, results=None, temp_url=None, timestamp=None):
        self.offset = offset  # type: float
        self.results = results  # type: list[VideoModerationResultResponseBodyDataFrameResultFramesResults]
        self.temp_url = temp_url  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFrames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.temp_url is not None:
            result['TempUrl'] = self.temp_url
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TempUrl') is not None:
            self.temp_url = m.get('TempUrl')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class VideoModerationResultResponseBodyDataFrameResult(TeaModel):
    def __init__(self, frame_num=None, frame_summarys=None, frames=None):
        self.frame_num = frame_num  # type: int
        self.frame_summarys = frame_summarys  # type: list[VideoModerationResultResponseBodyDataFrameResultFrameSummarys]
        self.frames = frames  # type: list[VideoModerationResultResponseBodyDataFrameResultFrames]

    def validate(self):
        if self.frame_summarys:
            for k in self.frame_summarys:
                if k:
                    k.validate()
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num
        result['FrameSummarys'] = []
        if self.frame_summarys is not None:
            for k in self.frame_summarys:
                result['FrameSummarys'].append(k.to_map() if k else None)
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')
        self.frame_summarys = []
        if m.get('FrameSummarys') is not None:
            for k in m.get('FrameSummarys'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFrameSummarys()
                self.frame_summarys.append(temp_model.from_map(k))
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFrames()
                self.frames.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyData(TeaModel):
    def __init__(self, audio_result=None, data_id=None, frame_result=None, live_id=None):
        self.audio_result = audio_result  # type: VideoModerationResultResponseBodyDataAudioResult
        self.data_id = data_id  # type: str
        self.frame_result = frame_result  # type: VideoModerationResultResponseBodyDataFrameResult
        self.live_id = live_id  # type: str

    def validate(self):
        if self.audio_result:
            self.audio_result.validate()
        if self.frame_result:
            self.frame_result.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_result is not None:
            result['AudioResult'] = self.audio_result.to_map()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.frame_result is not None:
            result['FrameResult'] = self.frame_result.to_map()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioResult') is not None:
            temp_model = VideoModerationResultResponseBodyDataAudioResult()
            self.audio_result = temp_model.from_map(m['AudioResult'])
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FrameResult') is not None:
            temp_model = VideoModerationResultResponseBodyDataFrameResult()
            self.frame_result = temp_model.from_map(m['FrameResult'])
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class VideoModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: VideoModerationResultResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponseBody, self).to_map()
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
            temp_model = VideoModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VideoModerationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponse, self).to_map()
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
            temp_model = VideoModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoiceModerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoiceModerationResponseBodyData, self).to_map()
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


class VoiceModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: VoiceModerationResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(VoiceModerationResponseBody, self).to_map()
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
            temp_model = VoiceModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VoiceModerationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VoiceModerationResponse, self).to_map()
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
            temp_model = VoiceModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationCancelRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoiceModerationCancelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationCancelResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoiceModerationCancelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationCancelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VoiceModerationCancelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VoiceModerationCancelResponse, self).to_map()
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
            temp_model = VoiceModerationCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationResultRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoiceModerationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationResultResponseBodyDataSliceDetails(TeaModel):
    def __init__(self, end_time=None, end_timestamp=None, extend=None, labels=None, origin_algo_result=None,
                 risk_tips=None, risk_words=None, score=None, start_time=None, start_timestamp=None, text=None, url=None):
        self.end_time = end_time  # type: long
        self.end_timestamp = end_timestamp  # type: long
        self.extend = extend  # type: str
        self.labels = labels  # type: str
        self.origin_algo_result = origin_algo_result  # type: dict[str, any]
        self.risk_tips = risk_tips  # type: str
        self.risk_words = risk_words  # type: str
        self.score = score  # type: float
        self.start_time = start_time  # type: long
        self.start_timestamp = start_timestamp  # type: long
        self.text = text  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoiceModerationResultResponseBodyDataSliceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.origin_algo_result is not None:
            result['OriginAlgoResult'] = self.origin_algo_result
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.score is not None:
            result['Score'] = self.score
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.text is not None:
            result['Text'] = self.text
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OriginAlgoResult') is not None:
            self.origin_algo_result = m.get('OriginAlgoResult')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VoiceModerationResultResponseBodyData(TeaModel):
    def __init__(self, live_id=None, slice_details=None, task_id=None, url=None):
        self.live_id = live_id  # type: str
        self.slice_details = slice_details  # type: list[VoiceModerationResultResponseBodyDataSliceDetails]
        self.task_id = task_id  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.slice_details:
            for k in self.slice_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VoiceModerationResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k in self.slice_details:
                result['SliceDetails'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VoiceModerationResultResponseBodyDataSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VoiceModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: VoiceModerationResultResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(VoiceModerationResultResponseBody, self).to_map()
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
            temp_model = VoiceModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VoiceModerationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VoiceModerationResultResponse, self).to_map()
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
            temp_model = VoiceModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


