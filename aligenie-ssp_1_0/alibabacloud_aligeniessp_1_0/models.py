# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class LoginStateInfo(TeaModel):
    def __init__(self, scene_code=None, third_user_identifier=None, third_user_type=None, user_id=None):
        self.scene_code = scene_code  # type: str
        self.third_user_identifier = third_user_identifier  # type: str
        self.third_user_type = third_user_type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginStateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ResultValueDeviceUnionIds(TeaModel):
    def __init__(self, organization_id=None, device_union_id=None):
        self.organization_id = organization_id  # type: str
        self.device_union_id = device_union_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResultValueDeviceUnionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        return self


class ResultValue(TeaModel):
    def __init__(self, device_open_id=None, device_union_ids=None, name=None, firmware_version=None, mac=None,
                 sn=None):
        self.device_open_id = device_open_id  # type: str
        self.device_union_ids = device_union_ids  # type: list[ResultValueDeviceUnionIds]
        self.name = name  # type: str
        self.firmware_version = firmware_version  # type: str
        self.mac = mac  # type: str
        self.sn = sn  # type: str

    def validate(self):
        if self.device_union_ids:
            for k in self.device_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ResultValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = ResultValueDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class AddAndRemoveFavoriteContentHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddAndRemoveFavoriteContentRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair(TeaModel):
    def __init__(self, extend_info=None, raw_id=None, source=None):
        self.extend_info = extend_info  # type: dict[str, any]
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest(TeaModel):
    def __init__(self, favorite_cmd=None, open_source_raw_id_pair=None, package_type=None):
        self.favorite_cmd = favorite_cmd  # type: str
        self.open_source_raw_id_pair = open_source_raw_id_pair  # type: AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair
        self.package_type = package_type  # type: str

    def validate(self):
        if self.open_source_raw_id_pair:
            self.open_source_raw_id_pair.validate()

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite_cmd is not None:
            result['FavoriteCmd'] = self.favorite_cmd
        if self.open_source_raw_id_pair is not None:
            result['OpenSourceRawIdPair'] = self.open_source_raw_id_pair.to_map()
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FavoriteCmd') is not None:
            self.favorite_cmd = m.get('FavoriteCmd')
        if m.get('OpenSourceRawIdPair') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair()
            self.open_source_raw_id_pair = temp_model.from_map(m['OpenSourceRawIdPair'])
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        return self


class AddAndRemoveFavoriteContentRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AddAndRemoveFavoriteContentRequest(TeaModel):
    def __init__(self, device_info=None, open_add_and_remove_favorite_content_request=None, user_info=None):
        self.device_info = device_info  # type: AddAndRemoveFavoriteContentRequestDeviceInfo
        self.open_add_and_remove_favorite_content_request = open_add_and_remove_favorite_content_request  # type: AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest
        self.user_info = user_info  # type: AddAndRemoveFavoriteContentRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_add_and_remove_favorite_content_request:
            self.open_add_and_remove_favorite_content_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_add_and_remove_favorite_content_request is not None:
            result['OpenAddAndRemoveFavoriteContentRequest'] = self.open_add_and_remove_favorite_content_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenAddAndRemoveFavoriteContentRequest') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest()
            self.open_add_and_remove_favorite_content_request = temp_model.from_map(m['OpenAddAndRemoveFavoriteContentRequest'])
        if m.get('UserInfo') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class AddAndRemoveFavoriteContentShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_add_and_remove_favorite_content_request_shrink=None,
                 user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_add_and_remove_favorite_content_request_shrink = open_add_and_remove_favorite_content_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_add_and_remove_favorite_content_request_shrink is not None:
            result['OpenAddAndRemoveFavoriteContentRequest'] = self.open_add_and_remove_favorite_content_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenAddAndRemoveFavoriteContentRequest') is not None:
            self.open_add_and_remove_favorite_content_request_shrink = m.get('OpenAddAndRemoveFavoriteContentRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class AddAndRemoveFavoriteContentResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAndRemoveFavoriteContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAndRemoveFavoriteContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAndRemoveFavoriteContentResponse, self).to_map()
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
            temp_model = AddAndRemoveFavoriteContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSubHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddSubRequestAddSubscriptionInfoRequestScheduleInfo(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubRequestAddSubscriptionInfoRequestScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class AddSubRequestAddSubscriptionInfoRequest(TeaModel):
    def __init__(self, album_id=None, daily_study_cnt=None, play_mode=None, schedule_info=None):
        self.album_id = album_id  # type: str
        self.daily_study_cnt = daily_study_cnt  # type: int
        self.play_mode = play_mode  # type: str
        self.schedule_info = schedule_info  # type: AddSubRequestAddSubscriptionInfoRequestScheduleInfo

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(AddSubRequestAddSubscriptionInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.daily_study_cnt is not None:
            result['DailyStudyCnt'] = self.daily_study_cnt
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('ScheduleInfo') is not None:
            temp_model = AddSubRequestAddSubscriptionInfoRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        return self


class AddSubRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AddSubRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AddSubRequest(TeaModel):
    def __init__(self, add_subscription_info_request=None, device_info=None, user_info=None):
        self.add_subscription_info_request = add_subscription_info_request  # type: AddSubRequestAddSubscriptionInfoRequest
        self.device_info = device_info  # type: AddSubRequestDeviceInfo
        self.user_info = user_info  # type: AddSubRequestUserInfo

    def validate(self):
        if self.add_subscription_info_request:
            self.add_subscription_info_request.validate()
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(AddSubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_subscription_info_request is not None:
            result['AddSubscriptionInfoRequest'] = self.add_subscription_info_request.to_map()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddSubscriptionInfoRequest') is not None:
            temp_model = AddSubRequestAddSubscriptionInfoRequest()
            self.add_subscription_info_request = temp_model.from_map(m['AddSubscriptionInfoRequest'])
        if m.get('DeviceInfo') is not None:
            temp_model = AddSubRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = AddSubRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class AddSubShrinkRequest(TeaModel):
    def __init__(self, add_subscription_info_request_shrink=None, device_info_shrink=None, user_info_shrink=None):
        self.add_subscription_info_request_shrink = add_subscription_info_request_shrink  # type: str
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_subscription_info_request_shrink is not None:
            result['AddSubscriptionInfoRequest'] = self.add_subscription_info_request_shrink
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddSubscriptionInfoRequest') is not None:
            self.add_subscription_info_request_shrink = m.get('AddSubscriptionInfoRequest')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class AddSubResponseBodyResultScheduleInfo(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSubResponseBodyResultScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class AddSubResponseBodyResult(TeaModel):
    def __init__(self, album_id=None, daily_study_cnt=None, device_id=None, id=None, play_mode=None,
                 schedule_info=None, user_id=None):
        self.album_id = album_id  # type: str
        self.daily_study_cnt = daily_study_cnt  # type: int
        self.device_id = device_id  # type: str
        self.id = id  # type: long
        self.play_mode = play_mode  # type: str
        self.schedule_info = schedule_info  # type: AddSubResponseBodyResultScheduleInfo
        self.user_id = user_id  # type: str

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(AddSubResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.daily_study_cnt is not None:
            result['DailyStudyCnt'] = self.daily_study_cnt
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('ScheduleInfo') is not None:
            temp_model = AddSubResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddSubResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AddSubResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AddSubResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddSubResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class AddSubResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddSubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSubResponse, self).to_map()
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
            temp_model = AddSubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithAligenieUserInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AuthLoginWithAligenieUserInfoRequest(TeaModel):
    def __init__(self, encrypted_aligenie_user_identifier=None, session_id=None):
        self.encrypted_aligenie_user_identifier = encrypted_aligenie_user_identifier  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_aligenie_user_identifier is not None:
            result['EncryptedAligenieUserIdentifier'] = self.encrypted_aligenie_user_identifier
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptedAligenieUserIdentifier') is not None:
            self.encrypted_aligenie_user_identifier = m.get('EncryptedAligenieUserIdentifier')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithAligenieUserInfoResponseBodyResult(TeaModel):
    def __init__(self, expired_time_long=None, login_state_access_token=None):
        self.expired_time_long = expired_time_long  # type: long
        self.login_state_access_token = login_state_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithAligenieUserInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AuthLoginWithAligenieUserInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AuthLoginWithAligenieUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithAligenieUserInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthLoginWithAligenieUserInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoResponse, self).to_map()
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
            temp_model = AuthLoginWithAligenieUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberRequest(TeaModel):
    def __init__(self, session_id=None):
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBodyResult(TeaModel):
    def __init__(self, expired_time_long=None, login_state_access_token=None):
        self.expired_time_long = expired_time_long  # type: long
        self.login_state_access_token = login_state_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse, self).to_map()
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
            temp_model = AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithTaobaoUserInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithTaobaoUserInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AuthLoginWithTaobaoUserInfoRequest(TeaModel):
    def __init__(self, encrypted_taobao_user_identifier=None, session_id=None):
        self.encrypted_taobao_user_identifier = encrypted_taobao_user_identifier  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithTaobaoUserInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_taobao_user_identifier is not None:
            result['EncryptedTaobaoUserIdentifier'] = self.encrypted_taobao_user_identifier
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptedTaobaoUserIdentifier') is not None:
            self.encrypted_taobao_user_identifier = m.get('EncryptedTaobaoUserIdentifier')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithTaobaoUserInfoResponseBodyResult(TeaModel):
    def __init__(self, expired_time_long=None, login_state_access_token=None):
        self.expired_time_long = expired_time_long  # type: long
        self.login_state_access_token = login_state_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithTaobaoUserInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithTaobaoUserInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AuthLoginWithTaobaoUserInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AuthLoginWithTaobaoUserInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AuthLoginWithTaobaoUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithTaobaoUserInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthLoginWithTaobaoUserInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthLoginWithTaobaoUserInfoResponse, self).to_map()
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
            temp_model = AuthLoginWithTaobaoUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithThirdUserInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithThirdUserInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AuthLoginWithThirdUserInfoRequest(TeaModel):
    def __init__(self, ext_info=None, scene_code=None, third_user_identifier=None, third_user_type=None):
        self.ext_info = ext_info  # type: dict[str, any]
        self.scene_code = scene_code  # type: str
        self.third_user_identifier = third_user_identifier  # type: str
        self.third_user_type = third_user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithThirdUserInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        return self


class AuthLoginWithThirdUserInfoShrinkRequest(TeaModel):
    def __init__(self, ext_info_shrink=None, scene_code=None, third_user_identifier=None, third_user_type=None):
        self.ext_info_shrink = ext_info_shrink  # type: str
        self.scene_code = scene_code  # type: str
        self.third_user_identifier = third_user_identifier  # type: str
        self.third_user_type = third_user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithThirdUserInfoShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info_shrink is not None:
            result['ExtInfo'] = self.ext_info_shrink
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info_shrink = m.get('ExtInfo')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        return self


class AuthLoginWithThirdUserInfoResponseBodyDataObj(TeaModel):
    def __init__(self, session_id=None):
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithThirdUserInfoResponseBodyDataObj, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithThirdUserInfoResponseBodyResult(TeaModel):
    def __init__(self, expired_time_long=None, login_state_access_token=None):
        self.expired_time_long = expired_time_long  # type: long
        self.login_state_access_token = login_state_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthLoginWithThirdUserInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithThirdUserInfoResponseBody(TeaModel):
    def __init__(self, code=None, data_obj=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.data_obj = data_obj  # type: AuthLoginWithThirdUserInfoResponseBodyDataObj
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AuthLoginWithThirdUserInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.data_obj:
            self.data_obj.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AuthLoginWithThirdUserInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data_obj is not None:
            result['DataObj'] = self.data_obj.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataObj') is not None:
            temp_model = AuthLoginWithThirdUserInfoResponseBodyDataObj()
            self.data_obj = temp_model.from_map(m['DataObj'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AuthLoginWithThirdUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithThirdUserInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthLoginWithThirdUserInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthLoginWithThirdUserInfoResponse, self).to_map()
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
            temp_model = AuthLoginWithThirdUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAndDoVoipCallForHotelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CheckAndDoVoipCallForHotelRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CheckAndDoVoipCallForHotelRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CheckAndDoVoipCallForHotelRequest(TeaModel):
    def __init__(self, biz_data=None, callee_nick=None, callee_phone_num=None, device_info=None, user_info=None):
        self.biz_data = biz_data  # type: str
        self.callee_nick = callee_nick  # type: str
        self.callee_phone_num = callee_phone_num  # type: str
        self.device_info = device_info  # type: CheckAndDoVoipCallForHotelRequestDeviceInfo
        self.user_info = user_info  # type: CheckAndDoVoipCallForHotelRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.callee_nick is not None:
            result['CalleeNick'] = self.callee_nick
        if self.callee_phone_num is not None:
            result['CalleePhoneNum'] = self.callee_phone_num
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('CalleeNick') is not None:
            self.callee_nick = m.get('CalleeNick')
        if m.get('CalleePhoneNum') is not None:
            self.callee_phone_num = m.get('CalleePhoneNum')
        if m.get('DeviceInfo') is not None:
            temp_model = CheckAndDoVoipCallForHotelRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = CheckAndDoVoipCallForHotelRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CheckAndDoVoipCallForHotelShrinkRequest(TeaModel):
    def __init__(self, biz_data=None, callee_nick=None, callee_phone_num=None, device_info_shrink=None,
                 user_info_shrink=None):
        self.biz_data = biz_data  # type: str
        self.callee_nick = callee_nick  # type: str
        self.callee_phone_num = callee_phone_num  # type: str
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.callee_nick is not None:
            result['CalleeNick'] = self.callee_nick
        if self.callee_phone_num is not None:
            result['CalleePhoneNum'] = self.callee_phone_num
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('CalleeNick') is not None:
            self.callee_nick = m.get('CalleeNick')
        if m.get('CalleePhoneNum') is not None:
            self.callee_phone_num = m.get('CalleePhoneNum')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData(TeaModel):
    def __init__(self, device_icon=None, device_name=None, device_type=None, online=None, uuid=None):
        self.device_icon = device_icon  # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: str
        self.online = online  # type: bool
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_icon is not None:
            result['DeviceIcon'] = self.device_icon
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.online is not None:
            result['Online'] = self.online
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceIcon') is not None:
            self.device_icon = m.get('DeviceIcon')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: int
        self.data = data  # type: list[CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData]
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult(TeaModel):
    def __init__(self, message=None, ret_code=None, ret_value=None, success=None, trace_id=None):
        self.message = message  # type: str
        self.ret_code = ret_code  # type: int
        self.ret_value = ret_value  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResult(TeaModel):
    def __init__(self, device_targets=None, is_start_call=None, passed=None, start_call_result=None):
        self.device_targets = device_targets  # type: CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets
        self.is_start_call = is_start_call  # type: bool
        self.passed = passed  # type: bool
        self.start_call_result = start_call_result  # type: CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult

    def validate(self):
        if self.device_targets:
            self.device_targets.validate()
        if self.start_call_result:
            self.start_call_result.validate()

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_targets is not None:
            result['DeviceTargets'] = self.device_targets.to_map()
        if self.is_start_call is not None:
            result['IsStartCall'] = self.is_start_call
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.start_call_result is not None:
            result['StartCallResult'] = self.start_call_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceTargets') is not None:
            temp_model = CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets()
            self.device_targets = temp_model.from_map(m['DeviceTargets'])
        if m.get('IsStartCall') is not None:
            self.is_start_call = m.get('IsStartCall')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('StartCallResult') is not None:
            temp_model = CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult()
            self.start_call_result = temp_model.from_map(m['StartCallResult'])
        return self


class CheckAndDoVoipCallForHotelResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CheckAndDoVoipCallForHotelResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CheckAndDoVoipCallForHotelResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckAndDoVoipCallForHotelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckAndDoVoipCallForHotelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckAndDoVoipCallForHotelResponse, self).to_map()
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
            temp_model = CheckAndDoVoipCallForHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAuthCodeBindForExtHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CheckAuthCodeBindForExtRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CheckAuthCodeBindForExtRequest(TeaModel):
    def __init__(self, auth_code=None, encode_key=None, encode_type=None, user_info=None):
        self.auth_code = auth_code  # type: str
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.user_info = user_info  # type: CheckAuthCodeBindForExtRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('UserInfo') is not None:
            temp_model = CheckAuthCodeBindForExtRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CheckAuthCodeBindForExtShrinkRequest(TeaModel):
    def __init__(self, auth_code=None, encode_key=None, encode_type=None, user_info_shrink=None):
        self.auth_code = auth_code  # type: str
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo(TeaModel):
    def __init__(self, id=None, id_type=None):
        self.id = id  # type: str
        # DEVICE_ID
        self.id_type = id_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo(TeaModel):
    def __init__(self, id=None, id_type=None):
        self.id = id  # type: str
        # USER_ID
        self.id_type = id_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class CheckAuthCodeBindForExtResponseBodyResult(TeaModel):
    def __init__(self, device_open_info=None, user_open_info=None):
        self.device_open_info = device_open_info  # type: CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo
        self.user_open_info = user_open_info  # type: CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo

    def validate(self):
        if self.device_open_info:
            self.device_open_info.validate()
        if self.user_open_info:
            self.user_open_info.validate()

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_info is not None:
            result['DeviceOpenInfo'] = self.device_open_info.to_map()
        if self.user_open_info is not None:
            result['UserOpenInfo'] = self.user_open_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceOpenInfo') is not None:
            temp_model = CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo()
            self.device_open_info = temp_model.from_map(m['DeviceOpenInfo'])
        if m.get('UserOpenInfo') is not None:
            temp_model = CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo()
            self.user_open_info = temp_model.from_map(m['UserOpenInfo'])
        return self


class CheckAuthCodeBindForExtResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CheckAuthCodeBindForExtResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CheckAuthCodeBindForExtResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckAuthCodeBindForExtResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckAuthCodeBindForExtResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckAuthCodeBindForExtResponse, self).to_map()
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
            temp_model = CheckAuthCodeBindForExtResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloudPlayerHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloudPlayerHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CloudPlayerRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloudPlayerRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CloudPlayerRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloudPlayerRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CloudPlayerRequest(TeaModel):
    def __init__(self, cur_play_index=None, device_info=None, play_mode=None, song_id=None, song_id_list=None,
                 source=None, user_info=None):
        self.cur_play_index = cur_play_index  # type: int
        self.device_info = device_info  # type: CloudPlayerRequestDeviceInfo
        self.play_mode = play_mode  # type: str
        self.song_id = song_id  # type: str
        self.song_id_list = song_id_list  # type: list[str]
        self.source = source  # type: str
        self.user_info = user_info  # type: CloudPlayerRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CloudPlayerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_play_index is not None:
            result['CurPlayIndex'] = self.cur_play_index
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.song_id is not None:
            result['SongId'] = self.song_id
        if self.song_id_list is not None:
            result['SongIdList'] = self.song_id_list
        if self.source is not None:
            result['Source'] = self.source
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurPlayIndex') is not None:
            self.cur_play_index = m.get('CurPlayIndex')
        if m.get('DeviceInfo') is not None:
            temp_model = CloudPlayerRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('SongId') is not None:
            self.song_id = m.get('SongId')
        if m.get('SongIdList') is not None:
            self.song_id_list = m.get('SongIdList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserInfo') is not None:
            temp_model = CloudPlayerRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CloudPlayerShrinkRequest(TeaModel):
    def __init__(self, cur_play_index=None, device_info_shrink=None, play_mode=None, song_id=None,
                 song_id_list_shrink=None, source=None, user_info_shrink=None):
        self.cur_play_index = cur_play_index  # type: int
        self.device_info_shrink = device_info_shrink  # type: str
        self.play_mode = play_mode  # type: str
        self.song_id = song_id  # type: str
        self.song_id_list_shrink = song_id_list_shrink  # type: str
        self.source = source  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloudPlayerShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_play_index is not None:
            result['CurPlayIndex'] = self.cur_play_index
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.song_id is not None:
            result['SongId'] = self.song_id
        if self.song_id_list_shrink is not None:
            result['SongIdList'] = self.song_id_list_shrink
        if self.source is not None:
            result['Source'] = self.source
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurPlayIndex') is not None:
            self.cur_play_index = m.get('CurPlayIndex')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('SongId') is not None:
            self.song_id = m.get('SongId')
        if m.get('SongIdList') is not None:
            self.song_id_list_shrink = m.get('SongIdList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CloudPlayerResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloudPlayerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CloudPlayerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloudPlayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloudPlayerResponse, self).to_map()
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
            temp_model = CloudPlayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateAlarmRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateAlarmRequestPayloadMusicInfo(TeaModel):
    def __init__(self, music_id=None, music_name=None, music_type=None, music_type_name=None, music_url=None):
        self.music_id = music_id  # type: long
        self.music_name = music_name  # type: str
        self.music_type = music_type  # type: long
        self.music_type_name = music_type_name  # type: str
        self.music_url = music_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRequestPayloadMusicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class CreateAlarmRequestPayloadScheduleInfoOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRequestPayloadScheduleInfoOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(self, hour=None, minute=None):
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class CreateAlarmRequestPayloadScheduleInfoWeekly(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRequestPayloadScheduleInfoWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class CreateAlarmRequestPayloadScheduleInfo(TeaModel):
    def __init__(self, once=None, statutory_working_day=None, type=None, weekly=None):
        self.once = once  # type: CreateAlarmRequestPayloadScheduleInfoOnce
        self.statutory_working_day = statutory_working_day  # type: CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay
        self.type = type  # type: str
        self.weekly = weekly  # type: CreateAlarmRequestPayloadScheduleInfoWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(CreateAlarmRequestPayloadScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class CreateAlarmRequestPayload(TeaModel):
    def __init__(self, music_info=None, schedule_info=None, volume=None):
        self.music_info = music_info  # type: CreateAlarmRequestPayloadMusicInfo
        self.schedule_info = schedule_info  # type: CreateAlarmRequestPayloadScheduleInfo
        self.volume = volume  # type: int

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(CreateAlarmRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MusicInfo') is not None:
            temp_model = CreateAlarmRequestPayloadMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class CreateAlarmRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateAlarmRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: CreateAlarmRequestDeviceInfo
        self.payload = payload  # type: CreateAlarmRequestPayload
        self.user_info = user_info  # type: CreateAlarmRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CreateAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreateAlarmRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = CreateAlarmRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = CreateAlarmRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreateAlarmShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreateAlarmResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateAlarmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlarmResponse, self).to_map()
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
            temp_model = CreateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePlayingListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlayingListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreatePlayingListRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlayingListRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreatePlayingListRequestOpenCreatePlayingListRequestContentList(TeaModel):
    def __init__(self, raw_id=None, source=None):
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlayingListRequestOpenCreatePlayingListRequestContentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreatePlayingListRequestOpenCreatePlayingListRequest(TeaModel):
    def __init__(self, content_list=None, content_type=None, extend_info=None, index=None,
                 need_album_continued=None, play_from=None, play_mode=None):
        self.content_list = content_list  # type: list[CreatePlayingListRequestOpenCreatePlayingListRequestContentList]
        self.content_type = content_type  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.index = index  # type: int
        self.need_album_continued = need_album_continued  # type: bool
        self.play_from = play_from  # type: str
        self.play_mode = play_mode  # type: str

    def validate(self):
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePlayingListRequestOpenCreatePlayingListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContentList'] = []
        if self.content_list is not None:
            for k in self.content_list:
                result['ContentList'].append(k.to_map() if k else None)
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.index is not None:
            result['Index'] = self.index
        if self.need_album_continued is not None:
            result['NeedAlbumContinued'] = self.need_album_continued
        if self.play_from is not None:
            result['PlayFrom'] = self.play_from
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.content_list = []
        if m.get('ContentList') is not None:
            for k in m.get('ContentList'):
                temp_model = CreatePlayingListRequestOpenCreatePlayingListRequestContentList()
                self.content_list.append(temp_model.from_map(k))
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('NeedAlbumContinued') is not None:
            self.need_album_continued = m.get('NeedAlbumContinued')
        if m.get('PlayFrom') is not None:
            self.play_from = m.get('PlayFrom')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        return self


class CreatePlayingListRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlayingListRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreatePlayingListRequest(TeaModel):
    def __init__(self, device_info=None, open_create_playing_list_request=None, user_info=None):
        self.device_info = device_info  # type: CreatePlayingListRequestDeviceInfo
        self.open_create_playing_list_request = open_create_playing_list_request  # type: CreatePlayingListRequestOpenCreatePlayingListRequest
        self.user_info = user_info  # type: CreatePlayingListRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_create_playing_list_request:
            self.open_create_playing_list_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CreatePlayingListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_create_playing_list_request is not None:
            result['OpenCreatePlayingListRequest'] = self.open_create_playing_list_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreatePlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenCreatePlayingListRequest') is not None:
            temp_model = CreatePlayingListRequestOpenCreatePlayingListRequest()
            self.open_create_playing_list_request = temp_model.from_map(m['OpenCreatePlayingListRequest'])
        if m.get('UserInfo') is not None:
            temp_model = CreatePlayingListRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreatePlayingListShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_create_playing_list_request_shrink=None,
                 user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_create_playing_list_request_shrink = open_create_playing_list_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlayingListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_create_playing_list_request_shrink is not None:
            result['OpenCreatePlayingListRequest'] = self.open_create_playing_list_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenCreatePlayingListRequest') is not None:
            self.open_create_playing_list_request_shrink = m.get('OpenCreatePlayingListRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreatePlayingListResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePlayingListResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class CreatePlayingListResponseBodyResult(TeaModel):
    def __init__(self, album_name=None, album_raw_id=None, audio_length=None, copyright=None, cover=None,
                 default_play_order=None, item_url=None, liked=None, lyric_url=None, play_mode=None, pos=None, progress=None,
                 raw_id=None, singer=None, source=None, title=None, type=None, valid=None):
        self.album_name = album_name  # type: str
        self.album_raw_id = album_raw_id  # type: str
        self.audio_length = audio_length  # type: int
        self.copyright = copyright  # type: int
        self.cover = cover  # type: CreatePlayingListResponseBodyResultCover
        self.default_play_order = default_play_order  # type: int
        self.item_url = item_url  # type: str
        self.liked = liked  # type: bool
        self.lyric_url = lyric_url  # type: str
        self.play_mode = play_mode  # type: str
        self.pos = pos  # type: int
        self.progress = progress  # type: int
        self.raw_id = raw_id  # type: str
        self.singer = singer  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(CreatePlayingListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = CreatePlayingListResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class CreatePlayingListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreatePlayingListResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreatePlayingListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreatePlayingListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePlayingListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePlayingListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePlayingListResponse, self).to_map()
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
            temp_model = CreatePlayingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduleTaskHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateScheduleTaskRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateScheduleTaskRequestPayloadActionDTOs(TeaModel):
    def __init__(self, custom_action=None):
        self.custom_action = custom_action  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskRequestPayloadActionDTOs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_action is not None:
            result['customAction'] = self.custom_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('customAction') is not None:
            self.custom_action = m.get('customAction')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTOOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskRequestPayloadScheduleDTOOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay(TeaModel):
    def __init__(self, hours=None, minutes=None):
        self.hours = hours  # type: list[int]
        self.minutes = minutes  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hours is not None:
            result['Hours'] = self.hours
        if self.minutes is not None:
            result['Minutes'] = self.minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hours') is not None:
            self.hours = m.get('Hours')
        if m.get('Minutes') is not None:
            self.minutes = m.get('Minutes')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTOWeekly(TeaModel):
    def __init__(self, days_of_week=None, hours=None, minutes=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hours = hours  # type: list[int]
        self.minutes = minutes  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskRequestPayloadScheduleDTOWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hours is not None:
            result['Hours'] = self.hours
        if self.minutes is not None:
            result['Minutes'] = self.minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hours') is not None:
            self.hours = m.get('Hours')
        if m.get('Minutes') is not None:
            self.minutes = m.get('Minutes')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTO(TeaModel):
    def __init__(self, once=None, schedule_end_time=None, schedule_start_time=None, schedule_type=None,
                 statutory_working_day=None, weekly=None):
        self.once = once  # type: CreateScheduleTaskRequestPayloadScheduleDTOOnce
        self.schedule_end_time = schedule_end_time  # type: long
        self.schedule_start_time = schedule_start_time  # type: long
        self.schedule_type = schedule_type  # type: str
        self.statutory_working_day = statutory_working_day  # type: CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay
        self.weekly = weekly  # type: CreateScheduleTaskRequestPayloadScheduleDTOWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(CreateScheduleTaskRequestPayloadScheduleDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.schedule_end_time is not None:
            result['ScheduleEndTime'] = self.schedule_end_time
        if self.schedule_start_time is not None:
            result['ScheduleStartTime'] = self.schedule_start_time
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTOOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('ScheduleEndTime') is not None:
            self.schedule_end_time = m.get('ScheduleEndTime')
        if m.get('ScheduleStartTime') is not None:
            self.schedule_start_time = m.get('ScheduleStartTime')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Weekly') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTOWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class CreateScheduleTaskRequestPayload(TeaModel):
    def __init__(self, action_dtos=None, idempotent_id=None, schedule_dto=None):
        self.action_dtos = action_dtos  # type: list[CreateScheduleTaskRequestPayloadActionDTOs]
        self.idempotent_id = idempotent_id  # type: str
        self.schedule_dto = schedule_dto  # type: CreateScheduleTaskRequestPayloadScheduleDTO

    def validate(self):
        if self.action_dtos:
            for k in self.action_dtos:
                if k:
                    k.validate()
        if self.schedule_dto:
            self.schedule_dto.validate()

    def to_map(self):
        _map = super(CreateScheduleTaskRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActionDTOs'] = []
        if self.action_dtos is not None:
            for k in self.action_dtos:
                result['ActionDTOs'].append(k.to_map() if k else None)
        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id
        if self.schedule_dto is not None:
            result['ScheduleDTO'] = self.schedule_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.action_dtos = []
        if m.get('ActionDTOs') is not None:
            for k in m.get('ActionDTOs'):
                temp_model = CreateScheduleTaskRequestPayloadActionDTOs()
                self.action_dtos.append(temp_model.from_map(k))
        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')
        if m.get('ScheduleDTO') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTO()
            self.schedule_dto = temp_model.from_map(m['ScheduleDTO'])
        return self


class CreateScheduleTaskRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateScheduleTaskRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: CreateScheduleTaskRequestDeviceInfo
        self.payload = payload  # type: CreateScheduleTaskRequestPayload
        self.user_info = user_info  # type: CreateScheduleTaskRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CreateScheduleTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreateScheduleTaskRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = CreateScheduleTaskRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = CreateScheduleTaskRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreateScheduleTaskShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreateScheduleTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateScheduleTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateScheduleTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateScheduleTaskResponse, self).to_map()
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
            temp_model = CreateScheduleTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteAlarmsRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmsRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteAlarmsRequestPayload(TeaModel):
    def __init__(self, alarm_ids=None):
        self.alarm_ids = alarm_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmsRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_ids is not None:
            result['AlarmIds'] = self.alarm_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmIds') is not None:
            self.alarm_ids = m.get('AlarmIds')
        return self


class DeleteAlarmsRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmsRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteAlarmsRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: DeleteAlarmsRequestDeviceInfo
        self.payload = payload  # type: DeleteAlarmsRequestPayload
        self.user_info = user_info  # type: DeleteAlarmsRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(DeleteAlarmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = DeleteAlarmsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = DeleteAlarmsRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeleteAlarmsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeleteAlarmsShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeleteAlarmsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteAlarmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlarmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlarmsResponse, self).to_map()
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
            temp_model = DeleteAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduleTaskHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleTaskHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteScheduleTaskRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleTaskRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteScheduleTaskRequestPayload(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleTaskRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteScheduleTaskRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleTaskRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteScheduleTaskRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: DeleteScheduleTaskRequestDeviceInfo
        self.payload = payload  # type: DeleteScheduleTaskRequestPayload
        self.user_info = user_info  # type: DeleteScheduleTaskRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(DeleteScheduleTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = DeleteScheduleTaskRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = DeleteScheduleTaskRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeleteScheduleTaskRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeleteScheduleTaskShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeleteScheduleTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteScheduleTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteScheduleTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteScheduleTaskResponse, self).to_map()
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
            temp_model = DeleteScheduleTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteSubRequest(TeaModel):
    def __init__(self, sub_id=None):
        self.sub_id = sub_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_id is not None:
            result['SubId'] = self.sub_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')
        return self


class DeleteSubResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteSubResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSubResponse, self).to_map()
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
            temp_model = DeleteSubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeviceControlHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeviceControlRequestControlRequest(TeaModel):
    def __init__(self, muted=None, volume=None):
        self.muted = muted  # type: bool
        self.volume = volume  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlRequestControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.muted is not None:
            result['Muted'] = self.muted
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Muted') is not None:
            self.muted = m.get('Muted')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class DeviceControlRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeviceControlRequest(TeaModel):
    def __init__(self, control_request=None, device_info=None):
        self.control_request = control_request  # type: DeviceControlRequestControlRequest
        self.device_info = device_info  # type: DeviceControlRequestDeviceInfo

    def validate(self):
        if self.control_request:
            self.control_request.validate()
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(DeviceControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_request is not None:
            result['ControlRequest'] = self.control_request.to_map()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlRequest') is not None:
            temp_model = DeviceControlRequestControlRequest()
            self.control_request = temp_model.from_map(m['ControlRequest'])
        if m.get('DeviceInfo') is not None:
            temp_model = DeviceControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class DeviceControlShrinkRequest(TeaModel):
    def __init__(self, control_request_shrink=None, device_info_shrink=None):
        self.control_request_shrink = control_request_shrink  # type: str
        self.device_info_shrink = device_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_request_shrink is not None:
            result['ControlRequest'] = self.control_request_shrink
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlRequest') is not None:
            self.control_request_shrink = m.get('ControlRequest')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class DeviceControlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeviceControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeviceControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeviceControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeviceControlResponse, self).to_map()
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
            temp_model = DeviceControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EcologyOpennessAuthenticateHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcologyOpennessAuthenticateHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class EcologyOpennessAuthenticateRequest(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, login_state_access_token=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.login_state_access_token = login_state_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcologyOpennessAuthenticateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class EcologyOpennessAuthenticateResponseBodyResult(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, scene_code=None, third_user_identifier=None,
                 third_user_type=None, user_open_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.scene_code = scene_code  # type: str
        self.third_user_identifier = third_user_identifier  # type: str
        self.third_user_type = third_user_type  # type: str
        self.user_open_id = user_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcologyOpennessAuthenticateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class EcologyOpennessAuthenticateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: EcologyOpennessAuthenticateResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(EcologyOpennessAuthenticateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = EcologyOpennessAuthenticateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EcologyOpennessAuthenticateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EcologyOpennessAuthenticateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EcologyOpennessAuthenticateResponse, self).to_map()
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
            temp_model = EcologyOpennessAuthenticateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EcologyOpennessSendVerificationCodeHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcologyOpennessSendVerificationCodeHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class EcologyOpennessSendVerificationCodeRequest(TeaModel):
    def __init__(self, phone_number=None, region=None, session_id=None):
        self.phone_number = phone_number  # type: str
        self.region = region  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcologyOpennessSendVerificationCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.region is not None:
            result['Region'] = self.region
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class EcologyOpennessSendVerificationCodeResponseBodyResult(TeaModel):
    def __init__(self, expire_in=None, repeat_interval=None):
        self.expire_in = expire_in  # type: int
        self.repeat_interval = repeat_interval  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcologyOpennessSendVerificationCodeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_in is not None:
            result['ExpireIn'] = self.expire_in
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireIn') is not None:
            self.expire_in = m.get('ExpireIn')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        return self


class EcologyOpennessSendVerificationCodeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: EcologyOpennessSendVerificationCodeResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(EcologyOpennessSendVerificationCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = EcologyOpennessSendVerificationCodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EcologyOpennessSendVerificationCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EcologyOpennessSendVerificationCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EcologyOpennessSendVerificationCodeResponse, self).to_map()
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
            temp_model = EcologyOpennessSendVerificationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindUserlistToAuthLoginWithPhoneNumberHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindUserlistToAuthLoginWithPhoneNumberHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class FindUserlistToAuthLoginWithPhoneNumberRequest(TeaModel):
    def __init__(self, code=None, phone_number=None, region=None, session_id=None):
        self.code = code  # type: str
        self.phone_number = phone_number  # type: str
        self.region = region  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindUserlistToAuthLoginWithPhoneNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.region is not None:
            result['Region'] = self.region
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj(TeaModel):
    def __init__(self, session_id=None):
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin(TeaModel):
    def __init__(self, avatar=None, encrypted_user_identifier=None, finding_type=None, nickname=None,
                 user_type=None):
        self.avatar = avatar  # type: str
        self.encrypted_user_identifier = encrypted_user_identifier  # type: str
        self.finding_type = finding_type  # type: str
        self.nickname = nickname  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.encrypted_user_identifier is not None:
            result['EncryptedUserIdentifier'] = self.encrypted_user_identifier
        if self.finding_type is not None:
            result['FindingType'] = self.finding_type
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('EncryptedUserIdentifier') is not None:
            self.encrypted_user_identifier = m.get('EncryptedUserIdentifier')
        if m.get('FindingType') is not None:
            self.finding_type = m.get('FindingType')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult(TeaModel):
    def __init__(self, user_list_to_auth_login=None):
        self.user_list_to_auth_login = user_list_to_auth_login  # type: list[FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin]

    def validate(self):
        if self.user_list_to_auth_login:
            for k in self.user_list_to_auth_login:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserListToAuthLogin'] = []
        if self.user_list_to_auth_login is not None:
            for k in self.user_list_to_auth_login:
                result['UserListToAuthLogin'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_list_to_auth_login = []
        if m.get('UserListToAuthLogin') is not None:
            for k in m.get('UserListToAuthLogin'):
                temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin()
                self.user_list_to_auth_login.append(temp_model.from_map(k))
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBody(TeaModel):
    def __init__(self, code=None, data_obj=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.data_obj = data_obj  # type: FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.data_obj:
            self.data_obj.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(FindUserlistToAuthLoginWithPhoneNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data_obj is not None:
            result['DataObj'] = self.data_obj.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataObj') is not None:
            temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj()
            self.data_obj = temp_model.from_map(m['DataObj'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FindUserlistToAuthLoginWithPhoneNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FindUserlistToAuthLoginWithPhoneNumberResponse, self).to_map()
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
            temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlarmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetAlarmRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetAlarmRequestPayload(TeaModel):
    def __init__(self, alarm_id=None):
        self.alarm_id = alarm_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        return self


class GetAlarmRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetAlarmRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: GetAlarmRequestDeviceInfo
        self.payload = payload  # type: GetAlarmRequestPayload
        self.user_info = user_info  # type: GetAlarmRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetAlarmRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetAlarmRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetAlarmRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetAlarmShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetAlarmResponseBodyResultMusicInfo(TeaModel):
    def __init__(self, music_id=None, music_name=None, music_type=None, music_type_name=None, music_url=None):
        self.music_id = music_id  # type: long
        self.music_name = music_name  # type: str
        self.music_type = music_type  # type: long
        self.music_type_name = music_type_name  # type: str
        self.music_url = music_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmResponseBodyResultMusicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class GetAlarmResponseBodyResultScheduleInfoOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmResponseBodyResultScheduleInfoOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(self, hour=None, minute=None):
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class GetAlarmResponseBodyResultScheduleInfoWeekly(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlarmResponseBodyResultScheduleInfoWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class GetAlarmResponseBodyResultScheduleInfo(TeaModel):
    def __init__(self, once=None, statutory_working_day=None, type=None, weekly=None):
        self.once = once  # type: GetAlarmResponseBodyResultScheduleInfoOnce
        self.statutory_working_day = statutory_working_day  # type: GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay
        self.type = type  # type: str
        self.weekly = weekly  # type: GetAlarmResponseBodyResultScheduleInfoWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(GetAlarmResponseBodyResultScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class GetAlarmResponseBodyResult(TeaModel):
    def __init__(self, alarm_id=None, music_info=None, schedule_info=None, schedule_type_desc=None, status=None,
                 trigger_date_desc=None, trigger_time_desc=None, volume=None):
        self.alarm_id = alarm_id  # type: long
        self.music_info = music_info  # type: GetAlarmResponseBodyResultMusicInfo
        self.schedule_info = schedule_info  # type: GetAlarmResponseBodyResultScheduleInfo
        self.schedule_type_desc = schedule_type_desc  # type: str
        self.status = status  # type: int
        self.trigger_date_desc = trigger_date_desc  # type: str
        self.trigger_time_desc = trigger_time_desc  # type: str
        self.volume = volume  # type: int

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(GetAlarmResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.schedule_type_desc is not None:
            result['ScheduleTypeDesc'] = self.schedule_type_desc
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_date_desc is not None:
            result['TriggerDateDesc'] = self.trigger_date_desc
        if self.trigger_time_desc is not None:
            result['TriggerTimeDesc'] = self.trigger_time_desc
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('MusicInfo') is not None:
            temp_model = GetAlarmResponseBodyResultMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('ScheduleTypeDesc') is not None:
            self.schedule_type_desc = m.get('ScheduleTypeDesc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerDateDesc') is not None:
            self.trigger_date_desc = m.get('TriggerDateDesc')
        if m.get('TriggerTimeDesc') is not None:
            self.trigger_time_desc = m.get('TriggerTimeDesc')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class GetAlarmResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetAlarmResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAlarmResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAlarmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlarmResponse, self).to_map()
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
            temp_model = GetAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlbumHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlbumHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetAlbumRequest(TeaModel):
    def __init__(self, id=None, type=None):
        self.id = id  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlbumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAlbumResponseBodyResultAuthors(TeaModel):
    def __init__(self, author_types=None, gender=None, id=None, online=None, source=None, title=None):
        self.author_types = author_types  # type: list[str]
        self.gender = gender  # type: str
        self.id = id  # type: long
        self.online = online  # type: bool
        self.source = source  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlbumResponseBodyResultAuthors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetAlbumResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlbumResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetAlbumResponseBodyResult(TeaModel):
    def __init__(self, alias=None, audition=None, authors=None, category=None, charge=None, comm_cate_id=None,
                 cover=None, description=None, finished=None, hot_score=None, id=None, item_type=None, raw_id=None,
                 source=None, title=None, total_episode=None, type=None, valid=None):
        self.alias = alias  # type: list[str]
        self.audition = audition  # type: bool
        self.authors = authors  # type: list[GetAlbumResponseBodyResultAuthors]
        self.category = category  # type: str
        self.charge = charge  # type: bool
        self.comm_cate_id = comm_cate_id  # type: long
        self.cover = cover  # type: GetAlbumResponseBodyResultCover
        self.description = description  # type: str
        self.finished = finished  # type: str
        self.hot_score = hot_score  # type: float
        self.id = id  # type: long
        self.item_type = item_type  # type: str
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.total_episode = total_episode  # type: int
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(GetAlbumResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.total_episode is not None:
            result['TotalEpisode'] = self.total_episode
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = GetAlbumResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = GetAlbumResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TotalEpisode') is not None:
            self.total_episode = m.get('TotalEpisode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetAlbumResponseBody(TeaModel):
    def __init__(self, code=None, request_id=None, result=None):
        self.code = code  # type: int
        self.request_id = request_id  # type: str
        self.result = result  # type: GetAlbumResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAlbumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAlbumResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAlbumResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlbumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlbumResponse, self).to_map()
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
            temp_model = GetAlbumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlbumDetailByIdHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlbumDetailByIdHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetAlbumDetailByIdRequest(TeaModel):
    def __init__(self, album_id=None):
        self.album_id = album_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlbumDetailByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        return self


class GetAlbumDetailByIdResponseBodyResultAlbumContentList(TeaModel):
    def __init__(self, duration=None, id=None, order_index=None, title=None):
        self.duration = duration  # type: str
        self.id = id  # type: str
        self.order_index = order_index  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlbumDetailByIdResponseBodyResultAlbumContentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.order_index is not None:
            result['OrderIndex'] = self.order_index
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetAlbumDetailByIdResponseBodyResult(TeaModel):
    def __init__(self, album_content_list=None, album_cover_url=None, album_description=None, album_id=None,
                 album_title=None):
        self.album_content_list = album_content_list  # type: list[GetAlbumDetailByIdResponseBodyResultAlbumContentList]
        self.album_cover_url = album_cover_url  # type: str
        self.album_description = album_description  # type: str
        self.album_id = album_id  # type: str
        self.album_title = album_title  # type: str

    def validate(self):
        if self.album_content_list:
            for k in self.album_content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAlbumDetailByIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlbumContentList'] = []
        if self.album_content_list is not None:
            for k in self.album_content_list:
                result['AlbumContentList'].append(k.to_map() if k else None)
        if self.album_cover_url is not None:
            result['AlbumCoverUrl'] = self.album_cover_url
        if self.album_description is not None:
            result['AlbumDescription'] = self.album_description
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.album_title is not None:
            result['AlbumTitle'] = self.album_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.album_content_list = []
        if m.get('AlbumContentList') is not None:
            for k in m.get('AlbumContentList'):
                temp_model = GetAlbumDetailByIdResponseBodyResultAlbumContentList()
                self.album_content_list.append(temp_model.from_map(k))
        if m.get('AlbumCoverUrl') is not None:
            self.album_cover_url = m.get('AlbumCoverUrl')
        if m.get('AlbumDescription') is not None:
            self.album_description = m.get('AlbumDescription')
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('AlbumTitle') is not None:
            self.album_title = m.get('AlbumTitle')
        return self


class GetAlbumDetailByIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetAlbumDetailByIdResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAlbumDetailByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAlbumDetailByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAlbumDetailByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlbumDetailByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlbumDetailByIdResponse, self).to_map()
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
            temp_model = GetAlbumDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAligenieUserInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAligenieUserInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetAligenieUserInfoRequest(TeaModel):
    def __init__(self, login_state_access_token=None):
        self.login_state_access_token = login_state_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAligenieUserInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class GetAligenieUserInfoResponseBodyResult(TeaModel):
    def __init__(self, aligenie_nickname=None, avatar=None, deletable=None):
        self.aligenie_nickname = aligenie_nickname  # type: str
        self.avatar = avatar  # type: str
        self.deletable = deletable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAligenieUserInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aligenie_nickname is not None:
            result['AligenieNickname'] = self.aligenie_nickname
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AligenieNickname') is not None:
            self.aligenie_nickname = m.get('AligenieNickname')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        return self


class GetAligenieUserInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetAligenieUserInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAligenieUserInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAligenieUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAligenieUserInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAligenieUserInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAligenieUserInfoResponse, self).to_map()
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
            temp_model = GetAligenieUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeEnhanceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeEnhanceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetCodeEnhanceRequestChannelInfo(TeaModel):
    def __init__(self, channel=None, ext_info=None):
        self.channel = channel  # type: str
        self.ext_info = ext_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeEnhanceRequestChannelInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class GetCodeEnhanceRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeEnhanceRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetCodeEnhanceRequest(TeaModel):
    def __init__(self, channel_info=None, user_info=None):
        self.channel_info = channel_info  # type: GetCodeEnhanceRequestChannelInfo
        self.user_info = user_info  # type: GetCodeEnhanceRequestUserInfo

    def validate(self):
        if self.channel_info:
            self.channel_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetCodeEnhanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info is not None:
            result['ChannelInfo'] = self.channel_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            temp_model = GetCodeEnhanceRequestChannelInfo()
            self.channel_info = temp_model.from_map(m['ChannelInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetCodeEnhanceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetCodeEnhanceShrinkRequest(TeaModel):
    def __init__(self, channel_info_shrink=None, user_info_shrink=None):
        self.channel_info_shrink = channel_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeEnhanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info_shrink is not None:
            result['ChannelInfo'] = self.channel_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            self.channel_info_shrink = m.get('ChannelInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetCodeEnhanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeEnhanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetCodeEnhanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCodeEnhanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCodeEnhanceResponse, self).to_map()
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
            temp_model = GetCodeEnhanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContentHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetContentRequest(TeaModel):
    def __init__(self, id=None, type=None):
        self.id = id  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetContentResponseBodyResultAuthors(TeaModel):
    def __init__(self, author_types=None, gender=None, id=None, online=None, source=None, title=None):
        self.author_types = author_types  # type: list[str]
        self.gender = gender  # type: str
        self.id = id  # type: long
        self.online = online  # type: bool
        self.source = source  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContentResponseBodyResultAuthors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetContentResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContentResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetContentResponseBodyResult(TeaModel):
    def __init__(self, album_id=None, alias=None, audition=None, authors=None, category=None, charge=None,
                 comm_cate_id=None, cover=None, description=None, duration=None, hot_score=None, id=None, item_type=None,
                 lyric=None, raw_id=None, source=None, styles=None, title=None, type=None, valid=None):
        self.album_id = album_id  # type: str
        self.alias = alias  # type: list[str]
        self.audition = audition  # type: bool
        self.authors = authors  # type: list[GetContentResponseBodyResultAuthors]
        self.category = category  # type: str
        self.charge = charge  # type: bool
        self.comm_cate_id = comm_cate_id  # type: long
        self.cover = cover  # type: GetContentResponseBodyResultCover
        self.description = description  # type: str
        self.duration = duration  # type: long
        self.hot_score = hot_score  # type: float
        self.id = id  # type: long
        self.item_type = item_type  # type: str
        self.lyric = lyric  # type: str
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.styles = styles  # type: list[str]
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(GetContentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.styles is not None:
            result['Styles'] = self.styles
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = GetContentResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = GetContentResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetContentResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetContentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetContentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetContentResponse, self).to_map()
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
            temp_model = GetContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCurrentPlayingItemHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingItemHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetCurrentPlayingItemRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingItemRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetCurrentPlayingItemRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingItemRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetCurrentPlayingItemRequest(TeaModel):
    def __init__(self, device_info=None, user_info=None):
        self.device_info = device_info  # type: GetCurrentPlayingItemRequestDeviceInfo
        self.user_info = user_info  # type: GetCurrentPlayingItemRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetCurrentPlayingItemRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetCurrentPlayingItemRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetCurrentPlayingItemShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingItemShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetCurrentPlayingItemResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingItemResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetCurrentPlayingItemResponseBodyResult(TeaModel):
    def __init__(self, album_name=None, album_raw_id=None, audio_length=None, copyright=None, cover=None,
                 default_play_order=None, item_url=None, liked=None, lyric_url=None, play_mode=None, pos=None, progress=None,
                 raw_id=None, singer=None, source=None, title=None, type=None, valid=None):
        self.album_name = album_name  # type: str
        self.album_raw_id = album_raw_id  # type: str
        self.audio_length = audio_length  # type: int
        self.copyright = copyright  # type: int
        self.cover = cover  # type: GetCurrentPlayingItemResponseBodyResultCover
        self.default_play_order = default_play_order  # type: int
        self.item_url = item_url  # type: str
        self.liked = liked  # type: str
        self.lyric_url = lyric_url  # type: str
        self.play_mode = play_mode  # type: str
        self.pos = pos  # type: int
        self.progress = progress  # type: int
        self.raw_id = raw_id  # type: str
        self.singer = singer  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingItemResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = GetCurrentPlayingItemResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetCurrentPlayingItemResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetCurrentPlayingItemResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetCurrentPlayingItemResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCurrentPlayingItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCurrentPlayingItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingItemResponse, self).to_map()
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
            temp_model = GetCurrentPlayingItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCurrentPlayingListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetCurrentPlayingListRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingListRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetCurrentPlayingListRequestOpenQueryPlayListRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingListRequestOpenQueryPlayListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetCurrentPlayingListRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingListRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetCurrentPlayingListRequest(TeaModel):
    def __init__(self, device_info=None, open_query_play_list_request=None, user_info=None):
        self.device_info = device_info  # type: GetCurrentPlayingListRequestDeviceInfo
        self.open_query_play_list_request = open_query_play_list_request  # type: GetCurrentPlayingListRequestOpenQueryPlayListRequest
        self.user_info = user_info  # type: GetCurrentPlayingListRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_query_play_list_request:
            self.open_query_play_list_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_query_play_list_request is not None:
            result['OpenQueryPlayListRequest'] = self.open_query_play_list_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetCurrentPlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenQueryPlayListRequest') is not None:
            temp_model = GetCurrentPlayingListRequestOpenQueryPlayListRequest()
            self.open_query_play_list_request = temp_model.from_map(m['OpenQueryPlayListRequest'])
        if m.get('UserInfo') is not None:
            temp_model = GetCurrentPlayingListRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetCurrentPlayingListShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_query_play_list_request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_query_play_list_request_shrink = open_query_play_list_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_query_play_list_request_shrink is not None:
            result['OpenQueryPlayListRequest'] = self.open_query_play_list_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenQueryPlayListRequest') is not None:
            self.open_query_play_list_request_shrink = m.get('OpenQueryPlayListRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetCurrentPlayingListResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCurrentPlayingListResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetCurrentPlayingListResponseBodyResult(TeaModel):
    def __init__(self, album_name=None, album_raw_id=None, audio_length=None, copyright=None, cover=None,
                 default_play_order=None, item_url=None, liked=None, lyric_url=None, play_mode=None, pos=None, progress=None,
                 raw_id=None, singer=None, source=None, title=None, type=None, valid=None):
        self.album_name = album_name  # type: str
        self.album_raw_id = album_raw_id  # type: str
        self.audio_length = audio_length  # type: int
        self.copyright = copyright  # type: int
        self.cover = cover  # type: GetCurrentPlayingListResponseBodyResultCover
        self.default_play_order = default_play_order  # type: int
        self.item_url = item_url  # type: str
        self.liked = liked  # type: bool
        self.lyric_url = lyric_url  # type: str
        self.play_mode = play_mode  # type: str
        self.pos = pos  # type: int
        self.progress = progress  # type: int
        self.raw_id = raw_id  # type: str
        self.singer = singer  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = GetCurrentPlayingListResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetCurrentPlayingListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetCurrentPlayingListResponseBodyResult]
        self.success = success  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetCurrentPlayingListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCurrentPlayingListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCurrentPlayingListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCurrentPlayingListResponse, self).to_map()
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
            temp_model = GetCurrentPlayingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceBasicInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceBasicInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceBasicInfoRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceBasicInfoRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceBasicInfoRequest(TeaModel):
    def __init__(self, device_info=None):
        self.device_info = device_info  # type: GetDeviceBasicInfoRequestDeviceInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(GetDeviceBasicInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceBasicInfoRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceBasicInfoShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceBasicInfoShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceBasicInfoResponseBodyResult(TeaModel):
    def __init__(self, firmware_version=None, mac=None, name=None, sn=None):
        self.firmware_version = firmware_version  # type: str
        self.mac = mac  # type: str
        self.name = name  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceBasicInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.name is not None:
            result['Name'] = self.name
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class GetDeviceBasicInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetDeviceBasicInfoResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDeviceBasicInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetDeviceBasicInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceBasicInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceBasicInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceBasicInfoResponse, self).to_map()
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
            temp_model = GetDeviceBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceIdByIdentityHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceIdByIdentityHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceIdByIdentityRequest(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, identity_id=None, identity_type=None, product_key=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.identity_id = identity_id  # type: str
        self.identity_type = identity_type  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceIdByIdentityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds(TeaModel):
    def __init__(self, device_union_id=None, organization_id=None):
        self.device_union_id = device_union_id  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceIdByIdentityResponseBodyResult(TeaModel):
    def __init__(self, device_open_id=None, device_union_ids=None):
        self.device_open_id = device_open_id  # type: str
        self.device_union_ids = device_union_ids  # type: list[GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds]

    def validate(self):
        if self.device_union_ids:
            for k in self.device_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDeviceIdByIdentityResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        return self


class GetDeviceIdByIdentityResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetDeviceIdByIdentityResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDeviceIdByIdentityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetDeviceIdByIdentityResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceIdByIdentityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceIdByIdentityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceIdByIdentityResponse, self).to_map()
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
            temp_model = GetDeviceIdByIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceSettingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceSettingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceSettingRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceSettingRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceSettingRequest(TeaModel):
    def __init__(self, device_info=None, keys=None):
        self.device_info = device_info  # type: GetDeviceSettingRequestDeviceInfo
        self.keys = keys  # type: list[str]

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(GetDeviceSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceSettingRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class GetDeviceSettingShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, keys_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.keys_shrink = keys_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceSettingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')
        return self


class GetDeviceSettingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetDeviceSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceSettingResponse, self).to_map()
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
            temp_model = GetDeviceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceStatusDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceStatusDetailRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusDetailRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceStatusDetailRequest(TeaModel):
    def __init__(self, device_info=None, keys=None):
        self.device_info = device_info  # type: GetDeviceStatusDetailRequestDeviceInfo
        self.keys = keys  # type: list[str]

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(GetDeviceStatusDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceStatusDetailRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class GetDeviceStatusDetailShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, keys_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.keys_shrink = keys_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusDetailShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')
        return self


class GetDeviceStatusDetailResponseBodyResultPlayer(TeaModel):
    def __init__(self, audio_album=None, audio_anchor=None, audio_ext=None, audio_id=None, audio_length=None,
                 audio_name=None, audio_source=None, audio_url=None, format=None, progress=None, source=None, status=None,
                 timestamp=None):
        self.audio_album = audio_album  # type: str
        self.audio_anchor = audio_anchor  # type: str
        self.audio_ext = audio_ext  # type: str
        self.audio_id = audio_id  # type: str
        self.audio_length = audio_length  # type: str
        self.audio_name = audio_name  # type: str
        self.audio_source = audio_source  # type: str
        self.audio_url = audio_url  # type: str
        self.format = format  # type: str
        self.progress = progress  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusDetailResponseBodyResultPlayer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_album is not None:
            result['AudioAlbum'] = self.audio_album
        if self.audio_anchor is not None:
            result['AudioAnchor'] = self.audio_anchor
        if self.audio_ext is not None:
            result['AudioExt'] = self.audio_ext
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.audio_name is not None:
            result['AudioName'] = self.audio_name
        if self.audio_source is not None:
            result['AudioSource'] = self.audio_source
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.format is not None:
            result['Format'] = self.format
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioAlbum') is not None:
            self.audio_album = m.get('AudioAlbum')
        if m.get('AudioAnchor') is not None:
            self.audio_anchor = m.get('AudioAnchor')
        if m.get('AudioExt') is not None:
            self.audio_ext = m.get('AudioExt')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('AudioName') is not None:
            self.audio_name = m.get('AudioName')
        if m.get('AudioSource') is not None:
            self.audio_source = m.get('AudioSource')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetDeviceStatusDetailResponseBodyResultPower(TeaModel):
    def __init__(self, quantity=None, status=None):
        self.quantity = quantity  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusDetailResponseBodyResultPower, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeviceStatusDetailResponseBodyResultSpeaker(TeaModel):
    def __init__(self, muted=None, volume=None):
        self.muted = muted  # type: bool
        self.volume = volume  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusDetailResponseBodyResultSpeaker, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.muted is not None:
            result['Muted'] = self.muted
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Muted') is not None:
            self.muted = m.get('Muted')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class GetDeviceStatusDetailResponseBodyResult(TeaModel):
    def __init__(self, player=None, power=None, speaker=None):
        self.player = player  # type: GetDeviceStatusDetailResponseBodyResultPlayer
        self.power = power  # type: GetDeviceStatusDetailResponseBodyResultPower
        self.speaker = speaker  # type: GetDeviceStatusDetailResponseBodyResultSpeaker

    def validate(self):
        if self.player:
            self.player.validate()
        if self.power:
            self.power.validate()
        if self.speaker:
            self.speaker.validate()

    def to_map(self):
        _map = super(GetDeviceStatusDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.player is not None:
            result['Player'] = self.player.to_map()
        if self.power is not None:
            result['Power'] = self.power.to_map()
        if self.speaker is not None:
            result['Speaker'] = self.speaker.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Player') is not None:
            temp_model = GetDeviceStatusDetailResponseBodyResultPlayer()
            self.player = temp_model.from_map(m['Player'])
        if m.get('Power') is not None:
            temp_model = GetDeviceStatusDetailResponseBodyResultPower()
            self.power = temp_model.from_map(m['Power'])
        if m.get('Speaker') is not None:
            temp_model = GetDeviceStatusDetailResponseBodyResultSpeaker()
            self.speaker = temp_model.from_map(m['Speaker'])
        return self


class GetDeviceStatusDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetDeviceStatusDetailResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDeviceStatusDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetDeviceStatusDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceStatusDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceStatusDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceStatusDetailResponse, self).to_map()
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
            temp_model = GetDeviceStatusDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceStatusInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceStatusInfoRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusInfoRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceStatusInfoRequest(TeaModel):
    def __init__(self, device_info=None):
        self.device_info = device_info  # type: GetDeviceStatusInfoRequestDeviceInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(GetDeviceStatusInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceStatusInfoRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceStatusInfoShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusInfoShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceStatusInfoResponseBodyResult(TeaModel):
    def __init__(self, online=None):
        self.online = online  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class GetDeviceStatusInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetDeviceStatusInfoResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDeviceStatusInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetDeviceStatusInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceStatusInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceStatusInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceStatusInfoResponse, self).to_map()
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
            temp_model = GetDeviceStatusInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceTagHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceTagHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetDeviceTagRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceTagRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceTagRequest(TeaModel):
    def __init__(self, device_info=None):
        self.device_info = device_info  # type: GetDeviceTagRequestDeviceInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(GetDeviceTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceTagRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceTagShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceTagShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceTagResponseBodyResult(TeaModel):
    def __init__(self, device_tags=None):
        self.device_tags = device_tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceTagResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        return self


class GetDeviceTagResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetDeviceTagResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDeviceTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetDeviceTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceTagResponse, self).to_map()
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
            temp_model = GetDeviceTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScheduleTaskHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScheduleTaskHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetScheduleTaskRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScheduleTaskRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetScheduleTaskRequestPayload(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScheduleTaskRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetScheduleTaskRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScheduleTaskRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetScheduleTaskRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: GetScheduleTaskRequestDeviceInfo
        self.payload = payload  # type: GetScheduleTaskRequestPayload
        self.user_info = user_info  # type: GetScheduleTaskRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetScheduleTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetScheduleTaskRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetScheduleTaskRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetScheduleTaskRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetScheduleTaskShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScheduleTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetScheduleTaskResponseBodyResultActionTopicList(TeaModel):
    def __init__(self, custom_action=None):
        self.custom_action = custom_action  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScheduleTaskResponseBodyResultActionTopicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_action is not None:
            result['CustomAction'] = self.custom_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomAction') is not None:
            self.custom_action = m.get('CustomAction')
        return self


class GetScheduleTaskResponseBodyResult(TeaModel):
    def __init__(self, action_topic_list=None, cron=None, schedule_end_time=None, schedule_id=None,
                 schedule_start_time=None, schedule_type=None):
        self.action_topic_list = action_topic_list  # type: list[GetScheduleTaskResponseBodyResultActionTopicList]
        self.cron = cron  # type: str
        self.schedule_end_time = schedule_end_time  # type: str
        self.schedule_id = schedule_id  # type: long
        self.schedule_start_time = schedule_start_time  # type: str
        self.schedule_type = schedule_type  # type: str

    def validate(self):
        if self.action_topic_list:
            for k in self.action_topic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetScheduleTaskResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActionTopicList'] = []
        if self.action_topic_list is not None:
            for k in self.action_topic_list:
                result['ActionTopicList'].append(k.to_map() if k else None)
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.schedule_end_time is not None:
            result['ScheduleEndTime'] = self.schedule_end_time
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_start_time is not None:
            result['ScheduleStartTime'] = self.schedule_start_time
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.action_topic_list = []
        if m.get('ActionTopicList') is not None:
            for k in m.get('ActionTopicList'):
                temp_model = GetScheduleTaskResponseBodyResultActionTopicList()
                self.action_topic_list.append(temp_model.from_map(k))
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('ScheduleEndTime') is not None:
            self.schedule_end_time = m.get('ScheduleEndTime')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleStartTime') is not None:
            self.schedule_start_time = m.get('ScheduleStartTime')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        return self


class GetScheduleTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetScheduleTaskResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetScheduleTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetScheduleTaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetScheduleTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScheduleTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScheduleTaskResponse, self).to_map()
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
            temp_model = GetScheduleTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUnreadMessageCountHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnreadMessageCountHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUnreadMessageCountRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnreadMessageCountRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetUnreadMessageCountRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: GetUnreadMessageCountRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetUnreadMessageCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetUnreadMessageCountRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetUnreadMessageCountShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnreadMessageCountShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetUnreadMessageCountResponseBody(TeaModel):
    def __init__(self, code=None, message=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnreadMessageCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetUnreadMessageCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUnreadMessageCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUnreadMessageCountResponse, self).to_map()
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
            temp_model = GetUnreadMessageCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserByDeviceIdHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserByDeviceIdHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUserByDeviceIdRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserByDeviceIdRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetUserByDeviceIdRequest(TeaModel):
    def __init__(self, device_info=None):
        self.device_info = device_info  # type: GetUserByDeviceIdRequestDeviceInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(GetUserByDeviceIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetUserByDeviceIdRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetUserByDeviceIdShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserByDeviceIdShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetUserByDeviceIdResponseBodyResultUserUnionIds(TeaModel):
    def __init__(self, organization_id=None, user_union_id=None):
        self.organization_id = organization_id  # type: str
        self.user_union_id = user_union_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserByDeviceIdResponseBodyResultUserUnionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.user_union_id is not None:
            result['UserUnionId'] = self.user_union_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('UserUnionId') is not None:
            self.user_union_id = m.get('UserUnionId')
        return self


class GetUserByDeviceIdResponseBodyResult(TeaModel):
    def __init__(self, user_open_id=None, user_union_ids=None):
        self.user_open_id = user_open_id  # type: str
        self.user_union_ids = user_union_ids  # type: list[GetUserByDeviceIdResponseBodyResultUserUnionIds]

    def validate(self):
        if self.user_union_ids:
            for k in self.user_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserByDeviceIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        result['UserUnionIds'] = []
        if self.user_union_ids is not None:
            for k in self.user_union_ids:
                result['UserUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        self.user_union_ids = []
        if m.get('UserUnionIds') is not None:
            for k in m.get('UserUnionIds'):
                temp_model = GetUserByDeviceIdResponseBodyResultUserUnionIds()
                self.user_union_ids.append(temp_model.from_map(k))
        return self


class GetUserByDeviceIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetUserByDeviceIdResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetUserByDeviceIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetUserByDeviceIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetUserByDeviceIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserByDeviceIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserByDeviceIdResponse, self).to_map()
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
            temp_model = GetUserByDeviceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeatherHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeatherHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetWeatherRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeatherRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetWeatherRequestPayload(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeatherRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m=None):
        m = m or dict()
        return self


class GetWeatherRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeatherRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetWeatherRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: GetWeatherRequestDeviceInfo
        self.payload = payload  # type: GetWeatherRequestPayload
        self.user_info = user_info  # type: GetWeatherRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetWeatherRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetWeatherRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetWeatherRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetWeatherRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetWeatherShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeatherShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetWeatherResponseBodyResultCurrentMeteorologyTemperature(TeaModel):
    def __init__(self, current=None, current_desc=None, high=None, high_desc=None, logical=None, low=None,
                 low_desc=None):
        self.current = current  # type: str
        self.current_desc = current_desc  # type: str
        self.high = high  # type: str
        self.high_desc = high_desc  # type: str
        self.logical = logical  # type: str
        self.low = low  # type: str
        self.low_desc = low_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeatherResponseBodyResultCurrentMeteorologyTemperature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.current_desc is not None:
            result['CurrentDesc'] = self.current_desc
        if self.high is not None:
            result['High'] = self.high
        if self.high_desc is not None:
            result['HighDesc'] = self.high_desc
        if self.logical is not None:
            result['Logical'] = self.logical
        if self.low is not None:
            result['Low'] = self.low
        if self.low_desc is not None:
            result['LowDesc'] = self.low_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CurrentDesc') is not None:
            self.current_desc = m.get('CurrentDesc')
        if m.get('High') is not None:
            self.high = m.get('High')
        if m.get('HighDesc') is not None:
            self.high_desc = m.get('HighDesc')
        if m.get('Logical') is not None:
            self.logical = m.get('Logical')
        if m.get('Low') is not None:
            self.low = m.get('Low')
        if m.get('LowDesc') is not None:
            self.low_desc = m.get('LowDesc')
        return self


class GetWeatherResponseBodyResultCurrentMeteorologyWeather(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeatherResponseBodyResultCurrentMeteorologyWeather, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetWeatherResponseBodyResultCurrentMeteorology(TeaModel):
    def __init__(self, temperature=None, weather=None):
        self.temperature = temperature  # type: GetWeatherResponseBodyResultCurrentMeteorologyTemperature
        self.weather = weather  # type: GetWeatherResponseBodyResultCurrentMeteorologyWeather

    def validate(self):
        if self.temperature:
            self.temperature.validate()
        if self.weather:
            self.weather.validate()

    def to_map(self):
        _map = super(GetWeatherResponseBodyResultCurrentMeteorology, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temperature is not None:
            result['Temperature'] = self.temperature.to_map()
        if self.weather is not None:
            result['Weather'] = self.weather.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Temperature') is not None:
            temp_model = GetWeatherResponseBodyResultCurrentMeteorologyTemperature()
            self.temperature = temp_model.from_map(m['Temperature'])
        if m.get('Weather') is not None:
            temp_model = GetWeatherResponseBodyResultCurrentMeteorologyWeather()
            self.weather = temp_model.from_map(m['Weather'])
        return self


class GetWeatherResponseBodyResult(TeaModel):
    def __init__(self, current_meteorology=None):
        self.current_meteorology = current_meteorology  # type: GetWeatherResponseBodyResultCurrentMeteorology

    def validate(self):
        if self.current_meteorology:
            self.current_meteorology.validate()

    def to_map(self):
        _map = super(GetWeatherResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_meteorology is not None:
            result['CurrentMeteorology'] = self.current_meteorology.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentMeteorology') is not None:
            temp_model = GetWeatherResponseBodyResultCurrentMeteorology()
            self.current_meteorology = temp_model.from_map(m['CurrentMeteorology'])
        return self


class GetWeatherResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        # HttpCode
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetWeatherResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetWeatherResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetWeatherResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetWeatherResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWeatherResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWeatherResponse, self).to_map()
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
            temp_model = GetWeatherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexControlPlayingListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexControlPlayingListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class IndexControlPlayingListRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexControlPlayingListRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class IndexControlPlayingListRequestOpenIndexControlRequest(TeaModel):
    def __init__(self, extend_info=None, index=None, need_content_continued=None):
        self.extend_info = extend_info  # type: dict[str, any]
        self.index = index  # type: int
        self.need_content_continued = need_content_continued  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexControlPlayingListRequestOpenIndexControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.index is not None:
            result['Index'] = self.index
        if self.need_content_continued is not None:
            result['NeedContentContinued'] = self.need_content_continued
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('NeedContentContinued') is not None:
            self.need_content_continued = m.get('NeedContentContinued')
        return self


class IndexControlPlayingListRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexControlPlayingListRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class IndexControlPlayingListRequest(TeaModel):
    def __init__(self, device_info=None, open_index_control_request=None, user_info=None):
        self.device_info = device_info  # type: IndexControlPlayingListRequestDeviceInfo
        self.open_index_control_request = open_index_control_request  # type: IndexControlPlayingListRequestOpenIndexControlRequest
        self.user_info = user_info  # type: IndexControlPlayingListRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_index_control_request:
            self.open_index_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(IndexControlPlayingListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_index_control_request is not None:
            result['OpenIndexControlRequest'] = self.open_index_control_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = IndexControlPlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenIndexControlRequest') is not None:
            temp_model = IndexControlPlayingListRequestOpenIndexControlRequest()
            self.open_index_control_request = temp_model.from_map(m['OpenIndexControlRequest'])
        if m.get('UserInfo') is not None:
            temp_model = IndexControlPlayingListRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class IndexControlPlayingListShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_index_control_request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_index_control_request_shrink = open_index_control_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexControlPlayingListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_index_control_request_shrink is not None:
            result['OpenIndexControlRequest'] = self.open_index_control_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenIndexControlRequest') is not None:
            self.open_index_control_request_shrink = m.get('OpenIndexControlRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class IndexControlPlayingListResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexControlPlayingListResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class IndexControlPlayingListResponseBodyResult(TeaModel):
    def __init__(self, album_name=None, album_raw_id=None, audio_length=None, copyright=None, cover=None,
                 default_play_order=None, item_url=None, liked=None, lyric_url=None, play_mode=None, pos=None, progress=None,
                 raw_id=None, singer=None, source=None, title=None, type=None, valid=None):
        self.album_name = album_name  # type: str
        self.album_raw_id = album_raw_id  # type: str
        self.audio_length = audio_length  # type: int
        self.copyright = copyright  # type: int
        self.cover = cover  # type: IndexControlPlayingListResponseBodyResultCover
        self.default_play_order = default_play_order  # type: int
        self.item_url = item_url  # type: str
        self.liked = liked  # type: bool
        self.lyric_url = lyric_url  # type: str
        self.play_mode = play_mode  # type: str
        self.pos = pos  # type: int
        self.progress = progress  # type: int
        self.raw_id = raw_id  # type: str
        self.singer = singer  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(IndexControlPlayingListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = IndexControlPlayingListResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class IndexControlPlayingListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: IndexControlPlayingListResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(IndexControlPlayingListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = IndexControlPlayingListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IndexControlPlayingListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IndexControlPlayingListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IndexControlPlayingListResponse, self).to_map()
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
            temp_model = IndexControlPlayingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListAlarmsRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListAlarmsRequestPayload(TeaModel):
    def __init__(self, current_page=None, page_size=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlarmsRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListAlarmsRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: ListAlarmsRequestDeviceInfo
        self.payload = payload  # type: ListAlarmsRequestPayload
        self.user_info = user_info  # type: ListAlarmsRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListAlarmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListAlarmsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = ListAlarmsRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListAlarmsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListAlarmsShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListAlarmsResponseBodyResultModelMusicInfo(TeaModel):
    def __init__(self, music_id=None, music_name=None, music_type=None, music_type_name=None, music_url=None):
        self.music_id = music_id  # type: long
        self.music_name = music_name  # type: str
        self.music_type = music_type  # type: long
        self.music_type_name = music_type_name  # type: str
        self.music_url = music_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsResponseBodyResultModelMusicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfoOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsResponseBodyResultModelScheduleInfoOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(self, hour=None, minute=None):
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsResponseBodyResultModelScheduleInfoStatutoryWorkingDay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfoWeekly(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmsResponseBodyResultModelScheduleInfoWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfo(TeaModel):
    def __init__(self, once=None, statutory_working_day=None, type=None, weekly=None):
        self.once = once  # type: ListAlarmsResponseBodyResultModelScheduleInfoOnce
        self.statutory_working_day = statutory_working_day  # type: ListAlarmsResponseBodyResultModelScheduleInfoStatutoryWorkingDay
        self.type = type  # type: str
        self.weekly = weekly  # type: ListAlarmsResponseBodyResultModelScheduleInfoWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(ListAlarmsResponseBodyResultModelScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class ListAlarmsResponseBodyResultModel(TeaModel):
    def __init__(self, alarm_id=None, music_info=None, schedule_info=None, schedule_type_desc=None, status=None,
                 trigger_date_desc=None, trigger_time_desc=None, volume=None):
        self.alarm_id = alarm_id  # type: long
        self.music_info = music_info  # type: ListAlarmsResponseBodyResultModelMusicInfo
        self.schedule_info = schedule_info  # type: ListAlarmsResponseBodyResultModelScheduleInfo
        self.schedule_type_desc = schedule_type_desc  # type: str
        self.status = status  # type: int
        self.trigger_date_desc = trigger_date_desc  # type: str
        self.trigger_time_desc = trigger_time_desc  # type: str
        self.volume = volume  # type: int

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(ListAlarmsResponseBodyResultModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.schedule_type_desc is not None:
            result['ScheduleTypeDesc'] = self.schedule_type_desc
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_date_desc is not None:
            result['TriggerDateDesc'] = self.trigger_date_desc
        if self.trigger_time_desc is not None:
            result['TriggerTimeDesc'] = self.trigger_time_desc
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('MusicInfo') is not None:
            temp_model = ListAlarmsResponseBodyResultModelMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('ScheduleTypeDesc') is not None:
            self.schedule_type_desc = m.get('ScheduleTypeDesc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerDateDesc') is not None:
            self.trigger_date_desc = m.get('TriggerDateDesc')
        if m.get('TriggerTimeDesc') is not None:
            self.trigger_time_desc = m.get('TriggerTimeDesc')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class ListAlarmsResponseBodyResult(TeaModel):
    def __init__(self, current_page=None, model=None, page_count=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.model = model  # type: list[ListAlarmsResponseBodyResultModel]
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListAlarmsResponseBodyResultModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ListAlarmsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListAlarmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListAlarmsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAlarmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlarmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmsResponse, self).to_map()
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
            temp_model = ListAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlbumDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListAlbumDetailRequest(TeaModel):
    def __init__(self, id=None, page_num=None, page_size=None):
        self.id = id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlbumDetailResponseBodyResultOpenDataItemListAuthors(TeaModel):
    def __init__(self, author_types=None, gender=None, id=None, online=None, source=None, title=None):
        self.author_types = author_types  # type: list[str]
        self.gender = gender  # type: str
        self.id = id  # type: long
        self.online = online  # type: bool
        self.source = source  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumDetailResponseBodyResultOpenDataItemListAuthors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListAlbumDetailResponseBodyResultOpenDataItemListCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumDetailResponseBodyResultOpenDataItemListCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListAlbumDetailResponseBodyResultOpenDataItemList(TeaModel):
    def __init__(self, alias=None, audition=None, authors=None, category=None, charge=None, comm_cate_id=None,
                 cover=None, description=None, duration=None, hot_score=None, id=None, item_type=None, order_index=None,
                 raw_id=None, source=None, styles=None, title=None, type=None, valid=None):
        self.alias = alias  # type: list[str]
        self.audition = audition  # type: bool
        self.authors = authors  # type: list[ListAlbumDetailResponseBodyResultOpenDataItemListAuthors]
        self.category = category  # type: str
        self.charge = charge  # type: bool
        self.comm_cate_id = comm_cate_id  # type: long
        self.cover = cover  # type: ListAlbumDetailResponseBodyResultOpenDataItemListCover
        self.description = description  # type: str
        self.duration = duration  # type: long
        self.hot_score = hot_score  # type: float
        self.id = id  # type: long
        self.item_type = item_type  # type: str
        self.order_index = order_index  # type: long
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.styles = styles  # type: list[str]
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ListAlbumDetailResponseBodyResultOpenDataItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.order_index is not None:
            result['OrderIndex'] = self.order_index
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.styles is not None:
            result['Styles'] = self.styles
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListAlbumDetailResponseBodyResultOpenDataItemListAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListAlbumDetailResponseBodyResultOpenDataItemListCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class ListAlbumDetailResponseBodyResult(TeaModel):
    def __init__(self, current_page_num=None, open_data_item_list=None, page_size=None, total_size=None):
        self.current_page_num = current_page_num  # type: long
        self.open_data_item_list = open_data_item_list  # type: list[ListAlbumDetailResponseBodyResultOpenDataItemList]
        self.page_size = page_size  # type: long
        self.total_size = total_size  # type: long

    def validate(self):
        if self.open_data_item_list:
            for k in self.open_data_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlbumDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['OpenDataItemList'] = []
        if self.open_data_item_list is not None:
            for k in self.open_data_item_list:
                result['OpenDataItemList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.open_data_item_list = []
        if m.get('OpenDataItemList') is not None:
            for k in m.get('OpenDataItemList'):
                temp_model = ListAlbumDetailResponseBodyResultOpenDataItemList()
                self.open_data_item_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAlbumDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: ListAlbumDetailResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListAlbumDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListAlbumDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAlbumDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlbumDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlbumDetailResponse, self).to_map()
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
            temp_model = ListAlbumDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlbumIsAddedHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumIsAddedHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListAlbumIsAddedRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumIsAddedRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListAlbumIsAddedRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumIsAddedRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListAlbumIsAddedRequest(TeaModel):
    def __init__(self, album_id_list=None, device_info=None, user_info=None):
        self.album_id_list = album_id_list  # type: list[str]
        self.device_info = device_info  # type: ListAlbumIsAddedRequestDeviceInfo
        self.user_info = user_info  # type: ListAlbumIsAddedRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListAlbumIsAddedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id_list is not None:
            result['AlbumIdList'] = self.album_id_list
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumIdList') is not None:
            self.album_id_list = m.get('AlbumIdList')
        if m.get('DeviceInfo') is not None:
            temp_model = ListAlbumIsAddedRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = ListAlbumIsAddedRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListAlbumIsAddedShrinkRequest(TeaModel):
    def __init__(self, album_id_list_shrink=None, device_info_shrink=None, user_info_shrink=None):
        self.album_id_list_shrink = album_id_list_shrink  # type: str
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumIsAddedShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id_list_shrink is not None:
            result['AlbumIdList'] = self.album_id_list_shrink
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumIdList') is not None:
            self.album_id_list_shrink = m.get('AlbumIdList')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListAlbumIsAddedResponseBodyResult(TeaModel):
    def __init__(self, album_id=None, is_added=None):
        self.album_id = album_id  # type: str
        self.is_added = is_added  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlbumIsAddedResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.is_added is not None:
            result['IsAdded'] = self.is_added
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('IsAdded') is not None:
            self.is_added = m.get('IsAdded')
        return self


class ListAlbumIsAddedResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListAlbumIsAddedResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlbumIsAddedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAlbumIsAddedResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAlbumIsAddedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlbumIsAddedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlbumIsAddedResponse, self).to_map()
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
            temp_model = ListAlbumIsAddedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCateContentHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateContentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCateContentRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateContentRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListCateContentRequestRequest(TeaModel):
    def __init__(self, cate_id=None, is_album=None, page_num=None, page_size=None, sort_by=None, sort_order=None):
        self.cate_id = cate_id  # type: long
        self.is_album = is_album  # type: bool
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.sort_order = sort_order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateContentRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.is_album is not None:
            result['IsAlbum'] = self.is_album
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('IsAlbum') is not None:
            self.is_album = m.get('IsAlbum')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListCateContentRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateContentRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListCateContentRequest(TeaModel):
    def __init__(self, device_info=None, request=None, user_info=None):
        self.device_info = device_info  # type: ListCateContentRequestDeviceInfo
        self.request = request  # type: ListCateContentRequestRequest
        self.user_info = user_info  # type: ListCateContentRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListCateContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListCateContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = ListCateContentRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = ListCateContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListCateContentShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.request_shrink = request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateContentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListCateContentResponseBodyResultOpenDataItemListAuthorsCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateContentResponseBodyResultOpenDataItemListAuthorsCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListCateContentResponseBodyResultOpenDataItemListAuthors(TeaModel):
    def __init__(self, author_types=None, cover=None, description=None, gender=None, id=None, online=None,
                 raw_id=None, source=None, title=None):
        self.author_types = author_types  # type: list[str]
        self.cover = cover  # type: ListCateContentResponseBodyResultOpenDataItemListAuthorsCover
        self.description = description  # type: str
        self.gender = gender  # type: str
        self.id = id  # type: long
        self.online = online  # type: bool
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ListCateContentResponseBodyResultOpenDataItemListAuthors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = ListCateContentResponseBodyResultOpenDataItemListAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListCateContentResponseBodyResultOpenDataItemListCover(TeaModel):
    def __init__(self, img=None, large=None, mediam=None, medium=None, small=None, can_resize=None):
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str
        self.can_resize = can_resize  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateContentResponseBodyResultOpenDataItemListCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        if self.can_resize is not None:
            result['canResize'] = self.can_resize
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        if m.get('canResize') is not None:
            self.can_resize = m.get('canResize')
        return self


class ListCateContentResponseBodyResultOpenDataItemList(TeaModel):
    def __init__(self, alias=None, audition=None, authors=None, category=None, charge=None, comm_cate_id=None,
                 cover=None, description=None, hot_score=None, item_type=None, raw_id=None, source=None, title=None,
                 type=None, valid=None, id=None):
        self.alias = alias  # type: list[str]
        self.audition = audition  # type: bool
        self.authors = authors  # type: list[ListCateContentResponseBodyResultOpenDataItemListAuthors]
        self.category = category  # type: str
        self.charge = charge  # type: bool
        self.comm_cate_id = comm_cate_id  # type: str
        self.cover = cover  # type: ListCateContentResponseBodyResultOpenDataItemListCover
        self.description = description  # type: str
        self.hot_score = hot_score  # type: float
        self.item_type = item_type  # type: str
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str
        self.id = id  # type: long

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ListCateContentResponseBodyResultOpenDataItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListCateContentResponseBodyResultOpenDataItemListAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListCateContentResponseBodyResultOpenDataItemListCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListCateContentResponseBodyResult(TeaModel):
    def __init__(self, current_page_num=None, open_data_item_list=None, page_size=None, total_size=None):
        self.current_page_num = current_page_num  # type: int
        self.open_data_item_list = open_data_item_list  # type: list[ListCateContentResponseBodyResultOpenDataItemList]
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: long

    def validate(self):
        if self.open_data_item_list:
            for k in self.open_data_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCateContentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['OpenDataItemList'] = []
        if self.open_data_item_list is not None:
            for k in self.open_data_item_list:
                result['OpenDataItemList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.open_data_item_list = []
        if m.get('OpenDataItemList') is not None:
            for k in m.get('OpenDataItemList'):
                temp_model = ListCateContentResponseBodyResultOpenDataItemList()
                self.open_data_item_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListCateContentResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: ListCateContentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListCateContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListCateContentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListCateContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCateContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCateContentResponse, self).to_map()
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
            temp_model = ListCateContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCateInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCateInfoRequest(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCateInfoResponseBodyResult(TeaModel):
    def __init__(self, cate_id=None, cate_name=None, parent_cate_id=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.parent_cate_id = parent_cate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCateInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCateInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListCateInfoResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCateInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCateInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCateInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCateInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCateInfoResponse, self).to_map()
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
            temp_model = ListCateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommonCateFirstFloorHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonCateFirstFloorHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCommonCateFirstFloorRequest(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonCateFirstFloorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCommonCateFirstFloorResponseBodyResult(TeaModel):
    def __init__(self, cate_id=None, cate_name=None, parent_cate_id=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.parent_cate_id = parent_cate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonCateFirstFloorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCommonCateFirstFloorResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListCommonCateFirstFloorResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCommonCateFirstFloorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCommonCateFirstFloorResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCommonCateFirstFloorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCommonCateFirstFloorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCommonCateFirstFloorResponse, self).to_map()
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
            temp_model = ListCommonCateFirstFloorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommonCateSecondFloorHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonCateSecondFloorHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCommonCateSecondFloorRequest(TeaModel):
    def __init__(self, parent_cate_id=None):
        self.parent_cate_id = parent_cate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonCateSecondFloorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCommonCateSecondFloorResponseBodyResult(TeaModel):
    def __init__(self, cate_id=None, cate_name=None, parent_cate_id=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.parent_cate_id = parent_cate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommonCateSecondFloorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCommonCateSecondFloorResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListCommonCateSecondFloorResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCommonCateSecondFloorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCommonCateSecondFloorResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCommonCateSecondFloorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCommonCateSecondFloorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCommonCateSecondFloorResponse, self).to_map()
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
            temp_model = ListCommonCateSecondFloorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceBasicInfoHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceBasicInfoHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDeviceBasicInfoRequestDeviceInfos(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id_type=None, ids=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id_type = id_type  # type: str
        self.ids = ids  # type: list[str]
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceBasicInfoRequestDeviceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceBasicInfoRequest(TeaModel):
    def __init__(self, device_infos=None):
        self.device_infos = device_infos  # type: ListDeviceBasicInfoRequestDeviceInfos

    def validate(self):
        if self.device_infos:
            self.device_infos.validate()

    def to_map(self):
        _map = super(ListDeviceBasicInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_infos is not None:
            result['DeviceInfos'] = self.device_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            temp_model = ListDeviceBasicInfoRequestDeviceInfos()
            self.device_infos = temp_model.from_map(m['DeviceInfos'])
        return self


class ListDeviceBasicInfoShrinkRequest(TeaModel):
    def __init__(self, device_infos_shrink=None):
        self.device_infos_shrink = device_infos_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceBasicInfoShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_infos_shrink is not None:
            result['DeviceInfos'] = self.device_infos_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            self.device_infos_shrink = m.get('DeviceInfos')
        return self


class ListDeviceBasicInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, ResultValue]

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(ListDeviceBasicInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['Result'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = {}
        if m.get('Result') is not None:
            for k, v in m.get('Result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListDeviceBasicInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeviceBasicInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceBasicInfoResponse, self).to_map()
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
            temp_model = ListDeviceBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceByUserIdHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDeviceByUserIdRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceByUserIdRequest(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: ListDeviceByUserIdRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = ListDeviceByUserIdRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListDeviceByUserIdShrinkRequest(TeaModel):
    def __init__(self, user_info_shrink=None):
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListDeviceByUserIdResponseBodyResultDeviceUnionIds(TeaModel):
    def __init__(self, device_union_id=None, organization_id=None):
        self.device_union_id = device_union_id  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdResponseBodyResultDeviceUnionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceByUserIdResponseBodyResult(TeaModel):
    def __init__(self, device_open_id=None, device_union_ids=None):
        self.device_open_id = device_open_id  # type: str
        self.device_union_ids = device_union_ids  # type: list[ListDeviceByUserIdResponseBodyResultDeviceUnionIds]

    def validate(self):
        if self.device_union_ids:
            for k in self.device_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = ListDeviceByUserIdResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListDeviceByUserIdResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDeviceByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeviceByUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdResponse, self).to_map()
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
            temp_model = ListDeviceByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceByUserIdAndChanelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDeviceByUserIdAndChanelRequestChannelInfo(TeaModel):
    def __init__(self, channel=None, ext_info=None):
        self.channel = channel  # type: str
        self.ext_info = ext_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelRequestChannelInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class ListDeviceByUserIdAndChanelRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceByUserIdAndChanelRequest(TeaModel):
    def __init__(self, channel_info=None, user_info=None):
        self.channel_info = channel_info  # type: ListDeviceByUserIdAndChanelRequestChannelInfo
        self.user_info = user_info  # type: ListDeviceByUserIdAndChanelRequestUserInfo

    def validate(self):
        if self.channel_info:
            self.channel_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info is not None:
            result['ChannelInfo'] = self.channel_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            temp_model = ListDeviceByUserIdAndChanelRequestChannelInfo()
            self.channel_info = temp_model.from_map(m['ChannelInfo'])
        if m.get('UserInfo') is not None:
            temp_model = ListDeviceByUserIdAndChanelRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListDeviceByUserIdAndChanelShrinkRequest(TeaModel):
    def __init__(self, channel_info_shrink=None, user_info_shrink=None):
        self.channel_info_shrink = channel_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info_shrink is not None:
            result['ChannelInfo'] = self.channel_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            self.channel_info_shrink = m.get('ChannelInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds(TeaModel):
    def __init__(self, device_union_id=None, organization_id=None):
        self.device_union_id = device_union_id  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceByUserIdAndChanelResponseBodyResult(TeaModel):
    def __init__(self, device_open_id=None, device_union_ids=None):
        self.device_open_id = device_open_id  # type: str
        self.device_union_ids = device_union_ids  # type: list[ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds]

    def validate(self):
        if self.device_union_ids:
            for k in self.device_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdAndChanelResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListDeviceByUserIdAndChanelResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDeviceByUserIdAndChanelResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdAndChanelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeviceByUserIdAndChanelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceByUserIdAndChanelResponse, self).to_map()
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
            temp_model = ListDeviceByUserIdAndChanelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceIdByIdentitiesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceIdByIdentitiesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDeviceIdByIdentitiesRequest(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, identity_ids=None, identity_type=None, product_key=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.identity_ids = identity_ids  # type: list[str]
        self.identity_type = identity_type  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceIdByIdentitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.identity_ids is not None:
            result['IdentityIds'] = self.identity_ids
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityIds') is not None:
            self.identity_ids = m.get('IdentityIds')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListDeviceIdByIdentitiesShrinkRequest(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, identity_ids_shrink=None, identity_type=None,
                 product_key=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.identity_ids_shrink = identity_ids_shrink  # type: str
        self.identity_type = identity_type  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceIdByIdentitiesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.identity_ids_shrink is not None:
            result['IdentityIds'] = self.identity_ids_shrink
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityIds') is not None:
            self.identity_ids_shrink = m.get('IdentityIds')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListDeviceIdByIdentitiesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, ResultValue]

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(ListDeviceIdByIdentitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['Result'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = {}
        if m.get('Result') is not None:
            for k, v in m.get('Result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListDeviceIdByIdentitiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeviceIdByIdentitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceIdByIdentitiesResponse, self).to_map()
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
            temp_model = ListDeviceIdByIdentitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMusicHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMusicHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListMusicRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMusicRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListMusicRequestPayload(TeaModel):
    def __init__(self, current_page=None, music_id=None, music_name=None, music_type=None, music_type_name=None,
                 page_size=None):
        self.current_page = current_page  # type: int
        self.music_id = music_id  # type: long
        self.music_name = music_name  # type: str
        self.music_type = music_type  # type: long
        self.music_type_name = music_type_name  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMusicRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMusicRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMusicRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListMusicRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: ListMusicRequestDeviceInfo
        self.payload = payload  # type: ListMusicRequestPayload
        self.user_info = user_info  # type: ListMusicRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListMusicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListMusicRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = ListMusicRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListMusicRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListMusicShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMusicShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListMusicResponseBodyResultModel(TeaModel):
    def __init__(self, music_id=None, music_name=None, music_type=None, music_type_name=None, music_url=None):
        self.music_id = music_id  # type: long
        self.music_name = music_name  # type: str
        self.music_type = music_type  # type: long
        self.music_type_name = music_type_name  # type: str
        self.music_url = music_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMusicResponseBodyResultModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class ListMusicResponseBodyResult(TeaModel):
    def __init__(self, current_page=None, model=None, page_count=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.model = model  # type: list[ListMusicResponseBodyResultModel]
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMusicResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListMusicResponseBodyResultModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMusicResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ListMusicResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListMusicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListMusicResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListMusicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMusicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMusicResponse, self).to_map()
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
            temp_model = ListMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPlayHistoryHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPlayHistoryHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListPlayHistoryRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPlayHistoryRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListPlayHistoryRequestRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, type=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPlayHistoryRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPlayHistoryRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPlayHistoryRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListPlayHistoryRequest(TeaModel):
    def __init__(self, device_info=None, request=None, user_info=None):
        self.device_info = device_info  # type: ListPlayHistoryRequestDeviceInfo
        self.request = request  # type: ListPlayHistoryRequestRequest
        self.user_info = user_info  # type: ListPlayHistoryRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListPlayHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListPlayHistoryRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = ListPlayHistoryRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = ListPlayHistoryRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListPlayHistoryShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.request_shrink = request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPlayHistoryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListPlayHistoryResponseBodyResultAuthorsCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPlayHistoryResponseBodyResultAuthorsCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListPlayHistoryResponseBodyResultAuthors(TeaModel):
    def __init__(self, author_types=None, cover=None, description=None, gender=None, id=None, online=None,
                 raw_id=None, source=None, title=None):
        self.author_types = author_types  # type: list[str]
        self.cover = cover  # type: ListPlayHistoryResponseBodyResultAuthorsCover
        self.description = description  # type: str
        self.gender = gender  # type: str
        self.id = id  # type: long
        self.online = online  # type: bool
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ListPlayHistoryResponseBodyResultAuthors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = ListPlayHistoryResponseBodyResultAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListPlayHistoryResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPlayHistoryResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListPlayHistoryResponseBodyResult(TeaModel):
    def __init__(self, alias=None, audition=None, authors=None, category=None, charge=None, comm_cate_id=None,
                 cover=None, description=None, hot_score=None, id=None, item_type=None, source=None, title=None, type=None,
                 valid=None):
        self.alias = alias  # type: list[str]
        self.audition = audition  # type: bool
        self.authors = authors  # type: list[ListPlayHistoryResponseBodyResultAuthors]
        self.category = category  # type: str
        self.charge = charge  # type: bool
        self.comm_cate_id = comm_cate_id  # type: long
        self.cover = cover  # type: ListPlayHistoryResponseBodyResultCover
        self.description = description  # type: str
        self.hot_score = hot_score  # type: float
        self.id = id  # type: long
        self.item_type = item_type  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ListPlayHistoryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListPlayHistoryResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListPlayHistoryResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class ListPlayHistoryResponseBody(TeaModel):
    def __init__(self, code=None, message=None, result=None, request_id=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.result = result  # type: list[ListPlayHistoryResponseBodyResult]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPlayHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPlayHistoryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListPlayHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPlayHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPlayHistoryResponse, self).to_map()
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
            temp_model = ListPlayHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecommendContentHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecommendContentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListRecommendContentRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecommendContentRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRecommendContentRequestRequest(TeaModel):
    def __init__(self, count=None, type=None):
        self.count = count  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecommendContentRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecommendContentRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecommendContentRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRecommendContentRequest(TeaModel):
    def __init__(self, device_info=None, request=None, user_info=None):
        self.device_info = device_info  # type: ListRecommendContentRequestDeviceInfo
        self.request = request  # type: ListRecommendContentRequestRequest
        self.user_info = user_info  # type: ListRecommendContentRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListRecommendContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListRecommendContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = ListRecommendContentRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = ListRecommendContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListRecommendContentShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.request_shrink = request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecommendContentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListRecommendContentResponseBodyResultAuthorsCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecommendContentResponseBodyResultAuthorsCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListRecommendContentResponseBodyResultAuthors(TeaModel):
    def __init__(self, author_types=None, cover=None, description=None, gender=None, id=None, online=None,
                 raw_id=None, source=None, title=None):
        self.author_types = author_types  # type: list[str]
        self.cover = cover  # type: ListRecommendContentResponseBodyResultAuthorsCover
        self.description = description  # type: str
        self.gender = gender  # type: str
        self.id = id  # type: long
        self.online = online  # type: bool
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ListRecommendContentResponseBodyResultAuthors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = ListRecommendContentResponseBodyResultAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListRecommendContentResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecommendContentResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListRecommendContentResponseBodyResult(TeaModel):
    def __init__(self, alias=None, audition=None, authors=None, category=None, charge=None, comm_cate_id=None,
                 cover=None, description=None, hot_score=None, id=None, item_type=None, raw_id=None, source=None,
                 title=None, type=None, valid=None):
        self.alias = alias  # type: list[str]
        self.audition = audition  # type: bool
        self.authors = authors  # type: list[ListRecommendContentResponseBodyResultAuthors]
        self.category = category  # type: str
        self.charge = charge  # type: bool
        self.comm_cate_id = comm_cate_id  # type: long
        self.cover = cover  # type: ListRecommendContentResponseBodyResultCover
        self.description = description  # type: str
        self.hot_score = hot_score  # type: float
        self.id = id  # type: long
        self.item_type = item_type  # type: str
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ListRecommendContentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListRecommendContentResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListRecommendContentResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class ListRecommendContentResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRecommendContentResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRecommendContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRecommendContentResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRecommendContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRecommendContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRecommendContentResponse, self).to_map()
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
            temp_model = ListRecommendContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListSubRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListSubRequestPage(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubRequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListSubRequest(TeaModel):
    def __init__(self, device_info=None, page=None, user_info=None):
        self.device_info = device_info  # type: ListSubRequestDeviceInfo
        self.page = page  # type: ListSubRequestPage
        self.user_info = user_info  # type: ListSubRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.page:
            self.page.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListSubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListSubRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Page') is not None:
            temp_model = ListSubRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('UserInfo') is not None:
            temp_model = ListSubRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListSubShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, page_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.page_shrink = page_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListSubResponseBodyResultDataListScheduleInfo(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubResponseBodyResultDataListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListSubResponseBodyResultDataList(TeaModel):
    def __init__(self, album_id=None, cover_url=None, daily_study_cnt=None, device_id=None, id=None, play_mode=None,
                 schedule_info=None, title=None, user_id=None):
        self.album_id = album_id  # type: str
        self.cover_url = cover_url  # type: str
        self.daily_study_cnt = daily_study_cnt  # type: int
        self.device_id = device_id  # type: str
        self.id = id  # type: long
        self.play_mode = play_mode  # type: str
        self.schedule_info = schedule_info  # type: ListSubResponseBodyResultDataListScheduleInfo
        self.title = title  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(ListSubResponseBodyResultDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.daily_study_cnt is not None:
            result['DailyStudyCnt'] = self.daily_study_cnt
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('ScheduleInfo') is not None:
            temp_model = ListSubResponseBodyResultDataListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListSubResponseBodyResult(TeaModel):
    def __init__(self, data_list=None, has_next=None, total_count=None, total_page_count=None):
        self.data_list = data_list  # type: list[ListSubResponseBodyResultDataList]
        self.has_next = has_next  # type: bool
        self.total_count = total_count  # type: long
        self.total_page_count = total_page_count  # type: int

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListSubResponseBodyResultDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        return self


class ListSubResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ListSubResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListSubResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListSubResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListSubResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubResponse, self).to_map()
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
            temp_model = ListSubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubAlbumHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubAlbumHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListSubAlbumRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubAlbumRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListSubAlbumRequestQuerySubscriptionAlbumRequestPage(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubAlbumRequestQuerySubscriptionAlbumRequestPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubAlbumRequestQuerySubscriptionAlbumRequest(TeaModel):
    def __init__(self, album_id=None, category_id=None, page=None, title=None):
        self.album_id = album_id  # type: str
        self.category_id = category_id  # type: int
        self.page = page  # type: ListSubAlbumRequestQuerySubscriptionAlbumRequestPage
        self.title = title  # type: str

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListSubAlbumRequestQuerySubscriptionAlbumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Page') is not None:
            temp_model = ListSubAlbumRequestQuerySubscriptionAlbumRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListSubAlbumRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubAlbumRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListSubAlbumRequest(TeaModel):
    def __init__(self, device_info=None, query_subscription_album_request=None, user_info=None):
        self.device_info = device_info  # type: ListSubAlbumRequestDeviceInfo
        # request
        self.query_subscription_album_request = query_subscription_album_request  # type: ListSubAlbumRequestQuerySubscriptionAlbumRequest
        self.user_info = user_info  # type: ListSubAlbumRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.query_subscription_album_request:
            self.query_subscription_album_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListSubAlbumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.query_subscription_album_request is not None:
            result['QuerySubscriptionAlbumRequest'] = self.query_subscription_album_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListSubAlbumRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('QuerySubscriptionAlbumRequest') is not None:
            temp_model = ListSubAlbumRequestQuerySubscriptionAlbumRequest()
            self.query_subscription_album_request = temp_model.from_map(m['QuerySubscriptionAlbumRequest'])
        if m.get('UserInfo') is not None:
            temp_model = ListSubAlbumRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListSubAlbumShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, query_subscription_album_request_shrink=None,
                 user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        # request
        self.query_subscription_album_request_shrink = query_subscription_album_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubAlbumShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.query_subscription_album_request_shrink is not None:
            result['QuerySubscriptionAlbumRequest'] = self.query_subscription_album_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('QuerySubscriptionAlbumRequest') is not None:
            self.query_subscription_album_request_shrink = m.get('QuerySubscriptionAlbumRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListSubAlbumResponseBodyResultDataListScheduleInfo(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None, schedule_id=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.schedule_id = schedule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubAlbumResponseBodyResultDataListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        return self


class ListSubAlbumResponseBodyResultDataList(TeaModel):
    def __init__(self, album_id=None, category_id=None, cover_url=None, id=None, is_added=None, schedule_info=None,
                 sequence=None, title=None, total_episode=None):
        self.album_id = album_id  # type: str
        self.category_id = category_id  # type: int
        self.cover_url = cover_url  # type: str
        self.id = id  # type: long
        self.is_added = is_added  # type: bool
        self.schedule_info = schedule_info  # type: ListSubAlbumResponseBodyResultDataListScheduleInfo
        self.sequence = sequence  # type: long
        self.title = title  # type: str
        self.total_episode = total_episode  # type: int

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(ListSubAlbumResponseBodyResultDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.id is not None:
            result['Id'] = self.id
        if self.is_added is not None:
            result['IsAdded'] = self.is_added
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.title is not None:
            result['Title'] = self.title
        if self.total_episode is not None:
            result['TotalEpisode'] = self.total_episode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsAdded') is not None:
            self.is_added = m.get('IsAdded')
        if m.get('ScheduleInfo') is not None:
            temp_model = ListSubAlbumResponseBodyResultDataListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TotalEpisode') is not None:
            self.total_episode = m.get('TotalEpisode')
        return self


class ListSubAlbumResponseBodyResult(TeaModel):
    def __init__(self, data_list=None, has_next=None, total_count=None, total_page_count=None):
        self.data_list = data_list  # type: list[ListSubAlbumResponseBodyResultDataList]
        self.has_next = has_next  # type: bool
        self.total_count = total_count  # type: int
        self.total_page_count = total_page_count  # type: int

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubAlbumResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListSubAlbumResponseBodyResultDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        return self


class ListSubAlbumResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ListSubAlbumResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListSubAlbumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListSubAlbumResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListSubAlbumResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubAlbumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubAlbumResponse, self).to_map()
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
            temp_model = ListSubAlbumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionAlbumCategoryHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionAlbumCategoryHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListSubscriptionAlbumCategoryRequest(TeaModel):
    def __init__(self, category_name=None):
        self.category_name = category_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionAlbumCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class ListSubscriptionAlbumCategoryResponseBodyResult(TeaModel):
    def __init__(self, category_id=None, category_name=None):
        self.category_id = category_id  # type: str
        self.category_name = category_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionAlbumCategoryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class ListSubscriptionAlbumCategoryResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListSubscriptionAlbumCategoryResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubscriptionAlbumCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListSubscriptionAlbumCategoryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSubscriptionAlbumCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubscriptionAlbumCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubscriptionAlbumCategoryResponse, self).to_map()
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
            temp_model = ListSubscriptionAlbumCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserMessageHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserMessageHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListUserMessageRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserMessageRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListUserMessageRequest(TeaModel):
    def __init__(self, before_time=None, user_info=None, limit=None):
        self.before_time = before_time  # type: str
        self.user_info = user_info  # type: ListUserMessageRequestUserInfo
        self.limit = limit  # type: int

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListUserMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('UserInfo') is not None:
            temp_model = ListUserMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class ListUserMessageShrinkRequest(TeaModel):
    def __init__(self, before_time=None, user_info_shrink=None, limit=None):
        self.before_time = before_time  # type: str
        self.user_info_shrink = user_info_shrink  # type: str
        self.limit = limit  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class ListUserMessageResponseBodyResult(TeaModel):
    def __init__(self, content=None, device_name=None, gmt_create=None, id=None, pic=None, source=None,
                 source_uuid=None, status=None, type=None, url=None):
        self.content = content  # type: str
        self.device_name = device_name  # type: str
        self.gmt_create = gmt_create  # type: str
        self.id = id  # type: str
        self.pic = pic  # type: str
        self.source = source  # type: str
        self.source_uuid = source_uuid  # type: str
        self.status = status  # type: int
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserMessageResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.pic is not None:
            result['Pic'] = self.pic
        if self.source is not None:
            result['Source'] = self.source
        if self.source_uuid is not None:
            result['SourceUuid'] = self.source_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Pic') is not None:
            self.pic = m.get('Pic')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUuid') is not None:
            self.source_uuid = m.get('SourceUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListUserMessageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: list[ListUserMessageResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListUserMessageResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListUserMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserMessageResponse, self).to_map()
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
            temp_model = ListUserMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PlayAndPauseControlHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayAndPauseControlHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PlayAndPauseControlRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayAndPauseControlRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PlayAndPauseControlRequestOpenPlayAndPauseControlParam(TeaModel):
    def __init__(self, open_play_and_pause_command=None):
        self.open_play_and_pause_command = open_play_and_pause_command  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayAndPauseControlRequestOpenPlayAndPauseControlParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_play_and_pause_command is not None:
            result['OpenPlayAndPauseCommand'] = self.open_play_and_pause_command
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenPlayAndPauseCommand') is not None:
            self.open_play_and_pause_command = m.get('OpenPlayAndPauseCommand')
        return self


class PlayAndPauseControlRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayAndPauseControlRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PlayAndPauseControlRequest(TeaModel):
    def __init__(self, device_info=None, open_play_and_pause_control_param=None, user_info=None):
        self.device_info = device_info  # type: PlayAndPauseControlRequestDeviceInfo
        self.open_play_and_pause_control_param = open_play_and_pause_control_param  # type: PlayAndPauseControlRequestOpenPlayAndPauseControlParam
        self.user_info = user_info  # type: PlayAndPauseControlRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_play_and_pause_control_param:
            self.open_play_and_pause_control_param.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(PlayAndPauseControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_play_and_pause_control_param is not None:
            result['OpenPlayAndPauseControlParam'] = self.open_play_and_pause_control_param.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PlayAndPauseControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenPlayAndPauseControlParam') is not None:
            temp_model = PlayAndPauseControlRequestOpenPlayAndPauseControlParam()
            self.open_play_and_pause_control_param = temp_model.from_map(m['OpenPlayAndPauseControlParam'])
        if m.get('UserInfo') is not None:
            temp_model = PlayAndPauseControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PlayAndPauseControlShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_play_and_pause_control_param_shrink=None,
                 user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_play_and_pause_control_param_shrink = open_play_and_pause_control_param_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayAndPauseControlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_play_and_pause_control_param_shrink is not None:
            result['OpenPlayAndPauseControlParam'] = self.open_play_and_pause_control_param_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenPlayAndPauseControlParam') is not None:
            self.open_play_and_pause_control_param_shrink = m.get('OpenPlayAndPauseControlParam')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PlayAndPauseControlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayAndPauseControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PlayAndPauseControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PlayAndPauseControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PlayAndPauseControlResponse, self).to_map()
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
            temp_model = PlayAndPauseControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PlayModeControlHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayModeControlHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PlayModeControlRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayModeControlRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PlayModeControlRequestOpenPlayModeControlRequest(TeaModel):
    def __init__(self, open_play_mode=None):
        self.open_play_mode = open_play_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayModeControlRequestOpenPlayModeControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_play_mode is not None:
            result['OpenPlayMode'] = self.open_play_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenPlayMode') is not None:
            self.open_play_mode = m.get('OpenPlayMode')
        return self


class PlayModeControlRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayModeControlRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PlayModeControlRequest(TeaModel):
    def __init__(self, device_info=None, open_play_mode_control_request=None, user_info=None):
        self.device_info = device_info  # type: PlayModeControlRequestDeviceInfo
        self.open_play_mode_control_request = open_play_mode_control_request  # type: PlayModeControlRequestOpenPlayModeControlRequest
        self.user_info = user_info  # type: PlayModeControlRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_play_mode_control_request:
            self.open_play_mode_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(PlayModeControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_play_mode_control_request is not None:
            result['OpenPlayModeControlRequest'] = self.open_play_mode_control_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PlayModeControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenPlayModeControlRequest') is not None:
            temp_model = PlayModeControlRequestOpenPlayModeControlRequest()
            self.open_play_mode_control_request = temp_model.from_map(m['OpenPlayModeControlRequest'])
        if m.get('UserInfo') is not None:
            temp_model = PlayModeControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PlayModeControlShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_play_mode_control_request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_play_mode_control_request_shrink = open_play_mode_control_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayModeControlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_play_mode_control_request_shrink is not None:
            result['OpenPlayModeControlRequest'] = self.open_play_mode_control_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenPlayModeControlRequest') is not None:
            self.open_play_mode_control_request_shrink = m.get('OpenPlayModeControlRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PlayModeControlResponseBodyResult(TeaModel):
    def __init__(self, open_play_mode=None):
        self.open_play_mode = open_play_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PlayModeControlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_play_mode is not None:
            result['OpenPlayMode'] = self.open_play_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenPlayMode') is not None:
            self.open_play_mode = m.get('OpenPlayMode')
        return self


class PlayModeControlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: PlayModeControlResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(PlayModeControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = PlayModeControlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PlayModeControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PlayModeControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PlayModeControlResponse, self).to_map()
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
            temp_model = PlayModeControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviousAndNextControlHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviousAndNextControlHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PreviousAndNextControlRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviousAndNextControlRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PreviousAndNextControlRequestOpenControlPlayingListRequest(TeaModel):
    def __init__(self, cmd=None, extend_info=None, is_from_device=None):
        self.cmd = cmd  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.is_from_device = is_from_device  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviousAndNextControlRequestOpenControlPlayingListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.is_from_device is not None:
            result['IsFromDevice'] = self.is_from_device
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('IsFromDevice') is not None:
            self.is_from_device = m.get('IsFromDevice')
        return self


class PreviousAndNextControlRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviousAndNextControlRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PreviousAndNextControlRequest(TeaModel):
    def __init__(self, device_info=None, open_control_playing_list_request=None, user_info=None):
        self.device_info = device_info  # type: PreviousAndNextControlRequestDeviceInfo
        self.open_control_playing_list_request = open_control_playing_list_request  # type: PreviousAndNextControlRequestOpenControlPlayingListRequest
        self.user_info = user_info  # type: PreviousAndNextControlRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_control_playing_list_request:
            self.open_control_playing_list_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(PreviousAndNextControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_control_playing_list_request is not None:
            result['OpenControlPlayingListRequest'] = self.open_control_playing_list_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PreviousAndNextControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenControlPlayingListRequest') is not None:
            temp_model = PreviousAndNextControlRequestOpenControlPlayingListRequest()
            self.open_control_playing_list_request = temp_model.from_map(m['OpenControlPlayingListRequest'])
        if m.get('UserInfo') is not None:
            temp_model = PreviousAndNextControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PreviousAndNextControlShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_control_playing_list_request_shrink=None,
                 user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_control_playing_list_request_shrink = open_control_playing_list_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviousAndNextControlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_control_playing_list_request_shrink is not None:
            result['OpenControlPlayingListRequest'] = self.open_control_playing_list_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenControlPlayingListRequest') is not None:
            self.open_control_playing_list_request_shrink = m.get('OpenControlPlayingListRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PreviousAndNextControlResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviousAndNextControlResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class PreviousAndNextControlResponseBodyResult(TeaModel):
    def __init__(self, album_name=None, album_raw_id=None, audio_length=None, copyright=None, cover=None,
                 default_play_order=None, item_url=None, liked=None, lyric_url=None, play_mode=None, pos=None, progress=None,
                 raw_id=None, singer=None, source=None, title=None, type=None, valid=None):
        self.album_name = album_name  # type: str
        self.album_raw_id = album_raw_id  # type: str
        self.audio_length = audio_length  # type: int
        self.copyright = copyright  # type: int
        self.cover = cover  # type: PreviousAndNextControlResponseBodyResultCover
        self.default_play_order = default_play_order  # type: int
        self.item_url = item_url  # type: str
        self.liked = liked  # type: bool
        self.lyric_url = lyric_url  # type: str
        self.play_mode = play_mode  # type: str
        self.pos = pos  # type: int
        self.progress = progress  # type: int
        self.raw_id = raw_id  # type: str
        self.singer = singer  # type: str
        self.source = source  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(PreviousAndNextControlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = PreviousAndNextControlResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class PreviousAndNextControlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: PreviousAndNextControlResponseBodyResult
        self.success = success  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(PreviousAndNextControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = PreviousAndNextControlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PreviousAndNextControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PreviousAndNextControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PreviousAndNextControlResponse, self).to_map()
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
            temp_model = PreviousAndNextControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProgressControlHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProgressControlHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ProgressControlRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProgressControlRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ProgressControlRequestOpenProgressControlRequest(TeaModel):
    def __init__(self, extend_info=None, progress=None):
        self.extend_info = extend_info  # type: dict[str, any]
        self.progress = progress  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProgressControlRequestOpenProgressControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class ProgressControlRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProgressControlRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ProgressControlRequest(TeaModel):
    def __init__(self, device_info=None, open_progress_control_request=None, user_info=None):
        self.device_info = device_info  # type: ProgressControlRequestDeviceInfo
        self.open_progress_control_request = open_progress_control_request  # type: ProgressControlRequestOpenProgressControlRequest
        self.user_info = user_info  # type: ProgressControlRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_progress_control_request:
            self.open_progress_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ProgressControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_progress_control_request is not None:
            result['OpenProgressControlRequest'] = self.open_progress_control_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ProgressControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenProgressControlRequest') is not None:
            temp_model = ProgressControlRequestOpenProgressControlRequest()
            self.open_progress_control_request = temp_model.from_map(m['OpenProgressControlRequest'])
        if m.get('UserInfo') is not None:
            temp_model = ProgressControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ProgressControlShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, open_progress_control_request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.open_progress_control_request_shrink = open_progress_control_request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProgressControlShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_progress_control_request_shrink is not None:
            result['OpenProgressControlRequest'] = self.open_progress_control_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenProgressControlRequest') is not None:
            self.open_progress_control_request_shrink = m.get('OpenProgressControlRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ProgressControlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProgressControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ProgressControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ProgressControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ProgressControlResponse, self).to_map()
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
            temp_model = ProgressControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMusicTypeHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMusicTypeHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryMusicTypeRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMusicTypeRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class QueryMusicTypeRequestPayload(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMusicTypeRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m=None):
        m = m or dict()
        return self


class QueryMusicTypeRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMusicTypeRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class QueryMusicTypeRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: QueryMusicTypeRequestDeviceInfo
        self.payload = payload  # type: QueryMusicTypeRequestPayload
        self.user_info = user_info  # type: QueryMusicTypeRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(QueryMusicTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = QueryMusicTypeRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = QueryMusicTypeRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = QueryMusicTypeRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class QueryMusicTypeShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMusicTypeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class QueryMusicTypeResponseBodyResult(TeaModel):
    def __init__(self, music_type=None, music_type_name=None):
        self.music_type = music_type  # type: long
        self.music_type_name = music_type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMusicTypeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        return self


class QueryMusicTypeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[QueryMusicTypeResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMusicTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryMusicTypeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryMusicTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMusicTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMusicTypeResponse, self).to_map()
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
            temp_model = QueryMusicTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserDeviceListByTmeUserIdHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserDeviceListByTmeUserIdHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryUserDeviceListByTmeUserIdRequest(TeaModel):
    def __init__(self, sp=None, tme_user_id=None):
        self.sp = sp  # type: str
        self.tme_user_id = tme_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserDeviceListByTmeUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sp is not None:
            result['Sp'] = self.sp
        if self.tme_user_id is not None:
            result['TmeUserId'] = self.tme_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        if m.get('TmeUserId') is not None:
            self.tme_user_id = m.get('TmeUserId')
        return self


class QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList(TeaModel):
    def __init__(self, device_name=None, online=None, open_device_id=None):
        self.device_name = device_name  # type: str
        self.online = online  # type: bool
        self.open_device_id = open_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.online is not None:
            result['Online'] = self.online
        if self.open_device_id is not None:
            result['OpenDeviceId'] = self.open_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('OpenDeviceId') is not None:
            self.open_device_id = m.get('OpenDeviceId')
        return self


class QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList(TeaModel):
    def __init__(self, authorized_device_list=None, open_user_id=None, user_nickname=None):
        self.authorized_device_list = authorized_device_list  # type: list[QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList]
        self.open_user_id = open_user_id  # type: str
        self.user_nickname = user_nickname  # type: str

    def validate(self):
        if self.authorized_device_list:
            for k in self.authorized_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizedDeviceList'] = []
        if self.authorized_device_list is not None:
            for k in self.authorized_device_list:
                result['AuthorizedDeviceList'].append(k.to_map() if k else None)
        if self.open_user_id is not None:
            result['OpenUserId'] = self.open_user_id
        if self.user_nickname is not None:
            result['UserNickname'] = self.user_nickname
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.authorized_device_list = []
        if m.get('AuthorizedDeviceList') is not None:
            for k in m.get('AuthorizedDeviceList'):
                temp_model = QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList()
                self.authorized_device_list.append(temp_model.from_map(k))
        if m.get('OpenUserId') is not None:
            self.open_user_id = m.get('OpenUserId')
        if m.get('UserNickname') is not None:
            self.user_nickname = m.get('UserNickname')
        return self


class QueryUserDeviceListByTmeUserIdResponseBodyResult(TeaModel):
    def __init__(self, aligenie_user_info_list=None, encode_key=None, encode_type=None, sp=None):
        self.aligenie_user_info_list = aligenie_user_info_list  # type: list[QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList]
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.sp = sp  # type: str

    def validate(self):
        if self.aligenie_user_info_list:
            for k in self.aligenie_user_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUserDeviceListByTmeUserIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AligenieUserInfoList'] = []
        if self.aligenie_user_info_list is not None:
            for k in self.aligenie_user_info_list:
                result['AligenieUserInfoList'].append(k.to_map() if k else None)
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.sp is not None:
            result['Sp'] = self.sp
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aligenie_user_info_list = []
        if m.get('AligenieUserInfoList') is not None:
            for k in m.get('AligenieUserInfoList'):
                temp_model = QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList()
                self.aligenie_user_info_list.append(temp_model.from_map(k))
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        return self


class QueryUserDeviceListByTmeUserIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryUserDeviceListByTmeUserIdResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryUserDeviceListByTmeUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserDeviceListByTmeUserIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserDeviceListByTmeUserIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryUserDeviceListByTmeUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserDeviceListByTmeUserIdResponse, self).to_map()
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
            temp_model = QueryUserDeviceListByTmeUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMessageHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReadMessageHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ReadMessageRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReadMessageRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ReadMessageRequest(TeaModel):
    def __init__(self, message_id=None, user_info=None):
        self.message_id = message_id  # type: long
        self.user_info = user_info  # type: ReadMessageRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ReadMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('UserInfo') is not None:
            temp_model = ReadMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ReadMessageShrinkRequest(TeaModel):
    def __init__(self, message_id=None, user_info_shrink=None):
        self.message_id = message_id  # type: long
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReadMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ReadMessageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReadMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ReadMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReadMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReadMessageResponse, self).to_map()
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
            temp_model = ReadMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScanCodeBindHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScanCodeBindHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ScanCodeBindRequestBindReq(TeaModel):
    def __init__(self, client_id=None, code=None, ext_info=None):
        self.client_id = client_id  # type: str
        # authCode
        self.code = code  # type: str
        self.ext_info = ext_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScanCodeBindRequestBindReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.code is not None:
            result['Code'] = self.code
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class ScanCodeBindRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScanCodeBindRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ScanCodeBindRequest(TeaModel):
    def __init__(self, bind_req=None, user_info=None):
        self.bind_req = bind_req  # type: ScanCodeBindRequestBindReq
        self.user_info = user_info  # type: ScanCodeBindRequestUserInfo

    def validate(self):
        if self.bind_req:
            self.bind_req.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ScanCodeBindRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_req is not None:
            result['BindReq'] = self.bind_req.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindReq') is not None:
            temp_model = ScanCodeBindRequestBindReq()
            self.bind_req = temp_model.from_map(m['BindReq'])
        if m.get('UserInfo') is not None:
            temp_model = ScanCodeBindRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ScanCodeBindShrinkRequest(TeaModel):
    def __init__(self, bind_req_shrink=None, user_info_shrink=None):
        self.bind_req_shrink = bind_req_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScanCodeBindShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_req_shrink is not None:
            result['BindReq'] = self.bind_req_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindReq') is not None:
            self.bind_req_shrink = m.get('BindReq')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ScanCodeBindResponseBodyResult(TeaModel):
    def __init__(self, biz_group=None, biz_type=None, device_open_id=None, user_open_id=None):
        self.biz_group = biz_group  # type: str
        self.biz_type = biz_type  # type: str
        # A963*0158
        self.device_open_id = device_open_id  # type: str
        # DAFE****ce3ej=\
        self.user_open_id = user_open_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScanCodeBindResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class ScanCodeBindResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ScanCodeBindResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ScanCodeBindResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ScanCodeBindResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ScanCodeBindResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScanCodeBindResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScanCodeBindResponse, self).to_map()
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
            temp_model = ScanCodeBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScgSearchHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScgSearchHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ScgSearchRequestScgFilterOffSetParam(TeaModel):
    def __init__(self, limit=None, offset=None):
        self.limit = limit  # type: int
        self.offset = offset  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScgSearchRequestScgFilterOffSetParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.offset is not None:
            result['Offset'] = self.offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        return self


class ScgSearchRequestScgFilterPageParam(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScgSearchRequestScgFilterPageParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ScgSearchRequestScgFilterSortParam(TeaModel):
    def __init__(self, sort_key=None, sort_order=None, sort_text=None):
        self.sort_key = sort_key  # type: str
        self.sort_order = sort_order  # type: str
        self.sort_text = sort_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScgSearchRequestScgFilterSortParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.sort_text is not None:
            result['SortText'] = self.sort_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SortText') is not None:
            self.sort_text = m.get('SortText')
        return self


class ScgSearchRequestScgFilter(TeaModel):
    def __init__(self, off_set_param=None, page_param=None, sort_param=None, use_off_set=None):
        self.off_set_param = off_set_param  # type: ScgSearchRequestScgFilterOffSetParam
        self.page_param = page_param  # type: ScgSearchRequestScgFilterPageParam
        self.sort_param = sort_param  # type: ScgSearchRequestScgFilterSortParam
        self.use_off_set = use_off_set  # type: bool

    def validate(self):
        if self.off_set_param:
            self.off_set_param.validate()
        if self.page_param:
            self.page_param.validate()
        if self.sort_param:
            self.sort_param.validate()

    def to_map(self):
        _map = super(ScgSearchRequestScgFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.off_set_param is not None:
            result['OffSetParam'] = self.off_set_param.to_map()
        if self.page_param is not None:
            result['PageParam'] = self.page_param.to_map()
        if self.sort_param is not None:
            result['SortParam'] = self.sort_param.to_map()
        if self.use_off_set is not None:
            result['UseOffSet'] = self.use_off_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OffSetParam') is not None:
            temp_model = ScgSearchRequestScgFilterOffSetParam()
            self.off_set_param = temp_model.from_map(m['OffSetParam'])
        if m.get('PageParam') is not None:
            temp_model = ScgSearchRequestScgFilterPageParam()
            self.page_param = temp_model.from_map(m['PageParam'])
        if m.get('SortParam') is not None:
            temp_model = ScgSearchRequestScgFilterSortParam()
            self.sort_param = temp_model.from_map(m['SortParam'])
        if m.get('UseOffSet') is not None:
            self.use_off_set = m.get('UseOffSet')
        return self


class ScgSearchRequest(TeaModel):
    def __init__(self, scg_filter=None, topic_id=None):
        self.scg_filter = scg_filter  # type: ScgSearchRequestScgFilter
        self.topic_id = topic_id  # type: str

    def validate(self):
        if self.scg_filter:
            self.scg_filter.validate()

    def to_map(self):
        _map = super(ScgSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scg_filter is not None:
            result['ScgFilter'] = self.scg_filter.to_map()
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScgFilter') is not None:
            temp_model = ScgSearchRequestScgFilter()
            self.scg_filter = temp_model.from_map(m['ScgFilter'])
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class ScgSearchShrinkRequest(TeaModel):
    def __init__(self, scg_filter_shrink=None, topic_id=None):
        self.scg_filter_shrink = scg_filter_shrink  # type: str
        self.topic_id = topic_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScgSearchShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scg_filter_shrink is not None:
            result['ScgFilter'] = self.scg_filter_shrink
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScgFilter') is not None:
            self.scg_filter_shrink = m.get('ScgFilter')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class ScgSearchResponseBodyResultCover(TeaModel):
    def __init__(self, img=None, large=None, medium=None, small=None, can_resize=None):
        self.img = img  # type: str
        self.large = large  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str
        self.can_resize = can_resize  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScgSearchResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        if self.can_resize is not None:
            result['canResize'] = self.can_resize
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        if m.get('canResize') is not None:
            self.can_resize = m.get('canResize')
        return self


class ScgSearchResponseBodyResult(TeaModel):
    def __init__(self, album=None, album_raw_id=None, album_type=None, alias=None, author_ids=None,
                 author_names=None, category=None, content_type=None, cover=None, is_audition=None, is_charge=None,
                 need_charge=None, raw_id=None, singers=None, source=None, support_audition=None, title=None, type=None):
        self.album = album  # type: bool
        self.album_raw_id = album_raw_id  # type: str
        self.album_type = album_type  # type: int
        self.alias = alias  # type: list[str]
        self.author_ids = author_ids  # type: list[long]
        self.author_names = author_names  # type: list[str]
        self.category = category  # type: str
        self.content_type = content_type  # type: str
        self.cover = cover  # type: ScgSearchResponseBodyResultCover
        self.is_audition = is_audition  # type: bool
        self.is_charge = is_charge  # type: str
        self.need_charge = need_charge  # type: bool
        self.raw_id = raw_id  # type: str
        self.singers = singers  # type: str
        self.source = source  # type: str
        self.support_audition = support_audition  # type: bool
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ScgSearchResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album is not None:
            result['Album'] = self.album
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.album_type is not None:
            result['AlbumType'] = self.album_type
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.author_ids is not None:
            result['AuthorIds'] = self.author_ids
        if self.author_names is not None:
            result['AuthorNames'] = self.author_names
        if self.category is not None:
            result['Category'] = self.category
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.is_audition is not None:
            result['IsAudition'] = self.is_audition
        if self.is_charge is not None:
            result['IsCharge'] = self.is_charge
        if self.need_charge is not None:
            result['NeedCharge'] = self.need_charge
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singers is not None:
            result['Singers'] = self.singers
        if self.source is not None:
            result['Source'] = self.source
        if self.support_audition is not None:
            result['SupportAudition'] = self.support_audition
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AlbumType') is not None:
            self.album_type = m.get('AlbumType')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AuthorIds') is not None:
            self.author_ids = m.get('AuthorIds')
        if m.get('AuthorNames') is not None:
            self.author_names = m.get('AuthorNames')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Cover') is not None:
            temp_model = ScgSearchResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('IsAudition') is not None:
            self.is_audition = m.get('IsAudition')
        if m.get('IsCharge') is not None:
            self.is_charge = m.get('IsCharge')
        if m.get('NeedCharge') is not None:
            self.need_charge = m.get('NeedCharge')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singers') is not None:
            self.singers = m.get('Singers')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SupportAudition') is not None:
            self.support_audition = m.get('SupportAudition')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ScgSearchResponseBody(TeaModel):
    def __init__(self, code=None, message=None, page_num=None, page_size=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ScgSearchResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ScgSearchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ScgSearchResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ScgSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScgSearchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScgSearchResponse, self).to_map()
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
            temp_model = ScgSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchContentHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchContentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SearchContentRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchContentRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SearchContentRequestRequest(TeaModel):
    def __init__(self, cate=None, page_num=None, page_size=None, query=None, query_album=None, sub_cate=None):
        self.cate = cate  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.query_album = query_album  # type: bool
        self.sub_cate = sub_cate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchContentRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate is not None:
            result['Cate'] = self.cate
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.query_album is not None:
            result['QueryAlbum'] = self.query_album
        if self.sub_cate is not None:
            result['SubCate'] = self.sub_cate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cate') is not None:
            self.cate = m.get('Cate')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryAlbum') is not None:
            self.query_album = m.get('QueryAlbum')
        if m.get('SubCate') is not None:
            self.sub_cate = m.get('SubCate')
        return self


class SearchContentRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchContentRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SearchContentRequest(TeaModel):
    def __init__(self, device_info=None, request=None, user_info=None):
        self.device_info = device_info  # type: SearchContentRequestDeviceInfo
        self.request = request  # type: SearchContentRequestRequest
        self.user_info = user_info  # type: SearchContentRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(SearchContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = SearchContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = SearchContentRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = SearchContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SearchContentShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, request_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.request_shrink = request_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchContentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SearchContentResponseBodyResultAuthorsCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchContentResponseBodyResultAuthorsCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class SearchContentResponseBodyResultAuthors(TeaModel):
    def __init__(self, author_types=None, cover=None, description=None, gender=None, id=None, online=None,
                 raw_id=None, source=None, title=None):
        self.author_types = author_types  # type: list[str]
        self.cover = cover  # type: SearchContentResponseBodyResultAuthorsCover
        self.description = description  # type: str
        self.gender = gender  # type: str
        self.id = id  # type: long
        self.online = online  # type: bool
        self.raw_id = raw_id  # type: str
        self.source = source  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(SearchContentResponseBodyResultAuthors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = SearchContentResponseBodyResultAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchContentResponseBodyResultCover(TeaModel):
    def __init__(self, can_resize=None, img=None, large=None, mediam=None, medium=None, small=None):
        self.can_resize = can_resize  # type: bool
        self.img = img  # type: str
        self.large = large  # type: str
        self.mediam = mediam  # type: str
        self.medium = medium  # type: str
        self.small = small  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchContentResponseBodyResultCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class SearchContentResponseBodyResult(TeaModel):
    def __init__(self, album_id=None, alias=None, audition=None, authors=None, category=None, charge=None,
                 comm_cate_id=None, cover=None, description=None, duration=None, hot_score=None, id=None, item_type=None,
                 lyric=None, order_index=None, source=None, styles=None, title=None, type=None, valid=None):
        self.album_id = album_id  # type: str
        self.alias = alias  # type: list[str]
        self.audition = audition  # type: bool
        self.authors = authors  # type: list[SearchContentResponseBodyResultAuthors]
        self.category = category  # type: str
        self.charge = charge  # type: bool
        self.comm_cate_id = comm_cate_id  # type: long
        self.cover = cover  # type: SearchContentResponseBodyResultCover
        self.description = description  # type: str
        self.duration = duration  # type: long
        self.hot_score = hot_score  # type: float
        self.id = id  # type: long
        self.item_type = item_type  # type: str
        self.lyric = lyric  # type: str
        self.order_index = order_index  # type: str
        self.source = source  # type: str
        self.styles = styles  # type: list[str]
        self.title = title  # type: str
        self.type = type  # type: str
        self.valid = valid  # type: str

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(SearchContentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        if self.order_index is not None:
            result['OrderIndex'] = self.order_index
        if self.source is not None:
            result['Source'] = self.source
        if self.styles is not None:
            result['Styles'] = self.styles
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = SearchContentResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = SearchContentResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class SearchContentResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: list[SearchContentResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = SearchContentResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class SearchContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchContentResponse, self).to_map()
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
            temp_model = SearchContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SendMessageRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, url=None, user_info=None):
        self.url = url  # type: str
        self.user_info = user_info  # type: SendMessageRequestUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserInfo') is not None:
            temp_model = SendMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(self, url=None, user_info_shrink=None):
        self.url = url  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SendMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMessageResponse, self).to_map()
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeviceSettingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeviceSettingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SetDeviceSettingRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeviceSettingRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SetDeviceSettingRequest(TeaModel):
    def __init__(self, device_info=None, key=None, value=None):
        self.device_info = device_info  # type: SetDeviceSettingRequestDeviceInfo
        self.key = key  # type: str
        self.value = value  # type: any

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super(SetDeviceSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = SetDeviceSettingRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetDeviceSettingShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, key=None, value=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.key = key  # type: str
        self.value = value  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeviceSettingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetDeviceSettingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeviceSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetDeviceSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDeviceSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDeviceSettingResponse, self).to_map()
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
            temp_model = SetDeviceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAligenieUserHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindAligenieUserHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UnbindAligenieUserRequest(TeaModel):
    def __init__(self, login_state_access_token=None):
        self.login_state_access_token = login_state_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindAligenieUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class UnbindAligenieUserResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindAligenieUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindAligenieUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindAligenieUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindAligenieUserResponse, self).to_map()
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
            temp_model = UnbindAligenieUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDeviceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDeviceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UnbindDeviceRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDeviceRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UnbindDeviceRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDeviceRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UnbindDeviceRequest(TeaModel):
    def __init__(self, device_info=None, user_info=None):
        self.device_info = device_info  # type: UnbindDeviceRequestDeviceInfo
        self.user_info = user_info  # type: UnbindDeviceRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(UnbindDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UnbindDeviceRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = UnbindDeviceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UnbindDeviceShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDeviceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UnbindDeviceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UnbindDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindDeviceResponse, self).to_map()
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
            temp_model = UnbindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlarmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateAlarmRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateAlarmRequestPayloadMusicInfo(TeaModel):
    def __init__(self, music_id=None, music_name=None, music_type=None, music_type_name=None, music_url=None):
        self.music_id = music_id  # type: long
        self.music_name = music_name  # type: str
        self.music_type = music_type  # type: long
        self.music_type_name = music_type_name  # type: str
        self.music_url = music_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmRequestPayloadMusicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class UpdateAlarmRequestPayloadScheduleInfoOnce(TeaModel):
    def __init__(self, day=None, hour=None, minute=None, month=None, year=None):
        self.day = day  # type: int
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmRequestPayloadScheduleInfoOnce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class UpdateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(self, hour=None, minute=None):
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class UpdateAlarmRequestPayloadScheduleInfoWeekly(TeaModel):
    def __init__(self, days_of_week=None, hour=None, minute=None):
        self.days_of_week = days_of_week  # type: list[int]
        self.hour = hour  # type: int
        self.minute = minute  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmRequestPayloadScheduleInfoWeekly, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class UpdateAlarmRequestPayloadScheduleInfo(TeaModel):
    def __init__(self, once=None, statutory_working_day=None, type=None, weekly=None):
        self.once = once  # type: UpdateAlarmRequestPayloadScheduleInfoOnce
        self.statutory_working_day = statutory_working_day  # type: UpdateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay
        self.type = type  # type: str
        self.weekly = weekly  # type: UpdateAlarmRequestPayloadScheduleInfoWeekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super(UpdateAlarmRequestPayloadScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class UpdateAlarmRequestPayload(TeaModel):
    def __init__(self, alarm_id=None, music_info=None, schedule_info=None, volume=None):
        self.alarm_id = alarm_id  # type: long
        self.music_info = music_info  # type: UpdateAlarmRequestPayloadMusicInfo
        self.schedule_info = schedule_info  # type: UpdateAlarmRequestPayloadScheduleInfo
        self.volume = volume  # type: int

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(UpdateAlarmRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('MusicInfo') is not None:
            temp_model = UpdateAlarmRequestPayloadMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class UpdateAlarmRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateAlarmRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: UpdateAlarmRequestDeviceInfo
        self.payload = payload  # type: UpdateAlarmRequestPayload
        self.user_info = user_info  # type: UpdateAlarmRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(UpdateAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UpdateAlarmRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = UpdateAlarmRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = UpdateAlarmRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UpdateAlarmShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UpdateAlarmResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAlarmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlarmResponse, self).to_map()
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
            temp_model = UpdateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


