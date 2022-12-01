# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Alert(TeaModel):
    def __init__(self, body=None, subtitle=None, title=None):
        self.body = body  # type: str
        self.subtitle = subtitle  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Alert, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.subtitle is not None:
            result['subtitle'] = self.subtitle
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('subtitle') is not None:
            self.subtitle = m.get('subtitle')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class AndroidPayload(TeaModel):
    def __init__(self, body=None, display_type=None, extra=None):
        self.body = body  # type: Body
        self.display_type = display_type  # type: str
        self.extra = extra  # type: dict[str, any]

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AndroidPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.display_type is not None:
            result['displayType'] = self.display_type
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Body()
            self.body = temp_model.from_map(m['body'])
        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        return self


class Aps(TeaModel):
    def __init__(self, alert=None, badge=None, category=None, content_available=None, interruption_level=None,
                 sound=None):
        self.alert = alert  # type: Alert
        self.badge = badge  # type: int
        self.category = category  # type: str
        self.content_available = content_available  # type: int
        self.interruption_level = interruption_level  # type: str
        self.sound = sound  # type: str

    def validate(self):
        if self.alert:
            self.alert.validate()

    def to_map(self):
        _map = super(Aps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert is not None:
            result['alert'] = self.alert.to_map()
        if self.badge is not None:
            result['badge'] = self.badge
        if self.category is not None:
            result['category'] = self.category
        if self.content_available is not None:
            result['contentAvailable'] = self.content_available
        if self.interruption_level is not None:
            result['interruptionLevel'] = self.interruption_level
        if self.sound is not None:
            result['sound'] = self.sound
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alert') is not None:
            temp_model = Alert()
            self.alert = temp_model.from_map(m['alert'])
        if m.get('badge') is not None:
            self.badge = m.get('badge')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('contentAvailable') is not None:
            self.content_available = m.get('contentAvailable')
        if m.get('interruptionLevel') is not None:
            self.interruption_level = m.get('interruptionLevel')
        if m.get('sound') is not None:
            self.sound = m.get('sound')
        return self


class Body(TeaModel):
    def __init__(self, activity=None, after_open=None, badge=None, builder_id=None, custom=None, expand_image=None,
                 icon=None, img=None, large_icon=None, play_lights=None, play_sound=None, play_vibrate=None, sound=None,
                 text=None, title=None, url=None):
        self.activity = activity  # type: str
        self.after_open = after_open  # type: str
        self.badge = badge  # type: int
        self.builder_id = builder_id  # type: long
        self.custom = custom  # type: str
        self.expand_image = expand_image  # type: str
        self.icon = icon  # type: str
        self.img = img  # type: str
        self.large_icon = large_icon  # type: str
        self.play_lights = play_lights  # type: bool
        self.play_sound = play_sound  # type: bool
        self.play_vibrate = play_vibrate  # type: bool
        self.sound = sound  # type: str
        self.text = text  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Body, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity is not None:
            result['activity'] = self.activity
        if self.after_open is not None:
            result['afterOpen'] = self.after_open
        if self.badge is not None:
            result['badge'] = self.badge
        if self.builder_id is not None:
            result['builderId'] = self.builder_id
        if self.custom is not None:
            result['custom'] = self.custom
        if self.expand_image is not None:
            result['expandImage'] = self.expand_image
        if self.icon is not None:
            result['icon'] = self.icon
        if self.img is not None:
            result['img'] = self.img
        if self.large_icon is not None:
            result['largeIcon'] = self.large_icon
        if self.play_lights is not None:
            result['playLights'] = self.play_lights
        if self.play_sound is not None:
            result['playSound'] = self.play_sound
        if self.play_vibrate is not None:
            result['playVibrate'] = self.play_vibrate
        if self.sound is not None:
            result['sound'] = self.sound
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('activity') is not None:
            self.activity = m.get('activity')
        if m.get('afterOpen') is not None:
            self.after_open = m.get('afterOpen')
        if m.get('badge') is not None:
            self.badge = m.get('badge')
        if m.get('builderId') is not None:
            self.builder_id = m.get('builderId')
        if m.get('custom') is not None:
            self.custom = m.get('custom')
        if m.get('expandImage') is not None:
            self.expand_image = m.get('expandImage')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('img') is not None:
            self.img = m.get('img')
        if m.get('largeIcon') is not None:
            self.large_icon = m.get('largeIcon')
        if m.get('playLights') is not None:
            self.play_lights = m.get('playLights')
        if m.get('playSound') is not None:
            self.play_sound = m.get('playSound')
        if m.get('playVibrate') is not None:
            self.play_vibrate = m.get('playVibrate')
        if m.get('sound') is not None:
            self.sound = m.get('sound')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ChannelProperties(TeaModel):
    def __init__(self, channel_activity=None, main_activity=None, oppo_channel_id=None, vivo_classification=None,
                 xiaomi_channel_id=None):
        self.channel_activity = channel_activity  # type: str
        self.main_activity = main_activity  # type: str
        self.oppo_channel_id = oppo_channel_id  # type: str
        self.vivo_classification = vivo_classification  # type: str
        self.xiaomi_channel_id = xiaomi_channel_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChannelProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_activity is not None:
            result['channelActivity'] = self.channel_activity
        if self.main_activity is not None:
            result['mainActivity'] = self.main_activity
        if self.oppo_channel_id is not None:
            result['oppoChannelId'] = self.oppo_channel_id
        if self.vivo_classification is not None:
            result['vivoClassification'] = self.vivo_classification
        if self.xiaomi_channel_id is not None:
            result['xiaomiChannelId'] = self.xiaomi_channel_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('channelActivity') is not None:
            self.channel_activity = m.get('channelActivity')
        if m.get('mainActivity') is not None:
            self.main_activity = m.get('mainActivity')
        if m.get('oppoChannelId') is not None:
            self.oppo_channel_id = m.get('oppoChannelId')
        if m.get('vivoClassification') is not None:
            self.vivo_classification = m.get('vivoClassification')
        if m.get('xiaomiChannelId') is not None:
            self.xiaomi_channel_id = m.get('xiaomiChannelId')
        return self


class IosPayload(TeaModel):
    def __init__(self, aps=None, extra=None):
        self.aps = aps  # type: Aps
        self.extra = extra  # type: dict[str, any]

    def validate(self):
        if self.aps:
            self.aps.validate()

    def to_map(self):
        _map = super(IosPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aps is not None:
            result['aps'] = self.aps.to_map()
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aps') is not None:
            temp_model = Aps()
            self.aps = temp_model.from_map(m['aps'])
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        return self


class Policy(TeaModel):
    def __init__(self, expire_time=None, outer_biz_no=None, speed=None, start_time=None):
        self.expire_time = expire_time  # type: str
        self.outer_biz_no = outer_biz_no  # type: str
        self.speed = speed  # type: int
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Policy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.outer_biz_no is not None:
            result['outerBizNo'] = self.outer_biz_no
        if self.speed is not None:
            result['speed'] = self.speed
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('outerBizNo') is not None:
            self.outer_biz_no = m.get('outerBizNo')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class SendByAppRequest(TeaModel):
    def __init__(self, android_payload=None, channel_properties=None, description=None, ios_payload=None,
                 policy=None, production_mode=None, receipt_type=None, receipt_url=None):
        self.android_payload = android_payload  # type: AndroidPayload
        self.channel_properties = channel_properties  # type: ChannelProperties
        self.description = description  # type: str
        self.ios_payload = ios_payload  # type: IosPayload
        self.policy = policy  # type: Policy
        self.production_mode = production_mode  # type: bool
        self.receipt_type = receipt_type  # type: int
        self.receipt_url = receipt_url  # type: str

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(SendByAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByAppShrinkRequest(TeaModel):
    def __init__(self, android_payload_shrink=None, channel_properties_shrink=None, description=None,
                 ios_payload_shrink=None, policy_shrink=None, production_mode=None, receipt_type=None, receipt_url=None):
        self.android_payload_shrink = android_payload_shrink  # type: str
        self.channel_properties_shrink = channel_properties_shrink  # type: str
        self.description = description  # type: str
        self.ios_payload_shrink = ios_payload_shrink  # type: str
        self.policy_shrink = policy_shrink  # type: str
        self.production_mode = production_mode  # type: bool
        self.receipt_type = receipt_type  # type: int
        self.receipt_url = receipt_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendByAppShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByAppResponseBodyData(TeaModel):
    def __init__(self, msg_id=None):
        self.msg_id = msg_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendByAppResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByAppResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SendByAppResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendByAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendByAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendByAppResponse, self).to_map()
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
            temp_model = SendByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByDeviceRequest(TeaModel):
    def __init__(self, android_payload=None, channel_properties=None, description=None, device_tokens=None,
                 ios_payload=None, policy=None, production_mode=None, receipt_type=None, receipt_url=None):
        self.android_payload = android_payload  # type: AndroidPayload
        self.channel_properties = channel_properties  # type: ChannelProperties
        self.description = description  # type: str
        self.device_tokens = device_tokens  # type: str
        self.ios_payload = ios_payload  # type: IosPayload
        self.policy = policy  # type: Policy
        self.production_mode = production_mode  # type: bool
        self.receipt_type = receipt_type  # type: int
        self.receipt_url = receipt_url  # type: str

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(SendByDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByDeviceShrinkRequest(TeaModel):
    def __init__(self, android_payload_shrink=None, channel_properties_shrink=None, description=None,
                 device_tokens=None, ios_payload_shrink=None, policy_shrink=None, production_mode=None, receipt_type=None,
                 receipt_url=None):
        self.android_payload_shrink = android_payload_shrink  # type: str
        self.channel_properties_shrink = channel_properties_shrink  # type: str
        self.description = description  # type: str
        self.device_tokens = device_tokens  # type: str
        self.ios_payload_shrink = ios_payload_shrink  # type: str
        self.policy_shrink = policy_shrink  # type: str
        self.production_mode = production_mode  # type: bool
        self.receipt_type = receipt_type  # type: int
        self.receipt_url = receipt_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendByDeviceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class SendByDeviceResponseBodyData(TeaModel):
    def __init__(self, msg_id=None):
        self.msg_id = msg_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendByDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SendByDeviceResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendByDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendByDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendByDeviceResponse, self).to_map()
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
            temp_model = SendByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


