# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeFileModerationResultRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
        # 
        # *   taskId: required. The URL of the object that you want to moderate. Make sure that the URL can be accessed over the Internet.
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
    def __init__(self, confidence=None, description=None, label=None):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence  # type: float
        # The description.
        self.description = description  # type: str
        # The details of the labels.
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
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        # The H value of the coordinate point.
        self.h = h  # type: int
        # The W value of the coordinate point.
        self.w = w  # type: int
        # The X value of the coordinate point.
        self.x = x  # type: int
        # The Y value of the coordinate point.
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
    def __init__(self, description=None, label_result=None, location=None, risk_level=None, service=None):
        # The description.
        self.description = description  # type: str
        # The label information.
        self.label_result = label_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult]
        # The location information
        self.location = location  # type: DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation
        # Risk Level
        self.risk_level = risk_level  # type: str
        # The moderation service.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultTextResult(TeaModel):
    def __init__(self, description=None, labels=None, risk_level=None, risk_tips=None, risk_words=None, service=None,
                 text=None, text_segment=None):
        # The description.
        self.description = description  # type: str
        # The details of the labels.
        self.labels = labels  # type: str
        # Risk Level
        self.risk_level = risk_level  # type: str
        # The risk details that are hit.
        self.risk_tips = risk_tips  # type: str
        # The risk words that are hit.
        self.risk_words = risk_words  # type: str
        # The moderation service.
        self.service = service  # type: str
        # The text content.
        self.text = text  # type: str
        # The text segmentation information.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        # The image moderation results.
        self.image_result = image_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResultImageResult]
        # The image URL.
        self.image_url = image_url  # type: str
        # The page number.
        self.page_num = page_num  # type: int
        # The text moderation results.
        self.text_result = text_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResultTextResult]
        # The text URL.
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


class DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels(TeaModel):
    def __init__(self, description=None, label=None, label_sum=None):
        # The description.
        self.description = description  # type: str
        # The details of the labels.
        self.label = label  # type: str
        # The number of times that the label is matched.
        self.label_sum = label_sum  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')
        return self


class DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary(TeaModel):
    def __init__(self, image_labels=None, risk_level=None):
        # Image Label
        self.image_labels = image_labels  # type: list[DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels]
        # Risk Level
        self.risk_level = risk_level  # type: str

    def validate(self):
        if self.image_labels:
            for k in self.image_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageLabels'] = []
        if self.image_labels is not None:
            for k in self.image_labels:
                result['ImageLabels'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.image_labels = []
        if m.get('ImageLabels') is not None:
            for k in m.get('ImageLabels'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels()
                self.image_labels.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels(TeaModel):
    def __init__(self, label=None, label_sum=None):
        # The details of the labels.
        self.label = label  # type: str
        # The number of times that the label is matched.
        self.label_sum = label_sum  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels, self).to_map()
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


class DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary(TeaModel):
    def __init__(self, risk_level=None, text_labels=None):
        # Risk Level
        self.risk_level = risk_level  # type: str
        # Text Label
        self.text_labels = text_labels  # type: list[DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels]

    def validate(self):
        if self.text_labels:
            for k in self.text_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        result['TextLabels'] = []
        if self.text_labels is not None:
            for k in self.text_labels:
                result['TextLabels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        self.text_labels = []
        if m.get('TextLabels') is not None:
            for k in m.get('TextLabels'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels()
                self.text_labels.append(temp_model.from_map(k))
        return self


class DescribeFileModerationResultResponseBodyDataPageSummary(TeaModel):
    def __init__(self, image_summary=None, page_sum=None, text_summary=None):
        # Image Results Summary
        self.image_summary = image_summary  # type: DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary
        # Number of pages
        self.page_sum = page_sum  # type: int
        # Text Results Summary
        self.text_summary = text_summary  # type: DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary

    def validate(self):
        if self.image_summary:
            self.image_summary.validate()
        if self.text_summary:
            self.text_summary.validate()

    def to_map(self):
        _map = super(DescribeFileModerationResultResponseBodyDataPageSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_summary is not None:
            result['ImageSummary'] = self.image_summary.to_map()
        if self.page_sum is not None:
            result['PageSum'] = self.page_sum
        if self.text_summary is not None:
            result['TextSummary'] = self.text_summary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageSummary') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary()
            self.image_summary = temp_model.from_map(m['ImageSummary'])
        if m.get('PageSum') is not None:
            self.page_sum = m.get('PageSum')
        if m.get('TextSummary') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary()
            self.text_summary = temp_model.from_map(m['TextSummary'])
        return self


class DescribeFileModerationResultResponseBodyData(TeaModel):
    def __init__(self, data_id=None, doc_type=None, page_result=None, page_summary=None, risk_level=None, url=None):
        # The ID of the moderated object.
        self.data_id = data_id  # type: str
        # Optional. The document type.
        self.doc_type = doc_type  # type: str
        # An array that consists of the moderation results.
        self.page_result = page_result  # type: list[DescribeFileModerationResultResponseBodyDataPageResult]
        # Summary of results
        self.page_summary = page_summary  # type: DescribeFileModerationResultResponseBodyDataPageSummary
        # Risk Level
        self.risk_level = risk_level  # type: str
        # The URL of the moderated object.
        self.url = url  # type: str

    def validate(self):
        if self.page_result:
            for k in self.page_result:
                if k:
                    k.validate()
        if self.page_summary:
            self.page_summary.validate()

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
        if self.page_summary is not None:
            result['PageSummary'] = self.page_summary.to_map()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('PageSummary') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageSummary()
            self.page_summary = temp_model.from_map(m['PageSummary'])
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeFileModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeFileModerationResultResponseBodyData
        # The message that is returned in response to the request.
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
        # The ReqId field returned by the asynchronous Image Moderation 2.0 API.
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
    def __init__(self, confidence=None, description=None, label=None):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence  # type: float
        # The description of the result.
        self.description = description  # type: str
        # The labels returned after the image moderation.
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
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeImageModerationResultResponseBodyData(TeaModel):
    def __init__(self, data_id=None, frame=None, frame_num=None, req_id=None, result=None, risk_level=None):
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, this field is not available in the response.
        self.data_id = data_id  # type: str
        # The information about the captured frames.
        self.frame = frame  # type: str
        # The number of frames.
        self.frame_num = frame_num  # type: int
        # The reqId field returned by the Image Async Moderation API.
        self.req_id = req_id  # type: str
        # The results of image moderation parameters such as the label parameter and the confidence parameter.
        self.result = result  # type: list[DescribeImageModerationResultResponseBodyDataResult]
        # Risk Level.
        self.risk_level = risk_level  # type: str

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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeImageModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        # The returned HTTP status code.
        self.code = code  # type: int
        # The image moderation results.
        self.data = data  # type: DescribeImageModerationResultResponseBodyData
        # The message that is returned in response to the request.
        self.msg = msg  # type: str
        # The request ID, which is used to locate and troubleshoot issues.
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
        # The content of the information to be obtained. Multiple values are separated by commas.
        self.info_type = info_type  # type: str
        # The reqId field returned by the Url Async Moderation API.
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
        # The image ID.
        self.image_id = image_id  # type: str
        # The image library ID.
        self.lib_id = lib_id  # type: str
        # The image library name.
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
        # Identified person coding information.
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


class DescribeImageResultExtResponseBodyDataTextInImageCustomTexts(TeaModel):
    def __init__(self, key_words=None, lib_id=None, lib_name=None):
        # Custom words, multiple words separated by commas.
        self.key_words = key_words  # type: str
        # Custom library ID.
        self.lib_id = lib_id  # type: str
        # Custom library name.
        self.lib_name = lib_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageResultExtResponseBodyDataTextInImageCustomTexts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        return self


class DescribeImageResultExtResponseBodyDataTextInImage(TeaModel):
    def __init__(self, custom_texts=None, ocr_datas=None, risk_words=None):
        # When a custom text library is hit, the custom library ID, custom library name, and custom word are returned.
        self.custom_texts = custom_texts  # type: list[DescribeImageResultExtResponseBodyDataTextInImageCustomTexts]
        # Returns the text information in the recognized image.
        self.ocr_datas = ocr_datas  # type: list[str]
        # The risk words that are hit. Multiple words are separated by commas (,).
        self.risk_words = risk_words  # type: list[str]

    def validate(self):
        if self.custom_texts:
            for k in self.custom_texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageResultExtResponseBodyDataTextInImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomTexts'] = []
        if self.custom_texts is not None:
            for k in self.custom_texts:
                result['CustomTexts'].append(k.to_map() if k else None)
        if self.ocr_datas is not None:
            result['OcrDatas'] = self.ocr_datas
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_texts = []
        if m.get('CustomTexts') is not None:
            for k in m.get('CustomTexts'):
                temp_model = DescribeImageResultExtResponseBodyDataTextInImageCustomTexts()
                self.custom_texts.append(temp_model.from_map(k))
        if m.get('OcrDatas') is not None:
            self.ocr_datas = m.get('OcrDatas')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        return self


class DescribeImageResultExtResponseBodyData(TeaModel):
    def __init__(self, custom_image=None, public_figure=None, text_in_image=None):
        # If a custom image library is hit, information about the hit custom image library is returned.
        self.custom_image = custom_image  # type: list[DescribeImageResultExtResponseBodyDataCustomImage]
        # Person information list.
        self.public_figure = public_figure  # type: list[DescribeImageResultExtResponseBodyDataPublicFigure]
        # Returns the text information in the hit image.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeImageResultExtResponseBodyData
        # The message that is returned in response to the request.
        self.msg = msg  # type: str
        # The request ID.
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
        # The AccessKey ID.
        self.access_key_id = access_key_id  # type: str
        # The AccessKey secret.
        self.access_key_secret = access_key_secret  # type: str
        # The bucket name.
        self.bucket_name = bucket_name  # type: str
        # The time when the file sharing link expires.
        self.expiration = expiration  # type: int
        # The file prefix.
        self.file_name_prefix = file_name_prefix  # type: str
        # the oss intranet point.
        self.oss_internal_end_point = oss_internal_end_point  # type: str
        # the oss internet point.
        self.oss_internet_end_point = oss_internet_end_point  # type: str
        # The security token.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeUploadTokenResponseBodyData
        # The message that is returned in response to the request.
        self.msg = msg  # type: str
        # The request ID.
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
        # The ReqId field returned by an asynchronous URL moderation operation.
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
    def __init__(self, icp_no=None, icp_type=None, site_type=None):
        # The ICP number.
        self.icp_no = icp_no  # type: str
        # The type of the ICP filing.
        self.icp_type = icp_type  # type: str
        # The type of site
        self.site_type = site_type  # type: str

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
        if self.site_type is not None:
            result['SiteType'] = self.site_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IcpNo') is not None:
            self.icp_no = m.get('IcpNo')
        if m.get('IcpType') is not None:
            self.icp_type = m.get('IcpType')
        if m.get('SiteType') is not None:
            self.site_type = m.get('SiteType')
        return self


class DescribeUrlModerationResultResponseBodyDataResult(TeaModel):
    def __init__(self, confidence=None, label=None):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence  # type: float
        # The labels returned after the asynchronous URL moderation.
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
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, this field is not available in the response.
        self.data_id = data_id  # type: str
        # The supplementary information.
        self.extra_info = extra_info  # type: DescribeUrlModerationResultResponseBodyDataExtraInfo
        # The ReqId field returned by an asynchronous URL moderation operation.
        self.req_id = req_id  # type: str
        # The returned results.
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
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeUrlModerationResultResponseBodyData
        # The message that is returned in response to the request.
        self.msg = msg  # type: str
        # The request ID.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The task ID.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: FileModerationResponseBodyData
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the moderated object.
        self.data_id = data_id  # type: str
        # The reqId field returned by the Image Async Moderation API. You can use this field to query the detection results.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: ImageAsyncModerationResponseBodyData
        # The message that is returned in response to the request.
        self.msg = msg  # type: str
        # The request ID.
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
        # The moderation services supported by Image Moderation 2.0. Valid values:
        # 
        # *   baselineCheck: common baseline moderation
        # *   baselineCheck_pro: common baseline moderation_Professional
        # *   baselineCheck_cb: common baseline moderation_For regions outside the Chinese mainland
        # *   tonalityImprove: content governance moderation
        # *   aigcCheck: AI-generated image identification
        # *   profilePhotoCheck: avatar image moderation
        # *   advertisingCheck: marketing material identification
        # *   liveStreamCheck: moderation of screenshots of videos and live streams
        # 
        # Valid values:
        # 
        # *   liveStreamCheck: moderation of screenshots of videos and live streams
        # *   baselineCheck: common baseline moderation
        # *   aigcCheck: AI-generated image identification
        # *   baselineCheck_pro: common baseline moderation_Professional
        # *   advertisingCheck: marketing material identification
        # *   baselineCheck_cb: common baseline moderation_For regions outside the Chinese mainland
        # *   tonalityImprove: content governance moderation
        # *   profilePhotoCheck: avatar image moderation
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
        # 
        # *   imageUrl: the URL of the object that you want to moderate. This parameter is required.
        # *   dataId: the ID of the object that you want to moderate. This parameter is optional.
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


class ImageModerationResponseBodyDataExtCustomImage(TeaModel):
    def __init__(self, image_id=None, lib_id=None, lib_name=None):
        # The image ID.
        self.image_id = image_id  # type: str
        # The image library ID.
        self.lib_id = lib_id  # type: str
        # The image library name.
        self.lib_name = lib_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtCustomImage, self).to_map()
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


class ImageModerationResponseBodyDataExtFaceDataBang(TeaModel):
    def __init__(self, confidence=None, value=None):
        # The confidence level of the bang recognition result. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence  # type: float
        # Indicates whether the recognition result of bangs is available.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataBang, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImageModerationResponseBodyDataExtFaceDataGender(TeaModel):
    def __init__(self, confidence=None, value=None):
        # The confidence level of the gender recognition result. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence  # type: float
        # The gender recognition result. Valid values:
        # 
        # - Male
        # 
        # - FeMale
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataGender, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImageModerationResponseBodyDataExtFaceDataHairstyle(TeaModel):
    def __init__(self, confidence=None, value=None):
        # The confidence level of the hairstyle recognition result. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence  # type: float
        # The hairstyle recognition result. Valid values:
        # 
        # - Bald: bald head.
        # 
        # - Long: Long hair.
        # 
        # - Short: Short hair.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataHairstyle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImageModerationResponseBodyDataExtFaceDataHat(TeaModel):
    def __init__(self, confidence=None, value=None):
        # The confidence level of the result of wearing the hat. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence  # type: float
        # The recognition result of whether to wear the hat. Valid values:
        # 
        # - Wear: Wear a hat.
        # 
        # - None: No hat.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataHat, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImageModerationResponseBodyDataExtFaceDataLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        # The height of the face area. Unit: pixels.
        self.h = h  # type: int
        # The width of the face area. Unit: pixels.
        self.w = w  # type: int
        # The distance from the upper-left corner of the face area to the y-axis with the upper-left corner of the image as the coordinate origin. Unit: pixels.
        self.x = x  # type: int
        # The distance from the upper-left corner of the face area to the x-axis with the upper-left corner of the image as the coordinate origin. Unit: pixels.
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataLocation, self).to_map()
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


class ImageModerationResponseBodyDataExtFaceDataMask(TeaModel):
    def __init__(self, confidence=None, value=None):
        # The confidence level of the result of wearing the mask. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence  # type: float
        # The recognition result of whether to wear a mask. Valid values:
        # 
        # - Wear a mask.
        # 
        #  - None: No mask.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataMask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImageModerationResponseBodyDataExtFaceDataMustache(TeaModel):
    def __init__(self, confidence=None, value=None):
        # The confidence level of the result of the beard. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence  # type: float
        # The identification result of whether there is a beard.Valid values:
        # 
        # - Has:have a beard.
        # 
        # - None:No beard.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataMustache, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImageModerationResponseBodyDataExtFaceDataQuality(TeaModel):
    def __init__(self, blur=None, integrity=None, pitch=None, roll=None, yaw=None):
        # The blur of the face image. Valid values: 0 to 100. The higher the score, the more fuzzy it is.
        # Recommended values: 0 to 25.
        self.blur = blur  # type: float
        # The integrity of the human face. Recommended values:80 to 100.
        self.integrity = integrity  # type: float
        # The head-up or head-down angle of the face.
        # Recommended values:-30 to 30.
        self.pitch = pitch  # type: float
        # The plane rotation angle of the face.
        # Recommended values:-30 to 30.
        self.roll = roll  # type: float
        # The left and right shaking angle of the human face.
        # Recommended values:-30 to 30.
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceDataQuality, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.integrity is not None:
            result['Integrity'] = self.integrity
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class ImageModerationResponseBodyDataExtFaceData(TeaModel):
    def __init__(self, age=None, bang=None, gender=None, glasses=None, hairstyle=None, hat=None, location=None,
                 mask=None, mustache=None, quality=None, smile=None):
        # The age recognition result.
        self.age = age  # type: int
        # Indicates whether the recognition result of bangs is available.
        self.bang = bang  # type: ImageModerationResponseBodyDataExtFaceDataBang
        # The gender recognition result.
        self.gender = gender  # type: ImageModerationResponseBodyDataExtFaceDataGender
        # The recognition result of whether to wear glasses.
        # 
        # - None: No glasses.
        # 
        # - Wear: Wear glasses.
        # 
        # - Sunglass: Wear sunglasses.
        self.glasses = glasses  # type: str
        # The hairstyle recognition result.
        self.hairstyle = hairstyle  # type: ImageModerationResponseBodyDataExtFaceDataHairstyle
        # The recognition result of whether to wear a hat.
        self.hat = hat  # type: ImageModerationResponseBodyDataExtFaceDataHat
        # The location of the face.
        self.location = location  # type: ImageModerationResponseBodyDataExtFaceDataLocation
        # The recognition result of whether to wear a mask.
        self.mask = mask  # type: ImageModerationResponseBodyDataExtFaceDataMask
        # The identification result of whether there is a beard.
        self.mustache = mustache  # type: ImageModerationResponseBodyDataExtFaceDataMustache
        # The quality information of the face image.
        self.quality = quality  # type: ImageModerationResponseBodyDataExtFaceDataQuality
        # The smiling degree of the face.
        self.smile = smile  # type: float

    def validate(self):
        if self.bang:
            self.bang.validate()
        if self.gender:
            self.gender.validate()
        if self.hairstyle:
            self.hairstyle.validate()
        if self.hat:
            self.hat.validate()
        if self.location:
            self.location.validate()
        if self.mask:
            self.mask.validate()
        if self.mustache:
            self.mustache.validate()
        if self.quality:
            self.quality.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtFaceData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.bang is not None:
            result['Bang'] = self.bang.to_map()
        if self.gender is not None:
            result['Gender'] = self.gender.to_map()
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.hairstyle is not None:
            result['Hairstyle'] = self.hairstyle.to_map()
        if self.hat is not None:
            result['Hat'] = self.hat.to_map()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.mask is not None:
            result['Mask'] = self.mask.to_map()
        if self.mustache is not None:
            result['Mustache'] = self.mustache.to_map()
        if self.quality is not None:
            result['Quality'] = self.quality.to_map()
        if self.smile is not None:
            result['Smile'] = self.smile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Bang') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataBang()
            self.bang = temp_model.from_map(m['Bang'])
        if m.get('Gender') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataGender()
            self.gender = temp_model.from_map(m['Gender'])
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Hairstyle') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataHairstyle()
            self.hairstyle = temp_model.from_map(m['Hairstyle'])
        if m.get('Hat') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataHat()
            self.hat = temp_model.from_map(m['Hat'])
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Mask') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataMask()
            self.mask = temp_model.from_map(m['Mask'])
        if m.get('Mustache') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataMustache()
            self.mustache = temp_model.from_map(m['Mustache'])
        if m.get('Quality') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataQuality()
            self.quality = temp_model.from_map(m['Quality'])
        if m.get('Smile') is not None:
            self.smile = m.get('Smile')
        return self


class ImageModerationResponseBodyDataExtLogoDataLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        # The height of the text area, in pixels.
        self.h = h  # type: int
        # The width of the text area, in pixels.
        self.w = w  # type: int
        # The distance between the upper-left corner of the text area and the y-axis, using the upper-left corner of the image as the coordinate origin, in pixels.
        self.x = x  # type: int
        # The distance between the upper left corner of the text area and the x-axis, with the upper left corner of the image as the coordinate origin, in pixels.
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtLogoDataLocation, self).to_map()
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


class ImageModerationResponseBodyDataExtLogoDataLogo(TeaModel):
    def __init__(self, confidence=None, label=None, name=None):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence  # type: float
        # Logo category.
        self.label = label  # type: str
        # Logo name.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtLogoDataLogo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ImageModerationResponseBodyDataExtLogoData(TeaModel):
    def __init__(self, location=None, logo=None):
        # Location information.
        self.location = location  # type: ImageModerationResponseBodyDataExtLogoDataLocation
        # Logo information.
        self.logo = logo  # type: list[ImageModerationResponseBodyDataExtLogoDataLogo]

    def validate(self):
        if self.location:
            self.location.validate()
        if self.logo:
            for k in self.logo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtLogoData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        result['Logo'] = []
        if self.logo is not None:
            for k in self.logo:
                result['Logo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtLogoDataLocation()
            self.location = temp_model.from_map(m['Location'])
        self.logo = []
        if m.get('Logo') is not None:
            for k in m.get('Logo'):
                temp_model = ImageModerationResponseBodyDataExtLogoDataLogo()
                self.logo.append(temp_model.from_map(k))
        return self


class ImageModerationResponseBodyDataExtOcrResultLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        # The height of the text area, in pixels.
        self.h = h  # type: int
        # The width of the text area, in pixels.
        self.w = w  # type: int
        # The distance between the upper-left corner of the text area and the y-axis, using the upper-left corner of the image as the coordinate origin, in pixels.
        self.x = x  # type: int
        # The distance between the upper left corner of the text area and the x-axis, with the upper left corner of the image as the coordinate origin, in pixels.
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtOcrResultLocation, self).to_map()
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


class ImageModerationResponseBodyDataExtOcrResult(TeaModel):
    def __init__(self, location=None, text=None):
        # Location information.
        self.location = location  # type: ImageModerationResponseBodyDataExtOcrResultLocation
        # The text information in the recognized image.
        self.text = text  # type: str

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtOcrResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtOcrResultLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ImageModerationResponseBodyDataExtPublicFigureLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        # The height
        self.h = h  # type: int
        # The weight
        self.w = w  # type: int
        # X coordinate
        self.x = x  # type: int
        # Y coordinate
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtPublicFigureLocation, self).to_map()
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


class ImageModerationResponseBodyDataExtPublicFigure(TeaModel):
    def __init__(self, figure_id=None, figure_name=None, location=None):
        # Identified person coding information.
        self.figure_id = figure_id  # type: str
        # Identified person name information.
        self.figure_name = figure_name  # type: str
        # the data array of location info
        self.location = location  # type: list[ImageModerationResponseBodyDataExtPublicFigureLocation]

    def validate(self):
        if self.location:
            for k in self.location:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtPublicFigure, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_name is not None:
            result['FigureName'] = self.figure_name
        result['Location'] = []
        if self.location is not None:
            for k in self.location:
                result['Location'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureName') is not None:
            self.figure_name = m.get('FigureName')
        self.location = []
        if m.get('Location') is not None:
            for k in m.get('Location'):
                temp_model = ImageModerationResponseBodyDataExtPublicFigureLocation()
                self.location.append(temp_model.from_map(k))
        return self


class ImageModerationResponseBodyDataExtRecognition(TeaModel):
    def __init__(self, classification=None, confidence=None):
        # The category of image recognition.
        self.classification = classification  # type: str
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtRecognition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class ImageModerationResponseBodyDataExtTextInImageCustomText(TeaModel):
    def __init__(self, key_words=None, lib_id=None, lib_name=None):
        # Custom words, multiple words separated by commas.
        self.key_words = key_words  # type: str
        # Custom library ID.
        self.lib_id = lib_id  # type: str
        # Custom library name.
        self.lib_name = lib_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtTextInImageCustomText, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        return self


class ImageModerationResponseBodyDataExtTextInImageOcrResultLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        # The height of the text area, in pixels.
        self.h = h  # type: int
        # The width of the text area, in pixels.
        self.w = w  # type: int
        # The distance between the upper-left corner of the text area and the y-axis, using the upper-left corner of the image as the coordinate origin, in pixels.
        self.x = x  # type: int
        # The distance between the upper left corner of the text area and the x-axis, with the upper left corner of the image as the coordinate origin, in pixels.
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtTextInImageOcrResultLocation, self).to_map()
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


class ImageModerationResponseBodyDataExtTextInImageOcrResult(TeaModel):
    def __init__(self, location=None, text=None):
        # Location information.
        self.location = location  # type: ImageModerationResponseBodyDataExtTextInImageOcrResultLocation
        # The text information in the recognized image.
        self.text = text  # type: str

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtTextInImageOcrResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtTextInImageOcrResultLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ImageModerationResponseBodyDataExtTextInImage(TeaModel):
    def __init__(self, custom_text=None, ocr_result=None, risk_word=None):
        # When a custom text library is hit, the custom library ID, custom library name, and custom word are returned.
        self.custom_text = custom_text  # type: list[ImageModerationResponseBodyDataExtTextInImageCustomText]
        # Returns the text information in the recognized image.
        self.ocr_result = ocr_result  # type: list[ImageModerationResponseBodyDataExtTextInImageOcrResult]
        # The risk words that are hit. Multiple words are separated by commas (,).
        self.risk_word = risk_word  # type: list[str]

    def validate(self):
        if self.custom_text:
            for k in self.custom_text:
                if k:
                    k.validate()
        if self.ocr_result:
            for k in self.ocr_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExtTextInImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomText'] = []
        if self.custom_text is not None:
            for k in self.custom_text:
                result['CustomText'].append(k.to_map() if k else None)
        result['OcrResult'] = []
        if self.ocr_result is not None:
            for k in self.ocr_result:
                result['OcrResult'].append(k.to_map() if k else None)
        if self.risk_word is not None:
            result['RiskWord'] = self.risk_word
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_text = []
        if m.get('CustomText') is not None:
            for k in m.get('CustomText'):
                temp_model = ImageModerationResponseBodyDataExtTextInImageCustomText()
                self.custom_text.append(temp_model.from_map(k))
        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k in m.get('OcrResult'):
                temp_model = ImageModerationResponseBodyDataExtTextInImageOcrResult()
                self.ocr_result.append(temp_model.from_map(k))
        if m.get('RiskWord') is not None:
            self.risk_word = m.get('RiskWord')
        return self


class ImageModerationResponseBodyDataExt(TeaModel):
    def __init__(self, custom_image=None, face_data=None, logo_data=None, ocr_result=None, public_figure=None,
                 recognition=None, text_in_image=None):
        # If a custom image library is hit, information about the hit custom image library is returned.
        self.custom_image = custom_image  # type: list[ImageModerationResponseBodyDataExtCustomImage]
        # The returned face attribute information
        self.face_data = face_data  # type: list[ImageModerationResponseBodyDataExtFaceData]
        # Logo information.
        self.logo_data = logo_data  # type: list[ImageModerationResponseBodyDataExtLogoData]
        # Returns the text information in the recognized image.
        self.ocr_result = ocr_result  # type: list[ImageModerationResponseBodyDataExtOcrResult]
        # Person information list.
        self.public_figure = public_figure  # type: list[ImageModerationResponseBodyDataExtPublicFigure]
        # The result of image recognition.
        self.recognition = recognition  # type: list[ImageModerationResponseBodyDataExtRecognition]
        # Returns the text information in the hit image.
        self.text_in_image = text_in_image  # type: ImageModerationResponseBodyDataExtTextInImage

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.face_data:
            for k in self.face_data:
                if k:
                    k.validate()
        if self.logo_data:
            for k in self.logo_data:
                if k:
                    k.validate()
        if self.ocr_result:
            for k in self.ocr_result:
                if k:
                    k.validate()
        if self.public_figure:
            for k in self.public_figure:
                if k:
                    k.validate()
        if self.recognition:
            for k in self.recognition:
                if k:
                    k.validate()
        if self.text_in_image:
            self.text_in_image.validate()

    def to_map(self):
        _map = super(ImageModerationResponseBodyDataExt, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k in self.custom_image:
                result['CustomImage'].append(k.to_map() if k else None)
        result['FaceData'] = []
        if self.face_data is not None:
            for k in self.face_data:
                result['FaceData'].append(k.to_map() if k else None)
        result['LogoData'] = []
        if self.logo_data is not None:
            for k in self.logo_data:
                result['LogoData'].append(k.to_map() if k else None)
        result['OcrResult'] = []
        if self.ocr_result is not None:
            for k in self.ocr_result:
                result['OcrResult'].append(k.to_map() if k else None)
        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k in self.public_figure:
                result['PublicFigure'].append(k.to_map() if k else None)
        result['Recognition'] = []
        if self.recognition is not None:
            for k in self.recognition:
                result['Recognition'].append(k.to_map() if k else None)
        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = ImageModerationResponseBodyDataExtCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.face_data = []
        if m.get('FaceData') is not None:
            for k in m.get('FaceData'):
                temp_model = ImageModerationResponseBodyDataExtFaceData()
                self.face_data.append(temp_model.from_map(k))
        self.logo_data = []
        if m.get('LogoData') is not None:
            for k in m.get('LogoData'):
                temp_model = ImageModerationResponseBodyDataExtLogoData()
                self.logo_data.append(temp_model.from_map(k))
        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k in m.get('OcrResult'):
                temp_model = ImageModerationResponseBodyDataExtOcrResult()
                self.ocr_result.append(temp_model.from_map(k))
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = ImageModerationResponseBodyDataExtPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        self.recognition = []
        if m.get('Recognition') is not None:
            for k in m.get('Recognition'):
                temp_model = ImageModerationResponseBodyDataExtRecognition()
                self.recognition.append(temp_model.from_map(k))
        if m.get('TextInImage') is not None:
            temp_model = ImageModerationResponseBodyDataExtTextInImage()
            self.text_in_image = temp_model.from_map(m['TextInImage'])
        return self


class ImageModerationResponseBodyDataResult(TeaModel):
    def __init__(self, confidence=None, description=None, label=None):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence  # type: float
        # The description of the result.
        self.description = description  # type: str
        # The labels returned after the image moderation. Multiple risk labels and the corresponding scores of confidence levels may be returned for an image.
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
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ImageModerationResponseBodyData(TeaModel):
    def __init__(self, data_id=None, ext=None, result=None, risk_level=None):
        # The ID of the moderated object.
        # 
        # >  If you specify the dataId parameter in the request, the value of the dataId parameter is returned in the response.
        self.data_id = data_id  # type: str
        # Auxiliary reference information.
        self.ext = ext  # type: ImageModerationResponseBodyDataExt
        # The results of image moderation parameters such as the label parameter and the confidence parameter, which are an array structure.
        self.result = result  # type: list[ImageModerationResponseBodyDataResult]
        # Risk Level.
        self.risk_level = risk_level  # type: str

    def validate(self):
        if self.ext:
            self.ext.validate()
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
        if self.ext is not None:
            result['Ext'] = self.ext.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Ext') is not None:
            temp_model = ImageModerationResponseBodyDataExt()
            self.ext = temp_model.from_map(m['Ext'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ImageModerationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ImageModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: int
        # The moderation results.
        self.data = data  # type: ImageModerationResponseBodyData
        # The message that is returned in response to the request.
        self.msg = msg  # type: str
        # The request ID, which is used to locate and troubleshoot issues.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id  # type: str
        # The device ID.
        self.device_id = device_id  # type: str
        # Labels.
        self.labels = labels  # type: str
        # The JSON string used to locate the cause.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The moderation results.
        self.data = data  # type: TextModerationResponseBodyData
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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
        # The moderation service.
        # 
        # Valid values:
        # 
        # *   chat_detection_pro: moderation of interactive content of private chats_Professional
        # *   llm_response_moderation: moderation of text generated by LLMs
        # *   llm_query_moderation: moderation of input text of LLMs
        # *   nickname_detection_pro: moderation of user nicknames_Professional
        # *   comment_detection_pro: moderation of comment content of public chats_Professional
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
    def __init__(self, answer=None, hit_label=None, hit_lib_name=None):
        # The answer.
        self.answer = answer  # type: str
        # Hit Label
        self.hit_label = hit_label  # type: str
        # Hit Library Name
        self.hit_lib_name = hit_lib_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TextModerationPlusResponseBodyDataAdvice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.hit_label is not None:
            result['HitLabel'] = self.hit_label
        if self.hit_lib_name is not None:
            result['HitLibName'] = self.hit_lib_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('HitLabel') is not None:
            self.hit_label = m.get('HitLabel')
        if m.get('HitLibName') is not None:
            self.hit_lib_name = m.get('HitLibName')
        return self


class TextModerationPlusResponseBodyDataResultCustomizedHit(TeaModel):
    def __init__(self, key_words=None, lib_name=None):
        # The terms that are hit. Multiple terms are separated by commas (,).
        self.key_words = key_words  # type: str
        # The library name.
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
    def __init__(self, confidence=None, customized_hit=None, description=None, label=None, risk_words=None):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence  # type: float
        # The custom term hit by the moderated content.
        self.customized_hit = customized_hit  # type: list[TextModerationPlusResponseBodyDataResultCustomizedHit]
        # The description of the label.
        self.description = description  # type: str
        # The label.
        self.label = label  # type: str
        # The term hit by the moderated content.
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
        if self.description is not None:
            result['Description'] = self.description
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        return self


class TextModerationPlusResponseBodyData(TeaModel):
    def __init__(self, advice=None, result=None, risk_level=None, score=None):
        # The suggestion.
        self.advice = advice  # type: list[TextModerationPlusResponseBodyDataAdvice]
        # The results.
        self.result = result  # type: list[TextModerationPlusResponseBodyDataResult]
        # Risk Level
        self.risk_level = risk_level  # type: str
        # The score.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class TextModerationPlusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: int
        # The moderation results.
        self.data = data  # type: TextModerationPlusResponseBodyData
        # The message that is returned in response to the request.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the moderated object.
        self.data_id = data_id  # type: str
        # The reqId field returned by the Url Async Moderation API.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: UrlAsyncModerationResponseBodyData
        # The message that is returned in response to the request.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
    def __init__(self, data_id=None, task_id=None):
        # The ID of the moderated object.
        self.data_id = data_id  # type: str
        # The task ID.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VideoModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: VideoModerationResponseBodyData
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # Voice label.
        self.label = label  # type: str
        # The number of times that the label is matched.
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
    def __init__(self, end_time=None, end_timestamp=None, extend=None, labels=None, risk_level=None, risk_tips=None,
                 risk_words=None, score=None, start_time=None, start_timestamp=None, text=None, url=None):
        # The end time of the text after voice-to-text conversion. Unit: seconds.
        self.end_time = end_time  # type: long
        # The end timestamp of the segment. Unit: milliseconds.
        self.end_timestamp = end_timestamp  # type: long
        # A reserved parameter.
        self.extend = extend  # type: str
        # The details of the labels.
        self.labels = labels  # type: str
        self.risk_level = risk_level  # type: str
        # Subcategory labels. Multiple labels are separated by commas (,).
        self.risk_tips = risk_tips  # type: str
        # The risk words that are hit. Multiple words are separated by commas (,).
        self.risk_words = risk_words  # type: str
        # Risk score, default range 0-99.
        self.score = score  # type: float
        # The start time of the text after voice-to-text conversion. Unit: seconds.
        self.start_time = start_time  # type: long
        # The start timestamp of the segment. Unit: milliseconds.
        self.start_timestamp = start_timestamp  # type: long
        # The text converted from voice.
        self.text = text  # type: str
        # If the moderation object is a voice stream, this parameter indicates the temporary access URL of the voice stream to which the text entry corresponds. The validity period of the URL is 30 minutes. You must prepare another URL to store the audio stream at the earliest opportunity.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
    def __init__(self, audio_summarys=None, risk_level=None, slice_details=None):
        # Summary of voice labels.
        self.audio_summarys = audio_summarys  # type: list[VideoModerationResultResponseBodyDataAudioResultAudioSummarys]
        self.risk_level = risk_level  # type: str
        # The details about the text in the moderated voice. The value is a JSON array that contains one or more elements. Each element corresponds to a text entry.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VideoModerationResultResponseBodyDataAudioResultSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyDataFrameResultFrameSummarys(TeaModel):
    def __init__(self, description=None, label=None, label_sum=None):
        self.description = description  # type: str
        # The label against which a captured frame is matched.
        self.label = label  # type: str
        # The number of times that the label is matched.
        self.label_sum = label_sum  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFrameSummarys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage(TeaModel):
    def __init__(self, image_id=None, lib_id=None):
        # The ID of the hit custom image.
        self.image_id = image_id  # type: str
        # The custom image library ID of the hit.
        self.lib_id = lib_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure(TeaModel):
    def __init__(self, figure_id=None):
        # Identified person coding information.
        self.figure_id = figure_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure, self).to_map()
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


class VideoModerationResultResponseBodyDataFrameResultFramesResultsResult(TeaModel):
    def __init__(self, confidence=None, description=None, label=None):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence  # type: float
        self.description = description  # type: str
        # The label returned after a frame is moderated. Multiple risk labels and the corresponding scores of confidence levels may be returned for a frame.
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
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResults(TeaModel):
    def __init__(self, custom_image=None, public_figure=None, result=None, service=None, text_in_image=None):
        # If a custom image library is hit, information about the hit custom image library is returned.
        self.custom_image = custom_image  # type: list[VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage]
        # If the video contains a specific person, the recognized person code is returned.
        self.public_figure = public_figure  # type: list[VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure]
        # The results of frame moderation parameters such as the label parameter and the confidence parameter.
        self.result = result  # type: list[VideoModerationResultResponseBodyDataFrameResultFramesResultsResult]
        # The moderation service that is called.
        self.service = service  # type: str
        # Returns the text information in the hit image.
        self.text_in_image = text_in_image  # type: dict[str, any]

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.public_figure:
            for k in self.public_figure:
                if k:
                    k.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VideoModerationResultResponseBodyDataFrameResultFramesResults, self).to_map()
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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.service is not None:
            result['Service'] = self.service
        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('TextInImage') is not None:
            self.text_in_image = m.get('TextInImage')
        return self


class VideoModerationResultResponseBodyDataFrameResultFrames(TeaModel):
    def __init__(self, offset=None, results=None, risk_level=None, temp_url=None, timestamp=None):
        # The interval between the start of the video file and the captured frame. Unit: seconds.
        self.offset = offset  # type: float
        # The results of frame moderation parameters such as the label parameter and the confidence parameter.
        self.results = results  # type: list[VideoModerationResultResponseBodyDataFrameResultFramesResults]
        self.risk_level = risk_level  # type: str
        # The temporary URL of a captured frame. This URL is valid for 30 minutes.
        self.temp_url = temp_url  # type: str
        # The absolute timestamp. Unit: milliseconds.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TempUrl') is not None:
            self.temp_url = m.get('TempUrl')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class VideoModerationResultResponseBodyDataFrameResult(TeaModel):
    def __init__(self, frame_num=None, frame_summarys=None, frames=None, risk_level=None):
        # The number of captured frames that are returned for the video file.
        self.frame_num = frame_num  # type: int
        # The summary of the labels against which captured frames are matched.
        self.frame_summarys = frame_summarys  # type: list[VideoModerationResultResponseBodyDataFrameResultFrameSummarys]
        # The information about the frames that match the labels.
        self.frames = frames  # type: list[VideoModerationResultResponseBodyDataFrameResultFrames]
        self.risk_level = risk_level  # type: str

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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class VideoModerationResultResponseBodyData(TeaModel):
    def __init__(self, audio_result=None, data_id=None, frame_result=None, live_id=None, risk_level=None,
                 task_id=None):
        # The voice moderation results. The moderation results contain a structure.
        self.audio_result = audio_result  # type: VideoModerationResultResponseBodyDataAudioResult
        # The ID of the moderated object.
        self.data_id = data_id  # type: str
        # The image moderation results. If the call is successful, the HTTP status code 200 and moderation results are returned. The moderation results contain a structure.
        self.frame_result = frame_result  # type: VideoModerationResultResponseBodyDataFrameResult
        # The unique ID of the live stream.
        self.live_id = live_id  # type: str
        self.risk_level = risk_level  # type: str
        # The task ID.
        self.task_id = task_id  # type: str

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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VideoModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: VideoModerationResultResponseBodyData
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
    def __init__(self, data_id=None, task_id=None):
        # The ID of the moderated object.
        self.data_id = data_id  # type: str
        # The task ID.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoiceModerationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VoiceModerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: VoiceModerationResponseBodyData
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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
        # The type of the moderation service.
        self.service = service  # type: str
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The end time of the text after audio-to-text conversion. Unit: seconds.
        self.end_time = end_time  # type: long
        # The end timestamp of the segment. Unit: milliseconds.
        self.end_timestamp = end_timestamp  # type: long
        # A reserved parameter.
        self.extend = extend  # type: str
        # The details of the labels.
        self.labels = labels  # type: str
        # Reserved field.
        self.origin_algo_result = origin_algo_result  # type: dict[str, any]
        # The risk details that are hit.
        self.risk_tips = risk_tips  # type: str
        # The risk words that are hit.
        self.risk_words = risk_words  # type: str
        # Risk score, default range 0-99.
        self.score = score  # type: float
        # The start time of the text after audio-to-text conversion. Unit: seconds.
        self.start_time = start_time  # type: long
        # The start timestamp of the segment. Unit: milliseconds.
        self.start_timestamp = start_timestamp  # type: long
        # The text converted from voice.
        self.text = text  # type: str
        # The temporary access address of the audio segment. The validity period of the URL is 30 minutes. You must prepare another URL to store the audio segment at the earliest opportunity.
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
    def __init__(self, data_id=None, live_id=None, slice_details=None, task_id=None, url=None):
        # The ID of the moderated object.
        self.data_id = data_id  # type: str
        # The unique ID of the live stream.
        self.live_id = live_id  # type: str
        # The details about the audio segments.
        self.slice_details = slice_details  # type: list[VoiceModerationResultResponseBodyDataSliceDetails]
        # The task ID.
        self.task_id = task_id  # type: str
        # The URL of the moderation object.
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
        if self.data_id is not None:
            result['DataId'] = self.data_id
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
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
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
        # The returned HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: VoiceModerationResultResponseBodyData
        # The message that is returned in response to the request.
        self.message = message  # type: str
        # The request ID.
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


