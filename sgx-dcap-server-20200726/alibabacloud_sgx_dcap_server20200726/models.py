# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetQeIdentityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(GetQeIdentityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetQveIdentityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(GetQveIdentityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetTcbInfoRequest(TeaModel):
    def __init__(self, fmspc=None):
        self.fmspc = fmspc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTcbInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fmspc is not None:
            result['fmspc'] = self.fmspc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fmspc') is not None:
            self.fmspc = m.get('fmspc')
        return self


class GetTcbInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(GetTcbInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PckCrlRequest(TeaModel):
    def __init__(self, ca=None):
        self.ca = ca  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PckCrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca is not None:
            result['ca'] = self.ca
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ca') is not None:
            self.ca = m.get('ca')
        return self


class PckCrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(PckCrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RootCaCrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(RootCaCrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class SimplePackagePckCertRequest(TeaModel):
    def __init__(self, cpusvn=None, encrypted_ppid=None, pceid=None, pcesvn=None, qeid=None):
        self.cpusvn = cpusvn  # type: str
        self.encrypted_ppid = encrypted_ppid  # type: str
        self.pceid = pceid  # type: str
        self.pcesvn = pcesvn  # type: str
        self.qeid = qeid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimplePackagePckCertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpusvn is not None:
            result['cpusvn'] = self.cpusvn
        if self.encrypted_ppid is not None:
            result['encrypted_ppid'] = self.encrypted_ppid
        if self.pceid is not None:
            result['pceid'] = self.pceid
        if self.pcesvn is not None:
            result['pcesvn'] = self.pcesvn
        if self.qeid is not None:
            result['qeid'] = self.qeid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpusvn') is not None:
            self.cpusvn = m.get('cpusvn')
        if m.get('encrypted_ppid') is not None:
            self.encrypted_ppid = m.get('encrypted_ppid')
        if m.get('pceid') is not None:
            self.pceid = m.get('pceid')
        if m.get('pcesvn') is not None:
            self.pcesvn = m.get('pcesvn')
        if m.get('qeid') is not None:
            self.qeid = m.get('qeid')
        return self


class SimplePackagePckCertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(SimplePackagePckCertResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


