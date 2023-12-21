# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class VerifyCaptchaRequest(TeaModel):
    def __init__(self, captcha_verify_param=None):
        self.captcha_verify_param = captcha_verify_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyCaptchaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.captcha_verify_param is not None:
            result['CaptchaVerifyParam'] = self.captcha_verify_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptchaVerifyParam') is not None:
            self.captcha_verify_param = m.get('CaptchaVerifyParam')
        return self


class VerifyCaptchaResponseBodyResult(TeaModel):
    def __init__(self, verify_result=None):
        self.verify_result = verify_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyCaptchaResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyCaptchaResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: VerifyCaptchaResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(VerifyCaptchaResponseBody, self).to_map()
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
            temp_model = VerifyCaptchaResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyCaptchaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyCaptchaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyCaptchaResponse, self).to_map()
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
            temp_model = VerifyCaptchaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyIntelligentCaptchaRequest(TeaModel):
    def __init__(self, captcha_verify_param=None, scene_id=None):
        self.captcha_verify_param = captcha_verify_param  # type: str
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyIntelligentCaptchaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.captcha_verify_param is not None:
            result['CaptchaVerifyParam'] = self.captcha_verify_param
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptchaVerifyParam') is not None:
            self.captcha_verify_param = m.get('CaptchaVerifyParam')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class VerifyIntelligentCaptchaResponseBodyResult(TeaModel):
    def __init__(self, verify_code=None, verify_result=None):
        self.verify_code = verify_code  # type: str
        self.verify_result = verify_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyIntelligentCaptchaResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyIntelligentCaptchaResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: VerifyIntelligentCaptchaResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(VerifyIntelligentCaptchaResponseBody, self).to_map()
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
            temp_model = VerifyIntelligentCaptchaResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyIntelligentCaptchaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyIntelligentCaptchaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyIntelligentCaptchaResponse, self).to_map()
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
            temp_model = VerifyIntelligentCaptchaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


