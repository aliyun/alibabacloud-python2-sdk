# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddRecordTemplateRequestBackgrounds(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordTemplateRequestBackgrounds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class AddRecordTemplateRequestClockWidgets(TeaModel):
    def __init__(self, font_color=None, font_size=None, font_type=None, x=None, y=None, zorder=None):
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordTemplateRequestClockWidgets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class AddRecordTemplateRequestWatermarks(TeaModel):
    def __init__(self, alpha=None, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordTemplateRequestWatermarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class AddRecordTemplateRequest(TeaModel):
    def __init__(self, app_id=None, background_color=None, backgrounds=None, clock_widgets=None,
                 delay_stop_time=None, enable_m3u_8date_time=None, file_split_interval=None, formats=None, http_callback_url=None,
                 layout_ids=None, media_encode=None, mns_queue=None, name=None, oss_bucket=None, oss_endpoint=None,
                 oss_file_prefix=None, owner_id=None, task_profile=None, watermarks=None):
        self.app_id = app_id  # type: str
        self.background_color = background_color  # type: int
        self.backgrounds = backgrounds  # type: list[AddRecordTemplateRequestBackgrounds]
        self.clock_widgets = clock_widgets  # type: list[AddRecordTemplateRequestClockWidgets]
        self.delay_stop_time = delay_stop_time  # type: int
        self.enable_m3u_8date_time = enable_m3u_8date_time  # type: bool
        self.file_split_interval = file_split_interval  # type: int
        self.formats = formats  # type: list[str]
        self.http_callback_url = http_callback_url  # type: str
        self.layout_ids = layout_ids  # type: list[long]
        self.media_encode = media_encode  # type: int
        self.mns_queue = mns_queue  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.owner_id = owner_id  # type: long
        self.task_profile = task_profile  # type: str
        self.watermarks = watermarks  # type: list[AddRecordTemplateRequestWatermarks]

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddRecordTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time
        if self.enable_m3u_8date_time is not None:
            result['EnableM3u8DateTime'] = self.enable_m3u_8date_time
        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval
        if self.formats is not None:
            result['Formats'] = self.formats
        if self.http_callback_url is not None:
            result['HttpCallbackUrl'] = self.http_callback_url
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = AddRecordTemplateRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = AddRecordTemplateRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')
        if m.get('EnableM3u8DateTime') is not None:
            self.enable_m3u_8date_time = m.get('EnableM3u8DateTime')
        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        if m.get('HttpCallbackUrl') is not None:
            self.http_callback_url = m.get('HttpCallbackUrl')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = AddRecordTemplateRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class AddRecordTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class AddRecordTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddRecordTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRecordTemplateResponse, self).to_map()
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
            temp_model = AddRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoLiveStreamRuleRequest(TeaModel):
    def __init__(self, app_id=None, call_back=None, channel_id_prefixes=None, channel_ids=None, media_encode=None,
                 owner_id=None, play_domain=None, rule_name=None):
        self.app_id = app_id  # type: str
        self.call_back = call_back  # type: str
        self.channel_id_prefixes = channel_id_prefixes  # type: list[str]
        self.channel_ids = channel_ids  # type: list[str]
        self.media_encode = media_encode  # type: int
        self.owner_id = owner_id  # type: long
        self.play_domain = play_domain  # type: str
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoLiveStreamRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.channel_id_prefixes is not None:
            result['ChannelIdPrefixes'] = self.channel_id_prefixes
        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('ChannelIdPrefixes') is not None:
            self.channel_id_prefixes = m.get('ChannelIdPrefixes')
        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_id=None):
        self.request_id = request_id  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoLiveStreamRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateAutoLiveStreamRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAutoLiveStreamRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAutoLiveStreamRuleResponse, self).to_map()
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
            temp_model = CreateAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventSubscribeRequest(TeaModel):
    def __init__(self, app_id=None, callback_url=None, channel_id=None, client_token=None, events=None,
                 need_callback_auth=None, owner_id=None, role=None, users=None):
        self.app_id = app_id  # type: str
        self.callback_url = callback_url  # type: str
        self.channel_id = channel_id  # type: str
        self.client_token = client_token  # type: str
        self.events = events  # type: list[str]
        self.need_callback_auth = need_callback_auth  # type: bool
        self.owner_id = owner_id  # type: long
        self.role = role  # type: long
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSubscribeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.events is not None:
            result['Events'] = self.events
        if self.need_callback_auth is not None:
            result['NeedCallbackAuth'] = self.need_callback_auth
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('NeedCallbackAuth') is not None:
            self.need_callback_auth = m.get('NeedCallbackAuth')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateEventSubscribeResponseBody(TeaModel):
    def __init__(self, request_id=None, subscribe_id=None):
        self.request_id = request_id  # type: str
        self.subscribe_id = subscribe_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSubscribeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')
        return self


class CreateEventSubscribeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEventSubscribeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEventSubscribeResponse, self).to_map()
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
            temp_model = CreateEventSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMPULayoutRequestPanes(TeaModel):
    def __init__(self, height=None, major_pane=None, pane_id=None, width=None, x=None, y=None, zorder=None):
        self.height = height  # type: float
        self.major_pane = major_pane  # type: int
        self.pane_id = pane_id  # type: int
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMPULayoutRequestPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class CreateMPULayoutRequest(TeaModel):
    def __init__(self, app_id=None, audio_mix_count=None, name=None, owner_id=None, panes=None):
        self.app_id = app_id  # type: str
        self.audio_mix_count = audio_mix_count  # type: int
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.panes = panes  # type: list[CreateMPULayoutRequestPanes]

    def validate(self):
        if self.panes:
            for k in self.panes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMPULayoutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        result['Panes'] = []
        if self.panes is not None:
            for k in self.panes:
                result['Panes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        self.panes = []
        if m.get('Panes') is not None:
            for k in m.get('Panes'):
                temp_model = CreateMPULayoutRequestPanes()
                self.panes.append(temp_model.from_map(k))
        return self


class CreateMPULayoutResponseBody(TeaModel):
    def __init__(self, layout_id=None, request_id=None):
        self.layout_id = layout_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMPULayoutResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMPULayoutResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMPULayoutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMPULayoutResponse, self).to_map()
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
            temp_model = CreateMPULayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoLiveStreamRuleRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, rule_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoLiveStreamRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoLiveStreamRuleResponseBody, self).to_map()
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


class DeleteAutoLiveStreamRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAutoLiveStreamRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAutoLiveStreamRuleResponse, self).to_map()
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
            temp_model = DeleteAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChannelRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, owner_id=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChannelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteChannelResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChannelResponseBody, self).to_map()
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


class DeleteChannelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteChannelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteChannelResponse, self).to_map()
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
            temp_model = DeleteChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventSubscribeRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, subscribe_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long
        self.subscribe_id = subscribe_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventSubscribeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')
        return self


class DeleteEventSubscribeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventSubscribeResponseBody, self).to_map()
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


class DeleteEventSubscribeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventSubscribeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventSubscribeResponse, self).to_map()
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
            temp_model = DeleteEventSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMPULayoutRequest(TeaModel):
    def __init__(self, app_id=None, layout_id=None, owner_id=None):
        self.app_id = app_id  # type: str
        self.layout_id = layout_id  # type: long
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMPULayoutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteMPULayoutResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMPULayoutResponseBody, self).to_map()
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


class DeleteMPULayoutResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMPULayoutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMPULayoutResponse, self).to_map()
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
            temp_model = DeleteMPULayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordTemplateRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, template_id=None):
        self.app_id = app_id  # type: str
        # 1
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteRecordTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordTemplateResponseBody, self).to_map()
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


class DeleteRecordTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRecordTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRecordTemplateResponse, self).to_map()
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
            temp_model = DeleteRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppKeyRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAppKeyResponseBody(TeaModel):
    def __init__(self, app_key=None, request_id=None):
        # AppKey。
        self.app_key = app_key  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppKeyResponse, self).to_map()
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
            temp_model = DescribeAppKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequest(TeaModel):
    def __init__(self, app_id=None, order=None, owner_id=None, page_num=None, page_size=None, status=None):
        self.app_id = app_id  # type: str
        self.order = order  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAppsResponseBodyAppListAppServiceAreas(TeaModel):
    def __init__(self, service_area=None):
        self.service_area = service_area  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsResponseBodyAppListAppServiceAreas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        return self


class DescribeAppsResponseBodyAppListApp(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_type=None, bill_type=None, create_time=None, region=None,
                 service_areas=None, status=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.bill_type = bill_type  # type: str
        self.create_time = create_time  # type: str
        self.region = region  # type: str
        self.service_areas = service_areas  # type: DescribeAppsResponseBodyAppListAppServiceAreas
        self.status = status  # type: int

    def validate(self):
        if self.service_areas:
            self.service_areas.validate()

    def to_map(self):
        _map = super(DescribeAppsResponseBodyAppListApp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.region is not None:
            result['Region'] = self.region
        if self.service_areas is not None:
            result['ServiceAreas'] = self.service_areas.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceAreas') is not None:
            temp_model = DescribeAppsResponseBodyAppListAppServiceAreas()
            self.service_areas = temp_model.from_map(m['ServiceAreas'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAppsResponseBodyAppList(TeaModel):
    def __init__(self, app=None):
        self.app = app  # type: list[DescribeAppsResponseBodyAppListApp]

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppsResponseBodyAppList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = DescribeAppsResponseBodyAppListApp()
                self.app.append(temp_model.from_map(k))
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(self, app_list=None, request_id=None, total_num=None, total_page=None):
        self.app_list = app_list  # type: DescribeAppsResponseBodyAppList
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        _map = super(DescribeAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppList') is not None:
            temp_model = DescribeAppsResponseBodyAppList()
            self.app_list = temp_model.from_map(m['AppList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppsResponse, self).to_map()
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
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoLiveStreamRuleRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoLiveStreamRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAutoLiveStreamRuleResponseBodyRules(TeaModel):
    def __init__(self, call_back=None, channel_id_prefixes=None, channel_ids=None, create_time=None,
                 media_encode=None, play_domain=None, rule_id=None, rule_name=None, status=None):
        self.call_back = call_back  # type: str
        self.channel_id_prefixes = channel_id_prefixes  # type: list[str]
        self.channel_ids = channel_ids  # type: list[str]
        self.create_time = create_time  # type: str
        self.media_encode = media_encode  # type: int
        self.play_domain = play_domain  # type: str
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoLiveStreamRuleResponseBodyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.channel_id_prefixes is not None:
            result['ChannelIdPrefixes'] = self.channel_id_prefixes
        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('ChannelIdPrefixes') is not None:
            self.channel_id_prefixes = m.get('ChannelIdPrefixes')
        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, rules=None):
        self.request_id = request_id  # type: str
        self.rules = rules  # type: list[DescribeAutoLiveStreamRuleResponseBodyRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutoLiveStreamRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeAutoLiveStreamRuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeAutoLiveStreamRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutoLiveStreamRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoLiveStreamRuleResponse, self).to_map()
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
            temp_model = DescribeAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None, ext_data_type=None,
                 query_exp_info=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.ext_data_type = ext_data_type  # type: str
        self.query_exp_info = query_exp_info  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.ext_data_type is not None:
            result['ExtDataType'] = self.ext_data_type
        if self.query_exp_info is not None:
            result['QueryExpInfo'] = self.query_exp_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('ExtDataType') is not None:
            self.ext_data_type = m.get('ExtDataType')
        if m.get('QueryExpInfo') is not None:
            self.query_exp_info = m.get('QueryExpInfo')
        return self


class DescribeCallResponseBodyCallInfo(TeaModel):
    def __init__(self, app_id=None, call_status=None, channel_id=None, created_ts=None, destroyed_ts=None,
                 duration=None):
        # App ID。
        self.app_id = app_id  # type: str
        self.call_status = call_status  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCallResponseBodyCallInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeCallResponseBodyUserDetailListDurMetricStatData(TeaModel):
    def __init__(self, pub_audio=None, pub_video_1080=None, pub_video_360=None, pub_video_720=None,
                 pub_video_screen_share=None, sub_audio=None, sub_video_1080=None, sub_video_360=None, sub_video_720=None,
                 sub_video_screen_share=None):
        self.pub_audio = pub_audio  # type: long
        self.pub_video_1080 = pub_video_1080  # type: long
        self.pub_video_360 = pub_video_360  # type: long
        self.pub_video_720 = pub_video_720  # type: long
        self.pub_video_screen_share = pub_video_screen_share  # type: long
        self.sub_audio = sub_audio  # type: long
        self.sub_video_1080 = sub_video_1080  # type: long
        self.sub_video_360 = sub_video_360  # type: long
        self.sub_video_720 = sub_video_720  # type: long
        self.sub_video_screen_share = sub_video_screen_share  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCallResponseBodyUserDetailListDurMetricStatData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pub_audio is not None:
            result['PubAudio'] = self.pub_audio
        if self.pub_video_1080 is not None:
            result['PubVideo1080'] = self.pub_video_1080
        if self.pub_video_360 is not None:
            result['PubVideo360'] = self.pub_video_360
        if self.pub_video_720 is not None:
            result['PubVideo720'] = self.pub_video_720
        if self.pub_video_screen_share is not None:
            result['PubVideoScreenShare'] = self.pub_video_screen_share
        if self.sub_audio is not None:
            result['SubAudio'] = self.sub_audio
        if self.sub_video_1080 is not None:
            result['SubVideo1080'] = self.sub_video_1080
        if self.sub_video_360 is not None:
            result['SubVideo360'] = self.sub_video_360
        if self.sub_video_720 is not None:
            result['SubVideo720'] = self.sub_video_720
        if self.sub_video_screen_share is not None:
            result['SubVideoScreenShare'] = self.sub_video_screen_share
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PubAudio') is not None:
            self.pub_audio = m.get('PubAudio')
        if m.get('PubVideo1080') is not None:
            self.pub_video_1080 = m.get('PubVideo1080')
        if m.get('PubVideo360') is not None:
            self.pub_video_360 = m.get('PubVideo360')
        if m.get('PubVideo720') is not None:
            self.pub_video_720 = m.get('PubVideo720')
        if m.get('PubVideoScreenShare') is not None:
            self.pub_video_screen_share = m.get('PubVideoScreenShare')
        if m.get('SubAudio') is not None:
            self.sub_audio = m.get('SubAudio')
        if m.get('SubVideo1080') is not None:
            self.sub_video_1080 = m.get('SubVideo1080')
        if m.get('SubVideo360') is not None:
            self.sub_video_360 = m.get('SubVideo360')
        if m.get('SubVideo720') is not None:
            self.sub_video_720 = m.get('SubVideo720')
        if m.get('SubVideoScreenShare') is not None:
            self.sub_video_screen_share = m.get('SubVideoScreenShare')
        return self


class DescribeCallResponseBodyUserDetailListOnlinePeriods(TeaModel):
    def __init__(self, join_ts=None, leave_ts=None):
        self.join_ts = join_ts  # type: long
        self.leave_ts = leave_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCallResponseBodyUserDetailListOnlinePeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeCallResponseBodyUserDetailList(TeaModel):
    def __init__(self, call_exp=None, created_ts=None, destroyed_ts=None, dur_metric_stat_data=None, duration=None,
                 location=None, network=None, network_list=None, online_duration=None, online_periods=None, os=None,
                 os_list=None, roles=None, sdk_version=None, sdk_version_list=None, user_id=None):
        self.call_exp = call_exp  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.dur_metric_stat_data = dur_metric_stat_data  # type: DescribeCallResponseBodyUserDetailListDurMetricStatData
        self.duration = duration  # type: long
        self.location = location  # type: str
        self.network = network  # type: str
        self.network_list = network_list  # type: list[str]
        self.online_duration = online_duration  # type: long
        self.online_periods = online_periods  # type: list[DescribeCallResponseBodyUserDetailListOnlinePeriods]
        self.os = os  # type: str
        self.os_list = os_list  # type: list[str]
        self.roles = roles  # type: list[str]
        self.sdk_version = sdk_version  # type: str
        self.sdk_version_list = sdk_version_list  # type: list[str]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.dur_metric_stat_data:
            self.dur_metric_stat_data.validate()
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCallResponseBodyUserDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_exp is not None:
            result['CallExp'] = self.call_exp
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.dur_metric_stat_data is not None:
            result['DurMetricStatData'] = self.dur_metric_stat_data.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallExp') is not None:
            self.call_exp = m.get('CallExp')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('DurMetricStatData') is not None:
            temp_model = DescribeCallResponseBodyUserDetailListDurMetricStatData()
            self.dur_metric_stat_data = temp_model.from_map(m['DurMetricStatData'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeCallResponseBodyUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCallResponseBody(TeaModel):
    def __init__(self, call_info=None, request_id=None, user_detail_list=None):
        self.call_info = call_info  # type: DescribeCallResponseBodyCallInfo
        self.request_id = request_id  # type: str
        self.user_detail_list = user_detail_list  # type: list[DescribeCallResponseBodyUserDetailList]

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.user_detail_list:
            for k in self.user_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserDetailList'] = []
        if self.user_detail_list is not None:
            for k in self.user_detail_list:
                result['UserDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeCallResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_detail_list = []
        if m.get('UserDetailList') is not None:
            for k in m.get('UserDetailList'):
                temp_model = DescribeCallResponseBodyUserDetailList()
                self.user_detail_list.append(temp_model.from_map(k))
        return self


class DescribeCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCallResponse, self).to_map()
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
            temp_model = DescribeCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallListRequest(TeaModel):
    def __init__(self, app_id=None, call_status=None, channel_id=None, end_ts=None, order_by=None, page_no=None,
                 page_size=None, query_mode=None, start_ts=None, user_id=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.call_status = call_status  # type: str
        self.channel_id = channel_id  # type: str
        self.end_ts = end_ts  # type: long
        self.order_by = order_by  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.query_mode = query_mode  # type: str
        self.start_ts = start_ts  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCallListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCallListResponseBodyCallList(TeaModel):
    def __init__(self, app_id=None, bad_exp_user_cnt=None, call_status=None, channel_id=None, created_ts=None,
                 destroyed_ts=None, duration=None, user_cnt=None):
        # App ID。
        self.app_id = app_id  # type: str
        self.bad_exp_user_cnt = bad_exp_user_cnt  # type: int
        self.call_status = call_status  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long
        self.user_cnt = user_cnt  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCallListResponseBodyCallList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bad_exp_user_cnt is not None:
            result['BadExpUserCnt'] = self.bad_exp_user_cnt
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.user_cnt is not None:
            result['UserCnt'] = self.user_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BadExpUserCnt') is not None:
            self.bad_exp_user_cnt = m.get('BadExpUserCnt')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('UserCnt') is not None:
            self.user_cnt = m.get('UserCnt')
        return self


class DescribeCallListResponseBody(TeaModel):
    def __init__(self, call_list=None, page_no=None, page_size=None, request_id=None, total_cnt=None):
        self.call_list = call_list  # type: list[DescribeCallListResponseBodyCallList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_cnt = total_cnt  # type: int

    def validate(self):
        if self.call_list:
            for k in self.call_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCallListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallList'] = []
        if self.call_list is not None:
            for k in self.call_list:
                result['CallList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.call_list = []
        if m.get('CallList') is not None:
            for k in m.get('CallList'):
                temp_model = DescribeCallListResponseBodyCallList()
                self.call_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        return self


class DescribeCallListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCallListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCallListResponse, self).to_map()
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
            temp_model = DescribeCallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelAreaDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None, parent_area=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.parent_area = parent_area  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelAreaDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        return self


class DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList(TeaModel):
    def __init__(self, area_name=None, call_user_count=None, high_quality_transmission_rate=None,
                 pub_user_count=None, sub_user_count=None):
        self.area_name = area_name  # type: str
        self.call_user_count = call_user_count  # type: int
        self.high_quality_transmission_rate = high_quality_transmission_rate  # type: str
        self.pub_user_count = pub_user_count  # type: int
        self.sub_user_count = sub_user_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count
        if self.high_quality_transmission_rate is not None:
            result['HighQualityTransmissionRate'] = self.high_quality_transmission_rate
        if self.pub_user_count is not None:
            result['PubUserCount'] = self.pub_user_count
        if self.sub_user_count is not None:
            result['SubUserCount'] = self.sub_user_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')
        if m.get('HighQualityTransmissionRate') is not None:
            self.high_quality_transmission_rate = m.get('HighQualityTransmissionRate')
        if m.get('PubUserCount') is not None:
            self.pub_user_count = m.get('PubUserCount')
        if m.get('SubUserCount') is not None:
            self.sub_user_count = m.get('SubUserCount')
        return self


class DescribeChannelAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(self, area_stat_list=None, request_id=None):
        self.area_stat_list = area_stat_list  # type: list[DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.area_stat_list:
            for k in self.area_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChannelAreaDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AreaStatList'] = []
        if self.area_stat_list is not None:
            for k in self.area_stat_list:
                result['AreaStatList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.area_stat_list = []
        if m.get('AreaStatList') is not None:
            for k in m.get('AreaStatList'):
                temp_model = DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList()
                self.area_stat_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelAreaDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChannelAreaDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChannelAreaDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeChannelAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None, stat_dim=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.stat_dim = stat_dim  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeChannelDistributionStatDataResponseBodyStatList(TeaModel):
    def __init__(self, call_user_count=None, call_user_ratio=None, name=None):
        self.call_user_count = call_user_count  # type: int
        self.call_user_ratio = call_user_ratio  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelDistributionStatDataResponseBodyStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count
        if self.call_user_ratio is not None:
            result['CallUserRatio'] = self.call_user_ratio
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')
        if m.get('CallUserRatio') is not None:
            self.call_user_ratio = m.get('CallUserRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeChannelDistributionStatDataResponseBody(TeaModel):
    def __init__(self, request_id=None, stat_list=None):
        self.request_id = request_id  # type: str
        self.stat_list = stat_list  # type: list[DescribeChannelDistributionStatDataResponseBodyStatList]

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChannelDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeChannelDistributionStatDataResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        return self


class DescribeChannelDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChannelDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChannelDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeChannelDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelOverallDataRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelOverallDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelOverallDataResponseBodyCallInfo(TeaModel):
    def __init__(self, app_id=None, call_status=None, channel_id=None, created_ts=None, destroyed_ts=None,
                 duration=None):
        self.app_id = app_id  # type: str
        self.call_status = call_status  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelOverallDataResponseBodyCallInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeChannelOverallDataResponseBodyMetricDatasNodes(TeaModel):
    def __init__(self, ext=None, x=None, y=None):
        self.ext = ext  # type: dict[str, any]
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelOverallDataResponseBodyMetricDatasNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeChannelOverallDataResponseBodyMetricDatas(TeaModel):
    def __init__(self, nodes=None, type=None):
        self.nodes = nodes  # type: list[DescribeChannelOverallDataResponseBodyMetricDatasNodes]
        self.type = type  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChannelOverallDataResponseBodyMetricDatas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeChannelOverallDataResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeChannelOverallDataResponseBodyOverallData(TeaModel):
    def __init__(self, conn_avg_time=None, five_sec_join_rate=None, total_audio_stuck_rate=None,
                 total_video_stuck_rate=None, total_video_vague_rate=None):
        self.conn_avg_time = conn_avg_time  # type: float
        self.five_sec_join_rate = five_sec_join_rate  # type: float
        self.total_audio_stuck_rate = total_audio_stuck_rate  # type: float
        self.total_video_stuck_rate = total_video_stuck_rate  # type: float
        self.total_video_vague_rate = total_video_vague_rate  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelOverallDataResponseBodyOverallData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_avg_time is not None:
            result['ConnAvgTime'] = self.conn_avg_time
        if self.five_sec_join_rate is not None:
            result['FiveSecJoinRate'] = self.five_sec_join_rate
        if self.total_audio_stuck_rate is not None:
            result['TotalAudioStuckRate'] = self.total_audio_stuck_rate
        if self.total_video_stuck_rate is not None:
            result['TotalVideoStuckRate'] = self.total_video_stuck_rate
        if self.total_video_vague_rate is not None:
            result['TotalVideoVagueRate'] = self.total_video_vague_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAvgTime') is not None:
            self.conn_avg_time = m.get('ConnAvgTime')
        if m.get('FiveSecJoinRate') is not None:
            self.five_sec_join_rate = m.get('FiveSecJoinRate')
        if m.get('TotalAudioStuckRate') is not None:
            self.total_audio_stuck_rate = m.get('TotalAudioStuckRate')
        if m.get('TotalVideoStuckRate') is not None:
            self.total_video_stuck_rate = m.get('TotalVideoStuckRate')
        if m.get('TotalVideoVagueRate') is not None:
            self.total_video_vague_rate = m.get('TotalVideoVagueRate')
        return self


class DescribeChannelOverallDataResponseBody(TeaModel):
    def __init__(self, call_info=None, metric_datas=None, overall_data=None, request_id=None):
        self.call_info = call_info  # type: DescribeChannelOverallDataResponseBodyCallInfo
        self.metric_datas = metric_datas  # type: list[DescribeChannelOverallDataResponseBodyMetricDatas]
        self.overall_data = overall_data  # type: DescribeChannelOverallDataResponseBodyOverallData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.metric_datas:
            for k in self.metric_datas:
                if k:
                    k.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super(DescribeChannelOverallDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        result['MetricDatas'] = []
        if self.metric_datas is not None:
            for k in self.metric_datas:
                result['MetricDatas'].append(k.to_map() if k else None)
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeChannelOverallDataResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k in m.get('MetricDatas'):
                temp_model = DescribeChannelOverallDataResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k))
        if m.get('OverallData') is not None:
            temp_model = DescribeChannelOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelOverallDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChannelOverallDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChannelOverallDataResponse, self).to_map()
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
            temp_model = DescribeChannelOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelParticipantsRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, order=None, owner_id=None, page_num=None, page_size=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.order = order  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelParticipantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeChannelParticipantsResponseBodyUserList(TeaModel):
    def __init__(self, user=None):
        self.user = user  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelParticipantsResponseBodyUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeChannelParticipantsResponseBody(TeaModel):
    def __init__(self, request_id=None, timestamp=None, total_num=None, total_page=None, user_list=None):
        self.request_id = request_id  # type: str
        self.timestamp = timestamp  # type: int
        self.total_num = total_num  # type: int
        self.total_page = total_page  # type: int
        self.user_list = user_list  # type: DescribeChannelParticipantsResponseBodyUserList

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        _map = super(DescribeChannelParticipantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('UserList') is not None:
            temp_model = DescribeChannelParticipantsResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        return self


class DescribeChannelParticipantsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChannelParticipantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChannelParticipantsResponse, self).to_map()
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
            temp_model = DescribeChannelParticipantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelTopPubUserListRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelTopPubUserListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods(TeaModel):
    def __init__(self, join_ts=None, leave_ts=None):
        self.join_ts = join_ts  # type: long
        self.leave_ts = leave_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList(TeaModel):
    def __init__(self, created_ts=None, destroyed_ts=None, duration=None, location=None, online_duration=None,
                 online_periods=None, user_id=None):
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long
        self.location = location  # type: str
        self.online_duration = online_duration  # type: long
        self.online_periods = online_periods  # type: list[DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeChannelTopPubUserListResponseBody(TeaModel):
    def __init__(self, request_id=None, top_pub_user_detail_list=None):
        self.request_id = request_id  # type: str
        self.top_pub_user_detail_list = top_pub_user_detail_list  # type: list[DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList]

    def validate(self):
        if self.top_pub_user_detail_list:
            for k in self.top_pub_user_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChannelTopPubUserListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TopPubUserDetailList'] = []
        if self.top_pub_user_detail_list is not None:
            for k in self.top_pub_user_detail_list:
                result['TopPubUserDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.top_pub_user_detail_list = []
        if m.get('TopPubUserDetailList') is not None:
            for k in m.get('TopPubUserDetailList'):
                temp_model = DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList()
                self.top_pub_user_detail_list.append(temp_model.from_map(k))
        return self


class DescribeChannelTopPubUserListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChannelTopPubUserListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChannelTopPubUserListResponse, self).to_map()
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
            temp_model = DescribeChannelTopPubUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelUserMetricsRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelUserMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelUserMetricsResponseBodyMetricDatasNodes(TeaModel):
    def __init__(self, ext=None, x=None, y=None):
        self.ext = ext  # type: dict[str, any]
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelUserMetricsResponseBodyMetricDatasNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeChannelUserMetricsResponseBodyMetricDatas(TeaModel):
    def __init__(self, nodes=None, type=None):
        self.nodes = nodes  # type: list[DescribeChannelUserMetricsResponseBodyMetricDatasNodes]
        self.type = type  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChannelUserMetricsResponseBodyMetricDatas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeChannelUserMetricsResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeChannelUserMetricsResponseBodyOverallData(TeaModel):
    def __init__(self, total_bad_exp_num=None, total_join_fail_num=None, total_pub_user_num=None,
                 total_sub_user_num=None, total_user_num=None):
        self.total_bad_exp_num = total_bad_exp_num  # type: long
        self.total_join_fail_num = total_join_fail_num  # type: long
        self.total_pub_user_num = total_pub_user_num  # type: long
        self.total_sub_user_num = total_sub_user_num  # type: long
        self.total_user_num = total_user_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelUserMetricsResponseBodyOverallData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_bad_exp_num is not None:
            result['TotalBadExpNum'] = self.total_bad_exp_num
        if self.total_join_fail_num is not None:
            result['TotalJoinFailNum'] = self.total_join_fail_num
        if self.total_pub_user_num is not None:
            result['TotalPubUserNum'] = self.total_pub_user_num
        if self.total_sub_user_num is not None:
            result['TotalSubUserNum'] = self.total_sub_user_num
        if self.total_user_num is not None:
            result['TotalUserNum'] = self.total_user_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalBadExpNum') is not None:
            self.total_bad_exp_num = m.get('TotalBadExpNum')
        if m.get('TotalJoinFailNum') is not None:
            self.total_join_fail_num = m.get('TotalJoinFailNum')
        if m.get('TotalPubUserNum') is not None:
            self.total_pub_user_num = m.get('TotalPubUserNum')
        if m.get('TotalSubUserNum') is not None:
            self.total_sub_user_num = m.get('TotalSubUserNum')
        if m.get('TotalUserNum') is not None:
            self.total_user_num = m.get('TotalUserNum')
        return self


class DescribeChannelUserMetricsResponseBody(TeaModel):
    def __init__(self, metric_datas=None, overall_data=None, request_id=None):
        self.metric_datas = metric_datas  # type: list[DescribeChannelUserMetricsResponseBodyMetricDatas]
        self.overall_data = overall_data  # type: DescribeChannelUserMetricsResponseBodyOverallData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metric_datas:
            for k in self.metric_datas:
                if k:
                    k.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super(DescribeChannelUserMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MetricDatas'] = []
        if self.metric_datas is not None:
            for k in self.metric_datas:
                result['MetricDatas'].append(k.to_map() if k else None)
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k in m.get('MetricDatas'):
                temp_model = DescribeChannelUserMetricsResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k))
        if m.get('OverallData') is not None:
            temp_model = DescribeChannelUserMetricsResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelUserMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChannelUserMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChannelUserMetricsResponse, self).to_map()
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
            temp_model = DescribeChannelUserMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelUsersRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, owner_id=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeChannelUsersResponseBody(TeaModel):
    def __init__(self, channel_profile=None, comm_total_num=None, interactive_user_list=None,
                 interactive_user_num=None, is_channel_exist=None, live_user_list=None, live_user_num=None, request_id=None,
                 timestamp=None, user_list=None):
        self.channel_profile = channel_profile  # type: int
        self.comm_total_num = comm_total_num  # type: int
        self.interactive_user_list = interactive_user_list  # type: list[str]
        self.interactive_user_num = interactive_user_num  # type: int
        self.is_channel_exist = is_channel_exist  # type: bool
        self.live_user_list = live_user_list  # type: list[str]
        self.live_user_num = live_user_num  # type: int
        self.request_id = request_id  # type: str
        self.timestamp = timestamp  # type: int
        self.user_list = user_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChannelUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_profile is not None:
            result['ChannelProfile'] = self.channel_profile
        if self.comm_total_num is not None:
            result['CommTotalNum'] = self.comm_total_num
        if self.interactive_user_list is not None:
            result['InteractiveUserList'] = self.interactive_user_list
        if self.interactive_user_num is not None:
            result['InteractiveUserNum'] = self.interactive_user_num
        if self.is_channel_exist is not None:
            result['IsChannelExist'] = self.is_channel_exist
        if self.live_user_list is not None:
            result['LiveUserList'] = self.live_user_list
        if self.live_user_num is not None:
            result['LiveUserNum'] = self.live_user_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.user_list is not None:
            result['UserList'] = self.user_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelProfile') is not None:
            self.channel_profile = m.get('ChannelProfile')
        if m.get('CommTotalNum') is not None:
            self.comm_total_num = m.get('CommTotalNum')
        if m.get('InteractiveUserList') is not None:
            self.interactive_user_list = m.get('InteractiveUserList')
        if m.get('InteractiveUserNum') is not None:
            self.interactive_user_num = m.get('InteractiveUserNum')
        if m.get('IsChannelExist') is not None:
            self.is_channel_exist = m.get('IsChannelExist')
        if m.get('LiveUserList') is not None:
            self.live_user_list = m.get('LiveUserList')
        if m.get('LiveUserNum') is not None:
            self.live_user_num = m.get('LiveUserNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')
        return self


class DescribeChannelUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChannelUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChannelUsersResponse, self).to_map()
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
            temp_model = DescribeChannelUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndPointEventListRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None, user_id_list=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.user_id_list = user_id_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndPointEventListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList(TeaModel):
    def __init__(self, event_name=None, event_type=None, ts=None, ts_in_ms=None):
        self.event_name = event_name  # type: str
        self.event_type = event_type  # type: str
        self.ts = ts  # type: long
        self.ts_in_ms = ts_in_ms  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ts is not None:
            result['Ts'] = self.ts
        if self.ts_in_ms is not None:
            result['TsInMs'] = self.ts_in_ms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        if m.get('TsInMs') is not None:
            self.ts_in_ms = m.get('TsInMs')
        return self


class DescribeEndPointEventListResponseBodyNodesEventDataItems(TeaModel):
    def __init__(self, event_list=None, ts=None):
        self.event_list = event_list  # type: list[DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList]
        self.ts = ts  # type: long

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndPointEventListResponseBodyNodesEventDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeEndPointEventListResponseBodyNodes(TeaModel):
    def __init__(self, event_data_items=None, user_id=None):
        self.event_data_items = event_data_items  # type: list[DescribeEndPointEventListResponseBodyNodesEventDataItems]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.event_data_items:
            for k in self.event_data_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndPointEventListResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k in self.event_data_items:
                result['EventDataItems'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k in m.get('EventDataItems'):
                temp_model = DescribeEndPointEventListResponseBodyNodesEventDataItems()
                self.event_data_items.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointEventListResponseBody(TeaModel):
    def __init__(self, nodes=None, request_id=None):
        self.nodes = nodes  # type: list[DescribeEndPointEventListResponseBodyNodes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndPointEventListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointEventListResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEndPointEventListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEndPointEventListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEndPointEventListResponse, self).to_map()
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
            temp_model = DescribeEndPointEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndPointMetricDataRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None, metrics=None,
                 pub_call_id_list=None, pub_user_id=None, sub_user_id=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.metrics = metrics  # type: str
        self.pub_call_id_list = pub_call_id_list  # type: str
        self.pub_user_id = pub_user_id  # type: str
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndPointMetricDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.pub_call_id_list is not None:
            result['PubCallIdList'] = self.pub_call_id_list
        if self.pub_user_id is not None:
            result['PubUserId'] = self.pub_user_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('PubCallIdList') is not None:
            self.pub_call_id_list = m.get('PubCallIdList')
        if m.get('PubUserId') is not None:
            self.pub_user_id = m.get('PubUserId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeEndPointMetricDataResponseBodyPubMetricsNodes(TeaModel):
    def __init__(self, ext=None, x=None, y=None):
        self.ext = ext  # type: dict[str, any]
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndPointMetricDataResponseBodyPubMetricsNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeEndPointMetricDataResponseBodyPubMetrics(TeaModel):
    def __init__(self, nodes=None, type=None, user_id=None):
        self.nodes = nodes  # type: list[DescribeEndPointMetricDataResponseBodyPubMetricsNodes]
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndPointMetricDataResponseBodyPubMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointMetricDataResponseBodyPubMetricsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointMetricDataResponseBodySubMetricsNodes(TeaModel):
    def __init__(self, ext=None, x=None, y=None):
        self.ext = ext  # type: dict[str, any]
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndPointMetricDataResponseBodySubMetricsNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeEndPointMetricDataResponseBodySubMetrics(TeaModel):
    def __init__(self, nodes=None, type=None, user_id=None):
        self.nodes = nodes  # type: list[DescribeEndPointMetricDataResponseBodySubMetricsNodes]
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndPointMetricDataResponseBodySubMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointMetricDataResponseBodySubMetricsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointMetricDataResponseBody(TeaModel):
    def __init__(self, pub_metrics=None, request_id=None, sub_metrics=None):
        self.pub_metrics = pub_metrics  # type: list[DescribeEndPointMetricDataResponseBodyPubMetrics]
        self.request_id = request_id  # type: str
        self.sub_metrics = sub_metrics  # type: list[DescribeEndPointMetricDataResponseBodySubMetrics]

    def validate(self):
        if self.pub_metrics:
            for k in self.pub_metrics:
                if k:
                    k.validate()
        if self.sub_metrics:
            for k in self.sub_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndPointMetricDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PubMetrics'] = []
        if self.pub_metrics is not None:
            for k in self.pub_metrics:
                result['PubMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubMetrics'] = []
        if self.sub_metrics is not None:
            for k in self.sub_metrics:
                result['SubMetrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.pub_metrics = []
        if m.get('PubMetrics') is not None:
            for k in m.get('PubMetrics'):
                temp_model = DescribeEndPointMetricDataResponseBodyPubMetrics()
                self.pub_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sub_metrics = []
        if m.get('SubMetrics') is not None:
            for k in m.get('SubMetrics'):
                temp_model = DescribeEndPointMetricDataResponseBodySubMetrics()
                self.sub_metrics.append(temp_model.from_map(k))
        return self


class DescribeEndPointMetricDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEndPointMetricDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEndPointMetricDataResponse, self).to_map()
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
            temp_model = DescribeEndPointMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisFactorDistributionStatRequest(TeaModel):
    def __init__(self, app_id=None, end_ts=None, start_ts=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.end_ts = end_ts  # type: long
        self.start_ts = start_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisFactorDistributionStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList(TeaModel):
    def __init__(self, factor_id=None, user_count=None, user_ratio=None):
        self.factor_id = factor_id  # type: str
        self.user_count = user_count  # type: int
        self.user_ratio = user_ratio  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.user_ratio is not None:
            result['UserRatio'] = self.user_ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('UserRatio') is not None:
            self.user_ratio = m.get('UserRatio')
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponseBody(TeaModel):
    def __init__(self, request_id=None, stat_list=None):
        self.request_id = request_id  # type: str
        self.stat_list = stat_list  # type: list[DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList]

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisFactorDistributionStatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFaultDiagnosisFactorDistributionStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisFactorDistributionStatResponse, self).to_map()
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
            temp_model = DescribeFaultDiagnosisFactorDistributionStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisOverallDataRequest(TeaModel):
    def __init__(self, app_id=None, end_ts=None, start_ts=None, stat_dim=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_ts = end_ts  # type: long
        self.start_ts = start_ts  # type: long
        self.stat_dim = stat_dim  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisOverallDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes(TeaModel):
    def __init__(self, ext=None, x=None, y=None):
        self.ext = ext  # type: dict[str, any]
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyMetricData(TeaModel):
    def __init__(self, nodes=None):
        self.nodes = nodes  # type: list[DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes]

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisOverallDataResponseBodyMetricData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyOverallData(TeaModel):
    def __init__(self, fault_user_count=None, fault_user_ratio=None, total_user_count=None):
        self.fault_user_count = fault_user_count  # type: int
        self.fault_user_ratio = fault_user_ratio  # type: float
        self.total_user_count = total_user_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisOverallDataResponseBodyOverallData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_user_count is not None:
            result['FaultUserCount'] = self.fault_user_count
        if self.fault_user_ratio is not None:
            result['FaultUserRatio'] = self.fault_user_ratio
        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaultUserCount') is not None:
            self.fault_user_count = m.get('FaultUserCount')
        if m.get('FaultUserRatio') is not None:
            self.fault_user_ratio = m.get('FaultUserRatio')
        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')
        return self


class DescribeFaultDiagnosisOverallDataResponseBody(TeaModel):
    def __init__(self, metric_data=None, overall_data=None, request_id=None):
        self.metric_data = metric_data  # type: DescribeFaultDiagnosisOverallDataResponseBodyMetricData
        self.overall_data = overall_data  # type: DescribeFaultDiagnosisOverallDataResponseBodyOverallData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metric_data:
            self.metric_data.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisOverallDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data.to_map()
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricData') is not None:
            temp_model = DescribeFaultDiagnosisOverallDataResponseBodyMetricData()
            self.metric_data = temp_model.from_map(m['MetricData'])
        if m.get('OverallData') is not None:
            temp_model = DescribeFaultDiagnosisOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFaultDiagnosisOverallDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFaultDiagnosisOverallDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisOverallDataResponse, self).to_map()
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
            temp_model = DescribeFaultDiagnosisOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisUserDetailRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, fault_type=None, query_call_user_info=None,
                 user_id=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.fault_type = fault_type  # type: str
        self.query_call_user_info = query_call_user_info  # type: bool
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        if self.query_call_user_info is not None:
            result['QueryCallUserInfo'] = self.query_call_user_info
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        if m.get('QueryCallUserInfo') is not None:
            self.query_call_user_info = m.get('QueryCallUserInfo')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyCallInfo(TeaModel):
    def __init__(self, app_id=None, call_status=None, channel_id=None, created_ts=None, destroyed_ts=None,
                 duration=None):
        # App ID。
        self.app_id = app_id  # type: str
        self.call_status = call_status  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyCallInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList(TeaModel):
    def __init__(self, event_name=None, event_type=None, ts=None):
        self.event_name = event_name  # type: str
        self.event_type = event_type  # type: str
        self.ts = ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems(TeaModel):
    def __init__(self, event_list=None, ts=None):
        self.event_list = event_list  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList]
        self.ts = ts  # type: long

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas(TeaModel):
    def __init__(self, event_data_items=None, role=None, user_id=None):
        self.event_data_items = event_data_items  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems]
        self.role = role  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.event_data_items:
            for k in self.event_data_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k in self.event_data_items:
                result['EventDataItems'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k in m.get('EventDataItems'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems()
                self.event_data_items.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes(TeaModel):
    def __init__(self, ext=None, x=None, y=None):
        self.ext = ext  # type: dict[str, any]
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas(TeaModel):
    def __init__(self, nodes=None, role=None, type=None, user_id=None):
        self.nodes = nodes  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes]
        self.role = role  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorList(TeaModel):
    def __init__(self, factor_id=None, fault_source=None, related_event_datas=None, related_metric_datas=None):
        self.factor_id = factor_id  # type: str
        self.fault_source = fault_source  # type: str
        self.related_event_datas = related_event_datas  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas]
        self.related_metric_datas = related_metric_datas  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas]

    def validate(self):
        if self.related_event_datas:
            for k in self.related_event_datas:
                if k:
                    k.validate()
        if self.related_metric_datas:
            for k in self.related_metric_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFactorList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id
        if self.fault_source is not None:
            result['FaultSource'] = self.fault_source
        result['RelatedEventDatas'] = []
        if self.related_event_datas is not None:
            for k in self.related_event_datas:
                result['RelatedEventDatas'].append(k.to_map() if k else None)
        result['RelatedMetricDatas'] = []
        if self.related_metric_datas is not None:
            for k in self.related_metric_datas:
                result['RelatedMetricDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')
        if m.get('FaultSource') is not None:
            self.fault_source = m.get('FaultSource')
        self.related_event_datas = []
        if m.get('RelatedEventDatas') is not None:
            for k in m.get('RelatedEventDatas'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas()
                self.related_event_datas.append(temp_model.from_map(k))
        self.related_metric_datas = []
        if m.get('RelatedMetricDatas') is not None:
            for k in m.get('RelatedMetricDatas'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas()
                self.related_metric_datas.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes, self).to_map()
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


class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData(TeaModel):
    def __init__(self, nodes=None):
        self.nodes = nodes  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes]

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods(TeaModel):
    def __init__(self, join_ts=None, leave_ts=None):
        self.join_ts = join_ts  # type: long
        self.leave_ts = leave_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyUserDetail(TeaModel):
    def __init__(self, created_ts=None, destroyed_ts=None, duration=None, location=None, network=None,
                 online_duration=None, online_periods=None, os=None, sdk_version=None, user_id=None):
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long
        self.location = location  # type: str
        self.network = network  # type: str
        self.online_duration = online_duration  # type: long
        self.online_periods = online_periods  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods]
        self.os = os  # type: str
        self.sdk_version = sdk_version  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBodyUserDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBody(TeaModel):
    def __init__(self, call_info=None, factor_list=None, fault_metric_data=None, network_operators=None,
                 request_id=None, user_detail=None):
        self.call_info = call_info  # type: DescribeFaultDiagnosisUserDetailResponseBodyCallInfo
        self.factor_list = factor_list  # type: list[DescribeFaultDiagnosisUserDetailResponseBodyFactorList]
        self.fault_metric_data = fault_metric_data  # type: DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData
        self.network_operators = network_operators  # type: list[str]
        self.request_id = request_id  # type: str
        self.user_detail = user_detail  # type: DescribeFaultDiagnosisUserDetailResponseBodyUserDetail

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.factor_list:
            for k in self.factor_list:
                if k:
                    k.validate()
        if self.fault_metric_data:
            self.fault_metric_data.validate()
        if self.user_detail:
            self.user_detail.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        result['FactorList'] = []
        if self.factor_list is not None:
            for k in self.factor_list:
                result['FactorList'].append(k.to_map() if k else None)
        if self.fault_metric_data is not None:
            result['FaultMetricData'] = self.fault_metric_data.to_map()
        if self.network_operators is not None:
            result['NetworkOperators'] = self.network_operators
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_detail is not None:
            result['UserDetail'] = self.user_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        self.factor_list = []
        if m.get('FactorList') is not None:
            for k in m.get('FactorList'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorList()
                self.factor_list.append(temp_model.from_map(k))
        if m.get('FaultMetricData') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData()
            self.fault_metric_data = temp_model.from_map(m['FaultMetricData'])
        if m.get('NetworkOperators') is not None:
            self.network_operators = m.get('NetworkOperators')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserDetail') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyUserDetail()
            self.user_detail = temp_model.from_map(m['UserDetail'])
        return self


class DescribeFaultDiagnosisUserDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFaultDiagnosisUserDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserDetailResponse, self).to_map()
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
            temp_model = DescribeFaultDiagnosisUserDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisUserListRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, end_ts=None, fault_types=None, page_no=None, page_size=None,
                 start_ts=None, user_id=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.end_ts = end_ts  # type: long
        self.fault_types = fault_types  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.start_ts = start_ts  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.fault_types is not None:
            result['FaultTypes'] = self.fault_types
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('FaultTypes') is not None:
            self.fault_types = m.get('FaultTypes')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserListResponseBodyUserListFaultList(TeaModel):
    def __init__(self, fault_type=None):
        self.fault_type = fault_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserListResponseBodyUserListFaultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        return self


class DescribeFaultDiagnosisUserListResponseBodyUserList(TeaModel):
    def __init__(self, channel_created_ts=None, channel_id=None, created_ts=None, destroyed_ts=None,
                 fault_list=None, user_id=None):
        self.channel_created_ts = channel_created_ts  # type: long
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.fault_list = fault_list  # type: list[DescribeFaultDiagnosisUserListResponseBodyUserListFaultList]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.fault_list:
            for k in self.fault_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserListResponseBodyUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_created_ts is not None:
            result['ChannelCreatedTs'] = self.channel_created_ts
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        result['FaultList'] = []
        if self.fault_list is not None:
            for k in self.fault_list:
                result['FaultList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelCreatedTs') is not None:
            self.channel_created_ts = m.get('ChannelCreatedTs')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        self.fault_list = []
        if m.get('FaultList') is not None:
            for k in m.get('FaultList'):
                temp_model = DescribeFaultDiagnosisUserListResponseBodyUserListFaultList()
                self.fault_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserListResponseBody(TeaModel):
    def __init__(self, page_no=None, page_size=None, request_id=None, total_cnt=None, user_list=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_cnt = total_cnt  # type: int
        self.user_list = user_list  # type: list[DescribeFaultDiagnosisUserListResponseBodyUserList]

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = DescribeFaultDiagnosisUserListResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFaultDiagnosisUserListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaultDiagnosisUserListResponse, self).to_map()
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
            temp_model = DescribeFaultDiagnosisUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPULayoutInfoListRequest(TeaModel):
    def __init__(self, app_id=None, layout_id=None, name=None, owner_id=None, page_num=None, page_size=None):
        self.app_id = app_id  # type: str
        self.layout_id = layout_id  # type: long
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMPULayoutInfoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanesPanes(TeaModel):
    def __init__(self, height=None, major_pane=None, pane_id=None, width=None, x=None, y=None, zorder=None):
        self.height = height  # type: float
        self.major_pane = major_pane  # type: int
        self.pane_id = pane_id  # type: int
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanesPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanes(TeaModel):
    def __init__(self, panes=None):
        self.panes = panes  # type: list[DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanesPanes]

    def validate(self):
        if self.panes:
            for k in self.panes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Panes'] = []
        if self.panes is not None:
            for k in self.panes:
                result['Panes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.panes = []
        if m.get('Panes') is not None:
            for k in m.get('Panes'):
                temp_model = DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanesPanes()
                self.panes.append(temp_model.from_map(k))
        return self


class DescribeMPULayoutInfoListResponseBodyLayoutsLayout(TeaModel):
    def __init__(self, audio_mix_count=None, layout_id=None, name=None, panes=None):
        self.audio_mix_count = audio_mix_count  # type: int
        self.layout_id = layout_id  # type: long
        self.name = name  # type: str
        self.panes = panes  # type: DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanes

    def validate(self):
        if self.panes:
            self.panes.validate()

    def to_map(self):
        _map = super(DescribeMPULayoutInfoListResponseBodyLayoutsLayout, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.name is not None:
            result['Name'] = self.name
        if self.panes is not None:
            result['Panes'] = self.panes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Panes') is not None:
            temp_model = DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanes()
            self.panes = temp_model.from_map(m['Panes'])
        return self


class DescribeMPULayoutInfoListResponseBodyLayouts(TeaModel):
    def __init__(self, layout=None):
        self.layout = layout  # type: list[DescribeMPULayoutInfoListResponseBodyLayoutsLayout]

    def validate(self):
        if self.layout:
            for k in self.layout:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMPULayoutInfoListResponseBodyLayouts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Layout'] = []
        if self.layout is not None:
            for k in self.layout:
                result['Layout'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.layout = []
        if m.get('Layout') is not None:
            for k in m.get('Layout'):
                temp_model = DescribeMPULayoutInfoListResponseBodyLayoutsLayout()
                self.layout.append(temp_model.from_map(k))
        return self


class DescribeMPULayoutInfoListResponseBody(TeaModel):
    def __init__(self, layouts=None, request_id=None, total_num=None, total_page=None):
        self.layouts = layouts  # type: DescribeMPULayoutInfoListResponseBodyLayouts
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: long
        self.total_page = total_page  # type: long

    def validate(self):
        if self.layouts:
            self.layouts.validate()

    def to_map(self):
        _map = super(DescribeMPULayoutInfoListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layouts is not None:
            result['Layouts'] = self.layouts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Layouts') is not None:
            temp_model = DescribeMPULayoutInfoListResponseBodyLayouts()
            self.layouts = temp_model.from_map(m['Layouts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeMPULayoutInfoListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMPULayoutInfoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMPULayoutInfoListResponse, self).to_map()
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
            temp_model = DescribeMPULayoutInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePubUserListBySubUserRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None, sub_user_id=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePubUserListBySubUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods(TeaModel):
    def __init__(self, join_ts=None, leave_ts=None):
        self.join_ts = join_ts  # type: long
        self.leave_ts = leave_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribePubUserListBySubUserResponseBodyPubUserDetailList(TeaModel):
    def __init__(self, call_id_list=None, client_type=None, created_ts=None, destroyed_ts=None, duration=None,
                 location=None, network=None, network_list=None, online_duration=None, online_periods=None, os=None,
                 os_list=None, roles=None, sdk_version=None, sdk_version_list=None, user_id=None, user_id_alias=None):
        self.call_id_list = call_id_list  # type: list[str]
        self.client_type = client_type  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long
        self.location = location  # type: str
        self.network = network  # type: str
        self.network_list = network_list  # type: list[str]
        self.online_duration = online_duration  # type: long
        self.online_periods = online_periods  # type: list[DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods]
        self.os = os  # type: str
        self.os_list = os_list  # type: list[str]
        self.roles = roles  # type: list[str]
        self.sdk_version = sdk_version  # type: str
        self.sdk_version_list = sdk_version_list  # type: list[str]
        self.user_id = user_id  # type: str
        self.user_id_alias = user_id_alias  # type: str

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePubUserListBySubUserResponseBodyPubUserDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id_list is not None:
            result['CallIdList'] = self.call_id_list
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallIdList') is not None:
            self.call_id_list = m.get('CallIdList')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods(TeaModel):
    def __init__(self, join_ts=None, leave_ts=None):
        self.join_ts = join_ts  # type: long
        self.leave_ts = leave_ts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribePubUserListBySubUserResponseBodySubUserDetail(TeaModel):
    def __init__(self, client_type=None, created_ts=None, destroyed_ts=None, duration=None, location=None,
                 network=None, network_list=None, online_duration=None, online_periods=None, os=None, os_list=None,
                 roles=None, sdk_version=None, sdk_version_list=None, user_id=None, user_id_alias=None):
        self.client_type = client_type  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.duration = duration  # type: long
        self.location = location  # type: str
        self.network = network  # type: str
        self.network_list = network_list  # type: list[str]
        self.online_duration = online_duration  # type: long
        self.online_periods = online_periods  # type: list[DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods]
        self.os = os  # type: str
        self.os_list = os_list  # type: list[str]
        self.roles = roles  # type: list[str]
        self.sdk_version = sdk_version  # type: str
        self.sdk_version_list = sdk_version_list  # type: list[str]
        self.user_id = user_id  # type: str
        self.user_id_alias = user_id_alias  # type: str

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePubUserListBySubUserResponseBodySubUserDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribePubUserListBySubUserResponseBody(TeaModel):
    def __init__(self, call_status=None, pub_user_detail_list=None, request_id=None, sub_user_detail=None):
        self.call_status = call_status  # type: str
        self.pub_user_detail_list = pub_user_detail_list  # type: list[DescribePubUserListBySubUserResponseBodyPubUserDetailList]
        self.request_id = request_id  # type: str
        self.sub_user_detail = sub_user_detail  # type: DescribePubUserListBySubUserResponseBodySubUserDetail

    def validate(self):
        if self.pub_user_detail_list:
            for k in self.pub_user_detail_list:
                if k:
                    k.validate()
        if self.sub_user_detail:
            self.sub_user_detail.validate()

    def to_map(self):
        _map = super(DescribePubUserListBySubUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        result['PubUserDetailList'] = []
        if self.pub_user_detail_list is not None:
            for k in self.pub_user_detail_list:
                result['PubUserDetailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_user_detail is not None:
            result['SubUserDetail'] = self.sub_user_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        self.pub_user_detail_list = []
        if m.get('PubUserDetailList') is not None:
            for k in m.get('PubUserDetailList'):
                temp_model = DescribePubUserListBySubUserResponseBodyPubUserDetailList()
                self.pub_user_detail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubUserDetail') is not None:
            temp_model = DescribePubUserListBySubUserResponseBodySubUserDetail()
            self.sub_user_detail = temp_model.from_map(m['SubUserDetail'])
        return self


class DescribePubUserListBySubUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePubUserListBySubUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePubUserListBySubUserResponse, self).to_map()
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
            temp_model = DescribePubUserListBySubUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQoeMetricDataRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, created_ts=None, destroyed_ts=None, user_id=None):
        # APP ID。
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.created_ts = created_ts  # type: long
        self.destroyed_ts = destroyed_ts  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQoeMetricDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBodyAudioDataNodes(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQoeMetricDataResponseBodyAudioDataNodes, self).to_map()
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


class DescribeQoeMetricDataResponseBodyAudioData(TeaModel):
    def __init__(self, nodes=None, type=None, user_id=None):
        self.nodes = nodes  # type: list[DescribeQoeMetricDataResponseBodyAudioDataNodes]
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQoeMetricDataResponseBodyAudioData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQoeMetricDataResponseBodyAudioDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBodyVideoDataNodes(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQoeMetricDataResponseBodyVideoDataNodes, self).to_map()
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


class DescribeQoeMetricDataResponseBodyVideoData(TeaModel):
    def __init__(self, nodes=None, type=None, user_id=None):
        self.nodes = nodes  # type: list[DescribeQoeMetricDataResponseBodyVideoDataNodes]
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQoeMetricDataResponseBodyVideoData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQoeMetricDataResponseBodyVideoDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBody(TeaModel):
    def __init__(self, audio_data=None, request_id=None, video_data=None):
        self.audio_data = audio_data  # type: list[DescribeQoeMetricDataResponseBodyAudioData]
        self.request_id = request_id  # type: str
        self.video_data = video_data  # type: list[DescribeQoeMetricDataResponseBodyVideoData]

    def validate(self):
        if self.audio_data:
            for k in self.audio_data:
                if k:
                    k.validate()
        if self.video_data:
            for k in self.video_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQoeMetricDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioData'] = []
        if self.audio_data is not None:
            for k in self.audio_data:
                result['AudioData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VideoData'] = []
        if self.video_data is not None:
            for k in self.video_data:
                result['VideoData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.audio_data = []
        if m.get('AudioData') is not None:
            for k in m.get('AudioData'):
                temp_model = DescribeQoeMetricDataResponseBodyAudioData()
                self.audio_data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.video_data = []
        if m.get('VideoData') is not None:
            for k in m.get('VideoData'):
                temp_model = DescribeQoeMetricDataResponseBodyVideoData()
                self.video_data.append(temp_model.from_map(k))
        return self


class DescribeQoeMetricDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeQoeMetricDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeQoeMetricDataResponse, self).to_map()
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
            temp_model = DescribeQoeMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityAreaDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, parent_area=None, start_date=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: long
        self.parent_area = parent_area  # type: str
        self.start_date = start_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityAreaDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList(TeaModel):
    def __init__(self, audio_delay=None, audio_high_quality_transmission_rate=None, audio_stuck_rate=None,
                 call_duration_ratio=None, join_channel_suc_five_sec_rate=None, join_channel_suc_rate=None, name=None,
                 video_delay=None, video_first_pic_duration=None, video_high_quality_transmission_rate=None,
                 video_stuck_rate=None):
        self.audio_delay = audio_delay  # type: long
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate  # type: str
        self.audio_stuck_rate = audio_stuck_rate  # type: str
        self.call_duration_ratio = call_duration_ratio  # type: str
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate  # type: str
        self.join_channel_suc_rate = join_channel_suc_rate  # type: str
        self.name = name  # type: str
        self.video_delay = video_delay  # type: long
        self.video_first_pic_duration = video_first_pic_duration  # type: long
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate  # type: str
        self.video_stuck_rate = video_stuck_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(self, quality_stat_data_list=None, request_id=None):
        self.quality_stat_data_list = quality_stat_data_list  # type: list[DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.quality_stat_data_list:
            for k in self.quality_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQualityAreaDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityStatDataList'] = []
        if self.quality_stat_data_list is not None:
            for k in self.quality_stat_data_list:
                result['QualityStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.quality_stat_data_list = []
        if m.get('QualityStatDataList') is not None:
            for k in m.get('QualityStatDataList'):
                temp_model = DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList()
                self.quality_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityAreaDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeQualityAreaDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeQualityAreaDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeQualityAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, start_date=None, stat_dim=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: long
        self.start_date = start_date  # type: long
        self.stat_dim = stat_dim  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeQualityDistributionStatDataResponseBodyQualityStatDataList(TeaModel):
    def __init__(self, audio_delay=None, audio_high_quality_transmission_rate=None, audio_stuck_rate=None,
                 call_duration_ratio=None, join_channel_suc_five_sec_rate=None, join_channel_suc_rate=None, name=None,
                 video_delay=None, video_first_pic_duration=None, video_high_quality_transmission_rate=None,
                 video_stuck_rate=None):
        self.audio_delay = audio_delay  # type: long
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate  # type: str
        self.audio_stuck_rate = audio_stuck_rate  # type: str
        self.call_duration_ratio = call_duration_ratio  # type: str
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate  # type: str
        self.join_channel_suc_rate = join_channel_suc_rate  # type: str
        self.name = name  # type: str
        self.video_delay = video_delay  # type: long
        self.video_first_pic_duration = video_first_pic_duration  # type: long
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate  # type: str
        self.video_stuck_rate = video_stuck_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityDistributionStatDataResponseBodyQualityStatDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityDistributionStatDataResponseBody(TeaModel):
    def __init__(self, quality_stat_data_list=None, request_id=None):
        self.quality_stat_data_list = quality_stat_data_list  # type: list[DescribeQualityDistributionStatDataResponseBodyQualityStatDataList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.quality_stat_data_list:
            for k in self.quality_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQualityDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityStatDataList'] = []
        if self.quality_stat_data_list is not None:
            for k in self.quality_stat_data_list:
                result['QualityStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.quality_stat_data_list = []
        if m.get('QualityStatDataList') is not None:
            for k in m.get('QualityStatDataList'):
                temp_model = DescribeQualityDistributionStatDataResponseBodyQualityStatDataList()
                self.quality_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeQualityDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeQualityDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeQualityDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityOsSdkVersionDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, start_date=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: long
        self.start_date = start_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityOsSdkVersionDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList(TeaModel):
    def __init__(self, audio_delay=None, audio_high_quality_transmission_rate=None, audio_stuck_rate=None,
                 call_duration_ratio=None, join_channel_suc_five_sec_rate=None, join_channel_suc_rate=None, name=None, os=None,
                 video_delay=None, video_first_pic_duration=None, video_high_quality_transmission_rate=None,
                 video_stuck_rate=None):
        self.audio_delay = audio_delay  # type: long
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate  # type: str
        self.audio_stuck_rate = audio_stuck_rate  # type: str
        self.call_duration_ratio = call_duration_ratio  # type: str
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate  # type: str
        self.join_channel_suc_rate = join_channel_suc_rate  # type: str
        self.name = name  # type: str
        self.os = os  # type: str
        self.video_delay = video_delay  # type: long
        self.video_first_pic_duration = video_first_pic_duration  # type: long
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate  # type: str
        self.video_stuck_rate = video_stuck_rate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.os is not None:
            result['Os'] = self.os
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponseBody(TeaModel):
    def __init__(self, quality_os_sdk_version_stat_data_list=None, request_id=None):
        self.quality_os_sdk_version_stat_data_list = quality_os_sdk_version_stat_data_list  # type: list[DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.quality_os_sdk_version_stat_data_list:
            for k in self.quality_os_sdk_version_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQualityOsSdkVersionDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityOsSdkVersionStatDataList'] = []
        if self.quality_os_sdk_version_stat_data_list is not None:
            for k in self.quality_os_sdk_version_stat_data_list:
                result['QualityOsSdkVersionStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.quality_os_sdk_version_stat_data_list = []
        if m.get('QualityOsSdkVersionStatDataList') is not None:
            for k in m.get('QualityOsSdkVersionStatDataList'):
                temp_model = DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList()
                self.quality_os_sdk_version_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeQualityOsSdkVersionDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeQualityOsSdkVersionDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeQualityOsSdkVersionDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityOverallDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, start_date=None, types=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: long
        self.start_date = start_date  # type: long
        self.types = types  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityOverallDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class DescribeQualityOverallDataResponseBodyQualityOverallDataNodes(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQualityOverallDataResponseBodyQualityOverallDataNodes, self).to_map()
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


class DescribeQualityOverallDataResponseBodyQualityOverallData(TeaModel):
    def __init__(self, average=None, nodes=None, type=None):
        self.average = average  # type: str
        self.nodes = nodes  # type: list[DescribeQualityOverallDataResponseBodyQualityOverallDataNodes]
        self.type = type  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQualityOverallDataResponseBodyQualityOverallData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQualityOverallDataResponseBodyQualityOverallDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeQualityOverallDataResponseBody(TeaModel):
    def __init__(self, quality_overall_data=None, request_id=None):
        self.quality_overall_data = quality_overall_data  # type: list[DescribeQualityOverallDataResponseBodyQualityOverallData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.quality_overall_data:
            for k in self.quality_overall_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeQualityOverallDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityOverallData'] = []
        if self.quality_overall_data is not None:
            for k in self.quality_overall_data:
                result['QualityOverallData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.quality_overall_data = []
        if m.get('QualityOverallData') is not None:
            for k in m.get('QualityOverallData'):
                temp_model = DescribeQualityOverallDataResponseBodyQualityOverallData()
                self.quality_overall_data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityOverallDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeQualityOverallDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeQualityOverallDataResponse, self).to_map()
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
            temp_model = DescribeQualityOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordFilesRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, end_time=None, owner_id=None, page_num=None, page_size=None,
                 start_time=None, task_ids=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: str
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DescribeRecordFilesResponseBodyRecordFiles(TeaModel):
    def __init__(self, app_id=None, channel_id=None, create_time=None, duration=None, start_time=None,
                 stop_time=None, task_id=None, url=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.create_time = create_time  # type: str
        self.duration = duration  # type: float
        self.start_time = start_time  # type: str
        self.stop_time = stop_time  # type: str
        self.task_id = task_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordFilesResponseBodyRecordFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeRecordFilesResponseBody(TeaModel):
    def __init__(self, record_files=None, request_id=None, total_num=None, total_page=None):
        self.record_files = record_files  # type: list[DescribeRecordFilesResponseBodyRecordFiles]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: long
        self.total_page = total_page  # type: long

    def validate(self):
        if self.record_files:
            for k in self.record_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRecordFilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RecordFiles'] = []
        if self.record_files is not None:
            for k in self.record_files:
                result['RecordFiles'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.record_files = []
        if m.get('RecordFiles') is not None:
            for k in m.get('RecordFiles'):
                temp_model = DescribeRecordFilesResponseBodyRecordFiles()
                self.record_files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeRecordFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRecordFilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecordFilesResponse, self).to_map()
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
            temp_model = DescribeRecordFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordTemplatesRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, page_num=None, page_size=None, template_ids=None):
        self.app_id = app_id  # type: str
        # 1
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.template_ids = template_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class DescribeRecordTemplatesResponseBodyTemplatesBackgrounds(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordTemplatesResponseBodyTemplatesBackgrounds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class DescribeRecordTemplatesResponseBodyTemplatesClockWidgets(TeaModel):
    def __init__(self, font_color=None, font_size=None, font_type=None, x=None, y=None, zorder=None):
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordTemplatesResponseBodyTemplatesClockWidgets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class DescribeRecordTemplatesResponseBodyTemplatesWatermarks(TeaModel):
    def __init__(self, alpha=None, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordTemplatesResponseBodyTemplatesWatermarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class DescribeRecordTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, background_color=None, backgrounds=None, clock_widgets=None, create_time=None,
                 delay_stop_time=None, enable_m3u_8date_time=None, file_split_interval=None, formats=None, http_callback_url=None,
                 layout_ids=None, media_encode=None, mns_queue=None, name=None, oss_bucket=None, oss_file_prefix=None,
                 task_profile=None, template_id=None, watermarks=None):
        self.background_color = background_color  # type: int
        self.backgrounds = backgrounds  # type: list[DescribeRecordTemplatesResponseBodyTemplatesBackgrounds]
        self.clock_widgets = clock_widgets  # type: list[DescribeRecordTemplatesResponseBodyTemplatesClockWidgets]
        self.create_time = create_time  # type: str
        self.delay_stop_time = delay_stop_time  # type: int
        self.enable_m3u_8date_time = enable_m3u_8date_time  # type: bool
        self.file_split_interval = file_split_interval  # type: int
        self.formats = formats  # type: list[str]
        self.http_callback_url = http_callback_url  # type: str
        self.layout_ids = layout_ids  # type: list[long]
        self.media_encode = media_encode  # type: int
        self.mns_queue = mns_queue  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.task_profile = task_profile  # type: str
        self.template_id = template_id  # type: str
        self.watermarks = watermarks  # type: list[DescribeRecordTemplatesResponseBodyTemplatesWatermarks]

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRecordTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time
        if self.enable_m3u_8date_time is not None:
            result['EnableM3u8DateTime'] = self.enable_m3u_8date_time
        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval
        if self.formats is not None:
            result['Formats'] = self.formats
        if self.http_callback_url is not None:
            result['HttpCallbackUrl'] = self.http_callback_url
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplatesBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplatesClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')
        if m.get('EnableM3u8DateTime') is not None:
            self.enable_m3u_8date_time = m.get('EnableM3u8DateTime')
        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        if m.get('HttpCallbackUrl') is not None:
            self.http_callback_url = m.get('HttpCallbackUrl')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplatesWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class DescribeRecordTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, templates=None, total_num=None, total_page=None):
        self.request_id = request_id  # type: str
        self.templates = templates  # type: list[DescribeRecordTemplatesResponseBodyTemplates]
        self.total_num = total_num  # type: long
        self.total_page = total_page  # type: long

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRecordTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeRecordTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRecordTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecordTemplatesResponse, self).to_map()
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
            temp_model = DescribeRecordTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelListRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, owner_id=None, page_no=None, page_size=None, service_area=None,
                 sort_type=None, time_point=None, user_id=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.service_area = service_area  # type: str
        self.sort_type = sort_type  # type: str
        self.time_point = time_point  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcChannelListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeRtcChannelListResponseBodyChannelListChannelListCallArea(TeaModel):
    def __init__(self, call_area=None):
        self.call_area = call_area  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcChannelListResponseBodyChannelListChannelListCallArea, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_area is not None:
            result['CallArea'] = self.call_area
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallArea') is not None:
            self.call_area = m.get('CallArea')
        return self


class DescribeRtcChannelListResponseBodyChannelListChannelList(TeaModel):
    def __init__(self, call_area=None, channel_id=None, end_time=None, start_time=None, total_user_cnt=None):
        self.call_area = call_area  # type: DescribeRtcChannelListResponseBodyChannelListChannelListCallArea
        self.channel_id = channel_id  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.total_user_cnt = total_user_cnt  # type: long

    def validate(self):
        if self.call_area:
            self.call_area.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelListResponseBodyChannelListChannelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_area is not None:
            result['CallArea'] = self.call_area.to_map()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_user_cnt is not None:
            result['TotalUserCnt'] = self.total_user_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallArea') is not None:
            temp_model = DescribeRtcChannelListResponseBodyChannelListChannelListCallArea()
            self.call_area = temp_model.from_map(m['CallArea'])
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalUserCnt') is not None:
            self.total_user_cnt = m.get('TotalUserCnt')
        return self


class DescribeRtcChannelListResponseBodyChannelList(TeaModel):
    def __init__(self, channel_list=None):
        self.channel_list = channel_list  # type: list[DescribeRtcChannelListResponseBodyChannelListChannelList]

    def validate(self):
        if self.channel_list:
            for k in self.channel_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelListResponseBodyChannelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChannelList'] = []
        if self.channel_list is not None:
            for k in self.channel_list:
                result['ChannelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.channel_list = []
        if m.get('ChannelList') is not None:
            for k in m.get('ChannelList'):
                temp_model = DescribeRtcChannelListResponseBodyChannelListChannelList()
                self.channel_list.append(temp_model.from_map(k))
        return self


class DescribeRtcChannelListResponseBody(TeaModel):
    def __init__(self, channel_list=None, page_no=None, page_size=None, request_id=None, total_cnt=None):
        self.channel_list = channel_list  # type: DescribeRtcChannelListResponseBodyChannelList
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_cnt = total_cnt  # type: long

    def validate(self):
        if self.channel_list:
            self.channel_list.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_list is not None:
            result['ChannelList'] = self.channel_list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelList') is not None:
            temp_model = DescribeRtcChannelListResponseBodyChannelList()
            self.channel_list = temp_model.from_map(m['ChannelList'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        return self


class DescribeRtcChannelListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRtcChannelListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelListResponse, self).to_map()
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
            temp_model = DescribeRtcChannelListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelMetricRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, owner_id=None, time_point=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.owner_id = owner_id  # type: long
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcChannelMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric(TeaModel):
    def __init__(self, channel_id=None, end_time=None, pub_user_count=None, start_time=None, sub_user_count=None,
                 user_count=None):
        self.channel_id = channel_id  # type: str
        self.end_time = end_time  # type: str
        self.pub_user_count = pub_user_count  # type: int
        self.start_time = start_time  # type: str
        self.sub_user_count = sub_user_count  # type: int
        self.user_count = user_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pub_user_count is not None:
            result['PubUserCount'] = self.pub_user_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_count is not None:
            result['SubUserCount'] = self.sub_user_count
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PubUserCount') is not None:
            self.pub_user_count = m.get('PubUserCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserCount') is not None:
            self.sub_user_count = m.get('SubUserCount')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration(TeaModel):
    def __init__(self, audio=None, content=None, video_1080=None, video_360=None, video_720=None):
        self.audio = audio  # type: int
        self.content = content  # type: int
        self.video_1080 = video_1080  # type: int
        self.video_360 = video_360  # type: int
        self.video_720 = video_720  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio
        if self.content is not None:
            result['Content'] = self.content
        if self.video_1080 is not None:
            result['Video1080'] = self.video_1080
        if self.video_360 is not None:
            result['Video360'] = self.video_360
        if self.video_720 is not None:
            result['Video720'] = self.video_720
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Video1080') is not None:
            self.video_1080 = m.get('Video1080')
        if m.get('Video360') is not None:
            self.video_360 = m.get('Video360')
        if m.get('Video720') is not None:
            self.video_720 = m.get('Video720')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration(TeaModel):
    def __init__(self, audio=None, content=None, video_1080=None, video_360=None, video_720=None):
        self.audio = audio  # type: int
        self.content = content  # type: int
        self.video_1080 = video_1080  # type: int
        self.video_360 = video_360  # type: int
        self.video_720 = video_720  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio
        if self.content is not None:
            result['Content'] = self.content
        if self.video_1080 is not None:
            result['Video1080'] = self.video_1080
        if self.video_360 is not None:
            result['Video360'] = self.video_360
        if self.video_720 is not None:
            result['Video720'] = self.video_720
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Video1080') is not None:
            self.video_1080 = m.get('Video1080')
        if m.get('Video360') is not None:
            self.video_360 = m.get('Video360')
        if m.get('Video720') is not None:
            self.video_720 = m.get('Video720')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration(TeaModel):
    def __init__(self, pub_duration=None, sub_duration=None):
        self.pub_duration = pub_duration  # type: DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration
        self.sub_duration = sub_duration  # type: DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration

    def validate(self):
        if self.pub_duration:
            self.pub_duration.validate()
        if self.sub_duration:
            self.sub_duration.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pub_duration is not None:
            result['PubDuration'] = self.pub_duration.to_map()
        if self.sub_duration is not None:
            result['SubDuration'] = self.sub_duration.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PubDuration') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration()
            self.pub_duration = temp_model.from_map(m['PubDuration'])
        if m.get('SubDuration') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration()
            self.sub_duration = temp_model.from_map(m['SubDuration'])
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfo(TeaModel):
    def __init__(self, channel_metric=None, duration=None):
        self.channel_metric = channel_metric  # type: DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric
        self.duration = duration  # type: DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration

    def validate(self):
        if self.channel_metric:
            self.channel_metric.validate()
        if self.duration:
            self.duration.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelMetricResponseBodyChannelMetricInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_metric is not None:
            result['ChannelMetric'] = self.channel_metric.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelMetric') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric()
            self.channel_metric = temp_model.from_map(m['ChannelMetric'])
        if m.get('Duration') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration()
            self.duration = temp_model.from_map(m['Duration'])
        return self


class DescribeRtcChannelMetricResponseBody(TeaModel):
    def __init__(self, channel_metric_info=None, request_id=None):
        self.channel_metric_info = channel_metric_info  # type: DescribeRtcChannelMetricResponseBodyChannelMetricInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.channel_metric_info:
            self.channel_metric_info.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_metric_info is not None:
            result['ChannelMetricInfo'] = self.channel_metric_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelMetricInfo') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfo()
            self.channel_metric_info = temp_model.from_map(m['ChannelMetricInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcChannelMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRtcChannelMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRtcChannelMetricResponse, self).to_map()
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
            temp_model = DescribeRtcChannelMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcDurationDataRequest(TeaModel):
    def __init__(self, app_id=None, end_time=None, interval=None, owner_id=None, service_area=None, start_time=None):
        self.app_id = app_id  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.service_area = service_area  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcDurationDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule(TeaModel):
    def __init__(self, audio_duration=None, content_duration=None, time_stamp=None, total_duration=None,
                 v_1080duration=None, v_360duration=None, v_720duration=None):
        self.audio_duration = audio_duration  # type: long
        self.content_duration = content_duration  # type: long
        self.time_stamp = time_stamp  # type: str
        self.total_duration = total_duration  # type: long
        self.v_1080duration = v_1080duration  # type: long
        self.v_360duration = v_360duration  # type: long
        self.v_720duration = v_720duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.content_duration is not None:
            result['ContentDuration'] = self.content_duration
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        if self.v_1080duration is not None:
            result['V1080Duration'] = self.v_1080duration
        if self.v_360duration is not None:
            result['V360Duration'] = self.v_360duration
        if self.v_720duration is not None:
            result['V720Duration'] = self.v_720duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('ContentDuration') is not None:
            self.content_duration = m.get('ContentDuration')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        if m.get('V1080Duration') is not None:
            self.v_1080duration = m.get('V1080Duration')
        if m.get('V360Duration') is not None:
            self.v_360duration = m.get('V360Duration')
        if m.get('V720Duration') is not None:
            self.v_720duration = m.get('V720Duration')
        return self


class DescribeRtcDurationDataResponseBodyDurationDataPerInterval(TeaModel):
    def __init__(self, duration_module=None):
        self.duration_module = duration_module  # type: list[DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule]

    def validate(self):
        if self.duration_module:
            for k in self.duration_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRtcDurationDataResponseBodyDurationDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DurationModule'] = []
        if self.duration_module is not None:
            for k in self.duration_module:
                result['DurationModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.duration_module = []
        if m.get('DurationModule') is not None:
            for k in m.get('DurationModule'):
                temp_model = DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule()
                self.duration_module.append(temp_model.from_map(k))
        return self


class DescribeRtcDurationDataResponseBody(TeaModel):
    def __init__(self, duration_data_per_interval=None, request_id=None):
        self.duration_data_per_interval = duration_data_per_interval  # type: DescribeRtcDurationDataResponseBodyDurationDataPerInterval
        self.request_id = request_id  # type: str

    def validate(self):
        if self.duration_data_per_interval:
            self.duration_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeRtcDurationDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_data_per_interval is not None:
            result['DurationDataPerInterval'] = self.duration_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DurationDataPerInterval') is not None:
            temp_model = DescribeRtcDurationDataResponseBodyDurationDataPerInterval()
            self.duration_data_per_interval = temp_model.from_map(m['DurationDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcDurationDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRtcDurationDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRtcDurationDataResponse, self).to_map()
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
            temp_model = DescribeRtcDurationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcPeakChannelCntDataRequest(TeaModel):
    def __init__(self, app_id=None, end_time=None, interval=None, owner_id=None, service_area=None, start_time=None):
        self.app_id = app_id  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.service_area = service_area  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcPeakChannelCntDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule(TeaModel):
    def __init__(self, active_channel_peak=None, active_channel_peak_time=None, time_stamp=None):
        self.active_channel_peak = active_channel_peak  # type: long
        self.active_channel_peak_time = active_channel_peak_time  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_channel_peak is not None:
            result['ActiveChannelPeak'] = self.active_channel_peak
        if self.active_channel_peak_time is not None:
            result['ActiveChannelPeakTime'] = self.active_channel_peak_time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveChannelPeak') is not None:
            self.active_channel_peak = m.get('ActiveChannelPeak')
        if m.get('ActiveChannelPeakTime') is not None:
            self.active_channel_peak_time = m.get('ActiveChannelPeakTime')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval(TeaModel):
    def __init__(self, peak_channel_cnt_module=None):
        self.peak_channel_cnt_module = peak_channel_cnt_module  # type: list[DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule]

    def validate(self):
        if self.peak_channel_cnt_module:
            for k in self.peak_channel_cnt_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PeakChannelCntModule'] = []
        if self.peak_channel_cnt_module is not None:
            for k in self.peak_channel_cnt_module:
                result['PeakChannelCntModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.peak_channel_cnt_module = []
        if m.get('PeakChannelCntModule') is not None:
            for k in m.get('PeakChannelCntModule'):
                temp_model = DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule()
                self.peak_channel_cnt_module.append(temp_model.from_map(k))
        return self


class DescribeRtcPeakChannelCntDataResponseBody(TeaModel):
    def __init__(self, peak_channel_cnt_data_per_interval=None, request_id=None):
        self.peak_channel_cnt_data_per_interval = peak_channel_cnt_data_per_interval  # type: DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval
        self.request_id = request_id  # type: str

    def validate(self):
        if self.peak_channel_cnt_data_per_interval:
            self.peak_channel_cnt_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeRtcPeakChannelCntDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_channel_cnt_data_per_interval is not None:
            result['PeakChannelCntDataPerInterval'] = self.peak_channel_cnt_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PeakChannelCntDataPerInterval') is not None:
            temp_model = DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval()
            self.peak_channel_cnt_data_per_interval = temp_model.from_map(m['PeakChannelCntDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcPeakChannelCntDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRtcPeakChannelCntDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRtcPeakChannelCntDataResponse, self).to_map()
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
            temp_model = DescribeRtcPeakChannelCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcUserCntDataRequest(TeaModel):
    def __init__(self, app_id=None, end_time=None, interval=None, owner_id=None, service_area=None, start_time=None):
        self.app_id = app_id  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.service_area = service_area  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcUserCntDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule(TeaModel):
    def __init__(self, active_user_cnt=None, time_stamp=None):
        self.active_user_cnt = active_user_cnt  # type: long
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_user_cnt is not None:
            result['ActiveUserCnt'] = self.active_user_cnt
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveUserCnt') is not None:
            self.active_user_cnt = m.get('ActiveUserCnt')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval(TeaModel):
    def __init__(self, user_cnt_module=None):
        self.user_cnt_module = user_cnt_module  # type: list[DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule]

    def validate(self):
        if self.user_cnt_module:
            for k in self.user_cnt_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserCntModule'] = []
        if self.user_cnt_module is not None:
            for k in self.user_cnt_module:
                result['UserCntModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_cnt_module = []
        if m.get('UserCntModule') is not None:
            for k in m.get('UserCntModule'):
                temp_model = DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule()
                self.user_cnt_module.append(temp_model.from_map(k))
        return self


class DescribeRtcUserCntDataResponseBody(TeaModel):
    def __init__(self, request_id=None, user_cnt_data_per_interval=None):
        self.request_id = request_id  # type: str
        self.user_cnt_data_per_interval = user_cnt_data_per_interval  # type: DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval

    def validate(self):
        if self.user_cnt_data_per_interval:
            self.user_cnt_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeRtcUserCntDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_cnt_data_per_interval is not None:
            result['UserCntDataPerInterval'] = self.user_cnt_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserCntDataPerInterval') is not None:
            temp_model = DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval()
            self.user_cnt_data_per_interval = temp_model.from_map(m['UserCntDataPerInterval'])
        return self


class DescribeRtcUserCntDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRtcUserCntDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRtcUserCntDataResponse, self).to_map()
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
            temp_model = DescribeRtcUserCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageAreaDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, parent_area=None, start_date=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: str
        self.parent_area = parent_area  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageAreaDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList(TeaModel):
    def __init__(self, audio_call_duration=None, name=None, total_call_duration=None, video_call_duration=None):
        self.audio_call_duration = audio_call_duration  # type: int
        self.name = name  # type: str
        self.total_call_duration = total_call_duration  # type: int
        self.video_call_duration = video_call_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.name is not None:
            result['Name'] = self.name
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(self, request_id=None, usage_area_stat_list=None):
        self.request_id = request_id  # type: str
        self.usage_area_stat_list = usage_area_stat_list  # type: list[DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList]

    def validate(self):
        if self.usage_area_stat_list:
            for k in self.usage_area_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsageAreaDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageAreaStatList'] = []
        if self.usage_area_stat_list is not None:
            for k in self.usage_area_stat_list:
                result['UsageAreaStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_area_stat_list = []
        if m.get('UsageAreaStatList') is not None:
            for k in m.get('UsageAreaStatList'):
                temp_model = DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList()
                self.usage_area_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageAreaDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUsageAreaDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUsageAreaDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeUsageAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, start_date=None, stat_dim=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: long
        self.start_date = start_date  # type: long
        self.stat_dim = stat_dim  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeUsageDistributionStatDataResponseBodyUsageStatList(TeaModel):
    def __init__(self, audio_call_duration=None, call_duration_ratio=None, name=None, total_call_duration=None,
                 video_call_duration=None):
        self.audio_call_duration = audio_call_duration  # type: long
        self.call_duration_ratio = call_duration_ratio  # type: str
        self.name = name  # type: str
        self.total_call_duration = total_call_duration  # type: long
        self.video_call_duration = video_call_duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageDistributionStatDataResponseBodyUsageStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.name is not None:
            result['Name'] = self.name
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageDistributionStatDataResponseBody(TeaModel):
    def __init__(self, request_id=None, usage_stat_list=None):
        self.request_id = request_id  # type: str
        self.usage_stat_list = usage_stat_list  # type: list[DescribeUsageDistributionStatDataResponseBodyUsageStatList]

    def validate(self):
        if self.usage_stat_list:
            for k in self.usage_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsageDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageStatList'] = []
        if self.usage_stat_list is not None:
            for k in self.usage_stat_list:
                result['UsageStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_stat_list = []
        if m.get('UsageStatList') is not None:
            for k in m.get('UsageStatList'):
                temp_model = DescribeUsageDistributionStatDataResponseBodyUsageStatList()
                self.usage_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUsageDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUsageDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeUsageDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageOsSdkVersionDistributionStatDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, start_date=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: long
        self.start_date = start_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageOsSdkVersionDistributionStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList(TeaModel):
    def __init__(self, audio_call_duration=None, call_duration_ratio=None, name=None, os=None,
                 total_call_duration=None, video_call_duration=None):
        self.audio_call_duration = audio_call_duration  # type: long
        self.call_duration_ratio = call_duration_ratio  # type: str
        self.name = name  # type: str
        self.os = os  # type: str
        self.total_call_duration = total_call_duration  # type: long
        self.video_call_duration = video_call_duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.name is not None:
            result['Name'] = self.name
        if self.os is not None:
            result['Os'] = self.os
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponseBody(TeaModel):
    def __init__(self, request_id=None, usage_os_sdk_version_stat_list=None):
        self.request_id = request_id  # type: str
        self.usage_os_sdk_version_stat_list = usage_os_sdk_version_stat_list  # type: list[DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList]

    def validate(self):
        if self.usage_os_sdk_version_stat_list:
            for k in self.usage_os_sdk_version_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsageOsSdkVersionDistributionStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageOsSdkVersionStatList'] = []
        if self.usage_os_sdk_version_stat_list is not None:
            for k in self.usage_os_sdk_version_stat_list:
                result['UsageOsSdkVersionStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_os_sdk_version_stat_list = []
        if m.get('UsageOsSdkVersionStatList') is not None:
            for k in m.get('UsageOsSdkVersionStatList'):
                temp_model = DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList()
                self.usage_os_sdk_version_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUsageOsSdkVersionDistributionStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUsageOsSdkVersionDistributionStatDataResponse, self).to_map()
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
            temp_model = DescribeUsageOsSdkVersionDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageOverallDataRequest(TeaModel):
    def __init__(self, app_id=None, end_date=None, start_date=None, types=None):
        # APP ID
        self.app_id = app_id  # type: str
        self.end_date = end_date  # type: long
        self.start_date = start_date  # type: long
        self.types = types  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageOverallDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class DescribeUsageOverallDataResponseBodyUsageOverallDataNodes(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: str
        self.y = y  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageOverallDataResponseBodyUsageOverallDataNodes, self).to_map()
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


class DescribeUsageOverallDataResponseBodyUsageOverallData(TeaModel):
    def __init__(self, nodes=None, type=None):
        self.nodes = nodes  # type: list[DescribeUsageOverallDataResponseBodyUsageOverallDataNodes]
        self.type = type  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsageOverallDataResponseBodyUsageOverallData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeUsageOverallDataResponseBodyUsageOverallDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeUsageOverallDataResponseBody(TeaModel):
    def __init__(self, request_id=None, usage_overall_data=None):
        self.request_id = request_id  # type: str
        self.usage_overall_data = usage_overall_data  # type: list[DescribeUsageOverallDataResponseBodyUsageOverallData]

    def validate(self):
        if self.usage_overall_data:
            for k in self.usage_overall_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsageOverallDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageOverallData'] = []
        if self.usage_overall_data is not None:
            for k in self.usage_overall_data:
                result['UsageOverallData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_overall_data = []
        if m.get('UsageOverallData') is not None:
            for k in m.get('UsageOverallData'):
                temp_model = DescribeUsageOverallDataResponseBodyUsageOverallData()
                self.usage_overall_data.append(temp_model.from_map(k))
        return self


class DescribeUsageOverallDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUsageOverallDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUsageOverallDataResponse, self).to_map()
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
            temp_model = DescribeUsageOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserInfoInChannelRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, owner_id=None, user_id=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.owner_id = owner_id  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserInfoInChannelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeUserInfoInChannelResponseBodyProperty(TeaModel):
    def __init__(self, join=None, role=None, session=None):
        self.join = join  # type: int
        self.role = role  # type: int
        self.session = session  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserInfoInChannelResponseBodyProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join is not None:
            result['Join'] = self.join
        if self.role is not None:
            result['Role'] = self.role
        if self.session is not None:
            result['Session'] = self.session
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Join') is not None:
            self.join = m.get('Join')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Session') is not None:
            self.session = m.get('Session')
        return self


class DescribeUserInfoInChannelResponseBody(TeaModel):
    def __init__(self, is_channel_exist=None, is_in_channel=None, property=None, request_id=None, timestamp=None):
        self.is_channel_exist = is_channel_exist  # type: bool
        self.is_in_channel = is_in_channel  # type: bool
        self.property = property  # type: list[DescribeUserInfoInChannelResponseBodyProperty]
        self.request_id = request_id  # type: str
        self.timestamp = timestamp  # type: int

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserInfoInChannelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_channel_exist is not None:
            result['IsChannelExist'] = self.is_channel_exist
        if self.is_in_channel is not None:
            result['IsInChannel'] = self.is_in_channel
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsChannelExist') is not None:
            self.is_channel_exist = m.get('IsChannelExist')
        if m.get('IsInChannel') is not None:
            self.is_in_channel = m.get('IsInChannel')
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeUserInfoInChannelResponseBodyProperty()
                self.property.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeUserInfoInChannelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserInfoInChannelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserInfoInChannelResponse, self).to_map()
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
            temp_model = DescribeUserInfoInChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAutoLiveStreamRuleRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, rule_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAutoLiveStreamRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DisableAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAutoLiveStreamRuleResponseBody, self).to_map()
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


class DisableAutoLiveStreamRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableAutoLiveStreamRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableAutoLiveStreamRuleResponse, self).to_map()
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
            temp_model = DisableAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAutoLiveStreamRuleRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, rule_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAutoLiveStreamRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class EnableAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAutoLiveStreamRuleResponseBody, self).to_map()
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


class EnableAutoLiveStreamRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableAutoLiveStreamRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableAutoLiveStreamRuleResponse, self).to_map()
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
            temp_model = EnableAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMPUTaskStatusRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, task_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMPUTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetMPUTaskStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMPUTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetMPUTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMPUTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMPUTaskStatusResponse, self).to_map()
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
            temp_model = GetMPUTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, owner_id=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppResponseBody, self).to_map()
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


class ModifyAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppResponse, self).to_map()
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMPULayoutRequestPanes(TeaModel):
    def __init__(self, height=None, major_pane=None, pane_id=None, width=None, x=None, y=None, zorder=None):
        self.height = height  # type: float
        self.major_pane = major_pane  # type: int
        self.pane_id = pane_id  # type: int
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMPULayoutRequestPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class ModifyMPULayoutRequest(TeaModel):
    def __init__(self, app_id=None, audio_mix_count=None, layout_id=None, name=None, owner_id=None, panes=None):
        self.app_id = app_id  # type: str
        self.audio_mix_count = audio_mix_count  # type: int
        self.layout_id = layout_id  # type: long
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.panes = panes  # type: list[ModifyMPULayoutRequestPanes]

    def validate(self):
        if self.panes:
            for k in self.panes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyMPULayoutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        result['Panes'] = []
        if self.panes is not None:
            for k in self.panes:
                result['Panes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        self.panes = []
        if m.get('Panes') is not None:
            for k in m.get('Panes'):
                temp_model = ModifyMPULayoutRequestPanes()
                self.panes.append(temp_model.from_map(k))
        return self


class ModifyMPULayoutResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMPULayoutResponseBody, self).to_map()
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


class ModifyMPULayoutResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyMPULayoutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMPULayoutResponse, self).to_map()
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
            temp_model = ModifyMPULayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTerminalsRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, owner_id=None, terminal_ids=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.owner_id = owner_id  # type: long
        self.terminal_ids = terminal_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTerminalsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.terminal_ids is not None:
            result['TerminalIds'] = self.terminal_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TerminalIds') is not None:
            self.terminal_ids = m.get('TerminalIds')
        return self


class RemoveTerminalsResponseBodyTerminalsTerminal(TeaModel):
    def __init__(self, code=None, id=None, message=None):
        self.code = code  # type: int
        self.id = id  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTerminalsResponseBodyTerminalsTerminal, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveTerminalsResponseBodyTerminals(TeaModel):
    def __init__(self, terminal=None):
        self.terminal = terminal  # type: list[RemoveTerminalsResponseBodyTerminalsTerminal]

    def validate(self):
        if self.terminal:
            for k in self.terminal:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveTerminalsResponseBodyTerminals, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Terminal'] = []
        if self.terminal is not None:
            for k in self.terminal:
                result['Terminal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.terminal = []
        if m.get('Terminal') is not None:
            for k in m.get('Terminal'):
                temp_model = RemoveTerminalsResponseBodyTerminalsTerminal()
                self.terminal.append(temp_model.from_map(k))
        return self


class RemoveTerminalsResponseBody(TeaModel):
    def __init__(self, request_id=None, terminals=None):
        self.request_id = request_id  # type: str
        self.terminals = terminals  # type: RemoveTerminalsResponseBodyTerminals

    def validate(self):
        if self.terminals:
            self.terminals.validate()

    def to_map(self):
        _map = super(RemoveTerminalsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terminals is not None:
            result['Terminals'] = self.terminals.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Terminals') is not None:
            temp_model = RemoveTerminalsResponseBodyTerminals()
            self.terminals = temp_model.from_map(m['Terminals'])
        return self


class RemoveTerminalsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveTerminalsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveTerminalsResponse, self).to_map()
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
            temp_model = RemoveTerminalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMPUTaskRequestBackgrounds(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMPUTaskRequestBackgrounds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartMPUTaskRequestClockWidgets(TeaModel):
    def __init__(self, alpha=None, border_color=None, border_width=None, box=None, box_border_width=None,
                 box_color=None, font_color=None, font_size=None, font_type=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.border_color = border_color  # type: long
        self.border_width = border_width  # type: int
        self.box = box  # type: bool
        self.box_border_width = box_border_width  # type: int
        self.box_color = box_color  # type: long
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMPUTaskRequestClockWidgets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.border_color is not None:
            result['BorderColor'] = self.border_color
        if self.border_width is not None:
            result['BorderWidth'] = self.border_width
        if self.box is not None:
            result['Box'] = self.box
        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width
        if self.box_color is not None:
            result['BoxColor'] = self.box_color
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')
        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')
        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartMPUTaskRequestEnhancedParam(TeaModel):
    def __init__(self, enable_portrait_segmentation=None):
        self.enable_portrait_segmentation = enable_portrait_segmentation  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMPUTaskRequestEnhancedParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_portrait_segmentation is not None:
            result['EnablePortraitSegmentation'] = self.enable_portrait_segmentation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePortraitSegmentation') is not None:
            self.enable_portrait_segmentation = m.get('EnablePortraitSegmentation')
        return self


class StartMPUTaskRequestUserPanesImages(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMPUTaskRequestUserPanesImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartMPUTaskRequestUserPanesTexts(TeaModel):
    def __init__(self, alpha=None, border_color=None, border_width=None, box=None, box_border_width=None,
                 box_color=None, font_color=None, font_size=None, font_type=None, text=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.border_color = border_color  # type: long
        self.border_width = border_width  # type: int
        self.box = box  # type: bool
        self.box_border_width = box_border_width  # type: int
        self.box_color = box_color  # type: long
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.text = text  # type: str
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMPUTaskRequestUserPanesTexts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.border_color is not None:
            result['BorderColor'] = self.border_color
        if self.border_width is not None:
            result['BorderWidth'] = self.border_width
        if self.box is not None:
            result['Box'] = self.box
        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width
        if self.box_color is not None:
            result['BoxColor'] = self.box_color
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.text is not None:
            result['Text'] = self.text
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')
        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')
        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartMPUTaskRequestUserPanes(TeaModel):
    def __init__(self, images=None, pane_id=None, segment_type=None, source_type=None, texts=None, user_id=None):
        self.images = images  # type: list[StartMPUTaskRequestUserPanesImages]
        self.pane_id = pane_id  # type: int
        self.segment_type = segment_type  # type: int
        self.source_type = source_type  # type: str
        self.texts = texts  # type: list[StartMPUTaskRequestUserPanesTexts]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartMPUTaskRequestUserPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.segment_type is not None:
            result['SegmentType'] = self.segment_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = StartMPUTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('SegmentType') is not None:
            self.segment_type = m.get('SegmentType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = StartMPUTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StartMPUTaskRequestWatermarks(TeaModel):
    def __init__(self, alpha=None, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMPUTaskRequestWatermarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartMPUTaskRequest(TeaModel):
    def __init__(self, app_id=None, background_color=None, backgrounds=None, channel_id=None, clock_widgets=None,
                 crop_mode=None, enhanced_param=None, layout_ids=None, media_encode=None, mix_mode=None, owner_id=None,
                 payload_type=None, report_vad=None, rtp_ext_info=None, source_type=None, stream_type=None, stream_url=None,
                 sub_spec_audio_users=None, sub_spec_camera_users=None, sub_spec_share_screen_users=None, sub_spec_users=None,
                 task_id=None, task_type=None, time_stamp_ref=None, unsub_spec_audio_users=None,
                 unsub_spec_camera_users=None, unsub_spec_share_screen_users=None, user_panes=None, vad_interval=None, watermarks=None):
        self.app_id = app_id  # type: str
        self.background_color = background_color  # type: int
        self.backgrounds = backgrounds  # type: list[StartMPUTaskRequestBackgrounds]
        self.channel_id = channel_id  # type: str
        self.clock_widgets = clock_widgets  # type: list[StartMPUTaskRequestClockWidgets]
        self.crop_mode = crop_mode  # type: int
        self.enhanced_param = enhanced_param  # type: StartMPUTaskRequestEnhancedParam
        self.layout_ids = layout_ids  # type: list[long]
        self.media_encode = media_encode  # type: int
        self.mix_mode = mix_mode  # type: int
        self.owner_id = owner_id  # type: long
        self.payload_type = payload_type  # type: int
        self.report_vad = report_vad  # type: int
        self.rtp_ext_info = rtp_ext_info  # type: int
        self.source_type = source_type  # type: str
        self.stream_type = stream_type  # type: int
        self.stream_url = stream_url  # type: str
        self.sub_spec_audio_users = sub_spec_audio_users  # type: list[str]
        self.sub_spec_camera_users = sub_spec_camera_users  # type: list[str]
        self.sub_spec_share_screen_users = sub_spec_share_screen_users  # type: list[str]
        self.sub_spec_users = sub_spec_users  # type: list[str]
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: int
        self.time_stamp_ref = time_stamp_ref  # type: long
        self.unsub_spec_audio_users = unsub_spec_audio_users  # type: list[str]
        self.unsub_spec_camera_users = unsub_spec_camera_users  # type: list[str]
        self.unsub_spec_share_screen_users = unsub_spec_share_screen_users  # type: list[str]
        self.user_panes = user_panes  # type: list[StartMPUTaskRequestUserPanes]
        self.vad_interval = vad_interval  # type: long
        self.watermarks = watermarks  # type: list[StartMPUTaskRequestWatermarks]

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.enhanced_param:
            self.enhanced_param.validate()
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartMPUTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.enhanced_param is not None:
            result['EnhancedParam'] = self.enhanced_param.to_map()
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payload_type is not None:
            result['PayloadType'] = self.payload_type
        if self.report_vad is not None:
            result['ReportVad'] = self.report_vad
        if self.rtp_ext_info is not None:
            result['RtpExtInfo'] = self.rtp_ext_info
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url
        if self.sub_spec_audio_users is not None:
            result['SubSpecAudioUsers'] = self.sub_spec_audio_users
        if self.sub_spec_camera_users is not None:
            result['SubSpecCameraUsers'] = self.sub_spec_camera_users
        if self.sub_spec_share_screen_users is not None:
            result['SubSpecShareScreenUsers'] = self.sub_spec_share_screen_users
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.time_stamp_ref is not None:
            result['TimeStampRef'] = self.time_stamp_ref
        if self.unsub_spec_audio_users is not None:
            result['UnsubSpecAudioUsers'] = self.unsub_spec_audio_users
        if self.unsub_spec_camera_users is not None:
            result['UnsubSpecCameraUsers'] = self.unsub_spec_camera_users
        if self.unsub_spec_share_screen_users is not None:
            result['UnsubSpecShareScreenUsers'] = self.unsub_spec_share_screen_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        if self.vad_interval is not None:
            result['VadInterval'] = self.vad_interval
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = StartMPUTaskRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = StartMPUTaskRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('EnhancedParam') is not None:
            temp_model = StartMPUTaskRequestEnhancedParam()
            self.enhanced_param = temp_model.from_map(m['EnhancedParam'])
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayloadType') is not None:
            self.payload_type = m.get('PayloadType')
        if m.get('ReportVad') is not None:
            self.report_vad = m.get('ReportVad')
        if m.get('RtpExtInfo') is not None:
            self.rtp_ext_info = m.get('RtpExtInfo')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')
        if m.get('SubSpecAudioUsers') is not None:
            self.sub_spec_audio_users = m.get('SubSpecAudioUsers')
        if m.get('SubSpecCameraUsers') is not None:
            self.sub_spec_camera_users = m.get('SubSpecCameraUsers')
        if m.get('SubSpecShareScreenUsers') is not None:
            self.sub_spec_share_screen_users = m.get('SubSpecShareScreenUsers')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TimeStampRef') is not None:
            self.time_stamp_ref = m.get('TimeStampRef')
        if m.get('UnsubSpecAudioUsers') is not None:
            self.unsub_spec_audio_users = m.get('UnsubSpecAudioUsers')
        if m.get('UnsubSpecCameraUsers') is not None:
            self.unsub_spec_camera_users = m.get('UnsubSpecCameraUsers')
        if m.get('UnsubSpecShareScreenUsers') is not None:
            self.unsub_spec_share_screen_users = m.get('UnsubSpecShareScreenUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = StartMPUTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        if m.get('VadInterval') is not None:
            self.vad_interval = m.get('VadInterval')
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = StartMPUTaskRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class StartMPUTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMPUTaskResponseBody, self).to_map()
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


class StartMPUTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartMPUTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartMPUTaskResponse, self).to_map()
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
            temp_model = StartMPUTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRecordTaskRequestUserPanesImages(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordTaskRequestUserPanesImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartRecordTaskRequestUserPanesTexts(TeaModel):
    def __init__(self, font_color=None, font_size=None, font_type=None, text=None, x=None, y=None, zorder=None):
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.text = text  # type: str
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordTaskRequestUserPanesTexts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.text is not None:
            result['Text'] = self.text
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartRecordTaskRequestUserPanes(TeaModel):
    def __init__(self, images=None, pane_id=None, source_type=None, texts=None, user_id=None):
        self.images = images  # type: list[StartRecordTaskRequestUserPanesImages]
        self.pane_id = pane_id  # type: int
        self.source_type = source_type  # type: str
        self.texts = texts  # type: list[StartRecordTaskRequestUserPanesTexts]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartRecordTaskRequestUserPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = StartRecordTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = StartRecordTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StartRecordTaskRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, crop_mode=None, layout_ids=None, media_encode=None,
                 mix_mode=None, owner_id=None, source_type=None, stream_type=None, sub_spec_audio_users=None,
                 sub_spec_camera_users=None, sub_spec_share_screen_users=None, sub_spec_users=None, task_id=None, task_profile=None,
                 template_id=None, unsub_spec_audio_users=None, unsub_spec_camera_users=None,
                 unsub_spec_share_screen_users=None, user_panes=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.crop_mode = crop_mode  # type: long
        self.layout_ids = layout_ids  # type: list[long]
        self.media_encode = media_encode  # type: int
        self.mix_mode = mix_mode  # type: int
        self.owner_id = owner_id  # type: long
        self.source_type = source_type  # type: str
        self.stream_type = stream_type  # type: int
        self.sub_spec_audio_users = sub_spec_audio_users  # type: list[str]
        self.sub_spec_camera_users = sub_spec_camera_users  # type: list[str]
        self.sub_spec_share_screen_users = sub_spec_share_screen_users  # type: list[str]
        self.sub_spec_users = sub_spec_users  # type: list[str]
        self.task_id = task_id  # type: str
        self.task_profile = task_profile  # type: str
        self.template_id = template_id  # type: str
        self.unsub_spec_audio_users = unsub_spec_audio_users  # type: list[str]
        self.unsub_spec_camera_users = unsub_spec_camera_users  # type: list[str]
        self.unsub_spec_share_screen_users = unsub_spec_share_screen_users  # type: list[str]
        self.user_panes = user_panes  # type: list[StartRecordTaskRequestUserPanes]

    def validate(self):
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartRecordTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.sub_spec_audio_users is not None:
            result['SubSpecAudioUsers'] = self.sub_spec_audio_users
        if self.sub_spec_camera_users is not None:
            result['SubSpecCameraUsers'] = self.sub_spec_camera_users
        if self.sub_spec_share_screen_users is not None:
            result['SubSpecShareScreenUsers'] = self.sub_spec_share_screen_users
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.unsub_spec_audio_users is not None:
            result['UnsubSpecAudioUsers'] = self.unsub_spec_audio_users
        if self.unsub_spec_camera_users is not None:
            result['UnsubSpecCameraUsers'] = self.unsub_spec_camera_users
        if self.unsub_spec_share_screen_users is not None:
            result['UnsubSpecShareScreenUsers'] = self.unsub_spec_share_screen_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('SubSpecAudioUsers') is not None:
            self.sub_spec_audio_users = m.get('SubSpecAudioUsers')
        if m.get('SubSpecCameraUsers') is not None:
            self.sub_spec_camera_users = m.get('SubSpecCameraUsers')
        if m.get('SubSpecShareScreenUsers') is not None:
            self.sub_spec_share_screen_users = m.get('SubSpecShareScreenUsers')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UnsubSpecAudioUsers') is not None:
            self.unsub_spec_audio_users = m.get('UnsubSpecAudioUsers')
        if m.get('UnsubSpecCameraUsers') is not None:
            self.unsub_spec_camera_users = m.get('UnsubSpecCameraUsers')
        if m.get('UnsubSpecShareScreenUsers') is not None:
            self.unsub_spec_share_screen_users = m.get('UnsubSpecShareScreenUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = StartRecordTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        return self


class StartRecordTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordTaskResponseBody, self).to_map()
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


class StartRecordTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartRecordTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartRecordTaskResponse, self).to_map()
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
            temp_model = StartRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMPUTaskRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, task_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMPUTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopMPUTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMPUTaskResponseBody, self).to_map()
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


class StopMPUTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopMPUTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopMPUTaskResponse, self).to_map()
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
            temp_model = StopMPUTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRecordTaskRequest(TeaModel):
    def __init__(self, app_id=None, owner_id=None, task_id=None):
        self.app_id = app_id  # type: str
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRecordTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopRecordTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRecordTaskResponseBody, self).to_map()
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


class StopRecordTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopRecordTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopRecordTaskResponse, self).to_map()
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
            temp_model = StopRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoLiveStreamRuleRequest(TeaModel):
    def __init__(self, app_id=None, call_back=None, channel_id_prefixes=None, channel_ids=None, media_encode=None,
                 owner_id=None, play_domain=None, rule_id=None, rule_name=None):
        self.app_id = app_id  # type: str
        self.call_back = call_back  # type: str
        self.channel_id_prefixes = channel_id_prefixes  # type: list[str]
        self.channel_ids = channel_ids  # type: list[str]
        self.media_encode = media_encode  # type: int
        self.owner_id = owner_id  # type: long
        self.play_domain = play_domain  # type: str
        self.rule_id = rule_id  # type: int
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutoLiveStreamRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.channel_id_prefixes is not None:
            result['ChannelIdPrefixes'] = self.channel_id_prefixes
        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('ChannelIdPrefixes') is not None:
            self.channel_id_prefixes = m.get('ChannelIdPrefixes')
        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutoLiveStreamRuleResponseBody, self).to_map()
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


class UpdateAutoLiveStreamRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAutoLiveStreamRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAutoLiveStreamRuleResponse, self).to_map()
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
            temp_model = UpdateAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMPUTaskRequestBackgrounds(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMPUTaskRequestBackgrounds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateMPUTaskRequestClockWidgets(TeaModel):
    def __init__(self, alpha=None, border_color=None, border_width=None, box=None, box_border_width=None,
                 box_color=None, font_color=None, font_size=None, font_type=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.border_color = border_color  # type: long
        self.border_width = border_width  # type: int
        self.box = box  # type: bool
        self.box_border_width = box_border_width  # type: int
        self.box_color = box_color  # type: long
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMPUTaskRequestClockWidgets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.border_color is not None:
            result['BorderColor'] = self.border_color
        if self.border_width is not None:
            result['BorderWidth'] = self.border_width
        if self.box is not None:
            result['Box'] = self.box
        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width
        if self.box_color is not None:
            result['BoxColor'] = self.box_color
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')
        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')
        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateMPUTaskRequestUserPanesImages(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMPUTaskRequestUserPanesImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateMPUTaskRequestUserPanesTexts(TeaModel):
    def __init__(self, alpha=None, border_color=None, border_width=None, box=None, box_border_width=None,
                 box_color=None, font_color=None, font_size=None, font_type=None, text=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.border_color = border_color  # type: long
        self.border_width = border_width  # type: int
        self.box = box  # type: bool
        self.box_border_width = box_border_width  # type: int
        self.box_color = box_color  # type: long
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.text = text  # type: str
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMPUTaskRequestUserPanesTexts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.border_color is not None:
            result['BorderColor'] = self.border_color
        if self.border_width is not None:
            result['BorderWidth'] = self.border_width
        if self.box is not None:
            result['Box'] = self.box
        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width
        if self.box_color is not None:
            result['BoxColor'] = self.box_color
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.text is not None:
            result['Text'] = self.text
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')
        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')
        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateMPUTaskRequestUserPanes(TeaModel):
    def __init__(self, images=None, pane_id=None, segment_type=None, source_type=None, texts=None, user_id=None):
        self.images = images  # type: list[UpdateMPUTaskRequestUserPanesImages]
        self.pane_id = pane_id  # type: int
        self.segment_type = segment_type  # type: int
        self.source_type = source_type  # type: str
        self.texts = texts  # type: list[UpdateMPUTaskRequestUserPanesTexts]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateMPUTaskRequestUserPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.segment_type is not None:
            result['SegmentType'] = self.segment_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = UpdateMPUTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('SegmentType') is not None:
            self.segment_type = m.get('SegmentType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = UpdateMPUTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateMPUTaskRequestWatermarks(TeaModel):
    def __init__(self, alpha=None, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMPUTaskRequestWatermarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateMPUTaskRequest(TeaModel):
    def __init__(self, app_id=None, background_color=None, backgrounds=None, clock_widgets=None, crop_mode=None,
                 layout_ids=None, media_encode=None, mix_mode=None, owner_id=None, source_type=None, stream_type=None,
                 sub_spec_audio_users=None, sub_spec_camera_users=None, sub_spec_share_screen_users=None, sub_spec_users=None,
                 task_id=None, unsub_spec_audio_users=None, unsub_spec_camera_users=None,
                 unsub_spec_share_screen_users=None, user_panes=None, watermarks=None):
        self.app_id = app_id  # type: str
        self.background_color = background_color  # type: int
        self.backgrounds = backgrounds  # type: list[UpdateMPUTaskRequestBackgrounds]
        self.clock_widgets = clock_widgets  # type: list[UpdateMPUTaskRequestClockWidgets]
        self.crop_mode = crop_mode  # type: int
        self.layout_ids = layout_ids  # type: list[long]
        self.media_encode = media_encode  # type: int
        self.mix_mode = mix_mode  # type: int
        self.owner_id = owner_id  # type: long
        self.source_type = source_type  # type: str
        self.stream_type = stream_type  # type: int
        self.sub_spec_audio_users = sub_spec_audio_users  # type: list[str]
        self.sub_spec_camera_users = sub_spec_camera_users  # type: list[str]
        self.sub_spec_share_screen_users = sub_spec_share_screen_users  # type: list[str]
        self.sub_spec_users = sub_spec_users  # type: list[str]
        self.task_id = task_id  # type: str
        self.unsub_spec_audio_users = unsub_spec_audio_users  # type: list[str]
        self.unsub_spec_camera_users = unsub_spec_camera_users  # type: list[str]
        self.unsub_spec_share_screen_users = unsub_spec_share_screen_users  # type: list[str]
        self.user_panes = user_panes  # type: list[UpdateMPUTaskRequestUserPanes]
        self.watermarks = watermarks  # type: list[UpdateMPUTaskRequestWatermarks]

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateMPUTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.sub_spec_audio_users is not None:
            result['SubSpecAudioUsers'] = self.sub_spec_audio_users
        if self.sub_spec_camera_users is not None:
            result['SubSpecCameraUsers'] = self.sub_spec_camera_users
        if self.sub_spec_share_screen_users is not None:
            result['SubSpecShareScreenUsers'] = self.sub_spec_share_screen_users
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.unsub_spec_audio_users is not None:
            result['UnsubSpecAudioUsers'] = self.unsub_spec_audio_users
        if self.unsub_spec_camera_users is not None:
            result['UnsubSpecCameraUsers'] = self.unsub_spec_camera_users
        if self.unsub_spec_share_screen_users is not None:
            result['UnsubSpecShareScreenUsers'] = self.unsub_spec_share_screen_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = UpdateMPUTaskRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = UpdateMPUTaskRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('SubSpecAudioUsers') is not None:
            self.sub_spec_audio_users = m.get('SubSpecAudioUsers')
        if m.get('SubSpecCameraUsers') is not None:
            self.sub_spec_camera_users = m.get('SubSpecCameraUsers')
        if m.get('SubSpecShareScreenUsers') is not None:
            self.sub_spec_share_screen_users = m.get('SubSpecShareScreenUsers')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UnsubSpecAudioUsers') is not None:
            self.unsub_spec_audio_users = m.get('UnsubSpecAudioUsers')
        if m.get('UnsubSpecCameraUsers') is not None:
            self.unsub_spec_camera_users = m.get('UnsubSpecCameraUsers')
        if m.get('UnsubSpecShareScreenUsers') is not None:
            self.unsub_spec_share_screen_users = m.get('UnsubSpecShareScreenUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = UpdateMPUTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = UpdateMPUTaskRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class UpdateMPUTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMPUTaskResponseBody, self).to_map()
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


class UpdateMPUTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMPUTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMPUTaskResponse, self).to_map()
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
            temp_model = UpdateMPUTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordTaskRequestUserPanesImages(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordTaskRequestUserPanesImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateRecordTaskRequestUserPanesTexts(TeaModel):
    def __init__(self, font_color=None, font_size=None, font_type=None, text=None, x=None, y=None, zorder=None):
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.text = text  # type: str
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordTaskRequestUserPanesTexts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.text is not None:
            result['Text'] = self.text
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateRecordTaskRequestUserPanes(TeaModel):
    def __init__(self, images=None, pane_id=None, source_type=None, texts=None, user_id=None):
        self.images = images  # type: list[UpdateRecordTaskRequestUserPanesImages]
        self.pane_id = pane_id  # type: int
        self.source_type = source_type  # type: str
        self.texts = texts  # type: list[UpdateRecordTaskRequestUserPanesTexts]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateRecordTaskRequestUserPanes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = UpdateRecordTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = UpdateRecordTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateRecordTaskRequest(TeaModel):
    def __init__(self, app_id=None, channel_id=None, crop_mode=None, layout_ids=None, media_encode=None,
                 owner_id=None, sub_spec_audio_users=None, sub_spec_camera_users=None, sub_spec_share_screen_users=None,
                 sub_spec_users=None, task_id=None, task_profile=None, template_id=None, unsub_spec_audio_users=None,
                 unsub_spec_camera_users=None, unsub_spec_share_screen_users=None, user_panes=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.crop_mode = crop_mode  # type: long
        self.layout_ids = layout_ids  # type: list[long]
        self.media_encode = media_encode  # type: long
        self.owner_id = owner_id  # type: long
        self.sub_spec_audio_users = sub_spec_audio_users  # type: list[str]
        self.sub_spec_camera_users = sub_spec_camera_users  # type: list[str]
        self.sub_spec_share_screen_users = sub_spec_share_screen_users  # type: list[str]
        self.sub_spec_users = sub_spec_users  # type: list[str]
        self.task_id = task_id  # type: str
        self.task_profile = task_profile  # type: str
        self.template_id = template_id  # type: str
        self.unsub_spec_audio_users = unsub_spec_audio_users  # type: list[str]
        self.unsub_spec_camera_users = unsub_spec_camera_users  # type: list[str]
        self.unsub_spec_share_screen_users = unsub_spec_share_screen_users  # type: list[str]
        self.user_panes = user_panes  # type: list[UpdateRecordTaskRequestUserPanes]

    def validate(self):
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateRecordTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sub_spec_audio_users is not None:
            result['SubSpecAudioUsers'] = self.sub_spec_audio_users
        if self.sub_spec_camera_users is not None:
            result['SubSpecCameraUsers'] = self.sub_spec_camera_users
        if self.sub_spec_share_screen_users is not None:
            result['SubSpecShareScreenUsers'] = self.sub_spec_share_screen_users
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.unsub_spec_audio_users is not None:
            result['UnsubSpecAudioUsers'] = self.unsub_spec_audio_users
        if self.unsub_spec_camera_users is not None:
            result['UnsubSpecCameraUsers'] = self.unsub_spec_camera_users
        if self.unsub_spec_share_screen_users is not None:
            result['UnsubSpecShareScreenUsers'] = self.unsub_spec_share_screen_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubSpecAudioUsers') is not None:
            self.sub_spec_audio_users = m.get('SubSpecAudioUsers')
        if m.get('SubSpecCameraUsers') is not None:
            self.sub_spec_camera_users = m.get('SubSpecCameraUsers')
        if m.get('SubSpecShareScreenUsers') is not None:
            self.sub_spec_share_screen_users = m.get('SubSpecShareScreenUsers')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UnsubSpecAudioUsers') is not None:
            self.unsub_spec_audio_users = m.get('UnsubSpecAudioUsers')
        if m.get('UnsubSpecCameraUsers') is not None:
            self.unsub_spec_camera_users = m.get('UnsubSpecCameraUsers')
        if m.get('UnsubSpecShareScreenUsers') is not None:
            self.unsub_spec_share_screen_users = m.get('UnsubSpecShareScreenUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = UpdateRecordTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        return self


class UpdateRecordTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordTaskResponseBody, self).to_map()
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


class UpdateRecordTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRecordTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRecordTaskResponse, self).to_map()
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
            temp_model = UpdateRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordTemplateRequestBackgrounds(TeaModel):
    def __init__(self, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordTemplateRequestBackgrounds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateRecordTemplateRequestClockWidgets(TeaModel):
    def __init__(self, font_color=None, font_size=None, font_type=None, x=None, y=None, zorder=None):
        self.font_color = font_color  # type: int
        self.font_size = font_size  # type: int
        self.font_type = font_type  # type: int
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordTemplateRequestClockWidgets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateRecordTemplateRequestWatermarks(TeaModel):
    def __init__(self, alpha=None, display=None, height=None, url=None, width=None, x=None, y=None, zorder=None):
        self.alpha = alpha  # type: float
        self.display = display  # type: int
        self.height = height  # type: float
        self.url = url  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.zorder = zorder  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordTemplateRequestWatermarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateRecordTemplateRequest(TeaModel):
    def __init__(self, app_id=None, background_color=None, backgrounds=None, clock_widgets=None,
                 delay_stop_time=None, enable_m3u_8date_time=None, file_split_interval=None, formats=None, http_callback_url=None,
                 layout_ids=None, media_encode=None, mns_queue=None, name=None, oss_bucket=None, oss_endpoint=None,
                 oss_file_prefix=None, owner_id=None, task_profile=None, template_id=None, watermarks=None):
        self.app_id = app_id  # type: str
        self.background_color = background_color  # type: int
        self.backgrounds = backgrounds  # type: list[UpdateRecordTemplateRequestBackgrounds]
        self.clock_widgets = clock_widgets  # type: list[UpdateRecordTemplateRequestClockWidgets]
        self.delay_stop_time = delay_stop_time  # type: int
        self.enable_m3u_8date_time = enable_m3u_8date_time  # type: bool
        self.file_split_interval = file_split_interval  # type: int
        self.formats = formats  # type: list[str]
        self.http_callback_url = http_callback_url  # type: str
        self.layout_ids = layout_ids  # type: list[long]
        self.media_encode = media_encode  # type: int
        self.mns_queue = mns_queue  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.owner_id = owner_id  # type: long
        self.task_profile = task_profile  # type: str
        self.template_id = template_id  # type: str
        self.watermarks = watermarks  # type: list[UpdateRecordTemplateRequestWatermarks]

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateRecordTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time
        if self.enable_m3u_8date_time is not None:
            result['EnableM3u8DateTime'] = self.enable_m3u_8date_time
        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval
        if self.formats is not None:
            result['Formats'] = self.formats
        if self.http_callback_url is not None:
            result['HttpCallbackUrl'] = self.http_callback_url
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = UpdateRecordTemplateRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = UpdateRecordTemplateRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')
        if m.get('EnableM3u8DateTime') is not None:
            self.enable_m3u_8date_time = m.get('EnableM3u8DateTime')
        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        if m.get('HttpCallbackUrl') is not None:
            self.http_callback_url = m.get('HttpCallbackUrl')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = UpdateRecordTemplateRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class UpdateRecordTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateRecordTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRecordTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRecordTemplateResponse, self).to_map()
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
            temp_model = UpdateRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


