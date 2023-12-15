# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateEenterpriseDIDRequest(TeaModel):
    def __init__(self, client_token=None, owner_unique_id=None):
        self.client_token = client_token  # type: str
        self.owner_unique_id = owner_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEenterpriseDIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_unique_id is not None:
            result['OwnerUniqueID'] = self.owner_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerUniqueID') is not None:
            self.owner_unique_id = m.get('OwnerUniqueID')
        return self


class CreateEenterpriseDIDResponseBody(TeaModel):
    def __init__(self, did=None, request_id=None, result_code=None, result_message=None, success=None):
        self.did = did  # type: str
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_message = result_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEenterpriseDIDResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEenterpriseDIDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEenterpriseDIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEenterpriseDIDResponse, self).to_map()
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
            temp_model = CreateEenterpriseDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePersonalDIDRequest(TeaModel):
    def __init__(self, client_token=None, owner_unique_id=None):
        self.client_token = client_token  # type: str
        self.owner_unique_id = owner_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePersonalDIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_unique_id is not None:
            result['OwnerUniqueID'] = self.owner_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerUniqueID') is not None:
            self.owner_unique_id = m.get('OwnerUniqueID')
        return self


class CreatePersonalDIDResponseBody(TeaModel):
    def __init__(self, did=None, request_id=None, result_code=None, result_message=None, success=None):
        self.did = did  # type: str
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_message = result_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePersonalDIDResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePersonalDIDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePersonalDIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePersonalDIDResponse, self).to_map()
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
            temp_model = CreatePersonalDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantDIDRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantDIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateTenantDIDResponseBody(TeaModel):
    def __init__(self, did=None, request_id=None, result_code=None, result_message=None, success=None):
        self.did = did  # type: str
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_message = result_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantDIDResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTenantDIDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTenantDIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTenantDIDResponse, self).to_map()
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
            temp_model = CreateTenantDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDIDRequest(TeaModel):
    def __init__(self, did=None):
        self.did = did  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        return self


class GetDIDResponseBody(TeaModel):
    def __init__(self, doc=None, request_id=None, result_code=None, result_message=None, success=None):
        self.doc = doc  # type: str
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_message = result_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDIDResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc is not None:
            result['Doc'] = self.doc
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Doc') is not None:
            self.doc = m.get('Doc')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDIDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDIDResponse, self).to_map()
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
            temp_model = GetDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IssueNormalVerifiableVCRequestBareClaimStructBody(TeaModel):
    def __init__(self, claim=None, claim_type=None):
        self.claim = claim  # type: str
        self.claim_type = claim_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IssueNormalVerifiableVCRequestBareClaimStructBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim is not None:
            result['Claim'] = self.claim
        if self.claim_type is not None:
            result['ClaimType'] = self.claim_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Claim') is not None:
            self.claim = m.get('Claim')
        if m.get('ClaimType') is not None:
            self.claim_type = m.get('ClaimType')
        return self


class IssueNormalVerifiableVCRequest(TeaModel):
    def __init__(self, bare_claim_struct_body=None, client_token=None, expiration=None, issuer=None, subject=None):
        self.bare_claim_struct_body = bare_claim_struct_body  # type: list[IssueNormalVerifiableVCRequestBareClaimStructBody]
        self.client_token = client_token  # type: str
        self.expiration = expiration  # type: long
        self.issuer = issuer  # type: str
        self.subject = subject  # type: str

    def validate(self):
        if self.bare_claim_struct_body:
            for k in self.bare_claim_struct_body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(IssueNormalVerifiableVCRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BareClaimStructBody'] = []
        if self.bare_claim_struct_body is not None:
            for k in self.bare_claim_struct_body:
                result['BareClaimStructBody'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bare_claim_struct_body = []
        if m.get('BareClaimStructBody') is not None:
            for k in m.get('BareClaimStructBody'):
                temp_model = IssueNormalVerifiableVCRequestBareClaimStructBody()
                self.bare_claim_struct_body.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class IssueNormalVerifiableVCResponseBody(TeaModel):
    def __init__(self, request_id=None, result_code=None, result_message=None, success=None,
                 verifiable_claim_content=None, verifiable_claim_id=None):
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_message = result_message  # type: str
        self.success = success  # type: bool
        self.verifiable_claim_content = verifiable_claim_content  # type: str
        self.verifiable_claim_id = verifiable_claim_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IssueNormalVerifiableVCResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        if self.verifiable_claim_content is not None:
            result['VerifiableClaimContent'] = self.verifiable_claim_content
        if self.verifiable_claim_id is not None:
            result['VerifiableClaimId'] = self.verifiable_claim_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VerifiableClaimContent') is not None:
            self.verifiable_claim_content = m.get('VerifiableClaimContent')
        if m.get('VerifiableClaimId') is not None:
            self.verifiable_claim_id = m.get('VerifiableClaimId')
        return self


class IssueNormalVerifiableVCResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IssueNormalVerifiableVCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IssueNormalVerifiableVCResponse, self).to_map()
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
            temp_model = IssueNormalVerifiableVCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVCRequest(TeaModel):
    def __init__(self, issuer_did=None, vcid=None, vcstatus=None):
        self.issuer_did = issuer_did  # type: str
        self.vcid = vcid  # type: str
        self.vcstatus = vcstatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVCRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issuer_did is not None:
            result['IssuerDid'] = self.issuer_did
        if self.vcid is not None:
            result['VCId'] = self.vcid
        if self.vcstatus is not None:
            result['VCStatus'] = self.vcstatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IssuerDid') is not None:
            self.issuer_did = m.get('IssuerDid')
        if m.get('VCId') is not None:
            self.vcid = m.get('VCId')
        if m.get('VCStatus') is not None:
            self.vcstatus = m.get('VCStatus')
        return self


class UpdateVCResponseBody(TeaModel):
    def __init__(self, request_id=None, result_code=None, result_message=None, success=None):
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_message = result_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVCResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateVCResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVCResponse, self).to_map()
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
            temp_model = UpdateVCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyVerifiableClaimRequest(TeaModel):
    def __init__(self, vccontent=None):
        self.vccontent = vccontent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyVerifiableClaimRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vccontent is not None:
            result['VCContent'] = self.vccontent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VCContent') is not None:
            self.vccontent = m.get('VCContent')
        return self


class VerifyVerifiableClaimResponseBody(TeaModel):
    def __init__(self, request_id=None, result_code=None, result_message=None, success=None):
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_message = result_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyVerifiableClaimResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyVerifiableClaimResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyVerifiableClaimResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyVerifiableClaimResponse, self).to_map()
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
            temp_model = VerifyVerifiableClaimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


