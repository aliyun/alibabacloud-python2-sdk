# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class GetAsyncJobResultRequest(TeaModel):
    def __init__(self, async=None, job_id=None):
        self.async = async  # type: bool
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.async is not None:
            result['Async'] = self.async
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async = m.get('Async')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(self, status=None, error_message=None, result=None, error_code=None, job_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.result = TeaConverter.to_unicode(result)  # type: unicode
        self.error_code = TeaConverter.to_unicode(error_code)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: GetAsyncJobResultResponseBodyData

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
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAsyncJobResultResponseBody

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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentGreenScreenVideoRequest(TeaModel):
    def __init__(self, video_url=None, async=None):
        # A short description of struct
        self.video_url = TeaConverter.to_unicode(video_url)  # type: unicode
        self.async = async  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.async is not None:
            result['Async'] = self.async
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        if m.get('Async') is not None:
            self.async = m.get('Async')
        return self


class SegmentGreenScreenVideoAdvanceRequest(TeaModel):
    def __init__(self, video_urlobject=None, async=None):
        self.video_urlobject = video_urlobject  # type: READABLE
        self.async = async  # type: bool

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        result = dict()
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.async is not None:
            result['Async'] = self.async
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURLObject') is not None:
            self.video_urlobject = m.get('VideoURLObject')
        if m.get('Async') is not None:
            self.async = m.get('Async')
        return self


class SegmentGreenScreenVideoResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = TeaConverter.to_unicode(video_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class SegmentGreenScreenVideoResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: SegmentGreenScreenVideoResponseBodyData

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
            temp_model = SegmentGreenScreenVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentGreenScreenVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SegmentGreenScreenVideoResponseBody

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
            temp_model = SegmentGreenScreenVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentHalfBodyRequest(TeaModel):
    def __init__(self, video_url=None, async=None):
        self.video_url = TeaConverter.to_unicode(video_url)  # type: unicode
        self.async = async  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async is not None:
            result['Async'] = self.async
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async = m.get('Async')
        return self


class SegmentHalfBodyAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, async=None):
        self.video_url_object = video_url_object  # type: READABLE
        self.async = async  # type: bool

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
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


class SegmentHalfBodyResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = TeaConverter.to_unicode(video_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class SegmentHalfBodyResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: SegmentHalfBodyResponseBodyData

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
            temp_model = SegmentHalfBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentHalfBodyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SegmentHalfBodyResponseBody

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
            temp_model = SegmentHalfBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentVideoBodyRequest(TeaModel):
    def __init__(self, video_url=None, async=None):
        self.video_url = TeaConverter.to_unicode(video_url)  # type: unicode
        self.async = async  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async is not None:
            result['Async'] = self.async
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async = m.get('Async')
        return self


class SegmentVideoBodyAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, async=None):
        self.video_url_object = video_url_object  # type: READABLE
        self.async = async  # type: bool

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
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


class SegmentVideoBodyResponseBodyData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = TeaConverter.to_unicode(video_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class SegmentVideoBodyResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: SegmentVideoBodyResponseBodyData

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
            temp_model = SegmentVideoBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentVideoBodyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SegmentVideoBodyResponseBody

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
            temp_model = SegmentVideoBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


