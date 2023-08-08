# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateFileTransRequest(TeaModel):
    def __init__(self, ability_params=None, app_key=None, asr_params=None, audio_language=None,
                 audio_oss_bucket=None, audio_oss_path=None, audio_output_enabled=None, audio_output_oss_bucket=None,
                 audio_output_oss_path=None, audio_role_num=None, audio_segments_enabled=None, lab_params=None, tags=None, trans_key=None,
                 trans_result_oss_bucket=None, trans_result_oss_path=None, video_output_enabled=None, video_output_oss_bucket=None,
                 video_output_oss_path=None):
        self.ability_params = ability_params  # type: dict[str, any]
        self.app_key = app_key  # type: str
        self.asr_params = asr_params  # type: dict[str, any]
        self.audio_language = audio_language  # type: str
        self.audio_oss_bucket = audio_oss_bucket  # type: str
        self.audio_oss_path = audio_oss_path  # type: str
        self.audio_output_enabled = audio_output_enabled  # type: bool
        self.audio_output_oss_bucket = audio_output_oss_bucket  # type: str
        self.audio_output_oss_path = audio_output_oss_path  # type: str
        self.audio_role_num = audio_role_num  # type: str
        self.audio_segments_enabled = audio_segments_enabled  # type: bool
        self.lab_params = lab_params  # type: dict[str, any]
        self.tags = tags  # type: dict[str, any]
        self.trans_key = trans_key  # type: str
        self.trans_result_oss_bucket = trans_result_oss_bucket  # type: str
        self.trans_result_oss_path = trans_result_oss_path  # type: str
        self.video_output_enabled = video_output_enabled  # type: bool
        self.video_output_oss_bucket = video_output_oss_bucket  # type: str
        self.video_output_oss_path = video_output_oss_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileTransRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ability_params is not None:
            result['AbilityParams'] = self.ability_params
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.asr_params is not None:
            result['AsrParams'] = self.asr_params
        if self.audio_language is not None:
            result['AudioLanguage'] = self.audio_language
        if self.audio_oss_bucket is not None:
            result['AudioOssBucket'] = self.audio_oss_bucket
        if self.audio_oss_path is not None:
            result['AudioOssPath'] = self.audio_oss_path
        if self.audio_output_enabled is not None:
            result['AudioOutputEnabled'] = self.audio_output_enabled
        if self.audio_output_oss_bucket is not None:
            result['AudioOutputOssBucket'] = self.audio_output_oss_bucket
        if self.audio_output_oss_path is not None:
            result['AudioOutputOssPath'] = self.audio_output_oss_path
        if self.audio_role_num is not None:
            result['AudioRoleNum'] = self.audio_role_num
        if self.audio_segments_enabled is not None:
            result['AudioSegmentsEnabled'] = self.audio_segments_enabled
        if self.lab_params is not None:
            result['LabParams'] = self.lab_params
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.trans_key is not None:
            result['TransKey'] = self.trans_key
        if self.trans_result_oss_bucket is not None:
            result['TransResultOssBucket'] = self.trans_result_oss_bucket
        if self.trans_result_oss_path is not None:
            result['TransResultOssPath'] = self.trans_result_oss_path
        if self.video_output_enabled is not None:
            result['VideoOutputEnabled'] = self.video_output_enabled
        if self.video_output_oss_bucket is not None:
            result['VideoOutputOssBucket'] = self.video_output_oss_bucket
        if self.video_output_oss_path is not None:
            result['VideoOutputOssPath'] = self.video_output_oss_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbilityParams') is not None:
            self.ability_params = m.get('AbilityParams')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AsrParams') is not None:
            self.asr_params = m.get('AsrParams')
        if m.get('AudioLanguage') is not None:
            self.audio_language = m.get('AudioLanguage')
        if m.get('AudioOssBucket') is not None:
            self.audio_oss_bucket = m.get('AudioOssBucket')
        if m.get('AudioOssPath') is not None:
            self.audio_oss_path = m.get('AudioOssPath')
        if m.get('AudioOutputEnabled') is not None:
            self.audio_output_enabled = m.get('AudioOutputEnabled')
        if m.get('AudioOutputOssBucket') is not None:
            self.audio_output_oss_bucket = m.get('AudioOutputOssBucket')
        if m.get('AudioOutputOssPath') is not None:
            self.audio_output_oss_path = m.get('AudioOutputOssPath')
        if m.get('AudioRoleNum') is not None:
            self.audio_role_num = m.get('AudioRoleNum')
        if m.get('AudioSegmentsEnabled') is not None:
            self.audio_segments_enabled = m.get('AudioSegmentsEnabled')
        if m.get('LabParams') is not None:
            self.lab_params = m.get('LabParams')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TransKey') is not None:
            self.trans_key = m.get('TransKey')
        if m.get('TransResultOssBucket') is not None:
            self.trans_result_oss_bucket = m.get('TransResultOssBucket')
        if m.get('TransResultOssPath') is not None:
            self.trans_result_oss_path = m.get('TransResultOssPath')
        if m.get('VideoOutputEnabled') is not None:
            self.video_output_enabled = m.get('VideoOutputEnabled')
        if m.get('VideoOutputOssBucket') is not None:
            self.video_output_oss_bucket = m.get('VideoOutputOssBucket')
        if m.get('VideoOutputOssPath') is not None:
            self.video_output_oss_path = m.get('VideoOutputOssPath')
        return self


class CreateFileTransResponseBodyData(TeaModel):
    def __init__(self, trans_id=None, trans_key=None):
        self.trans_id = trans_id  # type: str
        self.trans_key = trans_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileTransResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_id is not None:
            result['TransId'] = self.trans_id
        if self.trans_key is not None:
            result['TransKey'] = self.trans_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransId') is not None:
            self.trans_id = m.get('TransId')
        if m.get('TransKey') is not None:
            self.trans_key = m.get('TransKey')
        return self


class CreateFileTransResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateFileTransResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateFileTransResponseBody, self).to_map()
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
            temp_model = CreateFileTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFileTransResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileTransResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileTransResponse, self).to_map()
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
            temp_model = CreateFileTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMeetingTransRequest(TeaModel):
    def __init__(self, ability_params=None, app_key=None, asr_params=None, audio_bit_rate=None, audio_format=None,
                 audio_language=None, audio_output_enabled=None, audio_output_oss_bucket=None, audio_output_oss_path=None,
                 audio_package=None, audio_sample_rate=None, audio_segments_enabled=None, doc_result_enabled=None,
                 lab_params=None, meeting_key=None, meeting_result_enabled=None, meeting_result_oss_bucket=None,
                 meeting_result_oss_path=None, realtime_active_result_level=None, realtime_result_enabled=None,
                 realtime_result_level=None, realtime_result_meeting_info_enabled=None, realtime_result_words_enabled=None, tags=None,
                 translate_active_result_level=None, translate_languages=None, translate_result_enabled=None, translate_result_level=None):
        self.ability_params = ability_params  # type: dict[str, any]
        self.app_key = app_key  # type: str
        self.asr_params = asr_params  # type: dict[str, any]
        self.audio_bit_rate = audio_bit_rate  # type: int
        self.audio_format = audio_format  # type: str
        self.audio_language = audio_language  # type: str
        self.audio_output_enabled = audio_output_enabled  # type: bool
        self.audio_output_oss_bucket = audio_output_oss_bucket  # type: str
        self.audio_output_oss_path = audio_output_oss_path  # type: str
        self.audio_package = audio_package  # type: str
        self.audio_sample_rate = audio_sample_rate  # type: int
        self.audio_segments_enabled = audio_segments_enabled  # type: bool
        self.doc_result_enabled = doc_result_enabled  # type: bool
        self.lab_params = lab_params  # type: dict[str, any]
        self.meeting_key = meeting_key  # type: str
        self.meeting_result_enabled = meeting_result_enabled  # type: bool
        self.meeting_result_oss_bucket = meeting_result_oss_bucket  # type: str
        self.meeting_result_oss_path = meeting_result_oss_path  # type: str
        self.realtime_active_result_level = realtime_active_result_level  # type: int
        self.realtime_result_enabled = realtime_result_enabled  # type: bool
        self.realtime_result_level = realtime_result_level  # type: int
        self.realtime_result_meeting_info_enabled = realtime_result_meeting_info_enabled  # type: bool
        self.realtime_result_words_enabled = realtime_result_words_enabled  # type: bool
        self.tags = tags  # type: dict[str, any]
        self.translate_active_result_level = translate_active_result_level  # type: int
        self.translate_languages = translate_languages  # type: str
        self.translate_result_enabled = translate_result_enabled  # type: bool
        self.translate_result_level = translate_result_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMeetingTransRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ability_params is not None:
            result['AbilityParams'] = self.ability_params
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.asr_params is not None:
            result['AsrParams'] = self.asr_params
        if self.audio_bit_rate is not None:
            result['AudioBitRate'] = self.audio_bit_rate
        if self.audio_format is not None:
            result['AudioFormat'] = self.audio_format
        if self.audio_language is not None:
            result['AudioLanguage'] = self.audio_language
        if self.audio_output_enabled is not None:
            result['AudioOutputEnabled'] = self.audio_output_enabled
        if self.audio_output_oss_bucket is not None:
            result['AudioOutputOssBucket'] = self.audio_output_oss_bucket
        if self.audio_output_oss_path is not None:
            result['AudioOutputOssPath'] = self.audio_output_oss_path
        if self.audio_package is not None:
            result['AudioPackage'] = self.audio_package
        if self.audio_sample_rate is not None:
            result['AudioSampleRate'] = self.audio_sample_rate
        if self.audio_segments_enabled is not None:
            result['AudioSegmentsEnabled'] = self.audio_segments_enabled
        if self.doc_result_enabled is not None:
            result['DocResultEnabled'] = self.doc_result_enabled
        if self.lab_params is not None:
            result['LabParams'] = self.lab_params
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        if self.meeting_result_enabled is not None:
            result['MeetingResultEnabled'] = self.meeting_result_enabled
        if self.meeting_result_oss_bucket is not None:
            result['MeetingResultOssBucket'] = self.meeting_result_oss_bucket
        if self.meeting_result_oss_path is not None:
            result['MeetingResultOssPath'] = self.meeting_result_oss_path
        if self.realtime_active_result_level is not None:
            result['RealtimeActiveResultLevel'] = self.realtime_active_result_level
        if self.realtime_result_enabled is not None:
            result['RealtimeResultEnabled'] = self.realtime_result_enabled
        if self.realtime_result_level is not None:
            result['RealtimeResultLevel'] = self.realtime_result_level
        if self.realtime_result_meeting_info_enabled is not None:
            result['RealtimeResultMeetingInfoEnabled'] = self.realtime_result_meeting_info_enabled
        if self.realtime_result_words_enabled is not None:
            result['RealtimeResultWordsEnabled'] = self.realtime_result_words_enabled
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.translate_active_result_level is not None:
            result['TranslateActiveResultLevel'] = self.translate_active_result_level
        if self.translate_languages is not None:
            result['TranslateLanguages'] = self.translate_languages
        if self.translate_result_enabled is not None:
            result['TranslateResultEnabled'] = self.translate_result_enabled
        if self.translate_result_level is not None:
            result['TranslateResultLevel'] = self.translate_result_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbilityParams') is not None:
            self.ability_params = m.get('AbilityParams')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AsrParams') is not None:
            self.asr_params = m.get('AsrParams')
        if m.get('AudioBitRate') is not None:
            self.audio_bit_rate = m.get('AudioBitRate')
        if m.get('AudioFormat') is not None:
            self.audio_format = m.get('AudioFormat')
        if m.get('AudioLanguage') is not None:
            self.audio_language = m.get('AudioLanguage')
        if m.get('AudioOutputEnabled') is not None:
            self.audio_output_enabled = m.get('AudioOutputEnabled')
        if m.get('AudioOutputOssBucket') is not None:
            self.audio_output_oss_bucket = m.get('AudioOutputOssBucket')
        if m.get('AudioOutputOssPath') is not None:
            self.audio_output_oss_path = m.get('AudioOutputOssPath')
        if m.get('AudioPackage') is not None:
            self.audio_package = m.get('AudioPackage')
        if m.get('AudioSampleRate') is not None:
            self.audio_sample_rate = m.get('AudioSampleRate')
        if m.get('AudioSegmentsEnabled') is not None:
            self.audio_segments_enabled = m.get('AudioSegmentsEnabled')
        if m.get('DocResultEnabled') is not None:
            self.doc_result_enabled = m.get('DocResultEnabled')
        if m.get('LabParams') is not None:
            self.lab_params = m.get('LabParams')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        if m.get('MeetingResultEnabled') is not None:
            self.meeting_result_enabled = m.get('MeetingResultEnabled')
        if m.get('MeetingResultOssBucket') is not None:
            self.meeting_result_oss_bucket = m.get('MeetingResultOssBucket')
        if m.get('MeetingResultOssPath') is not None:
            self.meeting_result_oss_path = m.get('MeetingResultOssPath')
        if m.get('RealtimeActiveResultLevel') is not None:
            self.realtime_active_result_level = m.get('RealtimeActiveResultLevel')
        if m.get('RealtimeResultEnabled') is not None:
            self.realtime_result_enabled = m.get('RealtimeResultEnabled')
        if m.get('RealtimeResultLevel') is not None:
            self.realtime_result_level = m.get('RealtimeResultLevel')
        if m.get('RealtimeResultMeetingInfoEnabled') is not None:
            self.realtime_result_meeting_info_enabled = m.get('RealtimeResultMeetingInfoEnabled')
        if m.get('RealtimeResultWordsEnabled') is not None:
            self.realtime_result_words_enabled = m.get('RealtimeResultWordsEnabled')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TranslateActiveResultLevel') is not None:
            self.translate_active_result_level = m.get('TranslateActiveResultLevel')
        if m.get('TranslateLanguages') is not None:
            self.translate_languages = m.get('TranslateLanguages')
        if m.get('TranslateResultEnabled') is not None:
            self.translate_result_enabled = m.get('TranslateResultEnabled')
        if m.get('TranslateResultLevel') is not None:
            self.translate_result_level = m.get('TranslateResultLevel')
        return self


class CreateMeetingTransResponseBodyData(TeaModel):
    def __init__(self, meeting_id=None, meeting_join_url=None, meeting_key=None):
        self.meeting_id = meeting_id  # type: str
        self.meeting_join_url = meeting_join_url  # type: str
        self.meeting_key = meeting_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMeetingTransResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_id is not None:
            result['MeetingId'] = self.meeting_id
        if self.meeting_join_url is not None:
            result['MeetingJoinUrl'] = self.meeting_join_url
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MeetingId') is not None:
            self.meeting_id = m.get('MeetingId')
        if m.get('MeetingJoinUrl') is not None:
            self.meeting_join_url = m.get('MeetingJoinUrl')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        return self


class CreateMeetingTransResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateMeetingTransResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateMeetingTransResponseBody, self).to_map()
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
            temp_model = CreateMeetingTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMeetingTransResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMeetingTransResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMeetingTransResponse, self).to_map()
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
            temp_model = CreateMeetingTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileTransResponseBodyData(TeaModel):
    def __init__(self, trans_id=None, trans_key=None, trans_status=None):
        self.trans_id = trans_id  # type: str
        self.trans_key = trans_key  # type: str
        self.trans_status = trans_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileTransResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_id is not None:
            result['TransId'] = self.trans_id
        if self.trans_key is not None:
            result['TransKey'] = self.trans_key
        if self.trans_status is not None:
            result['TransStatus'] = self.trans_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransId') is not None:
            self.trans_id = m.get('TransId')
        if m.get('TransKey') is not None:
            self.trans_key = m.get('TransKey')
        if m.get('TransStatus') is not None:
            self.trans_status = m.get('TransStatus')
        return self


class GetFileTransResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetFileTransResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFileTransResponseBody, self).to_map()
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
            temp_model = GetFileTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFileTransResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFileTransResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileTransResponse, self).to_map()
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
            temp_model = GetFileTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMeetingTransResponseBodyData(TeaModel):
    def __init__(self, meeting_id=None, meeting_key=None, meeting_status=None):
        self.meeting_id = meeting_id  # type: str
        self.meeting_key = meeting_key  # type: str
        self.meeting_status = meeting_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMeetingTransResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_id is not None:
            result['MeetingId'] = self.meeting_id
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        if self.meeting_status is not None:
            result['MeetingStatus'] = self.meeting_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MeetingId') is not None:
            self.meeting_id = m.get('MeetingId')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        if m.get('MeetingStatus') is not None:
            self.meeting_status = m.get('MeetingStatus')
        return self


class GetMeetingTransResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetMeetingTransResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMeetingTransResponseBody, self).to_map()
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
            temp_model = GetMeetingTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMeetingTransResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMeetingTransResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMeetingTransResponse, self).to_map()
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
            temp_model = GetMeetingTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMeetingTransRequest(TeaModel):
    def __init__(self, meeting_role_num=None, only_role_split_result=None):
        self.meeting_role_num = meeting_role_num  # type: int
        self.only_role_split_result = only_role_split_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMeetingTransRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_role_num is not None:
            result['MeetingRoleNum'] = self.meeting_role_num
        if self.only_role_split_result is not None:
            result['OnlyRoleSplitResult'] = self.only_role_split_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MeetingRoleNum') is not None:
            self.meeting_role_num = m.get('MeetingRoleNum')
        if m.get('OnlyRoleSplitResult') is not None:
            self.only_role_split_result = m.get('OnlyRoleSplitResult')
        return self


class StopMeetingTransResponseBodyData(TeaModel):
    def __init__(self, meeting_id=None, meeting_key=None, meeting_status=None):
        self.meeting_id = meeting_id  # type: str
        self.meeting_key = meeting_key  # type: str
        self.meeting_status = meeting_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMeetingTransResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_id is not None:
            result['MeetingId'] = self.meeting_id
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        if self.meeting_status is not None:
            result['MeetingStatus'] = self.meeting_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MeetingId') is not None:
            self.meeting_id = m.get('MeetingId')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        if m.get('MeetingStatus') is not None:
            self.meeting_status = m.get('MeetingStatus')
        return self


class StopMeetingTransResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: StopMeetingTransResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StopMeetingTransResponseBody, self).to_map()
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
            temp_model = StopMeetingTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopMeetingTransResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopMeetingTransResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopMeetingTransResponse, self).to_map()
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
            temp_model = StopMeetingTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


