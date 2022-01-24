# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetTaskResultRequest(TeaModel):
    def __init__(self, debug=None, task_id=None):
        self.debug = debug  # type: bool
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResultResponseBodyResultParagraphs(TeaModel):
    def __init__(self, begin_time=None, channel_id=None, end_time=None, text=None):
        self.begin_time = begin_time  # type: long
        self.channel_id = channel_id  # type: long
        self.end_time = end_time  # type: long
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResultResponseBodyResultParagraphs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTIme'] = self.begin_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTIme') is not None:
            self.begin_time = m.get('BeginTIme')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetTaskResultResponseBodyResultSentences(TeaModel):
    def __init__(self, begin_time=None, channel_id=None, emotion_value=None, end_time=None, silence_duration=None,
                 speaker_id=None, speech_rate=None, text=None):
        self.begin_time = begin_time  # type: long
        self.channel_id = channel_id  # type: long
        self.emotion_value = emotion_value  # type: float
        self.end_time = end_time  # type: long
        self.silence_duration = silence_duration  # type: int
        self.speaker_id = speaker_id  # type: str
        self.speech_rate = speech_rate  # type: int
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResultResponseBodyResultSentences, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.speaker_id is not None:
            result['SpeakerId'] = self.speaker_id
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeakerId') is not None:
            self.speaker_id = m.get('SpeakerId')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetTaskResultResponseBodyResultWords(TeaModel):
    def __init__(self, begin_time=None, channel_id=None, end_time=None, word=None):
        self.begin_time = begin_time  # type: long
        self.channel_id = channel_id  # type: long
        self.end_time = end_time  # type: long
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResultResponseBodyResultWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class GetTaskResultResponseBodyResult(TeaModel):
    def __init__(self, paragraphs=None, sentences=None, words=None):
        self.paragraphs = paragraphs  # type: list[GetTaskResultResponseBodyResultParagraphs]
        self.sentences = sentences  # type: list[GetTaskResultResponseBodyResultSentences]
        self.words = words  # type: list[GetTaskResultResponseBodyResultWords]

    def validate(self):
        if self.paragraphs:
            for k in self.paragraphs:
                if k:
                    k.validate()
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()
        if self.words:
            for k in self.words:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskResultResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Paragraphs'] = []
        if self.paragraphs is not None:
            for k in self.paragraphs:
                result['Paragraphs'].append(k.to_map() if k else None)
        result['Sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['Sentences'].append(k.to_map() if k else None)
        result['Words'] = []
        if self.words is not None:
            for k in self.words:
                result['Words'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.paragraphs = []
        if m.get('Paragraphs') is not None:
            for k in m.get('Paragraphs'):
                temp_model = GetTaskResultResponseBodyResultParagraphs()
                self.paragraphs.append(temp_model.from_map(k))
        self.sentences = []
        if m.get('Sentences') is not None:
            for k in m.get('Sentences'):
                temp_model = GetTaskResultResponseBodyResultSentences()
                self.sentences.append(temp_model.from_map(k))
        self.words = []
        if m.get('Words') is not None:
            for k in m.get('Words'):
                temp_model = GetTaskResultResponseBodyResultWords()
                self.words.append(temp_model.from_map(k))
        return self


class GetTaskResultResponseBody(TeaModel):
    def __init__(self, biz_duration=None, request_id=None, result=None, solve_time=None, status_code=None,
                 status_text=None, task_id=None):
        self.biz_duration = biz_duration  # type: int
        self.request_id = request_id  # type: str
        self.result = result  # type: GetTaskResultResponseBodyResult
        self.solve_time = solve_time  # type: long
        self.status_code = status_code  # type: long
        self.status_text = status_text  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetTaskResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_duration is not None:
            result['BizDuration'] = self.biz_duration
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.solve_time is not None:
            result['SolveTime'] = self.solve_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_text is not None:
            result['StatusText'] = self.status_text
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizDuration') is not None:
            self.biz_duration = m.get('BizDuration')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetTaskResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('SolveTime') is not None:
            self.solve_time = m.get('SolveTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusText') is not None:
            self.status_text = m.get('StatusText')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTaskResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResultResponse, self).to_map()
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
            temp_model = GetTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTaskRequest(TeaModel):
    def __init__(self, debug=None, task=None):
        self.debug = debug  # type: bool
        self.task = task  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.task is not None:
            result['Task'] = self.task
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        return self


class SubmitTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, status_code=None, status_text=None, task_id=None):
        self.request_id = request_id  # type: str
        self.status_code = status_code  # type: long
        self.status_text = status_text  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_text is not None:
            result['StatusText'] = self.status_text
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusText') is not None:
            self.status_text = m.get('StatusText')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SubmitTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTaskResponse, self).to_map()
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
            temp_model = SubmitTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


