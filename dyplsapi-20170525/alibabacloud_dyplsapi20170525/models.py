# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddAxnTrackNoRequest(TeaModel):
    def __init__(self, owner_id=None, phone_no_x=None, pool_key=None, resource_owner_account=None,
                 resource_owner_id=None, subs_id=None, track_no=None):
        self.owner_id = owner_id  # type: long
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.subs_id = subs_id  # type: str
        self.track_no = track_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAxnTrackNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.track_no is not None:
            result['trackNo'] = self.track_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('trackNo') is not None:
            self.track_no = m.get('trackNo')
        return self


class AddAxnTrackNoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAxnTrackNoResponseBody, self).to_map()
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


class AddAxnTrackNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAxnTrackNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAxnTrackNoResponse, self).to_map()
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
            temp_model = AddAxnTrackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSecretBlacklistRequest(TeaModel):
    def __init__(self, black_no=None, black_type=None, pool_key=None, remark=None, way_control=None):
        self.black_no = black_no  # type: str
        self.black_type = black_type  # type: str
        self.pool_key = pool_key  # type: str
        self.remark = remark  # type: str
        self.way_control = way_control  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSecretBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.way_control is not None:
            result['WayControl'] = self.way_control
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('WayControl') is not None:
            self.way_control = m.get('WayControl')
        return self


class AddSecretBlacklistResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSecretBlacklistResponseBody, self).to_map()
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


class AddSecretBlacklistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddSecretBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSecretBlacklistResponse, self).to_map()
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
            temp_model = AddSecretBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxbRequest(TeaModel):
    def __init__(self, asrmodel_id=None, asrstatus=None, call_display_type=None, call_restrict=None,
                 call_timeout=None, dtmf_config=None, expect_city=None, expiration=None, is_recording_enabled=None, out_id=None,
                 out_order_id=None, owner_id=None, phone_no_a=None, phone_no_b=None, phone_no_x=None, pool_key=None,
                 resource_owner_account=None, resource_owner_id=None, ring_config=None):
        self.asrmodel_id = asrmodel_id  # type: str
        self.asrstatus = asrstatus  # type: bool
        self.call_display_type = call_display_type  # type: int
        self.call_restrict = call_restrict  # type: str
        self.call_timeout = call_timeout  # type: int
        self.dtmf_config = dtmf_config  # type: str
        self.expect_city = expect_city  # type: str
        self.expiration = expiration  # type: str
        self.is_recording_enabled = is_recording_enabled  # type: bool
        self.out_id = out_id  # type: str
        self.out_order_id = out_order_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.ring_config = ring_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.call_timeout is not None:
            result['CallTimeout'] = self.call_timeout
        if self.dtmf_config is not None:
            result['DtmfConfig'] = self.dtmf_config
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('CallTimeout') is not None:
            self.call_timeout = m.get('CallTimeout')
        if m.get('DtmfConfig') is not None:
            self.dtmf_config = m.get('DtmfConfig')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        return self


class BindAxbResponseBodySecretBindDTO(TeaModel):
    def __init__(self, extension=None, secret_no=None, subs_id=None):
        self.extension = extension  # type: str
        self.secret_no = secret_no  # type: str
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxbResponseBodySecretBindDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxbResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_bind_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_bind_dto = secret_bind_dto  # type: BindAxbResponseBodySecretBindDTO

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super(BindAxbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxbResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxbResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindAxbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindAxbResponse, self).to_map()
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
            temp_model = BindAxbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxgRequest(TeaModel):
    def __init__(self, asrmodel_id=None, asrstatus=None, call_display_type=None, call_restrict=None,
                 expect_city=None, expiration=None, group_id=None, is_recording_enabled=None, out_id=None, out_order_id=None,
                 owner_id=None, phone_no_a=None, phone_no_b=None, phone_no_x=None, pool_key=None,
                 resource_owner_account=None, resource_owner_id=None, ring_config=None):
        self.asrmodel_id = asrmodel_id  # type: str
        self.asrstatus = asrstatus  # type: bool
        self.call_display_type = call_display_type  # type: int
        self.call_restrict = call_restrict  # type: str
        self.expect_city = expect_city  # type: str
        self.expiration = expiration  # type: str
        self.group_id = group_id  # type: str
        self.is_recording_enabled = is_recording_enabled  # type: bool
        self.out_id = out_id  # type: str
        self.out_order_id = out_order_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.ring_config = ring_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxgRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        return self


class BindAxgResponseBodySecretBindDTO(TeaModel):
    def __init__(self, extension=None, secret_no=None, subs_id=None):
        self.extension = extension  # type: str
        self.secret_no = secret_no  # type: str
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxgResponseBodySecretBindDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxgResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_bind_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_bind_dto = secret_bind_dto  # type: BindAxgResponseBodySecretBindDTO

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super(BindAxgResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxgResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxgResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindAxgResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindAxgResponse, self).to_map()
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
            temp_model = BindAxgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxnRequest(TeaModel):
    def __init__(self, asrmodel_id=None, asrstatus=None, call_display_type=None, call_restrict=None,
                 call_timeout=None, expect_city=None, expiration=None, is_recording_enabled=None, no_type=None, out_id=None,
                 out_order_id=None, owner_id=None, phone_no_a=None, phone_no_b=None, phone_no_x=None, pool_key=None,
                 resource_owner_account=None, resource_owner_id=None, ring_config=None):
        self.asrmodel_id = asrmodel_id  # type: str
        self.asrstatus = asrstatus  # type: bool
        self.call_display_type = call_display_type  # type: int
        self.call_restrict = call_restrict  # type: str
        self.call_timeout = call_timeout  # type: int
        self.expect_city = expect_city  # type: str
        self.expiration = expiration  # type: str
        self.is_recording_enabled = is_recording_enabled  # type: bool
        self.no_type = no_type  # type: str
        self.out_id = out_id  # type: str
        self.out_order_id = out_order_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.ring_config = ring_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxnRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.call_timeout is not None:
            result['CallTimeout'] = self.call_timeout
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.no_type is not None:
            result['NoType'] = self.no_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('CallTimeout') is not None:
            self.call_timeout = m.get('CallTimeout')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('NoType') is not None:
            self.no_type = m.get('NoType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        return self


class BindAxnResponseBodySecretBindDTO(TeaModel):
    def __init__(self, extension=None, secret_no=None, subs_id=None):
        self.extension = extension  # type: str
        self.secret_no = secret_no  # type: str
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxnResponseBodySecretBindDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxnResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_bind_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_bind_dto = secret_bind_dto  # type: BindAxnResponseBodySecretBindDTO

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super(BindAxnResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxnResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxnResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindAxnResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindAxnResponse, self).to_map()
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
            temp_model = BindAxnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxnExtensionRequest(TeaModel):
    def __init__(self, asrmodel_id=None, asrstatus=None, call_display_type=None, call_restrict=None,
                 expect_city=None, expiration=None, extension=None, is_recording_enabled=None, out_id=None, out_order_id=None,
                 owner_id=None, phone_no_a=None, phone_no_b=None, phone_no_x=None, pool_key=None,
                 resource_owner_account=None, resource_owner_id=None, ring_config=None):
        self.asrmodel_id = asrmodel_id  # type: str
        self.asrstatus = asrstatus  # type: bool
        self.call_display_type = call_display_type  # type: int
        self.call_restrict = call_restrict  # type: str
        self.expect_city = expect_city  # type: str
        self.expiration = expiration  # type: str
        self.extension = extension  # type: str
        self.is_recording_enabled = is_recording_enabled  # type: bool
        self.out_id = out_id  # type: str
        self.out_order_id = out_order_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.ring_config = ring_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxnExtensionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        return self


class BindAxnExtensionResponseBodySecretBindDTO(TeaModel):
    def __init__(self, extension=None, secret_no=None, subs_id=None):
        self.extension = extension  # type: str
        self.secret_no = secret_no  # type: str
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAxnExtensionResponseBodySecretBindDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxnExtensionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_bind_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_bind_dto = secret_bind_dto  # type: BindAxnExtensionResponseBodySecretBindDTO

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super(BindAxnExtensionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxnExtensionResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxnExtensionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindAxnExtensionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindAxnExtensionResponse, self).to_map()
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
            temp_model = BindAxnExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuySecretNoRequest(TeaModel):
    def __init__(self, city=None, display_pool=None, owner_id=None, pool_key=None, resource_owner_account=None,
                 resource_owner_id=None, secret_no=None, spec_id=None):
        self.city = city  # type: str
        self.display_pool = display_pool  # type: bool
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str
        self.spec_id = spec_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuySecretNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.display_pool is not None:
            result['DisplayPool'] = self.display_pool
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('DisplayPool') is not None:
            self.display_pool = m.get('DisplayPool')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class BuySecretNoResponseBodySecretBuyInfoDTO(TeaModel):
    def __init__(self, secret_no=None):
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuySecretNoResponseBodySecretBuyInfoDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BuySecretNoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_buy_info_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_buy_info_dto = secret_buy_info_dto  # type: BuySecretNoResponseBodySecretBuyInfoDTO

    def validate(self):
        if self.secret_buy_info_dto:
            self.secret_buy_info_dto.validate()

    def to_map(self):
        _map = super(BuySecretNoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_buy_info_dto is not None:
            result['SecretBuyInfoDTO'] = self.secret_buy_info_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBuyInfoDTO') is not None:
            temp_model = BuySecretNoResponseBodySecretBuyInfoDTO()
            self.secret_buy_info_dto = temp_model.from_map(m['SecretBuyInfoDTO'])
        return self


class BuySecretNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BuySecretNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BuySecretNoResponse, self).to_map()
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
            temp_model = BuySecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPickUpWaybillRequest(TeaModel):
    def __init__(self, cancel_desc=None, outer_order_code=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cancel_desc = cancel_desc  # type: str
        self.outer_order_code = outer_order_code  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPickUpWaybillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancel_desc is not None:
            result['CancelDesc'] = self.cancel_desc
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CancelDesc') is not None:
            self.cancel_desc = m.get('CancelDesc')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CancelPickUpWaybillResponseBodyData(TeaModel):
    def __init__(self, error_code=None, error_msg=None, message=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPickUpWaybillResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelPickUpWaybillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CancelPickUpWaybillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CancelPickUpWaybillResponseBody, self).to_map()
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
            temp_model = CancelPickUpWaybillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelPickUpWaybillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelPickUpWaybillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelPickUpWaybillResponse, self).to_map()
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
            temp_model = CancelPickUpWaybillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAxgGroupRequest(TeaModel):
    def __init__(self, name=None, numbers=None, owner_id=None, pool_key=None, remark=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.name = name  # type: str
        self.numbers = numbers  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAxgGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateAxgGroupResponseBody(TeaModel):
    def __init__(self, code=None, group_id=None, message=None, request_id=None):
        self.code = code  # type: str
        self.group_id = group_id  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAxgGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAxgGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAxgGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAxgGroupResponse, self).to_map()
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
            temp_model = CreateAxgGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePickUpWaybillRequestConsigneeAddress(TeaModel):
    def __init__(self, address_detail=None, area_name=None, city_name=None, province_name=None, town_name=None):
        self.address_detail = address_detail  # type: str
        self.area_name = area_name  # type: str
        self.city_name = city_name  # type: str
        self.province_name = province_name  # type: str
        self.town_name = town_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillRequestConsigneeAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillRequestGoodsInfos(TeaModel):
    def __init__(self, name=None, quantity=None, weight=None):
        self.name = name  # type: str
        self.quantity = quantity  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillRequestGoodsInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreatePickUpWaybillRequestSendAddress(TeaModel):
    def __init__(self, address_detail=None, area_name=None, city_name=None, province_name=None, town_name=None):
        self.address_detail = address_detail  # type: str
        self.area_name = area_name  # type: str
        self.city_name = city_name  # type: str
        self.province_name = province_name  # type: str
        self.town_name = town_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillRequestSendAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillRequest(TeaModel):
    def __init__(self, appoint_got_end_time=None, appoint_got_start_time=None, biz_type=None,
                 consignee_address=None, consignee_mobile=None, consignee_name=None, consignee_phone=None, cp_code=None,
                 goods_infos=None, order_channels=None, outer_order_code=None, remark=None, send_address=None, send_mobile=None,
                 send_name=None, send_phone=None):
        self.appoint_got_end_time = appoint_got_end_time  # type: str
        self.appoint_got_start_time = appoint_got_start_time  # type: str
        self.biz_type = biz_type  # type: int
        self.consignee_address = consignee_address  # type: CreatePickUpWaybillRequestConsigneeAddress
        self.consignee_mobile = consignee_mobile  # type: str
        self.consignee_name = consignee_name  # type: str
        self.consignee_phone = consignee_phone  # type: str
        self.cp_code = cp_code  # type: str
        self.goods_infos = goods_infos  # type: list[CreatePickUpWaybillRequestGoodsInfos]
        self.order_channels = order_channels  # type: str
        self.outer_order_code = outer_order_code  # type: str
        self.remark = remark  # type: str
        self.send_address = send_address  # type: CreatePickUpWaybillRequestSendAddress
        self.send_mobile = send_mobile  # type: str
        self.send_name = send_name  # type: str
        self.send_phone = send_phone  # type: str

    def validate(self):
        if self.consignee_address:
            self.consignee_address.validate()
        if self.goods_infos:
            for k in self.goods_infos:
                if k:
                    k.validate()
        if self.send_address:
            self.send_address.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time
        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.consignee_address is not None:
            result['ConsigneeAddress'] = self.consignee_address.to_map()
        if self.consignee_mobile is not None:
            result['ConsigneeMobile'] = self.consignee_mobile
        if self.consignee_name is not None:
            result['ConsigneeName'] = self.consignee_name
        if self.consignee_phone is not None:
            result['ConsigneePhone'] = self.consignee_phone
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        result['GoodsInfos'] = []
        if self.goods_infos is not None:
            for k in self.goods_infos:
                result['GoodsInfos'].append(k.to_map() if k else None)
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.send_address is not None:
            result['SendAddress'] = self.send_address.to_map()
        if self.send_mobile is not None:
            result['SendMobile'] = self.send_mobile
        if self.send_name is not None:
            result['SendName'] = self.send_name
        if self.send_phone is not None:
            result['SendPhone'] = self.send_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')
        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ConsigneeAddress') is not None:
            temp_model = CreatePickUpWaybillRequestConsigneeAddress()
            self.consignee_address = temp_model.from_map(m['ConsigneeAddress'])
        if m.get('ConsigneeMobile') is not None:
            self.consignee_mobile = m.get('ConsigneeMobile')
        if m.get('ConsigneeName') is not None:
            self.consignee_name = m.get('ConsigneeName')
        if m.get('ConsigneePhone') is not None:
            self.consignee_phone = m.get('ConsigneePhone')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        self.goods_infos = []
        if m.get('GoodsInfos') is not None:
            for k in m.get('GoodsInfos'):
                temp_model = CreatePickUpWaybillRequestGoodsInfos()
                self.goods_infos.append(temp_model.from_map(k))
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SendAddress') is not None:
            temp_model = CreatePickUpWaybillRequestSendAddress()
            self.send_address = temp_model.from_map(m['SendAddress'])
        if m.get('SendMobile') is not None:
            self.send_mobile = m.get('SendMobile')
        if m.get('SendName') is not None:
            self.send_name = m.get('SendName')
        if m.get('SendPhone') is not None:
            self.send_phone = m.get('SendPhone')
        return self


class CreatePickUpWaybillShrinkRequest(TeaModel):
    def __init__(self, appoint_got_end_time=None, appoint_got_start_time=None, biz_type=None,
                 consignee_address_shrink=None, consignee_mobile=None, consignee_name=None, consignee_phone=None, cp_code=None,
                 goods_infos_shrink=None, order_channels=None, outer_order_code=None, remark=None, send_address_shrink=None,
                 send_mobile=None, send_name=None, send_phone=None):
        self.appoint_got_end_time = appoint_got_end_time  # type: str
        self.appoint_got_start_time = appoint_got_start_time  # type: str
        self.biz_type = biz_type  # type: int
        self.consignee_address_shrink = consignee_address_shrink  # type: str
        self.consignee_mobile = consignee_mobile  # type: str
        self.consignee_name = consignee_name  # type: str
        self.consignee_phone = consignee_phone  # type: str
        self.cp_code = cp_code  # type: str
        self.goods_infos_shrink = goods_infos_shrink  # type: str
        self.order_channels = order_channels  # type: str
        self.outer_order_code = outer_order_code  # type: str
        self.remark = remark  # type: str
        self.send_address_shrink = send_address_shrink  # type: str
        self.send_mobile = send_mobile  # type: str
        self.send_name = send_name  # type: str
        self.send_phone = send_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time
        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.consignee_address_shrink is not None:
            result['ConsigneeAddress'] = self.consignee_address_shrink
        if self.consignee_mobile is not None:
            result['ConsigneeMobile'] = self.consignee_mobile
        if self.consignee_name is not None:
            result['ConsigneeName'] = self.consignee_name
        if self.consignee_phone is not None:
            result['ConsigneePhone'] = self.consignee_phone
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.goods_infos_shrink is not None:
            result['GoodsInfos'] = self.goods_infos_shrink
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.send_address_shrink is not None:
            result['SendAddress'] = self.send_address_shrink
        if self.send_mobile is not None:
            result['SendMobile'] = self.send_mobile
        if self.send_name is not None:
            result['SendName'] = self.send_name
        if self.send_phone is not None:
            result['SendPhone'] = self.send_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')
        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ConsigneeAddress') is not None:
            self.consignee_address_shrink = m.get('ConsigneeAddress')
        if m.get('ConsigneeMobile') is not None:
            self.consignee_mobile = m.get('ConsigneeMobile')
        if m.get('ConsigneeName') is not None:
            self.consignee_name = m.get('ConsigneeName')
        if m.get('ConsigneePhone') is not None:
            self.consignee_phone = m.get('ConsigneePhone')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('GoodsInfos') is not None:
            self.goods_infos_shrink = m.get('GoodsInfos')
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SendAddress') is not None:
            self.send_address_shrink = m.get('SendAddress')
        if m.get('SendMobile') is not None:
            self.send_mobile = m.get('SendMobile')
        if m.get('SendName') is not None:
            self.send_name = m.get('SendName')
        if m.get('SendPhone') is not None:
            self.send_phone = m.get('SendPhone')
        return self


class CreatePickUpWaybillResponseBodyData(TeaModel):
    def __init__(self, cp_code=None, error_code=None, error_msg=None, got_code=None, mail_no=None, success=None):
        self.cp_code = cp_code  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.got_code = got_code  # type: str
        self.mail_no = mail_no  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.got_code is not None:
            result['GotCode'] = self.got_code
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GotCode') is not None:
            self.got_code = m.get('GotCode')
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePickUpWaybillResponseBody(TeaModel):
    def __init__(self, data=None, http_status_code=None, message=None, request_id=None):
        self.data = data  # type: CreatePickUpWaybillResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreatePickUpWaybillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePickUpWaybillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePickUpWaybillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillResponse, self).to_map()
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
            temp_model = CreatePickUpWaybillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo(TeaModel):
    def __init__(self, address_detail=None, area_name=None, city_name=None, province_name=None, town_name=None):
        self.address_detail = address_detail  # type: str
        self.area_name = area_name  # type: str
        self.city_name = city_name  # type: str
        self.province_name = province_name  # type: str
        self.town_name = town_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillPreQueryRequestConsigneeInfo(TeaModel):
    def __init__(self, address_info=None, mobile=None, name=None):
        self.address_info = address_info  # type: CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo
        self.mobile = mobile  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.address_info:
            self.address_info.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryRequestConsigneeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info.to_map()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo()
            self.address_info = temp_model.from_map(m['AddressInfo'])
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo(TeaModel):
    def __init__(self, address_detail=None, area_name=None, city_name=None, province_name=None, town_name=None):
        self.address_detail = address_detail  # type: str
        self.area_name = area_name  # type: str
        self.city_name = city_name  # type: str
        self.province_name = province_name  # type: str
        self.town_name = town_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillPreQueryRequestSenderInfo(TeaModel):
    def __init__(self, address_info=None, mobile=None, name=None):
        self.address_info = address_info  # type: CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo
        self.mobile = mobile  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.address_info:
            self.address_info.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryRequestSenderInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info.to_map()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo()
            self.address_info = temp_model.from_map(m['AddressInfo'])
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePickUpWaybillPreQueryRequest(TeaModel):
    def __init__(self, consignee_info=None, cp_code=None, order_channels=None, outer_order_code=None,
                 pre_weight=None, sender_info=None):
        self.consignee_info = consignee_info  # type: CreatePickUpWaybillPreQueryRequestConsigneeInfo
        self.cp_code = cp_code  # type: str
        self.order_channels = order_channels  # type: str
        self.outer_order_code = outer_order_code  # type: str
        self.pre_weight = pre_weight  # type: str
        self.sender_info = sender_info  # type: CreatePickUpWaybillPreQueryRequestSenderInfo

    def validate(self):
        if self.consignee_info:
            self.consignee_info.validate()
        if self.sender_info:
            self.sender_info.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consignee_info is not None:
            result['ConsigneeInfo'] = self.consignee_info.to_map()
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.pre_weight is not None:
            result['PreWeight'] = self.pre_weight
        if self.sender_info is not None:
            result['SenderInfo'] = self.sender_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsigneeInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestConsigneeInfo()
            self.consignee_info = temp_model.from_map(m['ConsigneeInfo'])
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('PreWeight') is not None:
            self.pre_weight = m.get('PreWeight')
        if m.get('SenderInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestSenderInfo()
            self.sender_info = temp_model.from_map(m['SenderInfo'])
        return self


class CreatePickUpWaybillPreQueryShrinkRequest(TeaModel):
    def __init__(self, consignee_info_shrink=None, cp_code=None, order_channels=None, outer_order_code=None,
                 pre_weight=None, sender_info_shrink=None):
        self.consignee_info_shrink = consignee_info_shrink  # type: str
        self.cp_code = cp_code  # type: str
        self.order_channels = order_channels  # type: str
        self.outer_order_code = outer_order_code  # type: str
        self.pre_weight = pre_weight  # type: str
        self.sender_info_shrink = sender_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consignee_info_shrink is not None:
            result['ConsigneeInfo'] = self.consignee_info_shrink
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.pre_weight is not None:
            result['PreWeight'] = self.pre_weight
        if self.sender_info_shrink is not None:
            result['SenderInfo'] = self.sender_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsigneeInfo') is not None:
            self.consignee_info_shrink = m.get('ConsigneeInfo')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('PreWeight') is not None:
            self.pre_weight = m.get('PreWeight')
        if m.get('SenderInfo') is not None:
            self.sender_info_shrink = m.get('SenderInfo')
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList(TeaModel):
    def __init__(self, end_time=None, select_disable_tip=None, selectable=None, start_time=None):
        self.end_time = end_time  # type: str
        self.select_disable_tip = select_disable_tip  # type: str
        self.selectable = selectable  # type: bool
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.select_disable_tip is not None:
            result['SelectDisableTip'] = self.select_disable_tip
        if self.selectable is not None:
            result['Selectable'] = self.selectable
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SelectDisableTip') is not None:
            self.select_disable_tip = m.get('SelectDisableTip')
        if m.get('Selectable') is not None:
            self.selectable = m.get('Selectable')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes(TeaModel):
    def __init__(self, date=None, date_selectable=None, time_list=None):
        self.date = date  # type: str
        self.date_selectable = date_selectable  # type: bool
        self.time_list = time_list  # type: list[CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList]

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.date_selectable is not None:
            result['DateSelectable'] = self.date_selectable
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DateSelectable') is not None:
            self.date_selectable = m.get('DateSelectable')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime(TeaModel):
    def __init__(self, name=None, select_disable_tip=None, selectable=None):
        self.name = name  # type: str
        self.select_disable_tip = select_disable_tip  # type: str
        self.selectable = selectable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.select_disable_tip is not None:
            result['SelectDisableTip'] = self.select_disable_tip
        if self.selectable is not None:
            result['Selectable'] = self.selectable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectDisableTip') is not None:
            self.select_disable_tip = m.get('SelectDisableTip')
        if m.get('Selectable') is not None:
            self.selectable = m.get('Selectable')
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList(TeaModel):
    def __init__(self, appoint_times=None, pre_price=None, real_time=None):
        self.appoint_times = appoint_times  # type: list[CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes]
        self.pre_price = pre_price  # type: str
        self.real_time = real_time  # type: CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime

    def validate(self):
        if self.appoint_times:
            for k in self.appoint_times:
                if k:
                    k.validate()
        if self.real_time:
            self.real_time.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppointTimes'] = []
        if self.appoint_times is not None:
            for k in self.appoint_times:
                result['AppointTimes'].append(k.to_map() if k else None)
        if self.pre_price is not None:
            result['PrePrice'] = self.pre_price
        if self.real_time is not None:
            result['RealTime'] = self.real_time.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.appoint_times = []
        if m.get('AppointTimes') is not None:
            for k in m.get('AppointTimes'):
                temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes()
                self.appoint_times.append(temp_model.from_map(k))
        if m.get('PrePrice') is not None:
            self.pre_price = m.get('PrePrice')
        if m.get('RealTime') is not None:
            temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime()
            self.real_time = temp_model.from_map(m['RealTime'])
        return self


class CreatePickUpWaybillPreQueryResponseBodyData(TeaModel):
    def __init__(self, code=None, cp_time_select_list=None, error_code=None, error_msg=None, message=None,
                 success=None):
        self.code = code  # type: str
        self.cp_time_select_list = cp_time_select_list  # type: list[CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList]
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.cp_time_select_list:
            for k in self.cp_time_select_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['CpTimeSelectList'] = []
        if self.cp_time_select_list is not None:
            for k in self.cp_time_select_list:
                result['CpTimeSelectList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.cp_time_select_list = []
        if m.get('CpTimeSelectList') is not None:
            for k in m.get('CpTimeSelectList'):
                temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList()
                self.cp_time_select_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePickUpWaybillPreQueryResponseBody(TeaModel):
    def __init__(self, data=None, http_status_code=None, message=None, request_id=None):
        self.data = data  # type: CreatePickUpWaybillPreQueryResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreatePickUpWaybillPreQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePickUpWaybillPreQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePickUpWaybillPreQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePickUpWaybillPreQueryResponse, self).to_map()
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
            temp_model = CreatePickUpWaybillPreQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretBlacklistRequest(TeaModel):
    def __init__(self, black_no=None, black_type=None, pool_key=None, remark=None, way_control=None):
        self.black_no = black_no  # type: str
        self.black_type = black_type  # type: str
        self.pool_key = pool_key  # type: str
        self.remark = remark  # type: str
        self.way_control = way_control  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.way_control is not None:
            result['WayControl'] = self.way_control
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('WayControl') is not None:
            self.way_control = m.get('WayControl')
        return self


class DeleteSecretBlacklistResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretBlacklistResponseBody, self).to_map()
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


class DeleteSecretBlacklistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSecretBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSecretBlacklistResponse, self).to_map()
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
            temp_model = DeleteSecretBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretAsrDetailRequest(TeaModel):
    def __init__(self, call_id=None, call_time=None, pool_key=None):
        self.call_id = call_id  # type: str
        self.call_time = call_time  # type: str
        self.pool_key = pool_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretAsrDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        return self


class GetSecretAsrDetailResponseBodyDataSentences(TeaModel):
    def __init__(self, begin_time=None, channel_id=None, emotion_value=None, end_time=None, silence_duration=None,
                 speech_rate=None, text=None):
        self.begin_time = begin_time  # type: long
        self.channel_id = channel_id  # type: int
        self.emotion_value = emotion_value  # type: str
        self.end_time = end_time  # type: long
        self.silence_duration = silence_duration  # type: long
        self.speech_rate = speech_rate  # type: int
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretAsrDetailResponseBodyDataSentences, self).to_map()
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
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSecretAsrDetailResponseBodyData(TeaModel):
    def __init__(self, biz_duration=None, business_id=None, business_key=None, code=None, msg=None, request_id=None,
                 sentences=None, type=None):
        self.biz_duration = biz_duration  # type: long
        self.business_id = business_id  # type: str
        self.business_key = business_key  # type: str
        self.code = code  # type: str
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.sentences = sentences  # type: list[GetSecretAsrDetailResponseBodyDataSentences]
        self.type = type  # type: str

    def validate(self):
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSecretAsrDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_duration is not None:
            result['BizDuration'] = self.biz_duration
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_key is not None:
            result['BusinessKey'] = self.business_key
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['Sentences'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizDuration') is not None:
            self.biz_duration = m.get('BizDuration')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessKey') is not None:
            self.business_key = m.get('BusinessKey')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sentences = []
        if m.get('Sentences') is not None:
            for k in m.get('Sentences'):
                temp_model = GetSecretAsrDetailResponseBodyDataSentences()
                self.sentences.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSecretAsrDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetSecretAsrDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSecretAsrDetailResponseBody, self).to_map()
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
            temp_model = GetSecretAsrDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretAsrDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSecretAsrDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecretAsrDetailResponse, self).to_map()
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
            temp_model = GetSecretAsrDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTotalPublicUrlRequest(TeaModel):
    def __init__(self, call_id=None, call_time=None, check_subs=None, owner_id=None, partner_key=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.call_id = call_id  # type: str
        self.call_time = call_time  # type: str
        self.check_subs = check_subs  # type: bool
        self.owner_id = owner_id  # type: long
        self.partner_key = partner_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTotalPublicUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.check_subs is not None:
            result['CheckSubs'] = self.check_subs
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CheckSubs') is not None:
            self.check_subs = m.get('CheckSubs')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetTotalPublicUrlResponseBodyData(TeaModel):
    def __init__(self, phone_public_url=None, ring_public_url=None):
        self.phone_public_url = phone_public_url  # type: str
        self.ring_public_url = ring_public_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTotalPublicUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_public_url is not None:
            result['PhonePublicUrl'] = self.phone_public_url
        if self.ring_public_url is not None:
            result['RingPublicUrl'] = self.ring_public_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhonePublicUrl') is not None:
            self.phone_public_url = m.get('PhonePublicUrl')
        if m.get('RingPublicUrl') is not None:
            self.ring_public_url = m.get('RingPublicUrl')
        return self


class GetTotalPublicUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetTotalPublicUrlResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTotalPublicUrlResponseBody, self).to_map()
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
            temp_model = GetTotalPublicUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTotalPublicUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTotalPublicUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTotalPublicUrlResponse, self).to_map()
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
            temp_model = GetTotalPublicUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockSecretNoRequest(TeaModel):
    def __init__(self, owner_id=None, pool_key=None, resource_owner_account=None, resource_owner_id=None,
                 secret_no=None):
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockSecretNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class LockSecretNoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockSecretNoResponseBody, self).to_map()
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


class LockSecretNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LockSecretNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockSecretNoResponse, self).to_map()
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
            temp_model = LockSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAxgGroupRequest(TeaModel):
    def __init__(self, group_id=None, numbers=None, operate_type=None, owner_id=None, pool_key=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.group_id = group_id  # type: long
        self.numbers = numbers  # type: str
        self.operate_type = operate_type  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateAxgGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OperateAxgGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateAxgGroupResponseBody, self).to_map()
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


class OperateAxgGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OperateAxgGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateAxgGroupResponse, self).to_map()
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
            temp_model = OperateAxgGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateBlackNoRequest(TeaModel):
    def __init__(self, black_no=None, operate_type=None, owner_id=None, pool_key=None, resource_owner_account=None,
                 resource_owner_id=None, tips=None):
        self.black_no = black_no  # type: str
        self.operate_type = operate_type  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tips = tips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateBlackNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class OperateBlackNoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateBlackNoResponseBody, self).to_map()
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


class OperateBlackNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OperateBlackNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateBlackNoResponse, self).to_map()
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
            temp_model = OperateBlackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPhoneNoAByTrackNoRequest(TeaModel):
    def __init__(self, cabinet_no=None, owner_id=None, phone_no_x=None, resource_owner_account=None,
                 resource_owner_id=None, track_no=None):
        self.cabinet_no = cabinet_no  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_no_x = phone_no_x  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.track_no = track_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPhoneNoAByTrackNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cabinet_no is not None:
            result['CabinetNo'] = self.cabinet_no
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.track_no is not None:
            result['trackNo'] = self.track_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CabinetNo') is not None:
            self.cabinet_no = m.get('CabinetNo')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('trackNo') is not None:
            self.track_no = m.get('trackNo')
        return self


class QueryPhoneNoAByTrackNoResponseBodyModule(TeaModel):
    def __init__(self, extension=None, phone_no_a=None, phone_no_x=None):
        self.extension = extension  # type: str
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_x = phone_no_x  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPhoneNoAByTrackNoResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        return self


class QueryPhoneNoAByTrackNoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: list[QueryPhoneNoAByTrackNoResponseBodyModule]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPhoneNoAByTrackNoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = QueryPhoneNoAByTrackNoResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPhoneNoAByTrackNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPhoneNoAByTrackNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPhoneNoAByTrackNoResponse, self).to_map()
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
            temp_model = QueryPhoneNoAByTrackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordFileDownloadUrlRequest(TeaModel):
    def __init__(self, call_id=None, call_time=None, owner_id=None, pool_key=None, product_type=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.call_id = call_id  # type: str
        self.call_time = call_time  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.product_type = product_type  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordFileDownloadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRecordFileDownloadUrlResponseBody(TeaModel):
    def __init__(self, code=None, download_url=None, message=None, request_id=None):
        self.code = code  # type: str
        self.download_url = download_url  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordFileDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRecordFileDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordFileDownloadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordFileDownloadUrlResponse, self).to_map()
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
            temp_model = QueryRecordFileDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySecretNoDetailRequest(TeaModel):
    def __init__(self, owner_id=None, pool_key=None, resource_owner_account=None, resource_owner_id=None,
                 secret_no=None):
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySecretNoDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class QuerySecretNoDetailResponseBodySecretNoInfoDTO(TeaModel):
    def __init__(self, certify_status=None, city=None, province=None, purchase_time=None, secret_status=None,
                 vendor=None):
        self.certify_status = certify_status  # type: int
        self.city = city  # type: str
        self.province = province  # type: str
        self.purchase_time = purchase_time  # type: str
        self.secret_status = secret_status  # type: long
        self.vendor = vendor  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySecretNoDetailResponseBodySecretNoInfoDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        if self.purchase_time is not None:
            result['PurchaseTime'] = self.purchase_time
        if self.secret_status is not None:
            result['SecretStatus'] = self.secret_status
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('PurchaseTime') is not None:
            self.purchase_time = m.get('PurchaseTime')
        if m.get('SecretStatus') is not None:
            self.secret_status = m.get('SecretStatus')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class QuerySecretNoDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_no_info_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_no_info_dto = secret_no_info_dto  # type: QuerySecretNoDetailResponseBodySecretNoInfoDTO

    def validate(self):
        if self.secret_no_info_dto:
            self.secret_no_info_dto.validate()

    def to_map(self):
        _map = super(QuerySecretNoDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_no_info_dto is not None:
            result['SecretNoInfoDTO'] = self.secret_no_info_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretNoInfoDTO') is not None:
            temp_model = QuerySecretNoDetailResponseBodySecretNoInfoDTO()
            self.secret_no_info_dto = temp_model.from_map(m['SecretNoInfoDTO'])
        return self


class QuerySecretNoDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySecretNoDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySecretNoDetailResponse, self).to_map()
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
            temp_model = QuerySecretNoDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySecretNoRemainRequest(TeaModel):
    def __init__(self, city=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 secret_no=None, spec_id=None):
        self.city = city  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str
        self.spec_id = spec_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySecretNoRemainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO(TeaModel):
    def __init__(self, amount=None, city=None):
        self.amount = amount  # type: long
        self.city = city  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.city is not None:
            result['City'] = self.city
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('City') is not None:
            self.city = m.get('City')
        return self


class QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList(TeaModel):
    def __init__(self, remain_dto=None):
        self.remain_dto = remain_dto  # type: list[QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO]

    def validate(self):
        if self.remain_dto:
            for k in self.remain_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['remainDTO'] = []
        if self.remain_dto is not None:
            for k in self.remain_dto:
                result['remainDTO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.remain_dto = []
        if m.get('remainDTO') is not None:
            for k in m.get('remainDTO'):
                temp_model = QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO()
                self.remain_dto.append(temp_model.from_map(k))
        return self


class QuerySecretNoRemainResponseBodySecretRemainDTO(TeaModel):
    def __init__(self, amount=None, city=None, remain_dtolist=None):
        self.amount = amount  # type: long
        self.city = city  # type: str
        self.remain_dtolist = remain_dtolist  # type: QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList

    def validate(self):
        if self.remain_dtolist:
            self.remain_dtolist.validate()

    def to_map(self):
        _map = super(QuerySecretNoRemainResponseBodySecretRemainDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.city is not None:
            result['City'] = self.city
        if self.remain_dtolist is not None:
            result['RemainDTOList'] = self.remain_dtolist.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('RemainDTOList') is not None:
            temp_model = QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList()
            self.remain_dtolist = temp_model.from_map(m['RemainDTOList'])
        return self


class QuerySecretNoRemainResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_remain_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_remain_dto = secret_remain_dto  # type: QuerySecretNoRemainResponseBodySecretRemainDTO

    def validate(self):
        if self.secret_remain_dto:
            self.secret_remain_dto.validate()

    def to_map(self):
        _map = super(QuerySecretNoRemainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_remain_dto is not None:
            result['SecretRemainDTO'] = self.secret_remain_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretRemainDTO') is not None:
            temp_model = QuerySecretNoRemainResponseBodySecretRemainDTO()
            self.secret_remain_dto = temp_model.from_map(m['SecretRemainDTO'])
        return self


class QuerySecretNoRemainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySecretNoRemainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySecretNoRemainResponse, self).to_map()
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
            temp_model = QuerySecretNoRemainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySubsIdRequest(TeaModel):
    def __init__(self, owner_id=None, phone_no_x=None, pool_key=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySubsIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySubsIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, subs_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySubsIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class QuerySubsIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySubsIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySubsIdResponse, self).to_map()
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
            temp_model = QuerySubsIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySubscriptionDetailRequest(TeaModel):
    def __init__(self, owner_id=None, phone_no_x=None, pool_key=None, product_type=None,
                 resource_owner_account=None, resource_owner_id=None, subs_id=None):
        self.owner_id = owner_id  # type: long
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.product_type = product_type  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySubscriptionDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class QuerySubscriptionDetailResponseBodySecretBindDetailDTO(TeaModel):
    def __init__(self, asrmodel_id=None, asrstatus=None, call_restrict=None, expire_date=None, extension=None,
                 gmt_create=None, group_id=None, need_record=None, phone_no_a=None, phone_no_b=None, phone_no_x=None,
                 status=None, subs_id=None):
        self.asrmodel_id = asrmodel_id  # type: str
        self.asrstatus = asrstatus  # type: bool
        self.call_restrict = call_restrict  # type: str
        self.expire_date = expire_date  # type: str
        self.extension = extension  # type: str
        self.gmt_create = gmt_create  # type: str
        self.group_id = group_id  # type: long
        self.need_record = need_record  # type: bool
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.phone_no_x = phone_no_x  # type: str
        self.status = status  # type: long
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySubscriptionDetailResponseBodySecretBindDetailDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.need_record is not None:
            result['NeedRecord'] = self.need_record
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.status is not None:
            result['Status'] = self.status
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NeedRecord') is not None:
            self.need_record = m.get('NeedRecord')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class QuerySubscriptionDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, secret_bind_detail_dto=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.secret_bind_detail_dto = secret_bind_detail_dto  # type: QuerySubscriptionDetailResponseBodySecretBindDetailDTO

    def validate(self):
        if self.secret_bind_detail_dto:
            self.secret_bind_detail_dto.validate()

    def to_map(self):
        _map = super(QuerySubscriptionDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_detail_dto is not None:
            result['SecretBindDetailDTO'] = self.secret_bind_detail_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDetailDTO') is not None:
            temp_model = QuerySubscriptionDetailResponseBodySecretBindDetailDTO()
            self.secret_bind_detail_dto = temp_model.from_map(m['SecretBindDetailDTO'])
        return self


class QuerySubscriptionDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySubscriptionDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySubscriptionDetailResponse, self).to_map()
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
            temp_model = QuerySubscriptionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseSecretNoRequest(TeaModel):
    def __init__(self, owner_id=None, pool_key=None, resource_owner_account=None, resource_owner_id=None,
                 secret_no=None):
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseSecretNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ReleaseSecretNoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseSecretNoResponseBody, self).to_map()
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


class ReleaseSecretNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseSecretNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseSecretNoResponse, self).to_map()
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
            temp_model = ReleaseSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindSubscriptionRequest(TeaModel):
    def __init__(self, owner_id=None, pool_key=None, product_type=None, resource_owner_account=None,
                 resource_owner_id=None, secret_no=None, subs_id=None):
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.product_type = product_type  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class UnbindSubscriptionResponseBody(TeaModel):
    def __init__(self, charge_id=None, code=None, message=None, request_id=None):
        self.charge_id = charge_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindSubscriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_id is not None:
            result['ChargeId'] = self.charge_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeId') is not None:
            self.charge_id = m.get('ChargeId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindSubscriptionResponse, self).to_map()
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
            temp_model = UnbindSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockSecretNoRequest(TeaModel):
    def __init__(self, owner_id=None, pool_key=None, resource_owner_account=None, resource_owner_id=None,
                 secret_no=None):
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockSecretNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnlockSecretNoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockSecretNoResponseBody, self).to_map()
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


class UnlockSecretNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockSecretNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockSecretNoResponse, self).to_map()
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
            temp_model = UnlockSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubscriptionRequest(TeaModel):
    def __init__(self, asrmodel_id=None, asrstatus=None, call_display_type=None, call_restrict=None,
                 expiration=None, group_id=None, is_recording_enabled=None, operate_type=None, out_id=None, owner_id=None,
                 phone_no_a=None, phone_no_b=None, phone_no_x=None, pool_key=None, product_type=None,
                 resource_owner_account=None, resource_owner_id=None, ring_config=None, subs_id=None):
        self.asrmodel_id = asrmodel_id  # type: str
        self.asrstatus = asrstatus  # type: bool
        self.call_display_type = call_display_type  # type: int
        self.call_restrict = call_restrict  # type: str
        self.expiration = expiration  # type: str
        self.group_id = group_id  # type: str
        self.is_recording_enabled = is_recording_enabled  # type: bool
        self.operate_type = operate_type  # type: str
        self.out_id = out_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.phone_no_x = phone_no_x  # type: str
        self.pool_key = pool_key  # type: str
        self.product_type = product_type  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.ring_config = ring_config  # type: str
        self.subs_id = subs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class UpdateSubscriptionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubscriptionResponseBody, self).to_map()
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


class UpdateSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSubscriptionResponse, self).to_map()
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
            temp_model = UpdateSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


