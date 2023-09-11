# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AsymmetricDecryptRequest(TeaModel):
    def __init__(self, algorithm=None, ciphertext_blob=None, key_id=None, key_version_id=None):
        # The decryption algorithm.
        self.algorithm = algorithm  # type: str
        # The ciphertext that you want to decrypt.
        # 
        # > * The value is encoded in Base64.
        # > * You can call the [AsymmetricEncrypt](~~148131~~) operation to generate the ciphertext.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id  # type: str
        # The version ID of the CMK. The ID must be globally unique.
        self.key_version_id = key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricDecryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricDecryptResponseBody(TeaModel):
    def __init__(self, key_id=None, key_version_id=None, plaintext=None, request_id=None):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The version ID of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id  # type: str
        # The Base64-encoded plaintext that is generated after decryption.
        self.plaintext = plaintext  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricDecryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AsymmetricDecryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AsymmetricDecryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AsymmetricDecryptResponse, self).to_map()
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
            temp_model = AsymmetricDecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricEncryptRequest(TeaModel):
    def __init__(self, algorithm=None, key_id=None, key_version_id=None, plaintext=None):
        # The encryption algorithm.
        self.algorithm = algorithm  # type: str
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The version ID of the CMK. The ID must be globally unique.
        # 
        # >  You can call the [ListKeyVersions](~~133966~~) operation to query the versions of a CMK. The ID of a version is specified by the KeyVersionId parameter.
        self.key_version_id = key_version_id  # type: str
        # The plaintext that you want to encrypt. The plaintext must be Base64-encoded.
        self.plaintext = plaintext  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricEncryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class AsymmetricEncryptResponseBody(TeaModel):
    def __init__(self, ciphertext_blob=None, key_id=None, key_version_id=None, request_id=None):
        # The Base64-encoded ciphertext that was generated after encryption.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The version ID of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricEncryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AsymmetricEncryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AsymmetricEncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AsymmetricEncryptResponse, self).to_map()
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
            temp_model = AsymmetricEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricSignRequest(TeaModel):
    def __init__(self, algorithm=None, digest=None, key_id=None, key_version_id=None):
        # The version ID of the CMK. The ID must be globally unique.
        self.algorithm = algorithm  # type: str
        # The signature algorithm.
        self.digest = digest  # type: str
        # The operation that you want to perform. Set the value to **AsymmetricSign**.
        self.key_id = key_id  # type: str
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_version_id = key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricSignResponseBody(TeaModel):
    def __init__(self, key_id=None, key_version_id=None, request_id=None, value=None):
        # The version ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str
        # The digest that is generated for the original message by using a hash algorithm. The hash algorithm is specified by the Algorithm parameter.
        # 
        # > * The value is encoded in Base64.
        # > * For more information about how to calculate message digests, see the **Preprocess signature: compute a message digest** section of the [Generate and verify a signature by using an asymmetric CMK](~~148146~~) topic.
        self.key_version_id = key_version_id  # type: str
        # The calculated signature.
        # 
        # >  The value is encoded in Base64.
        self.request_id = request_id  # type: str
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AsymmetricSignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AsymmetricSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AsymmetricSignResponse, self).to_map()
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
            temp_model = AsymmetricSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricVerifyRequest(TeaModel):
    def __init__(self, algorithm=None, digest=None, key_id=None, key_version_id=None, value=None):
        # The signature algorithm.
        self.algorithm = algorithm  # type: str
        # The digest that is generated for the original message by using a hash algorithm. The hash algorithm is specified by the **Algorithm** parameter.
        # 
        # >  The value is encoded in Base64.
        self.digest = digest  # type: str
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  You can also set this parameter to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The version ID of the CMK. The ID must be globally unique.
        self.key_version_id = key_version_id  # type: str
        # The signature value to be verified.
        # 
        # >  The value is encoded in Base64.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AsymmetricVerifyResponseBody(TeaModel):
    def __init__(self, key_id=None, key_version_id=None, request_id=None, value=None):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The version ID of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # Indicates whether the signature passed the verification.
        self.value = value  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsymmetricVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AsymmetricVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AsymmetricVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AsymmetricVerifyResponse, self).to_map()
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
            temp_model = AsymmetricVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelKeyDeletionRequest(TeaModel):
    def __init__(self, key_id=None):
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelKeyDeletionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class CancelKeyDeletionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelKeyDeletionResponseBody, self).to_map()
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


class CancelKeyDeletionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelKeyDeletionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelKeyDeletionResponse, self).to_map()
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
            temp_model = CancelKeyDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePrivateKeyDecryptRequest(TeaModel):
    def __init__(self, algorithm=None, certificate_id=None, ciphertext_blob=None):
        # The encryption algorithm. Valid values:
        # 
        # *   RSAES_OAEP_SHA\_1
        # 
        # *   RSAES_OAEP_SHA\_256
        # 
        # *   SM2PKE
        # 
        # > The SM2PKE encryption algorithm is supported only in regions in mainland China. In these regions, managed hardware security modules (HSMs) are used. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm  # type: str
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str
        # The data that you want to decrypt.
        # 
        # The value is encoded in Base64.
        self.ciphertext_blob = ciphertext_blob  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePrivateKeyDecryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        return self


class CertificatePrivateKeyDecryptResponseBody(TeaModel):
    def __init__(self, certificate_id=None, plaintext=None, request_id=None):
        # The ID of the certificate.
        self.certificate_id = certificate_id  # type: str
        # The plaintext after data is decrypted.
        # 
        # The value is encoded in Base64.
        self.plaintext = plaintext  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePrivateKeyDecryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CertificatePrivateKeyDecryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CertificatePrivateKeyDecryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CertificatePrivateKeyDecryptResponse, self).to_map()
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
            temp_model = CertificatePrivateKeyDecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePrivateKeySignRequest(TeaModel):
    def __init__(self, algorithm=None, certificate_id=None, message=None, message_type=None):
        # The signature algorithm. Valid values:
        # 
        # *   RSA_PKCS1\_SHA\_256
        # 
        # *   RSA_PSS_SHA\_256
        # 
        # *   ECDSA_SHA\_256
        # 
        # *   SM2DSA
        # 
        # >* The SM2DSA signature algorithm is supported only in regions where managed hardware security modules (HSMs) are used in mainland China. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm  # type: str
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str
        # The data to be signed.
        # 
        # The value is encoded in Base64. For example, if the hexadecimal data that you want to sign is `[0x31, 0x32, 0x33, 0x34]`, the Base64-encoded data is `MTIzNA==`.
        # 
        # If the MessageType parameter is set to RAW, the size of the data must be less than or equal to 4 KB.
        # 
        # If the size of the data is greater than 4 KB, you can set the MessageType parameter to DIGEST and set the Message parameter to the digest of the data. The digest is also called hash value. You can compute the digest of the data on an on-premises machine. Certificates Manager uses the digest that you compute in your own certificate application system. The message digest algorithm that you use must match the specified signature algorithm. Comply with the following mapping between signature algorithms and message digest algorithms:
        # 
        # *   If the signature algorithm is RSA_PKCS1\_SHA\_256, RSA_PSS_SHA\_256, or ECDSA_SHA\_256, the message digest algorithm must be SHA-256.
        # *   If the signature algorithm is SM2DSA, the message digest algorithm must be SM3.
        # 
        # >  If the key type of the certificate is EC_SM2 and the MessageType parameter is set to DIGEST, the value of the Message parameter is `e` that is described in GB/T 32918.2-2016 6.1.
        self.message = message  # type: str
        # The type of the message. Valid values:
        # 
        # *   RAW: the raw data. This is the default value.
        # *   DIGEST: the message digest (hash value) of the raw data.
        self.message_type = message_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePrivateKeySignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class CertificatePrivateKeySignResponseBody(TeaModel):
    def __init__(self, certificate_id=None, request_id=None, signature_value=None):
        # The ID of the certificate.
        self.certificate_id = certificate_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The signature value.
        # 
        # The value is encoded in Base64.
        self.signature_value = signature_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePrivateKeySignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        return self


class CertificatePrivateKeySignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CertificatePrivateKeySignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CertificatePrivateKeySignResponse, self).to_map()
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
            temp_model = CertificatePrivateKeySignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePublicKeyEncryptRequest(TeaModel):
    def __init__(self, algorithm=None, certificate_id=None, plaintext=None):
        # The encryption algorithm. Valid values:
        # 
        # *   RSAES_OAEP_SHA\_1
        # 
        # *   RSAES_OAEP_SHA\_256
        # 
        # *   SM2PKE
        # 
        # >The SM2PKE encryption algorithm is supported only in regions in mainland China. In these regions, managed hardware security modules (HSMs) are used. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm  # type: str
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str
        # The data that you want to encrypt.
        # 
        # The value is encoded in Base64. For example, if the hexadecimal data that you want to encrypt is `[0x31, 0x32, 0x33, 0x34]`, the Base64-encoded data is `MTIzNA==`.
        # 
        # The size of data that can be encrypted varies based on the encryption algorithm that you use:
        # 
        # *   RSAES_OAEP_SHA\_1: 214 bytes
        # *   RSAES_OAEP_SHA\_256: 190 bytes
        # *   SM2PKE: 6,047 bytes
        # 
        # If the size of data that you want to encrypt exceeds the preceding limits, you can call the [GenerateDataKey](~~28948~~) operation to generate a data key to encrypt the data. Then, call the CertificatePublicKeyEncrypt operation to encrypt the data key.
        self.plaintext = plaintext  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePublicKeyEncryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class CertificatePublicKeyEncryptResponseBody(TeaModel):
    def __init__(self, certificate_id=None, ciphertext_blob=None, request_id=None):
        # The ID of the certificate.
        self.certificate_id = certificate_id  # type: str
        # The ciphertext.
        # 
        # The value is encoded in Base64.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePublicKeyEncryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CertificatePublicKeyEncryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CertificatePublicKeyEncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CertificatePublicKeyEncryptResponse, self).to_map()
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
            temp_model = CertificatePublicKeyEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePublicKeyVerifyRequest(TeaModel):
    def __init__(self, algorithm=None, certificate_id=None, message=None, message_type=None, signature_value=None):
        # The signature algorithm. Valid values:
        # 
        # *   RSA_PKCS1\_SHA\_256
        # 
        # *   RSA_PSS_SHA\_256
        # 
        # *   ECDSA_SHA\_256
        # 
        # *   SM2DSA
        # 
        # > The SM2DSA signature algorithm is supported only in regions where managed hardware security modules (HSMs) are used in the Chinese mainland. For more information, see [Managed HSM overview](~~125803~~).
        self.algorithm = algorithm  # type: str
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str
        # The raw data that is signed.
        # 
        # The value is encoded in Base64. For example, if the raw data in the hexadecimal format is `[0x31, 0x32, 0x33, 0x34]`, set this parameter to the Base64-encoded value `MTIzNA==`.
        # 
        # If the MessageType parameter is set to RAW, the size of the data must be less than or equal to 4 KB.
        # 
        # If the size of the data is greater than 4 KB, you can set the MessageType parameter to DIGEST and set the Message parameter to the digest of the data. The digest is also called hash value. You can compute the digest of the data on an on-premises device. Certificates Manager uses the digest that you compute in your own certificate application system. The message digest algorithm that you use must match the specified signature algorithm. Comply with the following mapping between signature algorithms and message digest algorithms:
        # 
        # *   If the signature algorithm is RSA_PKCS1\_SHA\_256, RSA_PSS_SHA\_256, or ECDSA_SHA\_256, the message digest algorithm must be SHA-256.
        # *   If the signature algorithm is SM2DSA, the message digest algorithm must be SM3.
        # 
        # >  If the key type of the certificate is EC_SM2 and the MessageType parameter is set to DIGEST, the value of the Message parameter is `e` that is described in GB/T 32918.2-2016 6.1.
        self.message = message  # type: str
        # The type of the message. Valid values:
        # 
        # *   RAW: the raw data. This is the default value.
        # *   DIGEST: the message digest (hash value) of the raw data.
        self.message_type = message_type  # type: str
        # The signature value.
        # 
        # The value is encoded in Base64.
        self.signature_value = signature_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePublicKeyVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        return self


class CertificatePublicKeyVerifyResponseBody(TeaModel):
    def __init__(self, certificate_id=None, request_id=None, signature_valid=None):
        # The ID of the certificate.
        self.certificate_id = certificate_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The verification result. Valid values:
        # 
        # *   true: The signature is valid.
        # *   false: The signature is invalid.
        self.signature_valid = signature_valid  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertificatePublicKeyVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_valid is not None:
            result['SignatureValid'] = self.signature_valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureValid') is not None:
            self.signature_valid = m.get('SignatureValid')
        return self


class CertificatePublicKeyVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CertificatePublicKeyVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CertificatePublicKeyVerifyResponse, self).to_map()
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
            temp_model = CertificatePublicKeyVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConnectKmsInstanceRequest(TeaModel):
    def __init__(self, kmprovider=None, kms_instance_id=None, v_switch_ids=None, vpc_id=None, zone_ids=None):
        self.kmprovider = kmprovider  # type: str
        self.kms_instance_id = kms_instance_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_ids = zone_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConnectKmsInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kmprovider is not None:
            result['KMProvider'] = self.kmprovider
        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KMProvider') is not None:
            self.kmprovider = m.get('KMProvider')
        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')
        return self


class ConnectKmsInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConnectKmsInstanceResponseBody, self).to_map()
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


class ConnectKmsInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConnectKmsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConnectKmsInstanceResponse, self).to_map()
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
            temp_model = ConnectKmsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasRequest(TeaModel):
    def __init__(self, alias_name=None, key_id=None):
        # The alias of the CMK.
        # 
        # The alias must be 1 to 255 characters in length and must contain the prefix `alias/`. The alias cannot be prefixed with the reserved word `alias/acs`.
        self.alias_name = alias_name  # type: str
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class CreateAliasResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAliasResponseBody, self).to_map()
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


class CreateAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAliasResponse, self).to_map()
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
            temp_model = CreateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationAccessPointRequest(TeaModel):
    def __init__(self, authentication_method=None, description=None, name=None, policies=None):
        self.authentication_method = authentication_method  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.policies = policies  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationAccessPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_method is not None:
            result['AuthenticationMethod'] = self.authentication_method
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policies is not None:
            result['Policies'] = self.policies
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticationMethod') is not None:
            self.authentication_method = m.get('AuthenticationMethod')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        return self


class CreateApplicationAccessPointResponseBody(TeaModel):
    def __init__(self, arn=None, authentication_method=None, description=None, name=None, policies=None,
                 request_id=None):
        self.arn = arn  # type: str
        self.authentication_method = authentication_method  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.policies = policies  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationAccessPointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.authentication_method is not None:
            result['AuthenticationMethod'] = self.authentication_method
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AuthenticationMethod') is not None:
            self.authentication_method = m.get('AuthenticationMethod')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationAccessPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationAccessPointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationAccessPointResponse, self).to_map()
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
            temp_model = CreateApplicationAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateRequest(TeaModel):
    def __init__(self, exportable_private_key=None, key_spec=None, subject=None, subject_alternative_names=None):
        # Specifies whether the private key of the certificate can be exported for use. Valid values:
        # 
        # *   true: The private key of the certificate can be exported for use. This is the default value.
        # *   false: The private key of the certificate cannot be exported for use. We recommend that you set this parameter to false to protect keys with a higher security level.
        self.exportable_private_key = exportable_private_key  # type: bool
        # The type of the key. Valid values:
        # 
        # *   RSA\_2048
        # *   EC_P256
        # *   EC_SM2
        self.key_spec = key_spec  # type: str
        # The certificate subject, which is the owner of the certificate.
        # 
        # Specify the value in the distinguished name (DN) format, as defined in [RFC 2253](https://tools.ietf.org/html/rfc2253?spm=a2c4g.11186623.2.13.265f1a1cGFCn3Q). A DN is a sequence of relative distinguished names (RDNs).
        # 
        # RDNs are key-value pairs in the format of `attribute1=value1,attribute2=value2`. Separate multiple RDNs with commas (,).
        # 
        # The Subject parameter consists of the following fields:
        # 
        # *   CN: required. The name of the certificate subject.
        # *   C: required. The two-character country or region code in the [ISO 3166-1](https://www.iso.org/obp/ui/#search/code/) standard. For example, CN indicates China.
        # *   O: required. The legal name of the enterprise, company, organization, or institution.
        # *   OU: required. The name of the department.
        # *   ST: optional. The name of the province, municipality, autonomous region, or special administrative region.
        # *   L: optional. The name of the city.
        self.subject = subject  # type: str
        # The subject alternative names.
        # 
        # A domain name list is supported. A maximum of 10 domain names are supported.
        self.subject_alternative_names = subject_alternative_names  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exportable_private_key is not None:
            result['ExportablePrivateKey'] = self.exportable_private_key
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExportablePrivateKey') is not None:
            self.exportable_private_key = m.get('ExportablePrivateKey')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('SubjectAlternativeNames')
        return self


class CreateCertificateShrinkRequest(TeaModel):
    def __init__(self, exportable_private_key=None, key_spec=None, subject=None,
                 subject_alternative_names_shrink=None):
        # Specifies whether the private key of the certificate can be exported for use. Valid values:
        # 
        # *   true: The private key of the certificate can be exported for use. This is the default value.
        # *   false: The private key of the certificate cannot be exported for use. We recommend that you set this parameter to false to protect keys with a higher security level.
        self.exportable_private_key = exportable_private_key  # type: bool
        # The type of the key. Valid values:
        # 
        # *   RSA\_2048
        # *   EC_P256
        # *   EC_SM2
        self.key_spec = key_spec  # type: str
        # The certificate subject, which is the owner of the certificate.
        # 
        # Specify the value in the distinguished name (DN) format, as defined in [RFC 2253](https://tools.ietf.org/html/rfc2253?spm=a2c4g.11186623.2.13.265f1a1cGFCn3Q). A DN is a sequence of relative distinguished names (RDNs).
        # 
        # RDNs are key-value pairs in the format of `attribute1=value1,attribute2=value2`. Separate multiple RDNs with commas (,).
        # 
        # The Subject parameter consists of the following fields:
        # 
        # *   CN: required. The name of the certificate subject.
        # *   C: required. The two-character country or region code in the [ISO 3166-1](https://www.iso.org/obp/ui/#search/code/) standard. For example, CN indicates China.
        # *   O: required. The legal name of the enterprise, company, organization, or institution.
        # *   OU: required. The name of the department.
        # *   ST: optional. The name of the province, municipality, autonomous region, or special administrative region.
        # *   L: optional. The name of the city.
        self.subject = subject  # type: str
        # The subject alternative names.
        # 
        # A domain name list is supported. A maximum of 10 domain names are supported.
        self.subject_alternative_names_shrink = subject_alternative_names_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exportable_private_key is not None:
            result['ExportablePrivateKey'] = self.exportable_private_key
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names_shrink is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExportablePrivateKey') is not None:
            self.exportable_private_key = m.get('ExportablePrivateKey')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names_shrink = m.get('SubjectAlternativeNames')
        return self


class CreateCertificateResponseBody(TeaModel):
    def __init__(self, arn=None, certificate_id=None, csr=None, request_id=None):
        # The Alibaba Cloud Resource Name (ARN) of the certificate.
        self.arn = arn  # type: str
        # The ID of the certificate. It is the globally unique identifier (GUID) of the certificate in Certificates Manager.
        self.certificate_id = certificate_id  # type: str
        # The CSR in the PEM format.
        self.csr = csr  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCertificateResponse, self).to_map()
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
            temp_model = CreateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClientKeyRequest(TeaModel):
    def __init__(self, aap_name=None, not_after=None, not_before=None, password=None):
        self.aap_name = aap_name  # type: str
        self.not_after = not_after  # type: str
        self.not_before = not_before  # type: str
        self.password = password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aap_name is not None:
            result['AapName'] = self.aap_name
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AapName') is not None:
            self.aap_name = m.get('AapName')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class CreateClientKeyResponseBody(TeaModel):
    def __init__(self, client_key_id=None, key_algorithm=None, not_after=None, not_before=None,
                 private_key_data=None, request_id=None):
        self.client_key_id = client_key_id  # type: str
        self.key_algorithm = key_algorithm  # type: str
        self.not_after = not_after  # type: str
        self.not_before = not_before  # type: str
        self.private_key_data = private_key_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClientKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id
        if self.key_algorithm is not None:
            result['KeyAlgorithm'] = self.key_algorithm
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.private_key_data is not None:
            result['PrivateKeyData'] = self.private_key_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')
        if m.get('KeyAlgorithm') is not None:
            self.key_algorithm = m.get('KeyAlgorithm')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('PrivateKeyData') is not None:
            self.private_key_data = m.get('PrivateKeyData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClientKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClientKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClientKeyResponse, self).to_map()
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
            temp_model = CreateClientKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyRequest(TeaModel):
    def __init__(self, dkmsinstance_id=None, description=None, enable_automatic_rotation=None, key_spec=None,
                 key_usage=None, origin=None, protection_level=None, rotation_interval=None, tags=None):
        # The type of the CMK. Valid values:
        # 
        # *   Aliyun_AES\_256
        # *   Aliyun_AES\_128
        # *   Aliyun_AES\_192
        # *   Aliyun_SM4
        # *   RSA\_2048
        # *   RSA\_3072
        # *   EC_P256
        # *   EC_P256K
        # *   EC_SM2
        # 
        # > * The default type of the CMK is Aliyun\_AES\_256.
        # > * Only Dedicated KMS supports Aliyun\_AES\_128 and Aliyun\_AES\_192.
        self.dkmsinstance_id = dkmsinstance_id  # type: str
        # The operation that you want to perform. Set the value to **CreateKey**.
        self.description = description  # type: str
        # The protection level of the CMK. Valid values:
        # 
        # *   SOFTWARE
        # *   HSM
        # 
        # Default value: SOFTWARE.
        # 
        # > * The value of this parameter is case-sensitive.
        # > * Assume that you set this parameter to HSM. If you set the Origin parameter to Aliyun_KMS, the CMK is created in a managed HSM. If you set the Origin parameter to EXTERNAL, you can import an external key into the managed HSM.
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        # The period of automatic key rotation. Specify the value in the integer\[unit] format. Unit: d (day), h (hour), m (minute), or s (second). For example, you can use either 7d or 604800s to specify a seven-day period. The period can range from 7 days to 730 days.
        # 
        # >  If you set the EnableAutomaticRotation parameter to true, you must also specify this parameter. If you set the EnableAutomaticRotation parameter to false, you can leave this parameter unspecified.
        self.key_spec = key_spec  # type: str
        # The description of the CMK.
        # 
        # The description can be 0 to 8,192 characters in length.
        self.key_usage = key_usage  # type: str
        # The usage of the CMK. Valid values:
        # 
        # *   ENCRYPT/DECRYPT: encrypts or decrypts data.
        # *   SIGN/VERIFY: generates or verifies a digital signature.
        # 
        # If the CMK supports signature verification, the default value is SIGN/VERIFY. If the CMK does not support signature verification, the default value is ENCRYPT/DECRYPT.
        self.origin = origin  # type: str
        # The source of key material. Valid values:
        # 
        # *   Aliyun_KMS (default value)
        # *   EXTERNAL
        # 
        # > * The value of this parameter is case-sensitive.
        # > * If you set the KeySpec parameter to an asymmetric CMK type, you are not allowed to set the Origin parameter to EXTERNAL.
        # > * If you set the Origin parameter to EXTERNAL, you must import key material. For more information, see [Import key material](~~68523~~).
        self.protection_level = protection_level  # type: str
        # Specifies whether to enable automatic key rotation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        # 
        # >  If the Origin parameter is set to EXTERNAL or the KeySpec parameter is set to an asymmetric CMK type, automatic key rotation is not supported.
        self.rotation_interval = rotation_interval  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateKeyResponseBodyKeyMetadata(TeaModel):
    def __init__(self, arn=None, automatic_rotation=None, creation_date=None, creator=None, dkmsinstance_id=None,
                 delete_date=None, description=None, key_id=None, key_spec=None, key_state=None, key_usage=None,
                 last_rotation_date=None, material_expire_time=None, next_rotation_date=None, origin=None, primary_key_version=None,
                 protection_level=None, rotation_interval=None):
        # The period of automatic key rotation. Unit: seconds. The value is in the format of an integer followed by the letter s. For example, if the rotation period is seven days, this parameter is set to 604800s. This value is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.arn = arn  # type: str
        # The time when the key material expires. The time is displayed in UTC.
        # 
        # If this parameter value is empty, the key material does not expire.
        self.automatic_rotation = automatic_rotation  # type: str
        # The usage of the CMK.
        self.creation_date = creation_date  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the CMK.
        self.creator = creator  # type: str
        # The date and time when the CMK was created. The time is displayed in UTC.
        self.dkmsinstance_id = dkmsinstance_id  # type: str
        # The time when the last rotation was performed. The time is displayed in UTC.
        # 
        # For a new CMK, this parameter value is the time when the initial version of the CMK was generated.
        self.delete_date = delete_date  # type: str
        # The ID of the current primary key version of the symmetric CMK.
        # 
        # > * The primary key version of a symmetric CMK is an active encryption key. KMS uses the primary key version of a specified CMK to encrypt data.
        # > * This parameter is unavailable for asymmetric CMKs.
        self.description = description  # type: str
        # The metadata of the CMK.
        self.key_id = key_id  # type: str
        # The description of the CMK.
        self.key_spec = key_spec  # type: str
        # The time when the next rotation will be performed.
        # 
        # >  This value is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.key_state = key_state  # type: str
        # The protection level of the CMK.
        self.key_usage = key_usage  # type: str
        # The creator of the CMK.
        self.last_rotation_date = last_rotation_date  # type: str
        # The source of the key material for the CMK.
        self.material_expire_time = material_expire_time  # type: str
        # The ID of the CMK. The ID must be globally unique.
        self.next_rotation_date = next_rotation_date  # type: str
        # The type of the CMK.
        self.origin = origin  # type: str
        # The time when the CMK is scheduled for deletion.
        # 
        # For more information, see [ScheduleKeyDeletion](~~44196~~).
        # 
        # >  This value is returned only when the value of the KeyState parameter is PendingDeletion.
        self.primary_key_version = primary_key_version  # type: str
        # Indicates whether automatic key rotation is enabled. Valid values:
        # 
        # *   Enabled: Automatic key rotation is enabled.
        # *   Disabled: Automatic key rotation is disabled.
        # *   Suspended: Automatic key rotation is suspended. For more information, see [Automatic key rotation](~~134270~~).
        # 
        # >  Automatic key rotation is available only for symmetric CMKs.
        self.protection_level = protection_level  # type: str
        # The status of the CMK.
        # 
        # For more information, see [Impact of CMK status on API operations](~~44211~~).
        self.rotation_interval = rotation_interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeyResponseBodyKeyMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.key_state is not None:
            result['KeyState'] = self.key_state
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.primary_key_version is not None:
            result['PrimaryKeyVersion'] = self.primary_key_version
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('KeyState') is not None:
            self.key_state = m.get('KeyState')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('PrimaryKeyVersion') is not None:
            self.primary_key_version = m.get('PrimaryKeyVersion')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class CreateKeyResponseBody(TeaModel):
    def __init__(self, key_metadata=None, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.key_metadata = key_metadata  # type: CreateKeyResponseBodyKeyMetadata
        # The ID of the dedicated KMS instance.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.key_metadata:
            self.key_metadata.validate()

    def to_map(self):
        _map = super(CreateKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_metadata is not None:
            result['KeyMetadata'] = self.key_metadata.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyMetadata') is not None:
            temp_model = CreateKeyResponseBodyKeyMetadata()
            self.key_metadata = temp_model.from_map(m['KeyMetadata'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateKeyResponse, self).to_map()
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
            temp_model = CreateKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyVersionRequest(TeaModel):
    def __init__(self, key_id=None):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  You can also set the value to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeyVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class CreateKeyVersionResponseBodyKeyVersion(TeaModel):
    def __init__(self, creation_date=None, key_id=None, key_version_id=None):
        # The date and time when the version was created. The time is displayed in UTC.
        self.creation_date = creation_date  # type: str
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str
        # The ID of the version.
        self.key_version_id = key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeyVersionResponseBodyKeyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class CreateKeyVersionResponseBody(TeaModel):
    def __init__(self, key_version=None, request_id=None):
        # The metadata of the version.
        self.key_version = key_version  # type: CreateKeyVersionResponseBodyKeyVersion
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.key_version:
            self.key_version.validate()

    def to_map(self):
        _map = super(CreateKeyVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyVersion') is not None:
            temp_model = CreateKeyVersionResponseBodyKeyVersion()
            self.key_version = temp_model.from_map(m['KeyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateKeyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateKeyVersionResponse, self).to_map()
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
            temp_model = CreateKeyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkRuleRequest(TeaModel):
    def __init__(self, description=None, name=None, source_private_ip=None, type=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.source_private_ip = source_private_ip  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.source_private_ip is not None:
            result['SourcePrivateIp'] = self.source_private_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourcePrivateIp') is not None:
            self.source_private_ip = m.get('SourcePrivateIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateNetworkRuleResponseBody(TeaModel):
    def __init__(self, arn=None, description=None, name=None, request_id=None, source_private_ip=None, type=None):
        self.arn = arn  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.source_private_ip = source_private_ip  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_private_ip is not None:
            result['SourcePrivateIp'] = self.source_private_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourcePrivateIp') is not None:
            self.source_private_ip = m.get('SourcePrivateIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateNetworkRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNetworkRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNetworkRuleResponse, self).to_map()
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
            temp_model = CreateNetworkRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(self, access_control_rules=None, description=None, kms_instance=None, name=None, permissions=None,
                 resources=None):
        self.access_control_rules = access_control_rules  # type: str
        self.description = description  # type: str
        self.kms_instance = kms_instance  # type: str
        self.name = name  # type: str
        self.permissions = permissions  # type: str
        self.resources = resources  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_rules is not None:
            result['AccessControlRules'] = self.access_control_rules
        if self.description is not None:
            result['Description'] = self.description
        if self.kms_instance is not None:
            result['KmsInstance'] = self.kms_instance
        if self.name is not None:
            result['Name'] = self.name
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlRules') is not None:
            self.access_control_rules = m.get('AccessControlRules')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KmsInstance') is not None:
            self.kms_instance = m.get('KmsInstance')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(self, access_control_rules=None, arn=None, description=None, kms_instance=None, name=None,
                 permissions=None, request_id=None, resources=None):
        self.access_control_rules = access_control_rules  # type: str
        self.arn = arn  # type: str
        self.description = description  # type: str
        self.kms_instance = kms_instance  # type: str
        self.name = name  # type: str
        self.permissions = permissions  # type: str
        self.request_id = request_id  # type: str
        self.resources = resources  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_rules is not None:
            result['AccessControlRules'] = self.access_control_rules
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.kms_instance is not None:
            result['KmsInstance'] = self.kms_instance
        if self.name is not None:
            result['Name'] = self.name
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlRules') is not None:
            self.access_control_rules = m.get('AccessControlRules')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KmsInstance') is not None:
            self.kms_instance = m.get('KmsInstance')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolicyResponse, self).to_map()
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretRequest(TeaModel):
    def __init__(self, dkmsinstance_id=None, description=None, enable_automatic_rotation=None,
                 encryption_key_id=None, extended_config=None, rotation_interval=None, secret_data=None, secret_data_type=None,
                 secret_name=None, secret_type=None, tags=None, version_id=None):
        # The version number of the secret.
        self.dkmsinstance_id = dkmsinstance_id  # type: str
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # *   true: specifies to enable automatic rotation.
        # *   false: specifies to disable automatic rotation. This is the default value.
        # 
        # >  This parameter is valid if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.description = description  # type: str
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        # The description of the secret.
        self.encryption_key_id = encryption_key_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.extended_config = extended_config  # type: dict[str, any]
        # The name of the secret.
        self.rotation_interval = rotation_interval  # type: str
        # The tags of the secret.
        self.secret_data = secret_data  # type: str
        # The extended configuration of the secret. This parameter specifies the properties of the secret of the specific type. The description can be up to 1,024 characters in length.
        # 
        # *   If you set the SecretType parameter to Generic, you do not need to configure this parameter.
        # 
        # *   If you set the SecretType parameter to Rds, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   SingleUser: Secrets Manager manages the ApsaraDB RDS secret in single-account mode. When the secret is rotated, the password of the specified account is reset to a new random password.
        #         *   DoubleUsers: Secrets Manager manages the ApsaraDB RDS secret in dual-account mode. One account is referenced by the ACSCurrent version, and the other account is referenced by the ACSPrevious version. When the secret is rotated, the password of the account referenced by the ACSPrevious version is reset to a new random password. Then, Secrets Manager switches the referenced accounts between the ACSCurrent and ACSPrevious versions.
        # 
        #     *   DBInstanceId: required. The ApsaraDB RDS instance to which the ApsaraDB RDS account belongs.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to RAMCredentials, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Set the value to RamUserAccessKey.
        #     *   UserName: required. The name of the RAM user.
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to ECS, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   Password: the password that is used to log on to the ECS instance.
        #         *   SSHKey: the SSH public key and private key that are used to log on to the ECS instance.
        # 
        #     *   RegionId: required. The ID of the region in which the ECS instance resides.
        # 
        #     *   InstanceId: required. The ID of the ECS instance.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # >  This parameter is required if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.secret_data_type = secret_data_type  # type: str
        # The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores the encrypted value in the initial version.
        # 
        # *   If you set the SecretType parameter to Generic that indicates a generic secret, you can customize the secret value.
        # 
        # *   If you set the SecretType parameter to Rds that indicates a managed ApsaraDB RDS secret, the secret value must be in the format of `{"Accounts":[{"AccountName":"","AccountPassword":""}]}`. In the preceding format, `AccountName` indicates the username of the account that is used to connect to your ApsaraDB RDS instance, and `AccountPassword` specifies the password of the account.
        # 
        # *   If you set the SecretType parameter to RAMCredentials that indicates a managed RAM secret, the secret value must be in the format of `{"AccessKeys":[{"AccessKeyId":"","AccessKeySecret":"",}]}`. In the preceding format, `AccessKeyId` indicates the AccessKey ID of the RAM user and `AccessKeySecret` specifies the AccessKey secret of the RAM user. You must specify all the AccessKey pairs of the RAM user.
        # 
        # *   If you set the SecretType parameter to ECS that indicates a managed ECS secret, the secret value must be in one of the following formats:
        # 
        #     *   `{"UserName":"","Password": ""}`: In the format, `UserName` specifies the username that is used to log on to the ECS instance, and `Password` specifies the password that is used to log on to the ECS instance.
        #     *   `{"UserName":"","PublicKey": "", "PrivateKey": ""}`: In the format, `PublicKey` indicates the SSH public key that is used to log on to the ECS instance, and `PrivateKey` specifies the SSH private key that is used to log on to the ECS instance.
        self.secret_name = secret_name  # type: str
        # The ID of the dedicated KMS instance.
        self.secret_type = secret_type  # type: str
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).
        # 
        # The value is in the `integer[unit]` format.
        # 
        # The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s indicate a seven-day interval.
        # 
        # >  This parameter is required if you set the EnableAutomaticRotation parameter to true. This parameter is ignored if you set the EnableAutomaticRotation parameter to false or if the EnableAutomaticRotation parameter is not configured.
        self.tags = tags  # type: str
        # The type of the secret value. Valid values:
        # 
        # *   text
        # *   binary
        # 
        # >  If you set the SecretType parameter to Rds, RAMCredentials, or ECS, the SecretDataType parameter must be set to text.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateSecretShrinkRequest(TeaModel):
    def __init__(self, dkmsinstance_id=None, description=None, enable_automatic_rotation=None,
                 encryption_key_id=None, extended_config_shrink=None, rotation_interval=None, secret_data=None,
                 secret_data_type=None, secret_name=None, secret_type=None, tags=None, version_id=None):
        # The version number of the secret.
        self.dkmsinstance_id = dkmsinstance_id  # type: str
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # *   true: specifies to enable automatic rotation.
        # *   false: specifies to disable automatic rotation. This is the default value.
        # 
        # >  This parameter is valid if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.description = description  # type: str
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        # The description of the secret.
        self.encryption_key_id = encryption_key_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.extended_config_shrink = extended_config_shrink  # type: str
        # The name of the secret.
        self.rotation_interval = rotation_interval  # type: str
        # The tags of the secret.
        self.secret_data = secret_data  # type: str
        # The extended configuration of the secret. This parameter specifies the properties of the secret of the specific type. The description can be up to 1,024 characters in length.
        # 
        # *   If you set the SecretType parameter to Generic, you do not need to configure this parameter.
        # 
        # *   If you set the SecretType parameter to Rds, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   SingleUser: Secrets Manager manages the ApsaraDB RDS secret in single-account mode. When the secret is rotated, the password of the specified account is reset to a new random password.
        #         *   DoubleUsers: Secrets Manager manages the ApsaraDB RDS secret in dual-account mode. One account is referenced by the ACSCurrent version, and the other account is referenced by the ACSPrevious version. When the secret is rotated, the password of the account referenced by the ACSPrevious version is reset to a new random password. Then, Secrets Manager switches the referenced accounts between the ACSCurrent and ACSPrevious versions.
        # 
        #     *   DBInstanceId: required. The ApsaraDB RDS instance to which the ApsaraDB RDS account belongs.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to RAMCredentials, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Set the value to RamUserAccessKey.
        #     *   UserName: required. The name of the RAM user.
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # *   If you set the SecretType parameter to ECS, configure the following fields for the ExtendedConfig parameter:
        # 
        #     *   SecretSubType: required. The subtype of the secret. Valid values:
        # 
        #         *   Password: the password that is used to log on to the ECS instance.
        #         *   SSHKey: the SSH public key and private key that are used to log on to the ECS instance.
        # 
        #     *   RegionId: required. The ID of the region in which the ECS instance resides.
        # 
        #     *   InstanceId: required. The ID of the ECS instance.
        # 
        #     *   CustomData: optional. The custom data. The value is a collection of key-value pairs in the JSON format. Up to 10 key-value pairs can be specified. Separate multiple key-value pairs with commas (,). The default value is a pair of empty braces (`{}`).
        # 
        # >  This parameter is required if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.secret_data_type = secret_data_type  # type: str
        # The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores the encrypted value in the initial version.
        # 
        # *   If you set the SecretType parameter to Generic that indicates a generic secret, you can customize the secret value.
        # 
        # *   If you set the SecretType parameter to Rds that indicates a managed ApsaraDB RDS secret, the secret value must be in the format of `{"Accounts":[{"AccountName":"","AccountPassword":""}]}`. In the preceding format, `AccountName` indicates the username of the account that is used to connect to your ApsaraDB RDS instance, and `AccountPassword` specifies the password of the account.
        # 
        # *   If you set the SecretType parameter to RAMCredentials that indicates a managed RAM secret, the secret value must be in the format of `{"AccessKeys":[{"AccessKeyId":"","AccessKeySecret":"",}]}`. In the preceding format, `AccessKeyId` indicates the AccessKey ID of the RAM user and `AccessKeySecret` specifies the AccessKey secret of the RAM user. You must specify all the AccessKey pairs of the RAM user.
        # 
        # *   If you set the SecretType parameter to ECS that indicates a managed ECS secret, the secret value must be in one of the following formats:
        # 
        #     *   `{"UserName":"","Password": ""}`: In the format, `UserName` specifies the username that is used to log on to the ECS instance, and `Password` specifies the password that is used to log on to the ECS instance.
        #     *   `{"UserName":"","PublicKey": "", "PrivateKey": ""}`: In the format, `PublicKey` indicates the SSH public key that is used to log on to the ECS instance, and `PrivateKey` specifies the SSH private key that is used to log on to the ECS instance.
        self.secret_name = secret_name  # type: str
        # The ID of the dedicated KMS instance.
        self.secret_type = secret_type  # type: str
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).
        # 
        # The value is in the `integer[unit]` format.
        # 
        # The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s indicate a seven-day interval.
        # 
        # >  This parameter is required if you set the EnableAutomaticRotation parameter to true. This parameter is ignored if you set the EnableAutomaticRotation parameter to false or if the EnableAutomaticRotation parameter is not configured.
        self.tags = tags  # type: str
        # The type of the secret value. Valid values:
        # 
        # *   text
        # *   binary
        # 
        # >  If you set the SecretType parameter to Rds, RAMCredentials, or ECS, the SecretDataType parameter must be set to text.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.extended_config_shrink is not None:
            result['ExtendedConfig'] = self.extended_config_shrink
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config_shrink = m.get('ExtendedConfig')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateSecretResponseBody(TeaModel):
    def __init__(self, arn=None, automatic_rotation=None, dkmsinstance_id=None, extended_config=None,
                 next_rotation_date=None, request_id=None, rotation_interval=None, secret_name=None, secret_type=None, version_id=None):
        self.arn = arn  # type: str
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        # *   RAMCredentials: indicates a managed RAM secret.
        # *   ECS: indicates a managed ECS secret.
        self.automatic_rotation = automatic_rotation  # type: str
        self.dkmsinstance_id = dkmsinstance_id  # type: str
        self.extended_config = extended_config  # type: str
        # The extended configuration of the secret.
        # 
        # >  This parameter is returned if you set the SecretType parameter to Rds, RAMCredentials, or ECS.
        self.next_rotation_date = next_rotation_date  # type: str
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.request_id = request_id  # type: str
        self.rotation_interval = rotation_interval  # type: str
        # The interval for automatic rotation.
        # 
        # The value is in the `integer[unit]` format. The value of the `unit` field is fixed as s. For example, if the value is 604800s, automatic rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.secret_name = secret_name  # type: str
        # The ID of the dedicated KMS instance.
        self.secret_type = secret_type  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSecretResponse, self).to_map()
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
            temp_model = CreateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecryptRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, encryption_context=None):
        # The ciphertext that you want to decrypt.
        # 
        # You can generate the ciphertext by calling the following operations:
        # 
        # *   [GenerateDataKey](~~28948~~)
        # *   [Encrypt](~~28949~~)
        # *   [GenerateDataKeyWithoutPlaintext](~~134043~~)
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The JSON string that consists of key-value pairs.
        # 
        # >  If you specify the EncryptionContext parameter when you call the [GenerateDataKey](~~28948~~), [Encrypt](~~28949~~), or [GenerateDataKeyWithoutPlaintext](~~134043~~) operation, you must specify the same context when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        return self


class DecryptShrinkRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, encryption_context_shrink=None):
        # The ciphertext that you want to decrypt.
        # 
        # You can generate the ciphertext by calling the following operations:
        # 
        # *   [GenerateDataKey](~~28948~~)
        # *   [Encrypt](~~28949~~)
        # *   [GenerateDataKeyWithoutPlaintext](~~134043~~)
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The JSON string that consists of key-value pairs.
        # 
        # >  If you specify the EncryptionContext parameter when you call the [GenerateDataKey](~~28948~~), [Encrypt](~~28949~~), or [GenerateDataKeyWithoutPlaintext](~~134043~~) operation, you must specify the same context when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecryptShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        return self


class DecryptResponseBody(TeaModel):
    def __init__(self, key_id=None, key_version_id=None, plaintext=None, request_id=None):
        # The ID of the customer master key (CMK) that is used to decrypt the ciphertext.
        # 
        # It is the GUID of the CMK.
        self.key_id = key_id  # type: str
        # The ID of the CMK version that is used to decrypt the ciphertext.
        self.key_version_id = key_version_id  # type: str
        # The plaintext that is generated after decryption.
        self.plaintext = plaintext  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DecryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DecryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DecryptResponse, self).to_map()
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
            temp_model = DecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAliasRequest(TeaModel):
    def __init__(self, alias_name=None):
        # The alias that you want to delete.
        # 
        # The value must be 1 to 255 characters in length and must include the alias/ prefix.
        self.alias_name = alias_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class DeleteAliasResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAliasResponseBody, self).to_map()
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


class DeleteAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAliasResponse, self).to_map()
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
            temp_model = DeleteAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationAccessPointRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationAccessPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteApplicationAccessPointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationAccessPointResponseBody, self).to_map()
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


class DeleteApplicationAccessPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationAccessPointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationAccessPointResponse, self).to_map()
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
            temp_model = DeleteApplicationAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None):
        # The ID of the certificate. It is the globally unique identifier (GUID) of the certificate in Alibaba Cloud Certificate Manager.
        self.certificate_id = certificate_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class DeleteCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCertificateResponseBody, self).to_map()
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


class DeleteCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCertificateResponse, self).to_map()
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
            temp_model = DeleteCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClientKeyRequest(TeaModel):
    def __init__(self, client_key_id=None):
        self.client_key_id = client_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClientKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')
        return self


class DeleteClientKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClientKeyResponseBody, self).to_map()
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


class DeleteClientKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClientKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClientKeyResponse, self).to_map()
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
            temp_model = DeleteClientKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyMaterialRequest(TeaModel):
    def __init__(self, key_id=None):
        # The globally unique ID of the CMK.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKeyMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DeleteKeyMaterialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKeyMaterialResponseBody, self).to_map()
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


class DeleteKeyMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteKeyMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteKeyMaterialResponse, self).to_map()
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
            temp_model = DeleteKeyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkRuleRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteNetworkRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkRuleResponseBody, self).to_map()
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


class DeleteNetworkRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNetworkRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNetworkRuleResponse, self).to_map()
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
            temp_model = DeleteNetworkRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyResponseBody, self).to_map()
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


class DeletePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyResponse, self).to_map()
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretRequest(TeaModel):
    def __init__(self, force_delete_without_recovery=None, recovery_window_in_days=None, secret_name=None):
        # Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered.
        # 
        # Valid values:
        # 
        # *   **true**\
        # *   **false** (default value)
        self.force_delete_without_recovery = force_delete_without_recovery  # type: str
        # Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. Unit: Days.
        self.recovery_window_in_days = recovery_window_in_days  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete_without_recovery is not None:
            result['ForceDeleteWithoutRecovery'] = self.force_delete_without_recovery
        if self.recovery_window_in_days is not None:
            result['RecoveryWindowInDays'] = self.recovery_window_in_days
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForceDeleteWithoutRecovery') is not None:
            self.force_delete_without_recovery = m.get('ForceDeleteWithoutRecovery')
        if m.get('RecoveryWindowInDays') is not None:
            self.recovery_window_in_days = m.get('RecoveryWindowInDays')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class DeleteSecretResponseBody(TeaModel):
    def __init__(self, planned_delete_time=None, request_id=None, secret_name=None):
        # The time when the secret is scheduled to be deleted.
        self.planned_delete_time = planned_delete_time  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class DeleteSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSecretResponse, self).to_map()
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
            temp_model = DeleteSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountKmsStatusResponseBody(TeaModel):
    def __init__(self, account_status=None, request_id=None):
        # The status of KMS within your Alibaba cloud account. Valid values:
        # 
        # *   Enabled: KMS is enabled.
        # 
        # *   NotEnabled: KMS is disabled.
        # 
        # *   InDebt: Your account is overdue, and KMS stops providing services.
        # 
        # > If your Alibaba Cloud account is overdue, top up your account at the earliest opportunity to avoid impacts on your services.
        # 
        # *   Suspended: KMS is suspended.
        self.account_status = account_status  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountKmsStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountKmsStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAccountKmsStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccountKmsStatusResponse, self).to_map()
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
            temp_model = DescribeAccountKmsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationAccessPointRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationAccessPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeApplicationAccessPointResponseBody(TeaModel):
    def __init__(self, arn=None, authentication_method=None, description=None, name=None, policies=None,
                 request_id=None):
        self.arn = arn  # type: str
        self.authentication_method = authentication_method  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.policies = policies  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationAccessPointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.authentication_method is not None:
            result['AuthenticationMethod'] = self.authentication_method
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AuthenticationMethod') is not None:
            self.authentication_method = m.get('AuthenticationMethod')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApplicationAccessPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationAccessPointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationAccessPointResponse, self).to_map()
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
            temp_model = DescribeApplicationAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None):
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class DescribeCertificateResponseBody(TeaModel):
    def __init__(self, arn=None, certificate_id=None, created_at=None, exportable_private_key=None, issuer=None,
                 key_spec=None, not_after=None, not_before=None, request_id=None, serial=None, signature_algorithm=None,
                 status=None, subject=None, subject_alternative_names=None, subject_key_identifier=None,
                 subject_public_key=None, tags=None, updated_at=None):
        # The Alibaba Cloud Resource Name (ARN) of the certificate.
        self.arn = arn  # type: str
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str
        # The time when the certificate was created.
        self.created_at = created_at  # type: str
        # Indicates whether the private key of the certificate can be exported for use. Valid values:
        # 
        # *   true: The private key of the certificate can be exported for use. This is the default value.
        # *   false: The private key of the certificate cannot be exported for use.
        self.exportable_private_key = exportable_private_key  # type: bool
        # The certificate issuer in the distinguished name (DN) format.
        self.issuer = issuer  # type: str
        # The type of the key.
        self.key_spec = key_spec  # type: str
        # The end of the validity period of the certificate.
        self.not_after = not_after  # type: str
        # The beginning of the validity period of the certificate.
        self.not_before = not_before  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The serial number of the certificate.
        self.serial = serial  # type: str
        # The signature algorithm of the certificate. Valid values:
        # 
        # *   RSA2048-SHA256
        # *   ECDSA-SHA256
        # *   SM2-SM3
        self.signature_algorithm = signature_algorithm  # type: str
        # The status of the certificate. Valid values:
        # 
        # *   PENDING: The certificate is to be imported.
        # *   ACTIVE: The certificate is enabled.
        # *   INACTIVE: The certificate is disabled.
        # *   REVOKED: The certificate is revoked.
        self.status = status  # type: str
        # The subject of the certificate, which is in the DN format.
        self.subject = subject  # type: str
        # The alias of the certificate subject.
        # 
        # A domain name list is supported. A maximum of 10 domain names are supported.
        self.subject_alternative_names = subject_alternative_names  # type: list[str]
        # The public key identifier of the certificate subject.
        self.subject_key_identifier = subject_key_identifier  # type: str
        # The public key of the certificate.
        self.subject_public_key = subject_public_key  # type: str
        # The tag of the certificate.
        self.tags = tags  # type: dict[str, any]
        # The time when the certificate was updated.
        self.updated_at = updated_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.exportable_private_key is not None:
            result['ExportablePrivateKey'] = self.exportable_private_key
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serial is not None:
            result['Serial'] = self.serial
        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm
        if self.status is not None:
            result['Status'] = self.status
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names
        if self.subject_key_identifier is not None:
            result['SubjectKeyIdentifier'] = self.subject_key_identifier
        if self.subject_public_key is not None:
            result['SubjectPublicKey'] = self.subject_public_key
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ExportablePrivateKey') is not None:
            self.exportable_private_key = m.get('ExportablePrivateKey')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')
        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('SubjectAlternativeNames')
        if m.get('SubjectKeyIdentifier') is not None:
            self.subject_key_identifier = m.get('SubjectKeyIdentifier')
        if m.get('SubjectPublicKey') is not None:
            self.subject_public_key = m.get('SubjectPublicKey')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class DescribeCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCertificateResponse, self).to_map()
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
            temp_model = DescribeCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyRequest(TeaModel):
    def __init__(self, key_id=None):
        # The ID of the CMK. The ID must be globally unique.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Overview of aliases](~~68522~~).
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DescribeKeyResponseBodyKeyMetadata(TeaModel):
    def __init__(self, arn=None, automatic_rotation=None, creation_date=None, creator=None, dkmsinstance_id=None,
                 delete_date=None, deletion_protection=None, deletion_protection_description=None, description=None,
                 key_id=None, key_spec=None, key_state=None, key_usage=None, last_rotation_date=None,
                 material_expire_time=None, next_rotation_date=None, origin=None, primary_key_version=None, protection_level=None,
                 rotation_interval=None):
        # The Alibaba Cloud Resource Name (ARN) of the CMK.
        self.arn = arn  # type: str
        # Indicates whether automatic key rotation is enabled. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        # *   Suspended
        # 
        # For more information, see [Automatic key rotation](~~134270~~).
        # 
        # >  Only symmetric CMKs support automatic key rotation.
        self.automatic_rotation = automatic_rotation  # type: str
        # The time when the CMK was created. The time is displayed in UTC.
        self.creation_date = creation_date  # type: str
        # The Alibaba Cloud account that is used to create the CMK.
        self.creator = creator  # type: str
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id  # type: str
        # The time at which the CMK is scheduled for deletion. The time is displayed in UTC.
        # 
        # For more information, see [ScheduleKeyDeletion](~~44196~~).
        # 
        # >  This parameter is returned only when the value of the KeyState parameter is PendingDeletion.
        self.delete_date = delete_date  # type: str
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.deletion_protection = deletion_protection  # type: str
        # The description of deletion protection.
        self.deletion_protection_description = deletion_protection_description  # type: str
        # The description of the CMK.
        self.description = description  # type: str
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str
        # The type of the CMK.
        self.key_spec = key_spec  # type: str
        # The status of the CMK.
        # 
        # For more information, see [Impact of CMK status on API operations](~~44211~~).
        self.key_state = key_state  # type: str
        # The usage of the CMK.
        self.key_usage = key_usage  # type: str
        # The time when the last rotation was performed. The time is displayed in UTC. For a new CMK, the value of this parameter is the time when the initial version of the CMK was generated.
        self.last_rotation_date = last_rotation_date  # type: str
        # The time when the key material expires. The time is displayed in UTC. If this parameter value is empty, the key material does not expire.
        self.material_expire_time = material_expire_time  # type: str
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.next_rotation_date = next_rotation_date  # type: str
        # The source of the key material for the CMK.
        self.origin = origin  # type: str
        # The ID of the current primary key version for the symmetric CMK.
        self.primary_key_version = primary_key_version  # type: str
        # The protection level of the CMK.
        self.protection_level = protection_level  # type: str
        # The interval for automatic key rotation.
        # 
        # Unit: seconds.
        # 
        # For example, if the value is 604800s, automatic key rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned only when the value of the AutomaticRotation parameter is Enabled or Suspended.
        self.rotation_interval = rotation_interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeyResponseBodyKeyMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.deletion_protection_description is not None:
            result['DeletionProtectionDescription'] = self.deletion_protection_description
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.key_state is not None:
            result['KeyState'] = self.key_state
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.primary_key_version is not None:
            result['PrimaryKeyVersion'] = self.primary_key_version
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('DeletionProtectionDescription') is not None:
            self.deletion_protection_description = m.get('DeletionProtectionDescription')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('KeyState') is not None:
            self.key_state = m.get('KeyState')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('PrimaryKeyVersion') is not None:
            self.primary_key_version = m.get('PrimaryKeyVersion')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class DescribeKeyResponseBody(TeaModel):
    def __init__(self, key_metadata=None, request_id=None):
        # The metadata of the CMK.
        self.key_metadata = key_metadata  # type: DescribeKeyResponseBodyKeyMetadata
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.key_metadata:
            self.key_metadata.validate()

    def to_map(self):
        _map = super(DescribeKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_metadata is not None:
            result['KeyMetadata'] = self.key_metadata.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyMetadata') is not None:
            temp_model = DescribeKeyResponseBodyKeyMetadata()
            self.key_metadata = temp_model.from_map(m['KeyMetadata'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeKeyResponse, self).to_map()
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
            temp_model = DescribeKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyVersionRequest(TeaModel):
    def __init__(self, key_id=None, key_version_id=None):
        # The globally unique ID of the CMK.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id  # type: str
        # The globally unique ID of the CMK version.
        # 
        # You can call the [ListKeyVersions](~~133966~~) operation to query the versions of the CMK.
        self.key_version_id = key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeyVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class DescribeKeyVersionResponseBodyKeyVersion(TeaModel):
    def __init__(self, creation_date=None, key_id=None, key_version_id=None):
        # The date and time when the CMK version was created. The time is displayed in UTC.
        self.creation_date = creation_date  # type: str
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter in the request to an alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The globally unique ID of the CMK version.
        self.key_version_id = key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeyVersionResponseBodyKeyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class DescribeKeyVersionResponseBody(TeaModel):
    def __init__(self, key_version=None, request_id=None):
        # The metadata of the CMK version.
        self.key_version = key_version  # type: DescribeKeyVersionResponseBodyKeyVersion
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.key_version:
            self.key_version.validate()

    def to_map(self):
        _map = super(DescribeKeyVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyVersion') is not None:
            temp_model = DescribeKeyVersionResponseBodyKeyVersion()
            self.key_version = temp_model.from_map(m['KeyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeKeyVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeKeyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeKeyVersionResponse, self).to_map()
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
            temp_model = DescribeKeyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRuleRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeNetworkRuleResponseBody(TeaModel):
    def __init__(self, arn=None, description=None, request_id=None, source_private_ip=None, type=None):
        self.arn = arn  # type: str
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.source_private_ip = source_private_ip  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_private_ip is not None:
            result['SourcePrivateIp'] = self.source_private_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourcePrivateIp') is not None:
            self.source_private_ip = m.get('SourcePrivateIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeNetworkRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNetworkRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNetworkRuleResponse, self).to_map()
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
            temp_model = DescribeNetworkRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribePolicyResponseBody(TeaModel):
    def __init__(self, access_control_rules=None, arn=None, description=None, kms_instance=None, name=None,
                 permissions=None, request_id=None, resources=None):
        self.access_control_rules = access_control_rules  # type: str
        self.arn = arn  # type: str
        self.description = description  # type: str
        self.kms_instance = kms_instance  # type: str
        self.name = name  # type: str
        self.permissions = permissions  # type: list[str]
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_rules is not None:
            result['AccessControlRules'] = self.access_control_rules
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.description is not None:
            result['Description'] = self.description
        if self.kms_instance is not None:
            result['KmsInstance'] = self.kms_instance
        if self.name is not None:
            result['Name'] = self.name
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlRules') is not None:
            self.access_control_rules = m.get('AccessControlRules')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KmsInstance') is not None:
            self.kms_instance = m.get('KmsInstance')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class DescribePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyResponse, self).to_map()
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
            temp_model = DescribePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, region_id=None):
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # The region.
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecretRequest(TeaModel):
    def __init__(self, fetch_tags=None, secret_name=None):
        # Specifies whether to return the resource tags of the secret. Valid values:
        # 
        # *   true: The resource tags are returned.
        # *   false: The resource tags are not returned. This is the default value.
        self.fetch_tags = fetch_tags  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class DescribeSecretResponseBodyTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecretResponseBodyTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeSecretResponseBodyTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeSecretResponseBodyTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecretResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSecretResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSecretResponseBody(TeaModel):
    def __init__(self, arn=None, automatic_rotation=None, create_time=None, dkmsinstance_id=None, description=None,
                 encryption_key_id=None, extended_config=None, last_rotation_date=None, next_rotation_date=None,
                 planned_delete_time=None, request_id=None, rotation_interval=None, secret_name=None, secret_type=None, tags=None,
                 update_time=None):
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.arn = arn  # type: str
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.automatic_rotation = automatic_rotation  # type: str
        # The time when the secret was created.
        self.create_time = create_time  # type: str
        # The ID of the dedicated KMS instance.
        self.dkmsinstance_id = dkmsinstance_id  # type: str
        # The description of the secret.
        self.description = description  # type: str
        # The ID of the customer master key (CMK) that is used to encrypt the secret value.
        self.encryption_key_id = encryption_key_id  # type: str
        # The extended configuration of the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed Resource Access Management (RAM) secret, or a managed Elastic Compute Service (ECS) secret.
        self.extended_config = extended_config  # type: str
        # The time when the last rotation was performed.
        # 
        # >  This parameter is returned if the secret was rotated.
        self.last_rotation_date = last_rotation_date  # type: str
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned when automatic rotation is enabled.
        self.next_rotation_date = next_rotation_date  # type: str
        # The time when the secret is scheduled to be deleted.
        self.planned_delete_time = planned_delete_time  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The interval for automatic rotation.
        # 
        # The value is in the `integer[unit]` format. `integer` indicates the length of time. `unit`: indicates the time unit. The value of `unit` is fixed as s. For example, if the value is 604800s, automatic rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned when automatic rotation is enabled.
        self.rotation_interval = rotation_interval  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        # *   RAMCredentials: indicates a managed RAM secret.
        # *   ECS: indicates a managed ECS secret.
        self.secret_type = secret_type  # type: str
        # The resource tags of the secret.
        # 
        # This parameter is not returned if you set the FetchTags parameter to false or you do not specify the FetchTags parameter.
        self.tags = tags  # type: DescribeSecretResponseBodyTags
        # The time when the secret was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            temp_model = DescribeSecretResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecretResponse, self).to_map()
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
            temp_model = DescribeSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableKeyRequest(TeaModel):
    def __init__(self, key_id=None):
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DisableKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableKeyResponseBody, self).to_map()
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


class DisableKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableKeyResponse, self).to_map()
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
            temp_model = DisableKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableKeyRequest(TeaModel):
    def __init__(self, key_id=None):
        # The globally unique ID of the CMK.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class EnableKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableKeyResponseBody, self).to_map()
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


class EnableKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableKeyResponse, self).to_map()
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
            temp_model = EnableKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptRequest(TeaModel):
    def __init__(self, encryption_context=None, key_id=None, plaintext=None):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context  # type: dict[str, any]
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The plaintext to be encrypted. The plaintext must be Base64 encoded.
        self.plaintext = plaintext  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class EncryptShrinkRequest(TeaModel):
    def __init__(self, encryption_context_shrink=None, key_id=None, plaintext=None):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink  # type: str
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The plaintext to be encrypted. The plaintext must be Base64 encoded.
        self.plaintext = plaintext  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class EncryptResponseBody(TeaModel):
    def __init__(self, ciphertext_blob=None, key_id=None, key_version_id=None, request_id=None):
        # The ciphertext of the data that is encrypted by using the primary CMK version.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The globally unique ID of the CMK. If you set the KeyId parameter to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The ID of the key version that is used to encrypt the plaintext. It is the primary version of the CMK.
        self.key_version_id = key_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EncryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EncryptResponse, self).to_map()
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
            temp_model = EncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportDataKeyRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, encryption_context=None, public_key_blob=None,
                 wrapping_algorithm=None, wrapping_key_spec=None):
        # The ciphertext of the data key encrypted by using a CMK.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # A JSON string that consists of key-value pairs. If you specify this parameter when you use a CMK to encrypt the data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context  # type: dict[str, any]
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob  # type: str
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm  # type: str
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportDataKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class ExportDataKeyShrinkRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, encryption_context_shrink=None, public_key_blob=None,
                 wrapping_algorithm=None, wrapping_key_spec=None):
        # The ciphertext of the data key encrypted by using a CMK.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # A JSON string that consists of key-value pairs. If you specify this parameter when you use a CMK to encrypt the data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink  # type: str
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob  # type: str
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm  # type: str
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportDataKeyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class ExportDataKeyResponseBody(TeaModel):
    def __init__(self, exported_data_key=None, key_id=None, key_version_id=None, request_id=None):
        # The data key encrypted by using the public key and then exported.
        self.exported_data_key = exported_data_key  # type: str
        # The ID of the CMK that is used to decrypt the specified ciphertext of the data key.
        # 
        # This parameter is the globally unique ID of the CMK.
        self.key_id = key_id  # type: str
        # The ID of the CMK version that is used to decrypt the specified ciphertext of the data key.
        self.key_version_id = key_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportDataKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exported_data_key is not None:
            result['ExportedDataKey'] = self.exported_data_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExportedDataKey') is not None:
            self.exported_data_key = m.get('ExportedDataKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportDataKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportDataKeyResponse, self).to_map()
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
            temp_model = ExportDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAndExportDataKeyRequest(TeaModel):
    def __init__(self, encryption_context=None, key_id=None, key_spec=None, number_of_bytes=None,
                 public_key_blob=None, wrapping_algorithm=None, wrapping_key_spec=None):
        # A JSON string of key-value pairs. If you specify this parameter here, an equivalent value is required when you decrypt or re-encrypt the data key. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context  # type: dict[str, any]
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both parameters are not specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec  # type: str
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes  # type: int
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob  # type: str
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm  # type: str
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateAndExportDataKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class GenerateAndExportDataKeyShrinkRequest(TeaModel):
    def __init__(self, encryption_context_shrink=None, key_id=None, key_spec=None, number_of_bytes=None,
                 public_key_blob=None, wrapping_algorithm=None, wrapping_key_spec=None):
        # A JSON string of key-value pairs. If you specify this parameter here, an equivalent value is required when you decrypt or re-encrypt the data key. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink  # type: str
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both parameters are not specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec  # type: str
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes  # type: int
        # A Base64-encoded public key.
        self.public_key_blob = public_key_blob  # type: str
        # The encryption algorithm based on which you want to use the public key specified by PublicKeyBlob to encrypt the data key. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        self.wrapping_algorithm = wrapping_algorithm  # type: str
        # The key type of the public key specified by PublicKeyBlob. For more information about key types, see [Introduction to asymmetric keys](~~148147~~).
        # 
        # Valid values:
        # 
        # *   RSA\_2048
        # *   EC_SM2
        self.wrapping_key_spec = wrapping_key_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateAndExportDataKeyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class GenerateAndExportDataKeyResponseBody(TeaModel):
    def __init__(self, ciphertext_blob=None, exported_data_key=None, key_id=None, key_version_id=None,
                 request_id=None):
        # The ciphertext of the data key encrypted by using the primary CMK version.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The data key encrypted by using the public key and then exported.
        self.exported_data_key = exported_data_key  # type: str
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The ID of the CMK version that is used to encrypt the plaintext. It is the primary version of the CMK.
        self.key_version_id = key_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateAndExportDataKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.exported_data_key is not None:
            result['ExportedDataKey'] = self.exported_data_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('ExportedDataKey') is not None:
            self.exported_data_key = m.get('ExportedDataKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAndExportDataKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateAndExportDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateAndExportDataKeyResponse, self).to_map()
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
            temp_model = GenerateAndExportDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDataKeyRequest(TeaModel):
    def __init__(self, encryption_context=None, key_id=None, key_spec=None, number_of_bytes=None):
        # The JSON string that consists of key-value pairs.
        # 
        # If you specify this parameter, an equivalent value is required when you call the [Decrypt](~~28950~~) operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context  # type: dict[str, any]
        # The ID of the CMK. The ID must be globally unique.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id  # type: str
        # The type of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If none of the parameters are specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec  # type: str
        # The length of the data key that you want to generate. Unit: bytes.
        # 
        # Valid values: 1 to 1024.
        # 
        # Default value:
        # 
        # *   If the KeySpec parameter is set to AES\_256, set the value of the NumberOfBytes parameter to 32.
        # *   If the KeySpec parameter is set to AES\_128, set the value of the NumberOfBytes parameter to 16.
        self.number_of_bytes = number_of_bytes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDataKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyShrinkRequest(TeaModel):
    def __init__(self, encryption_context_shrink=None, key_id=None, key_spec=None, number_of_bytes=None):
        # The JSON string that consists of key-value pairs.
        # 
        # If you specify this parameter, an equivalent value is required when you call the [Decrypt](~~28950~~) operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink  # type: str
        # The ID of the CMK. The ID must be globally unique.
        # 
        # You can also set this parameter to an alias that is bound to the CMK. For more information, see [Alias overview](~~68522~~).
        self.key_id = key_id  # type: str
        # The type of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: a 256-bit symmetric key
        # *   AES\_128: a 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If none of the parameters are specified, KMS generates a 256-bit data key. If both parameters are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec  # type: str
        # The length of the data key that you want to generate. Unit: bytes.
        # 
        # Valid values: 1 to 1024.
        # 
        # Default value:
        # 
        # *   If the KeySpec parameter is set to AES\_256, set the value of the NumberOfBytes parameter to 32.
        # *   If the KeySpec parameter is set to AES\_128, set the value of the NumberOfBytes parameter to 16.
        self.number_of_bytes = number_of_bytes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDataKeyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyResponseBody(TeaModel):
    def __init__(self, ciphertext_blob=None, key_id=None, key_version_id=None, plaintext=None, request_id=None):
        # The ciphertext of the data key that is encrypted by using the primary version of the specified CMK.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The ID of the CMK. The ID must be globally unique.
        # 
        # >  If you set the KeyId parameter in the request to an alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The ID of the CMK version. The ID must be globally unique.
        self.key_version_id = key_version_id  # type: str
        # The Base64 encoded plaintext of the data key.
        self.plaintext = plaintext  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDataKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateDataKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateDataKeyResponse, self).to_map()
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
            temp_model = GenerateDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDataKeyWithoutPlaintextRequest(TeaModel):
    def __init__(self, encryption_context=None, key_id=None, key_spec=None, number_of_bytes=None):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context = encryption_context  # type: dict[str, any]
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see Use aliases.
        self.key_id = key_id  # type: str
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: 256-bit symmetric key
        # *   AES\_128: 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both of them are not specified, KMS generates a 256-bit data key. If both of them are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec  # type: str
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDataKeyWithoutPlaintextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyWithoutPlaintextShrinkRequest(TeaModel):
    def __init__(self, encryption_context_shrink=None, key_id=None, key_spec=None, number_of_bytes=None):
        # A JSON string that consists of key-value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. For more information, see [EncryptionContext](~~42975~~).
        self.encryption_context_shrink = encryption_context_shrink  # type: str
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see Use aliases.
        self.key_id = key_id  # type: str
        # The length of the data key that you want to generate. Valid values:
        # 
        # *   AES\_256: 256-bit symmetric key
        # *   AES\_128: 128-bit symmetric key
        # 
        # >  We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If both of them are not specified, KMS generates a 256-bit data key. If both of them are specified, KMS ignores the KeySpec parameter.
        self.key_spec = key_spec  # type: str
        # The length of the data key that you want to generate.
        # 
        # Valid values: 1 to 1024.
        # 
        # Unit: bytes.
        self.number_of_bytes = number_of_bytes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDataKeyWithoutPlaintextShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        return self


class GenerateDataKeyWithoutPlaintextResponseBody(TeaModel):
    def __init__(self, ciphertext_blob=None, key_id=None, key_version_id=None, request_id=None):
        # The ciphertext of the data that is encrypted by using the primary CMK version.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to an alias, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The ID of the key version that is used to encrypt the plaintext. It is the primary version of the CMK.
        self.key_version_id = key_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDataKeyWithoutPlaintextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateDataKeyWithoutPlaintextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateDataKeyWithoutPlaintextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateDataKeyWithoutPlaintextResponse, self).to_map()
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
            temp_model = GenerateDataKeyWithoutPlaintextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None):
        # The ID of the certificate. It is the globally unique identifier (GUID) of the certificate in Certificates Manager.
        self.certificate_id = certificate_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class GetCertificateResponseBody(TeaModel):
    def __init__(self, certificate=None, certificate_chain=None, certificate_id=None, csr=None, request_id=None):
        # The certificate in the Privacy Enhanced Mail (PEM) format.
        self.certificate = certificate  # type: str
        # The certificate chain in the PEM format.
        self.certificate_chain = certificate_chain  # type: str
        # The ID of the certificate.
        self.certificate_id = certificate_id  # type: str
        # The CSR in the PEM format.
        self.csr = csr  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCertificateResponse, self).to_map()
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
            temp_model = GetCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClientKeyRequest(TeaModel):
    def __init__(self, client_key_id=None):
        self.client_key_id = client_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClientKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')
        return self


class GetClientKeyResponseBody(TeaModel):
    def __init__(self, aap_name=None, client_key_id=None, create_time=None, key_algorithm=None, key_origin=None,
                 not_after=None, not_before=None, public_key_data=None, request_id=None):
        self.aap_name = aap_name  # type: str
        self.client_key_id = client_key_id  # type: str
        self.create_time = create_time  # type: str
        self.key_algorithm = key_algorithm  # type: str
        self.key_origin = key_origin  # type: str
        self.not_after = not_after  # type: str
        self.not_before = not_before  # type: str
        self.public_key_data = public_key_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClientKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aap_name is not None:
            result['AapName'] = self.aap_name
        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.key_algorithm is not None:
            result['KeyAlgorithm'] = self.key_algorithm
        if self.key_origin is not None:
            result['KeyOrigin'] = self.key_origin
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.public_key_data is not None:
            result['PublicKeyData'] = self.public_key_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AapName') is not None:
            self.aap_name = m.get('AapName')
        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('KeyAlgorithm') is not None:
            self.key_algorithm = m.get('KeyAlgorithm')
        if m.get('KeyOrigin') is not None:
            self.key_origin = m.get('KeyOrigin')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('PublicKeyData') is not None:
            self.public_key_data = m.get('PublicKeyData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClientKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClientKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClientKeyResponse, self).to_map()
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
            temp_model = GetClientKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKmsInstanceRequest(TeaModel):
    def __init__(self, kms_instance_id=None):
        self.kms_instance_id = kms_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKmsInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')
        return self


class GetKmsInstanceResponseBodyKmsInstanceBindVpcsBindVpc(TeaModel):
    def __init__(self, region_id=None, v_switch_id=None, vpc_id=None, vpc_owner_id=None):
        self.region_id = region_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_owner_id = vpc_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKmsInstanceResponseBodyKmsInstanceBindVpcsBindVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')
        return self


class GetKmsInstanceResponseBodyKmsInstanceBindVpcs(TeaModel):
    def __init__(self, bind_vpc=None):
        self.bind_vpc = bind_vpc  # type: list[GetKmsInstanceResponseBodyKmsInstanceBindVpcsBindVpc]

    def validate(self):
        if self.bind_vpc:
            for k in self.bind_vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetKmsInstanceResponseBodyKmsInstanceBindVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindVpc'] = []
        if self.bind_vpc is not None:
            for k in self.bind_vpc:
                result['BindVpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bind_vpc = []
        if m.get('BindVpc') is not None:
            for k in m.get('BindVpc'):
                temp_model = GetKmsInstanceResponseBodyKmsInstanceBindVpcsBindVpc()
                self.bind_vpc.append(temp_model.from_map(k))
        return self


class GetKmsInstanceResponseBodyKmsInstance(TeaModel):
    def __init__(self, bind_vpcs=None, ca_certificate_chain_pem=None, create_time=None, end_date=None,
                 instance_id=None, instance_name=None, key_num=None, secret_num=None, spec=None, start_date=None, status=None,
                 vpc_id=None, vpc_num=None, vswitch_ids=None, zone_ids=None):
        self.bind_vpcs = bind_vpcs  # type: GetKmsInstanceResponseBodyKmsInstanceBindVpcs
        self.ca_certificate_chain_pem = ca_certificate_chain_pem  # type: str
        self.create_time = create_time  # type: str
        self.end_date = end_date  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.key_num = key_num  # type: long
        self.secret_num = secret_num  # type: str
        self.spec = spec  # type: long
        self.start_date = start_date  # type: str
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_num = vpc_num  # type: long
        self.vswitch_ids = vswitch_ids  # type: str
        self.zone_ids = zone_ids  # type: str

    def validate(self):
        if self.bind_vpcs:
            self.bind_vpcs.validate()

    def to_map(self):
        _map = super(GetKmsInstanceResponseBodyKmsInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs.to_map()
        if self.ca_certificate_chain_pem is not None:
            result['CaCertificateChainPem'] = self.ca_certificate_chain_pem
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.key_num is not None:
            result['KeyNum'] = self.key_num
        if self.secret_num is not None:
            result['SecretNum'] = self.secret_num
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_num is not None:
            result['VpcNum'] = self.vpc_num
        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindVpcs') is not None:
            temp_model = GetKmsInstanceResponseBodyKmsInstanceBindVpcs()
            self.bind_vpcs = temp_model.from_map(m['BindVpcs'])
        if m.get('CaCertificateChainPem') is not None:
            self.ca_certificate_chain_pem = m.get('CaCertificateChainPem')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KeyNum') is not None:
            self.key_num = m.get('KeyNum')
        if m.get('SecretNum') is not None:
            self.secret_num = m.get('SecretNum')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcNum') is not None:
            self.vpc_num = m.get('VpcNum')
        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')
        return self


class GetKmsInstanceResponseBody(TeaModel):
    def __init__(self, kms_instance=None, request_id=None):
        self.kms_instance = kms_instance  # type: GetKmsInstanceResponseBodyKmsInstance
        self.request_id = request_id  # type: str

    def validate(self):
        if self.kms_instance:
            self.kms_instance.validate()

    def to_map(self):
        _map = super(GetKmsInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kms_instance is not None:
            result['KmsInstance'] = self.kms_instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KmsInstance') is not None:
            temp_model = GetKmsInstanceResponseBodyKmsInstance()
            self.kms_instance = temp_model.from_map(m['KmsInstance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetKmsInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetKmsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetKmsInstanceResponse, self).to_map()
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
            temp_model = GetKmsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersForImportRequest(TeaModel):
    def __init__(self, key_id=None, wrapping_algorithm=None, wrapping_key_spec=None):
        # The globally unique ID of the CMK.
        # 
        # >  You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        self.key_id = key_id  # type: str
        # The algorithm that is used to encrypt key material.
        self.wrapping_algorithm = wrapping_algorithm  # type: str
        # The type of the public key that is used to encrypt key material.
        self.wrapping_key_spec = wrapping_key_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParametersForImportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        return self


class GetParametersForImportResponseBody(TeaModel):
    def __init__(self, import_token=None, key_id=None, public_key=None, request_id=None, token_expire_time=None):
        # The token that is used to import key material.
        # 
        # The token is valid for 24 hours. The value of this parameter is required when you call the [ImportKeyMaterial](~~68622~~) operation.
        self.import_token = import_token  # type: str
        # The globally unique ID of the CMK.
        # 
        # The value of this parameter is required when you call the [ImportKeyMaterial](~~68622~~) operation.
        self.key_id = key_id  # type: str
        # The public key that is used to encrypt key material.
        # 
        # The public key is Base64-encoded.
        self.public_key = public_key  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The time when the token expires.
        self.token_expire_time = token_expire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParametersForImportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_token is not None:
            result['ImportToken'] = self.import_token
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token_expire_time is not None:
            result['TokenExpireTime'] = self.token_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TokenExpireTime') is not None:
            self.token_expire_time = m.get('TokenExpireTime')
        return self


class GetParametersForImportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetParametersForImportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetParametersForImportResponse, self).to_map()
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
            temp_model = GetParametersForImportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicKeyRequest(TeaModel):
    def __init__(self, key_id=None, key_version_id=None):
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The globally unique ID of the CMK version.
        self.key_version_id = key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublicKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class GetPublicKeyResponseBody(TeaModel):
    def __init__(self, key_id=None, key_version_id=None, public_key=None, request_id=None):
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to the alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The version of the CMK that is used to encrypt the plaintext.
        self.key_version_id = key_version_id  # type: str
        # The public key returned in the PEM format.
        self.public_key = public_key  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublicKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPublicKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPublicKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPublicKeyResponse, self).to_map()
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
            temp_model = GetPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRandomPasswordRequest(TeaModel):
    def __init__(self, exclude_characters=None, exclude_lowercase=None, exclude_numbers=None,
                 exclude_punctuation=None, exclude_uppercase=None, password_length=None, require_each_included_type=None):
        # The characters that are not included in the password to be generated.
        # 
        # Valid values:
        # 
        # ` Valid characters: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! \"#$%&\"()*+,-. /:;<=>? @[\] your_project_id} ~  `.
        # 
        # This parameter is empty by default.
        self.exclude_characters = exclude_characters  # type: str
        # Specifies whether to exclude lowercase letters.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_lowercase = exclude_lowercase  # type: str
        # Specifies whether to exclude digits.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_numbers = exclude_numbers  # type: str
        # Specifies whether to exclude special characters.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_punctuation = exclude_punctuation  # type: str
        # Specifies whether to exclude uppercase letters.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.exclude_uppercase = exclude_uppercase  # type: str
        # The number of bytes that the password to be generated contains.
        # 
        # Valid values: 8 to 128.
        # 
        # Default value: 32
        self.password_length = password_length  # type: str
        # Specifies whether to include all the preceding character types.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.require_each_included_type = require_each_included_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRandomPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_characters is not None:
            result['ExcludeCharacters'] = self.exclude_characters
        if self.exclude_lowercase is not None:
            result['ExcludeLowercase'] = self.exclude_lowercase
        if self.exclude_numbers is not None:
            result['ExcludeNumbers'] = self.exclude_numbers
        if self.exclude_punctuation is not None:
            result['ExcludePunctuation'] = self.exclude_punctuation
        if self.exclude_uppercase is not None:
            result['ExcludeUppercase'] = self.exclude_uppercase
        if self.password_length is not None:
            result['PasswordLength'] = self.password_length
        if self.require_each_included_type is not None:
            result['RequireEachIncludedType'] = self.require_each_included_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeCharacters') is not None:
            self.exclude_characters = m.get('ExcludeCharacters')
        if m.get('ExcludeLowercase') is not None:
            self.exclude_lowercase = m.get('ExcludeLowercase')
        if m.get('ExcludeNumbers') is not None:
            self.exclude_numbers = m.get('ExcludeNumbers')
        if m.get('ExcludePunctuation') is not None:
            self.exclude_punctuation = m.get('ExcludePunctuation')
        if m.get('ExcludeUppercase') is not None:
            self.exclude_uppercase = m.get('ExcludeUppercase')
        if m.get('PasswordLength') is not None:
            self.password_length = m.get('PasswordLength')
        if m.get('RequireEachIncludedType') is not None:
            self.require_each_included_type = m.get('RequireEachIncludedType')
        return self


class GetRandomPasswordResponseBody(TeaModel):
    def __init__(self, random_password=None, request_id=None):
        # The generated random password.
        self.random_password = random_password  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRandomPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.random_password is not None:
            result['RandomPassword'] = self.random_password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RandomPassword') is not None:
            self.random_password = m.get('RandomPassword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRandomPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRandomPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRandomPasswordResponse, self).to_map()
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
            temp_model = GetRandomPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretValueRequest(TeaModel):
    def __init__(self, fetch_extended_config=None, secret_name=None, version_id=None, version_stage=None):
        # Specifies whether to obtain the extended configuration of the secret. Valid values:
        # 
        # *   true
        # *   false: This is the default value.
        # 
        # >  This parameter is ignored for a generic secret.
        self.fetch_extended_config = fetch_extended_config  # type: bool
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The version number of the secret value. If you specify this parameter, Secrets Manager returns the secret value of the specified version.
        # 
        # >  This parameter is ignored for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.version_id = version_id  # type: str
        # The stage label that marks the secret version. If you specify this parameter, Secrets Manager returns the secret value of the version that is marked with the specified stage label.
        # 
        # Default value: ACSCurrent.
        # 
        # >  For a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret, Secrets Manager can return only the secret value of the version marked with ACSPrevious or ACSCurrent.
        self.version_stage = version_stage  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_extended_config is not None:
            result['FetchExtendedConfig'] = self.fetch_extended_config
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchExtendedConfig') is not None:
            self.fetch_extended_config = m.get('FetchExtendedConfig')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class GetSecretValueResponseBodyVersionStages(TeaModel):
    def __init__(self, version_stage=None):
        self.version_stage = version_stage  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretValueResponseBodyVersionStages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class GetSecretValueResponseBody(TeaModel):
    def __init__(self, automatic_rotation=None, create_time=None, extended_config=None, last_rotation_date=None,
                 next_rotation_date=None, request_id=None, rotation_interval=None, secret_data=None, secret_data_type=None,
                 secret_name=None, secret_type=None, version_id=None, version_stages=None):
        # Indicates whether automatic rotation is enabled. Valid values:
        # 
        # *   Enabled: indicates that automatic rotation is enabled.
        # *   Disabled: indicates that automatic rotation is disabled.
        # *   Invalid: indicates that the status of automatic rotation is abnormal. In this case, Secrets Manager cannot automatically rotate the secret.
        # 
        # >  This parameter is returned only for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.automatic_rotation = automatic_rotation  # type: str
        # The time when the secret was created.
        self.create_time = create_time  # type: str
        # The extended configuration of the secret.
        # 
        # >  This parameter is returned if you set the FetchExtendedConfig parameter to true. This parameter is returned only for a managed ApsaraDB RDS secret, a managed RAM secret, or a managed ECS secret.
        self.extended_config = extended_config  # type: str
        # The time when the last rotation was performed.
        # 
        # >  This parameter is returned if the secret was rotated.
        self.last_rotation_date = last_rotation_date  # type: str
        # The time when the next rotation will be performed.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.next_rotation_date = next_rotation_date  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The interval for automatic rotation.
        # 
        # The value is in the `integer[unit]` format. The `unit` field has a fixed value of s. For example, if the value is 604800s, automatic rotation is performed at a 7-day interval.
        # 
        # >  This parameter is returned if automatic rotation is enabled.
        self.rotation_interval = rotation_interval  # type: str
        # The secret value. Secrets Manager decrypts the ciphertext of the secret value and returns the plaintext of the secret value in this parameter.
        # 
        # *   For a generic secret, the secret value of the specified version is returned.
        # 
        # *   For a managed ApsaraDB RDS secret, the value is returned in the following format:`{"AccountName":"","AccountPassword":""}` .
        # 
        # *   For a managed RAM secret, the secret value is returned in the following format: `{"AccessKeyId":"Adfdsfd","AccessKeySecret":"fdsfdsf","GenerateTimestamp": "2016-03-25T10:42:40Z"}`.
        # 
        # *   For a managed ECS secret, the secret value is returned in one of the following formats:
        # 
        #     *   `{"UserName":"root","Password":"H5asdasdsads****"}`: The secret value is returned in this format if the ECS secret is a password.
        #     *   `{"UserName":"root","PublicKey":"ssh-rsa ****mKwnVix9YTFY9Rs= imported-openssh-key","PrivateKey": "d6bee1cb-2e14-4277-ba6b-73786b21****"}`: The secret value is returned in this format is the ECS secret is a pair of SSH keys. The private key is in the Privacy Enhanced Mail (PEM) format.
        self.secret_data = secret_data  # type: str
        # The type of the secret value. Valid values:
        # 
        # *   text
        # *   binary
        self.secret_data_type = secret_data_type  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        # *   RAMCredentials: indicates a managed RAM secret.
        # *   ECS: indicates a managed ECS secret.
        self.secret_type = secret_type  # type: str
        # The version number of the secret value.
        self.version_id = version_id  # type: str
        # The stage labels that mark the secret versions.
        self.version_stages = version_stages  # type: GetSecretValueResponseBodyVersionStages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        _map = super(GetSecretValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            temp_model = GetSecretValueResponseBodyVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        return self


class GetSecretValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSecretValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecretValueResponse, self).to_map()
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
            temp_model = GetSecretValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyMaterialRequest(TeaModel):
    def __init__(self, encrypted_key_material=None, import_token=None, key_id=None, key_material_expire_unix=None):
        # Use **GetParametersForImport** the Returned public key and the base64-encoded key material.
        self.encrypted_key_material = encrypted_key_material  # type: str
        # By calling **GetParametersForImport** the import token.
        self.import_token = import_token  # type: str
        # The ID of the CMK to be imported.
        self.key_id = key_id  # type: str
        # The time when the key material expires.
        # 
        # If this parameter is not specified or set this parameter to 0, the key material does not expire.
        # 
        # >  The value cannot be earlier than the time when the API is called (based on the server time).
        self.key_material_expire_unix = key_material_expire_unix  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportKeyMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_key_material is not None:
            result['EncryptedKeyMaterial'] = self.encrypted_key_material
        if self.import_token is not None:
            result['ImportToken'] = self.import_token
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_material_expire_unix is not None:
            result['KeyMaterialExpireUnix'] = self.key_material_expire_unix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptedKeyMaterial') is not None:
            self.encrypted_key_material = m.get('EncryptedKeyMaterial')
        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyMaterialExpireUnix') is not None:
            self.key_material_expire_unix = m.get('KeyMaterialExpireUnix')
        return self


class ImportKeyMaterialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportKeyMaterialResponseBody, self).to_map()
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


class ImportKeyMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportKeyMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportKeyMaterialResponse, self).to_map()
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
            temp_model = ImportKeyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliasesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAliasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAliasesResponseBodyAliasesAlias(TeaModel):
    def __init__(self, alias_arn=None, alias_name=None, key_id=None):
        # The Alibaba Cloud Resource Name (ARN) of the alias.
        self.alias_arn = alias_arn  # type: str
        # The ID of the alias.
        self.alias_name = alias_name  # type: str
        # The CMK to which the alias belongs.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAliasesResponseBodyAliasesAlias, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_arn is not None:
            result['AliasArn'] = self.alias_arn
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasArn') is not None:
            self.alias_arn = m.get('AliasArn')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListAliasesResponseBodyAliases(TeaModel):
    def __init__(self, alias=None):
        self.alias = alias  # type: list[ListAliasesResponseBodyAliasesAlias]

    def validate(self):
        if self.alias:
            for k in self.alias:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAliasesResponseBodyAliases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alias'] = []
        if self.alias is not None:
            for k in self.alias:
                result['Alias'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alias = []
        if m.get('Alias') is not None:
            for k in m.get('Alias'):
                temp_model = ListAliasesResponseBodyAliasesAlias()
                self.alias.append(temp_model.from_map(k))
        return self


class ListAliasesResponseBody(TeaModel):
    def __init__(self, aliases=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The alias of the user.
        self.aliases = aliases  # type: ListAliasesResponseBodyAliases
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned aliases.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.aliases:
            self.aliases.validate()

    def to_map(self):
        _map = super(ListAliasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['Aliases'] = self.aliases.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aliases') is not None:
            temp_model = ListAliasesResponseBodyAliases()
            self.aliases = temp_model.from_map(m['Aliases'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAliasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAliasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAliasesResponse, self).to_map()
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
            temp_model = ListAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliasesByKeyIdRequest(TeaModel):
    def __init__(self, key_id=None, page_number=None, page_size=None):
        # The globally unique ID of the CMK.
        self.key_id = key_id  # type: str
        # The number of the page to return.
        # 
        # Valid values: an integer that is greater than 0.
        # 
        # Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 101.
        # 
        # Default value: 10
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAliasesByKeyIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAliasesByKeyIdResponseBodyAliasesAlias(TeaModel):
    def __init__(self, alias_arn=None, alias_name=None, key_id=None):
        # The Alibaba Cloud Resource Name (ARN) of the alias.
        self.alias_arn = alias_arn  # type: str
        # The ID of the alias.
        self.alias_name = alias_name  # type: str
        # The CMK to which an alias is bound.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAliasesByKeyIdResponseBodyAliasesAlias, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_arn is not None:
            result['AliasArn'] = self.alias_arn
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasArn') is not None:
            self.alias_arn = m.get('AliasArn')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListAliasesByKeyIdResponseBodyAliases(TeaModel):
    def __init__(self, alias=None):
        self.alias = alias  # type: list[ListAliasesByKeyIdResponseBodyAliasesAlias]

    def validate(self):
        if self.alias:
            for k in self.alias:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAliasesByKeyIdResponseBodyAliases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alias'] = []
        if self.alias is not None:
            for k in self.alias:
                result['Alias'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alias = []
        if m.get('Alias') is not None:
            for k in m.get('Alias'):
                temp_model = ListAliasesByKeyIdResponseBodyAliasesAlias()
                self.alias.append(temp_model.from_map(k))
        return self


class ListAliasesByKeyIdResponseBody(TeaModel):
    def __init__(self, aliases=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # An array that consists of aliases.
        self.aliases = aliases  # type: ListAliasesByKeyIdResponseBodyAliases
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of returned CMKs.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.aliases:
            self.aliases.validate()

    def to_map(self):
        _map = super(ListAliasesByKeyIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['Aliases'] = self.aliases.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aliases') is not None:
            temp_model = ListAliasesByKeyIdResponseBodyAliases()
            self.aliases = temp_model.from_map(m['Aliases'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAliasesByKeyIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAliasesByKeyIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAliasesByKeyIdResponse, self).to_map()
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
            temp_model = ListAliasesByKeyIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationAccessPointsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationAccessPointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListApplicationAccessPointsResponseBodyApplicationAccessPointsApplicationAccessPoint(TeaModel):
    def __init__(self, authentication_method=None, name=None):
        self.authentication_method = authentication_method  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationAccessPointsResponseBodyApplicationAccessPointsApplicationAccessPoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_method is not None:
            result['AuthenticationMethod'] = self.authentication_method
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticationMethod') is not None:
            self.authentication_method = m.get('AuthenticationMethod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListApplicationAccessPointsResponseBodyApplicationAccessPoints(TeaModel):
    def __init__(self, application_access_point=None):
        self.application_access_point = application_access_point  # type: list[ListApplicationAccessPointsResponseBodyApplicationAccessPointsApplicationAccessPoint]

    def validate(self):
        if self.application_access_point:
            for k in self.application_access_point:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationAccessPointsResponseBodyApplicationAccessPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationAccessPoint'] = []
        if self.application_access_point is not None:
            for k in self.application_access_point:
                result['ApplicationAccessPoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_access_point = []
        if m.get('ApplicationAccessPoint') is not None:
            for k in m.get('ApplicationAccessPoint'):
                temp_model = ListApplicationAccessPointsResponseBodyApplicationAccessPointsApplicationAccessPoint()
                self.application_access_point.append(temp_model.from_map(k))
        return self


class ListApplicationAccessPointsResponseBody(TeaModel):
    def __init__(self, application_access_points=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.application_access_points = application_access_points  # type: ListApplicationAccessPointsResponseBodyApplicationAccessPoints
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.application_access_points:
            self.application_access_points.validate()

    def to_map(self):
        _map = super(ListApplicationAccessPointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_points is not None:
            result['ApplicationAccessPoints'] = self.application_access_points.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationAccessPoints') is not None:
            temp_model = ListApplicationAccessPointsResponseBodyApplicationAccessPoints()
            self.application_access_points = temp_model.from_map(m['ApplicationAccessPoints'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationAccessPointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationAccessPointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationAccessPointsResponse, self).to_map()
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
            temp_model = ListApplicationAccessPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientKeysRequest(TeaModel):
    def __init__(self, aap_name=None):
        self.aap_name = aap_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClientKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aap_name is not None:
            result['AapName'] = self.aap_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AapName') is not None:
            self.aap_name = m.get('AapName')
        return self


class ListClientKeysResponseBodyClientKeys(TeaModel):
    def __init__(self, aap_name=None, client_key_id=None, create_time=None, key_algorithm=None, key_origin=None,
                 not_after=None, not_before=None, public_key_data=None):
        self.aap_name = aap_name  # type: str
        self.client_key_id = client_key_id  # type: str
        self.create_time = create_time  # type: str
        self.key_algorithm = key_algorithm  # type: str
        self.key_origin = key_origin  # type: str
        self.not_after = not_after  # type: str
        self.not_before = not_before  # type: str
        self.public_key_data = public_key_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClientKeysResponseBodyClientKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aap_name is not None:
            result['AapName'] = self.aap_name
        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.key_algorithm is not None:
            result['KeyAlgorithm'] = self.key_algorithm
        if self.key_origin is not None:
            result['KeyOrigin'] = self.key_origin
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.public_key_data is not None:
            result['PublicKeyData'] = self.public_key_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AapName') is not None:
            self.aap_name = m.get('AapName')
        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('KeyAlgorithm') is not None:
            self.key_algorithm = m.get('KeyAlgorithm')
        if m.get('KeyOrigin') is not None:
            self.key_origin = m.get('KeyOrigin')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('PublicKeyData') is not None:
            self.public_key_data = m.get('PublicKeyData')
        return self


class ListClientKeysResponseBody(TeaModel):
    def __init__(self, client_keys=None, request_id=None):
        self.client_keys = client_keys  # type: list[ListClientKeysResponseBodyClientKeys]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.client_keys:
            for k in self.client_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClientKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientKeys'] = []
        if self.client_keys is not None:
            for k in self.client_keys:
                result['ClientKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.client_keys = []
        if m.get('ClientKeys') is not None:
            for k in m.get('ClientKeys'):
                temp_model = ListClientKeysResponseBodyClientKeys()
                self.client_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClientKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClientKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClientKeysResponse, self).to_map()
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
            temp_model = ListClientKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeyVersionsRequest(TeaModel):
    def __init__(self, key_id=None, page_number=None, page_size=None):
        # The globally unique ID of the CMK. You can also set this parameter to an alias that is bound to the CMK. For more information, see [Use aliases](~~68522~~).
        self.key_id = key_id  # type: str
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 0 to 101.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKeyVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListKeyVersionsResponseBodyKeyVersionsKeyVersion(TeaModel):
    def __init__(self, creation_date=None, key_id=None, key_version_id=None):
        # The date and time when the CMK version was created. The time is displayed in UTC.
        self.creation_date = creation_date  # type: str
        # The globally unique ID of the CMK.
        # 
        # >  If you set the KeyId parameter to the alias of the CMK, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id  # type: str
        # The globally unique ID of the CMK version.
        self.key_version_id = key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKeyVersionsResponseBodyKeyVersionsKeyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class ListKeyVersionsResponseBodyKeyVersions(TeaModel):
    def __init__(self, key_version=None):
        self.key_version = key_version  # type: list[ListKeyVersionsResponseBodyKeyVersionsKeyVersion]

    def validate(self):
        if self.key_version:
            for k in self.key_version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListKeyVersionsResponseBodyKeyVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyVersion'] = []
        if self.key_version is not None:
            for k in self.key_version:
                result['KeyVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key_version = []
        if m.get('KeyVersion') is not None:
            for k in m.get('KeyVersion'):
                temp_model = ListKeyVersionsResponseBodyKeyVersionsKeyVersion()
                self.key_version.append(temp_model.from_map(k))
        return self


class ListKeyVersionsResponseBody(TeaModel):
    def __init__(self, key_versions=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # An array that consists of key versions.
        self.key_versions = key_versions  # type: ListKeyVersionsResponseBodyKeyVersions
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned key versions.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.key_versions:
            self.key_versions.validate()

    def to_map(self):
        _map = super(ListKeyVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_versions is not None:
            result['KeyVersions'] = self.key_versions.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyVersions') is not None:
            temp_model = ListKeyVersionsResponseBodyKeyVersions()
            self.key_versions = temp_model.from_map(m['KeyVersions'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKeyVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListKeyVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListKeyVersionsResponse, self).to_map()
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
            temp_model = ListKeyVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeysRequest(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.filters = filters  # type: str
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListKeysResponseBodyKeysKey(TeaModel):
    def __init__(self, key_arn=None, key_id=None):
        self.key_arn = key_arn  # type: str
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKeysResponseBodyKeysKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_arn is not None:
            result['KeyArn'] = self.key_arn
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyArn') is not None:
            self.key_arn = m.get('KeyArn')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListKeysResponseBodyKeys(TeaModel):
    def __init__(self, key=None):
        self.key = key  # type: list[ListKeysResponseBodyKeysKey]

    def validate(self):
        if self.key:
            for k in self.key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListKeysResponseBodyKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Key'] = []
        if self.key is not None:
            for k in self.key:
                result['Key'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key = []
        if m.get('Key') is not None:
            for k in m.get('Key'):
                temp_model = ListKeysResponseBodyKeysKey()
                self.key.append(temp_model.from_map(k))
        return self


class ListKeysResponseBody(TeaModel):
    def __init__(self, keys=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.keys = keys  # type: ListKeysResponseBodyKeys
        # The total number of CMKs.
        self.page_number = page_number  # type: int
        # An array that consists of the CMKs of the current Alibaba Cloud account in the current region.
        self.page_size = page_size  # type: int
        # The ID of the CMK. The ID must be globally unique.
        self.request_id = request_id  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the CMK.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        _map = super(ListKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keys') is not None:
            temp_model = ListKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListKeysResponse, self).to_map()
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
            temp_model = ListKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKmsInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKmsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListKmsInstancesResponseBodyKmsInstancesKmsInstance(TeaModel):
    def __init__(self, kms_instance_arn=None, kms_instance_id=None):
        self.kms_instance_arn = kms_instance_arn  # type: str
        self.kms_instance_id = kms_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKmsInstancesResponseBodyKmsInstancesKmsInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kms_instance_arn is not None:
            result['KmsInstanceArn'] = self.kms_instance_arn
        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KmsInstanceArn') is not None:
            self.kms_instance_arn = m.get('KmsInstanceArn')
        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')
        return self


class ListKmsInstancesResponseBodyKmsInstances(TeaModel):
    def __init__(self, kms_instance=None):
        self.kms_instance = kms_instance  # type: list[ListKmsInstancesResponseBodyKmsInstancesKmsInstance]

    def validate(self):
        if self.kms_instance:
            for k in self.kms_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListKmsInstancesResponseBodyKmsInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KmsInstance'] = []
        if self.kms_instance is not None:
            for k in self.kms_instance:
                result['KmsInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.kms_instance = []
        if m.get('KmsInstance') is not None:
            for k in m.get('KmsInstance'):
                temp_model = ListKmsInstancesResponseBodyKmsInstancesKmsInstance()
                self.kms_instance.append(temp_model.from_map(k))
        return self


class ListKmsInstancesResponseBody(TeaModel):
    def __init__(self, kms_instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.kms_instances = kms_instances  # type: ListKmsInstancesResponseBodyKmsInstances
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.kms_instances:
            self.kms_instances.validate()

    def to_map(self):
        _map = super(ListKmsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kms_instances is not None:
            result['KmsInstances'] = self.kms_instances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KmsInstances') is not None:
            temp_model = ListKmsInstancesResponseBodyKmsInstances()
            self.kms_instances = temp_model.from_map(m['KmsInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKmsInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListKmsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListKmsInstancesResponse, self).to_map()
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
            temp_model = ListKmsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkRulesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNetworkRulesResponseBodyNetworkRulesNetworkRule(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkRulesResponseBodyNetworkRulesNetworkRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNetworkRulesResponseBodyNetworkRules(TeaModel):
    def __init__(self, network_rule=None):
        self.network_rule = network_rule  # type: list[ListNetworkRulesResponseBodyNetworkRulesNetworkRule]

    def validate(self):
        if self.network_rule:
            for k in self.network_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkRulesResponseBodyNetworkRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkRule'] = []
        if self.network_rule is not None:
            for k in self.network_rule:
                result['NetworkRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network_rule = []
        if m.get('NetworkRule') is not None:
            for k in m.get('NetworkRule'):
                temp_model = ListNetworkRulesResponseBodyNetworkRulesNetworkRule()
                self.network_rule.append(temp_model.from_map(k))
        return self


class ListNetworkRulesResponseBody(TeaModel):
    def __init__(self, network_rules=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.network_rules = network_rules  # type: ListNetworkRulesResponseBodyNetworkRules
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.network_rules:
            self.network_rules.validate()

    def to_map(self):
        _map = super(ListNetworkRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkRules') is not None:
            temp_model = ListNetworkRulesResponseBodyNetworkRules()
            self.network_rules = temp_model.from_map(m['NetworkRules'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNetworkRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNetworkRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkRulesResponse, self).to_map()
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
            temp_model = ListNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPoliciesResponseBodyPoliciesPolicy(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesResponseBodyPoliciesPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, policy=None):
        self.policy = policy  # type: list[ListPoliciesResponseBodyPoliciesPolicy]

    def validate(self):
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPoliciesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, policies=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policies = policies  # type: ListPoliciesResponseBodyPolicies
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        _map = super(ListPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Policies') is not None:
            temp_model = ListPoliciesResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPoliciesResponse, self).to_map()
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTagsRequest(TeaModel):
    def __init__(self, key_id=None):
        # The globally unique ID of the CMK.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class ListResourceTagsResponseBodyTagsTag(TeaModel):
    def __init__(self, key_id=None, tag_key=None, tag_value=None):
        # The globally unique ID of the CMK.
        self.key_id = key_id  # type: str
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTagsResponseBodyTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListResourceTagsResponseBodyTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListResourceTagsResponseBodyTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListResourceTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListResourceTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The tags of the CMK.
        self.tags = tags  # type: ListResourceTagsResponseBodyTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListResourceTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            temp_model = ListResourceTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class ListResourceTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceTagsResponse, self).to_map()
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
            temp_model = ListResourceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretVersionIdsRequest(TeaModel):
    def __init__(self, include_deprecated=None, page_number=None, page_size=None, secret_name=None):
        # Specifies whether to return deprecated secret versions.
        # 
        # Valid values:
        # 
        # *   false: no
        # *   true: yes
        # 
        # Default value: false.
        self.include_deprecated = include_deprecated  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size  # type: int
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretVersionIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_deprecated is not None:
            result['IncludeDeprecated'] = self.include_deprecated
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncludeDeprecated') is not None:
            self.include_deprecated = m.get('IncludeDeprecated')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages(TeaModel):
    def __init__(self, version_stage=None):
        self.version_stage = version_stage  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class ListSecretVersionIdsResponseBodyVersionIdsVersionId(TeaModel):
    def __init__(self, create_time=None, version_id=None, version_stages=None):
        # The time when the secret version was created.
        self.create_time = create_time  # type: str
        # The version number.
        self.version_id = version_id  # type: str
        # The stage labels that mark the secret version.
        self.version_stages = version_stages  # type: ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        _map = super(ListSecretVersionIdsResponseBodyVersionIdsVersionId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            temp_model = ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        return self


class ListSecretVersionIdsResponseBodyVersionIds(TeaModel):
    def __init__(self, version_id=None):
        self.version_id = version_id  # type: list[ListSecretVersionIdsResponseBodyVersionIdsVersionId]

    def validate(self):
        if self.version_id:
            for k in self.version_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecretVersionIdsResponseBodyVersionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VersionId'] = []
        if self.version_id is not None:
            for k in self.version_id:
                result['VersionId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.version_id = []
        if m.get('VersionId') is not None:
            for k in m.get('VersionId'):
                temp_model = ListSecretVersionIdsResponseBodyVersionIdsVersionId()
                self.version_id.append(temp_model.from_map(k))
        return self


class ListSecretVersionIdsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, secret_name=None, total_count=None,
                 version_ids=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The number of entries returned on the current page.
        self.total_count = total_count  # type: int
        # The list of secret versions.
        self.version_ids = version_ids  # type: ListSecretVersionIdsResponseBodyVersionIds

    def validate(self):
        if self.version_ids:
            self.version_ids.validate()

    def to_map(self):
        _map = super(ListSecretVersionIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VersionIds') is not None:
            temp_model = ListSecretVersionIdsResponseBodyVersionIds()
            self.version_ids = temp_model.from_map(m['VersionIds'])
        return self


class ListSecretVersionIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSecretVersionIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecretVersionIdsResponse, self).to_map()
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
            temp_model = ListSecretVersionIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretsRequest(TeaModel):
    def __init__(self, fetch_tags=None, filters=None, page_number=None, page_size=None):
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.fetch_tags = fetch_tags  # type: str
        # The number of entries returned per page.
        self.filters = filters  # type: str
        # The secret filter. The filter consists of one or more key-value pairs. You can specify one key-value pair or leave this parameter empty. If you use one tag key or tag value to filter resources, up to 4,000 resources can be queried. If you want to query more than 4,000 resources, call the [ListResourceTags](~~120090~~) operation.
        # 
        # *   Key
        # 
        #     *   Description: the property that you want to filter.
        # 
        #     *   Type: string.
        # 
        #     *   Valid values:
        # 
        #         *   SecretName: the secret name.
        #         *   Description: the description of the secret.
        #         *   TagKey: the tag key.
        #         *   TagValue: the tag value.
        # 
        # *   Values
        # 
        #     *   Description: the value to be included after filtering.
        # 
        #     *   Type: string.
        # 
        #     *   Length: 0 to 10.
        # 
        #     *   Valid values:
        # 
        #         *   If the Key field is set to SecretName, the value must be 1 to 192 characters in length and can contain letters, digits, and special characters `_ / + = . @ -`.
        #         *   If the Key field is set to Description, the value must be 1 to 256 characters in length.
        #         *   If the Key field is set to TagKey, the value must be 1 to 256 characters in length and can contain letters, digits, and special characters `/ _ - . + = @ :`.
        #         *   If the Key field is set to TagValue, the value must be 1 to 256 characters in length and can contain letters, numbers, and special characters `/ _ - . + = @ :`.
        # 
        # The logical relationship between values of the Values field in a key-value pair is OR. Example: `[ {"Key":"SecretName", "Values":["sec1","sec2"]}]`. In this example, the semantics are `SecretName=sec 1 OR SecretName=sec 2`.
        self.page_number = page_number  # type: int
        # The page number of the returned page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSecretsResponseBodySecretListSecretTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretsResponseBodySecretListSecretTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListSecretsResponseBodySecretListSecretTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListSecretsResponseBodySecretListSecretTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecretsResponseBodySecretListSecretTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListSecretsResponseBodySecretListSecretTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListSecretsResponseBodySecretListSecret(TeaModel):
    def __init__(self, create_time=None, planned_delete_time=None, secret_name=None, secret_type=None, tags=None,
                 update_time=None):
        # The tag value.
        self.create_time = create_time  # type: str
        # The resource tags of the secret.
        # 
        # This parameter is not returned if you set the FetchTags parameter to false or do not specify the FetchTags parameter.
        self.planned_delete_time = planned_delete_time  # type: str
        # The type of the secret. Valid values:
        # 
        # *   Generic: indicates a generic secret.
        # *   Rds: indicates a managed ApsaraDB RDS secret.
        self.secret_name = secret_name  # type: str
        # The time when the secret was created.
        self.secret_type = secret_type  # type: str
        # The tag key.
        self.tags = tags  # type: ListSecretsResponseBodySecretListSecretTags
        # The time when the secret is scheduled to be deleted.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListSecretsResponseBodySecretListSecret, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('Tags') is not None:
            temp_model = ListSecretsResponseBodySecretListSecretTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSecretsResponseBodySecretList(TeaModel):
    def __init__(self, secret=None):
        self.secret = secret  # type: list[ListSecretsResponseBodySecretListSecret]

    def validate(self):
        if self.secret:
            for k in self.secret:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecretsResponseBodySecretList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Secret'] = []
        if self.secret is not None:
            for k in self.secret:
                result['Secret'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.secret = []
        if m.get('Secret') is not None:
            for k in m.get('Secret'):
                temp_model = ListSecretsResponseBodySecretListSecret()
                self.secret.append(temp_model.from_map(k))
        return self


class ListSecretsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, secret_list=None, total_count=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.page_number = page_number  # type: int
        # The number of returned secrets.
        self.page_size = page_size  # type: int
        # The list of secrets.
        self.request_id = request_id  # type: str
        # The time when the secret was updated.
        self.secret_list = secret_list  # type: ListSecretsResponseBodySecretList
        # The secret name.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.secret_list:
            self.secret_list.validate()

    def to_map(self):
        _map = super(ListSecretsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_list is not None:
            result['SecretList'] = self.secret_list.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretList') is not None:
            temp_model = ListSecretsResponseBodySecretList()
            self.secret_list = temp_model.from_map(m['SecretList'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSecretsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSecretsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecretsResponse, self).to_map()
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
            temp_model = ListSecretsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, region_id=None, resource_id=None, resource_type=None, tag=None):
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenKmsServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenKmsServiceResponseBody, self).to_map()
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


class OpenKmsServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenKmsServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenKmsServiceResponse, self).to_map()
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
            temp_model = OpenKmsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutSecretValueRequest(TeaModel):
    def __init__(self, secret_data=None, secret_data_type=None, secret_name=None, version_id=None,
                 version_stages=None):
        # The secret value. The value is encrypted and then stored in the new version.
        self.secret_data = secret_data  # type: str
        # The type of the secret value. Valid values:
        # 
        # *   text: This is the default value.
        # *   binary
        self.secret_data_type = secret_data_type  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The new version of the secret value. Version numbers must be unique in each secret.
        self.version_id = version_id  # type: str
        # The stage labels that are used to mark the new version. If you do not specify this parameter, Secrets Manager marks the new version with ACSCurrent.
        self.version_stages = version_stages  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutSecretValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            self.version_stages = m.get('VersionStages')
        return self


class PutSecretValueResponseBodyVersionStages(TeaModel):
    def __init__(self, version_stage=None):
        self.version_stage = version_stage  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutSecretValueResponseBodyVersionStages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class PutSecretValueResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_name=None, version_id=None, version_stages=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The new version of the secret value.
        self.version_id = version_id  # type: str
        # The stage labels that are used to mark the new version.
        self.version_stages = version_stages  # type: PutSecretValueResponseBodyVersionStages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        _map = super(PutSecretValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionStages') is not None:
            temp_model = PutSecretValueResponseBodyVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        return self


class PutSecretValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutSecretValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutSecretValueResponse, self).to_map()
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
            temp_model = PutSecretValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReEncryptRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, destination_encryption_context=None, destination_key_id=None,
                 source_encryption_algorithm=None, source_encryption_context=None, source_key_id=None, source_key_version_id=None):
        # The ciphertext that you want to re-encrypt.
        # 
        # You can set this parameter to the ciphertext that is returned after a symmetric or asymmetric encryption operation.
        # 
        # *   Symmetric encryption: the ciphertext returned after you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation
        # *   Asymmetric encryption: the public key-encrypted ciphertext returned after you call the [GenerateAndExportDataKey](~~176804~~) operation, or the ciphertext encrypted by using the public key of an asymmetric key pair outside KMS
        self.ciphertext_blob = ciphertext_blob  # type: str
        # A JSON string that consists of key-value pairs. This parameter specifies the EncryptionContext that is used to re-encrypt the decrypted data or data key.
        self.destination_encryption_context = destination_encryption_context  # type: dict[str, any]
        # The ID of the symmetric CMK that is used to re-encrypt the ciphertext after the ciphertext is decrypted.
        self.destination_key_id = destination_key_id  # type: str
        # The encryption algorithm based on which the public key is used to encrypt the ciphertext specified by CiphertextBlob. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_encryption_algorithm = source_encryption_algorithm  # type: str
        # A JSON string that consists of key-value pairs. If you specify EncryptionContext when you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation to encrypt the data or data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        # 
        # >  If you set CiphertextBlob to the ciphertext that is returned after a symmetric encryption operation, specify this parameter.
        self.source_encryption_context = source_encryption_context  # type: dict[str, any]
        # The ID of the CMK that is used to decrypt the ciphertext.
        # 
        # This parameter is the globally unique ID of the CMK.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_id = source_key_id  # type: str
        # The ID of the CMK version that is used to decrypt the ciphertext.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_version_id = source_key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReEncryptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.destination_encryption_context is not None:
            result['DestinationEncryptionContext'] = self.destination_encryption_context
        if self.destination_key_id is not None:
            result['DestinationKeyId'] = self.destination_key_id
        if self.source_encryption_algorithm is not None:
            result['SourceEncryptionAlgorithm'] = self.source_encryption_algorithm
        if self.source_encryption_context is not None:
            result['SourceEncryptionContext'] = self.source_encryption_context
        if self.source_key_id is not None:
            result['SourceKeyId'] = self.source_key_id
        if self.source_key_version_id is not None:
            result['SourceKeyVersionId'] = self.source_key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('DestinationEncryptionContext') is not None:
            self.destination_encryption_context = m.get('DestinationEncryptionContext')
        if m.get('DestinationKeyId') is not None:
            self.destination_key_id = m.get('DestinationKeyId')
        if m.get('SourceEncryptionAlgorithm') is not None:
            self.source_encryption_algorithm = m.get('SourceEncryptionAlgorithm')
        if m.get('SourceEncryptionContext') is not None:
            self.source_encryption_context = m.get('SourceEncryptionContext')
        if m.get('SourceKeyId') is not None:
            self.source_key_id = m.get('SourceKeyId')
        if m.get('SourceKeyVersionId') is not None:
            self.source_key_version_id = m.get('SourceKeyVersionId')
        return self


class ReEncryptShrinkRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, destination_encryption_context_shrink=None, destination_key_id=None,
                 source_encryption_algorithm=None, source_encryption_context_shrink=None, source_key_id=None, source_key_version_id=None):
        # The ciphertext that you want to re-encrypt.
        # 
        # You can set this parameter to the ciphertext that is returned after a symmetric or asymmetric encryption operation.
        # 
        # *   Symmetric encryption: the ciphertext returned after you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation
        # *   Asymmetric encryption: the public key-encrypted ciphertext returned after you call the [GenerateAndExportDataKey](~~176804~~) operation, or the ciphertext encrypted by using the public key of an asymmetric key pair outside KMS
        self.ciphertext_blob = ciphertext_blob  # type: str
        # A JSON string that consists of key-value pairs. This parameter specifies the EncryptionContext that is used to re-encrypt the decrypted data or data key.
        self.destination_encryption_context_shrink = destination_encryption_context_shrink  # type: str
        # The ID of the symmetric CMK that is used to re-encrypt the ciphertext after the ciphertext is decrypted.
        self.destination_key_id = destination_key_id  # type: str
        # The encryption algorithm based on which the public key is used to encrypt the ciphertext specified by CiphertextBlob. For more information about encryption algorithms, see [AsymmetricDecrypt](~~148130~~).
        # 
        # Valid values:
        # 
        # *   RSAES_OAEP_SHA\_256
        # *   RSAES_OAEP_SHA\_1
        # *   SM2PKE
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_encryption_algorithm = source_encryption_algorithm  # type: str
        # A JSON string that consists of key-value pairs. If you specify EncryptionContext when you call the [Encrypt](~~28949~~), [GenerateDataKey](~~28948~~), [GenerateDataKeyWithoutPlaintext](~~134043~~), or [GenerateAndExportDataKey](~~176804~~) operation to encrypt the data or data key, an equivalent value is required here. For more information, see [EncryptionContext](~~42975~~).
        # 
        # >  If you set CiphertextBlob to the ciphertext that is returned after a symmetric encryption operation, specify this parameter.
        self.source_encryption_context_shrink = source_encryption_context_shrink  # type: str
        # The ID of the CMK that is used to decrypt the ciphertext.
        # 
        # This parameter is the globally unique ID of the CMK.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_id = source_key_id  # type: str
        # The ID of the CMK version that is used to decrypt the ciphertext.
        # 
        # >  If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter.
        self.source_key_version_id = source_key_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReEncryptShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.destination_encryption_context_shrink is not None:
            result['DestinationEncryptionContext'] = self.destination_encryption_context_shrink
        if self.destination_key_id is not None:
            result['DestinationKeyId'] = self.destination_key_id
        if self.source_encryption_algorithm is not None:
            result['SourceEncryptionAlgorithm'] = self.source_encryption_algorithm
        if self.source_encryption_context_shrink is not None:
            result['SourceEncryptionContext'] = self.source_encryption_context_shrink
        if self.source_key_id is not None:
            result['SourceKeyId'] = self.source_key_id
        if self.source_key_version_id is not None:
            result['SourceKeyVersionId'] = self.source_key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('DestinationEncryptionContext') is not None:
            self.destination_encryption_context_shrink = m.get('DestinationEncryptionContext')
        if m.get('DestinationKeyId') is not None:
            self.destination_key_id = m.get('DestinationKeyId')
        if m.get('SourceEncryptionAlgorithm') is not None:
            self.source_encryption_algorithm = m.get('SourceEncryptionAlgorithm')
        if m.get('SourceEncryptionContext') is not None:
            self.source_encryption_context_shrink = m.get('SourceEncryptionContext')
        if m.get('SourceKeyId') is not None:
            self.source_key_id = m.get('SourceKeyId')
        if m.get('SourceKeyVersionId') is not None:
            self.source_key_version_id = m.get('SourceKeyVersionId')
        return self


class ReEncryptResponseBody(TeaModel):
    def __init__(self, ciphertext_blob=None, key_id=None, key_version_id=None, request_id=None):
        # The ciphertext re-encrypted.
        self.ciphertext_blob = ciphertext_blob  # type: str
        # The ID of the CMK that is used to decrypt the original ciphertext.
        # 
        # This parameter is the globally unique ID of the CMK.
        self.key_id = key_id  # type: str
        # The ID of the CMK version that is used to decrypt the original ciphertext.
        self.key_version_id = key_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReEncryptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReEncryptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReEncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReEncryptResponse, self).to_map()
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
            temp_model = ReEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreSecretRequest(TeaModel):
    def __init__(self, secret_name=None):
        # The name of the secret you want to restore.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class RestoreSecretResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_name=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class RestoreSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestoreSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreSecretResponse, self).to_map()
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
            temp_model = RestoreSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RotateSecretRequest(TeaModel):
    def __init__(self, secret_name=None, version_id=None):
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The version number of the secret after the secret is rotated.
        # 
        # >  The version number is used to ensure the idempotence of the request. Secrets Manager uses this version number to prevent your application from creating the same version of the secret when the application retries a request. If a version number already exists, Secrets Manager ignores the request for rotation and returns a success message.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RotateSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RotateSecretResponseBody(TeaModel):
    def __init__(self, arn=None, request_id=None, secret_name=None, version_id=None):
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.arn = arn  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str
        # The version number of the secret after the secret is rotated.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RotateSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RotateSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RotateSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RotateSecretResponse, self).to_map()
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
            temp_model = RotateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScheduleKeyDeletionRequest(TeaModel):
    def __init__(self, key_id=None, pending_window_in_days=None):
        # The ID of the customer master key (CMK). The ID must be globally unique.
        self.key_id = key_id  # type: str
        # The scheduled period after which the CMK is deleted. During this period, the CMK is in the PendingDeletion state. After this period ends, you cannot cancel the key deletion task.
        # 
        # Valid values: 7 to 366.
        # 
        # Unit: days.
        self.pending_window_in_days = pending_window_in_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScheduleKeyDeletionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.pending_window_in_days is not None:
            result['PendingWindowInDays'] = self.pending_window_in_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('PendingWindowInDays') is not None:
            self.pending_window_in_days = m.get('PendingWindowInDays')
        return self


class ScheduleKeyDeletionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScheduleKeyDeletionResponseBody, self).to_map()
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


class ScheduleKeyDeletionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScheduleKeyDeletionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScheduleKeyDeletionResponse, self).to_map()
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
            temp_model = ScheduleKeyDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeletionProtectionRequest(TeaModel):
    def __init__(self, deletion_protection_description=None, enable_deletion_protection=None,
                 protected_resource_arn=None):
        # The description of deletion protection.
        # 
        # >  This parameter takes effect only when you set the EnableDeletionProtection parameter to true.
        self.deletion_protection_description = deletion_protection_description  # type: str
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # *   true: enables deletion protection.
        # *   false: disables deletion protection.
        self.enable_deletion_protection = enable_deletion_protection  # type: bool
        # The ARN of the CMK for which you want to set deletion protection.
        # 
        # You can call the [DescribeKey](~~28952~~) operation to query the CMK ARN.
        self.protected_resource_arn = protected_resource_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeletionProtectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_protection_description is not None:
            result['DeletionProtectionDescription'] = self.deletion_protection_description
        if self.enable_deletion_protection is not None:
            result['EnableDeletionProtection'] = self.enable_deletion_protection
        if self.protected_resource_arn is not None:
            result['ProtectedResourceArn'] = self.protected_resource_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletionProtectionDescription') is not None:
            self.deletion_protection_description = m.get('DeletionProtectionDescription')
        if m.get('EnableDeletionProtection') is not None:
            self.enable_deletion_protection = m.get('EnableDeletionProtection')
        if m.get('ProtectedResourceArn') is not None:
            self.protected_resource_arn = m.get('ProtectedResourceArn')
        return self


class SetDeletionProtectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeletionProtectionResponseBody, self).to_map()
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


class SetDeletionProtectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDeletionProtectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDeletionProtectionResponse, self).to_map()
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
            temp_model = SetDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourceRequest(TeaModel):
    def __init__(self, certificate_id=None, key_id=None, secret_name=None, tags=None):
        # The ID of the certificate.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.certificate_id = certificate_id  # type: str
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.key_id = key_id  # type: str
        # The name of the secret.
        # 
        # >  You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.secret_name = secret_name  # type: str
        # One or more tags that you want to add. The value is in the array format.
        # 
        # Tag attributes:
        # 
        # *   TagKey: the tag key.
        # *   TagValue: the tag value.
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourceResponseBody, self).to_map()
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


class TagResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourceResponse, self).to_map()
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
            temp_model = TagResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_id=None, resource_type=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourceRequest(TeaModel):
    def __init__(self, certificate_id=None, key_id=None, secret_name=None, tag_keys=None):
        self.certificate_id = certificate_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.key_id = key_id  # type: str
        self.secret_name = secret_name  # type: str
        self.tag_keys = tag_keys  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourceResponseBody, self).to_map()
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


class UntagResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourceResponse, self).to_map()
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
            temp_model = UntagResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(self, alias_name=None, key_id=None):
        # The alias that you want to bind.
        # 
        # The value must be 1 to 255 characters in length and must include the alias/ prefix.
        self.alias_name = alias_name  # type: str
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class UpdateAliasResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAliasResponseBody, self).to_map()
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


class UpdateAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAliasResponse, self).to_map()
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
            temp_model = UpdateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationAccessPointRequest(TeaModel):
    def __init__(self, description=None, name=None, policies=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.policies = policies  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationAccessPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policies is not None:
            result['Policies'] = self.policies
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        return self


class UpdateApplicationAccessPointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationAccessPointResponseBody, self).to_map()
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


class UpdateApplicationAccessPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationAccessPointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationAccessPointResponse, self).to_map()
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
            temp_model = UpdateApplicationAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCertificateStatusRequest(TeaModel):
    def __init__(self, certificate_id=None, status=None):
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str
        # The status of the certificate. Valid values:
        # 
        # *   INACTIVE: The certificate is disabled.
        # 
        # *   ACTIVE: The certificate is enabled.
        # 
        # *   REVOKED: The certificate is revoked.
        # 
        # > If the certificate is in the REVOKED state, you can use the certificate only to verify a signature, but not to generate a signature.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCertificateStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateCertificateStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCertificateStatusResponseBody, self).to_map()
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


class UpdateCertificateStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCertificateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCertificateStatusResponse, self).to_map()
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
            temp_model = UpdateCertificateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKeyDescriptionRequest(TeaModel):
    def __init__(self, description=None, key_id=None):
        # The description of the CMK. This description includes the purpose of the CMK, such as the types of data that you want to protect and applications that can use the CMK.
        self.description = description  # type: str
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKeyDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class UpdateKeyDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKeyDescriptionResponseBody, self).to_map()
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


class UpdateKeyDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateKeyDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateKeyDescriptionResponse, self).to_map()
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
            temp_model = UpdateKeyDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKmsInstanceBindVpcRequest(TeaModel):
    def __init__(self, bind_vpcs=None, kms_instance_id=None):
        self.bind_vpcs = bind_vpcs  # type: str
        self.kms_instance_id = kms_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKmsInstanceBindVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs
        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindVpcs') is not None:
            self.bind_vpcs = m.get('BindVpcs')
        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')
        return self


class UpdateKmsInstanceBindVpcResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKmsInstanceBindVpcResponseBody, self).to_map()
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


class UpdateKmsInstanceBindVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateKmsInstanceBindVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateKmsInstanceBindVpcResponse, self).to_map()
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
            temp_model = UpdateKmsInstanceBindVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNetworkRuleRequest(TeaModel):
    def __init__(self, description=None, name=None, source_private_ip=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.source_private_ip = source_private_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNetworkRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.source_private_ip is not None:
            result['SourcePrivateIp'] = self.source_private_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourcePrivateIp') is not None:
            self.source_private_ip = m.get('SourcePrivateIp')
        return self


class UpdateNetworkRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNetworkRuleResponseBody, self).to_map()
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


class UpdateNetworkRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNetworkRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNetworkRuleResponse, self).to_map()
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
            temp_model = UpdateNetworkRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyRequest(TeaModel):
    def __init__(self, access_control_rules=None, description=None, name=None, permissions=None, resources=None):
        self.access_control_rules = access_control_rules  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.permissions = permissions  # type: str
        self.resources = resources  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_rules is not None:
            result['AccessControlRules'] = self.access_control_rules
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlRules') is not None:
            self.access_control_rules = m.get('AccessControlRules')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class UpdatePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolicyResponseBody, self).to_map()
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


class UpdatePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePolicyResponse, self).to_map()
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
            temp_model = UpdatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRotationPolicyRequest(TeaModel):
    def __init__(self, enable_automatic_rotation=None, key_id=None, rotation_interval=None):
        # Specifies whether to enable automatic key rotation. Valid values:
        # 
        # *   true: enables automatic key rotation.
        # *   false: disables automatic key rotation.
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        # The ID of the customer master key (CMK). The ID must be globally unique.
        self.key_id = key_id  # type: str
        # The period of automatic key rotation. Specify the value in the integer\[unit] format. The following units are supported: d (day), h (hour), m (minute), and s (second). For example, you can use either 7d or 604800s to specify a seven-day period. The period can range from 7 days to 730 days.
        # 
        # >  If you set the EnableAutomaticRotation parameter to true, you must also specify this parameter. If you set the EnableAutomaticRotation parameter to false, you can leave this parameter unspecified.
        self.rotation_interval = rotation_interval  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRotationPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class UpdateRotationPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRotationPolicyResponseBody, self).to_map()
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


class UpdateRotationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRotationPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRotationPolicyResponse, self).to_map()
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
            temp_model = UpdateRotationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretRequestExtendedConfig(TeaModel):
    def __init__(self, custom_data=None):
        # The custom data in the extended configuration of the secret.
        # 
        # > *   If this parameter is specified, the existing extended configuration of the secret is updated.
        # > *   This parameter is unavailable for generic secrets.
        self.custom_data = custom_data  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretRequestExtendedConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_data is not None:
            result['CustomData'] = self.custom_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')
        return self


class UpdateSecretRequest(TeaModel):
    def __init__(self, extended_config=None, description=None, secret_name=None):
        self.extended_config = extended_config  # type: UpdateSecretRequestExtendedConfig
        # The description of the secret.
        self.description = description  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        if self.extended_config:
            self.extended_config.validate()

    def to_map(self):
        _map = super(UpdateSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendedConfig') is not None:
            temp_model = UpdateSecretRequestExtendedConfig()
            self.extended_config = temp_model.from_map(m['ExtendedConfig'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretShrinkRequestExtendedConfig(TeaModel):
    def __init__(self, custom_data=None):
        # The custom data in the extended configuration of the secret.
        # 
        # > *   If this parameter is specified, the existing extended configuration of the secret is updated.
        # > *   This parameter is unavailable for generic secrets.
        self.custom_data = custom_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretShrinkRequestExtendedConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_data is not None:
            result['CustomData'] = self.custom_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')
        return self


class UpdateSecretShrinkRequest(TeaModel):
    def __init__(self, extended_config=None, description=None, secret_name=None):
        self.extended_config = extended_config  # type: UpdateSecretShrinkRequestExtendedConfig
        # The description of the secret.
        self.description = description  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        if self.extended_config:
            self.extended_config.validate()

    def to_map(self):
        _map = super(UpdateSecretShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendedConfig') is not None:
            temp_model = UpdateSecretShrinkRequestExtendedConfig()
            self.extended_config = temp_model.from_map(m['ExtendedConfig'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_name=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSecretResponse, self).to_map()
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
            temp_model = UpdateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretRotationPolicyRequest(TeaModel):
    def __init__(self, enable_automatic_rotation=None, rotation_interval=None, secret_name=None):
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # *   true: enables automatic rotation.
        # *   false: does not enable automatic rotation. This is the default value.
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).
        # 
        # The value is in the `integer[unit]` format.````
        # 
        # The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s indicate a seven-day interval.
        # 
        # >  This parameter is required if you set the EnableAutomaticRotation parameter to true. This parameter is ignored if you set the EnableAutomaticRotation parameter to false or does not specify the EnableAutomaticRotation parameter.
        self.rotation_interval = rotation_interval  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretRotationPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretRotationPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_name=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The name of the secret.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretRotationPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretRotationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSecretRotationPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSecretRotationPolicyResponse, self).to_map()
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
            temp_model = UpdateSecretRotationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretVersionStageRequest(TeaModel):
    def __init__(self, move_to_version=None, remove_from_version=None, secret_name=None, version_stage=None):
        # The version from which you want to remove the specified stage label.
        # 
        # >  You must specify at least one of the RemoveFromVersion and MoveToVersion parameters.
        self.move_to_version = move_to_version  # type: str
        # The specified stage label. Valid values:
        # 
        # *   ACSCurrent
        # *   ACSPrevious
        # *   Custom stage label
        self.remove_from_version = remove_from_version  # type: str
        # The operation that you want to perform. Set the value to **UpdateSecretVersionStage**.
        self.secret_name = secret_name  # type: str
        # The name of the secret.
        self.version_stage = version_stage  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretVersionStageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.move_to_version is not None:
            result['MoveToVersion'] = self.move_to_version
        if self.remove_from_version is not None:
            result['RemoveFromVersion'] = self.remove_from_version
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MoveToVersion') is not None:
            self.move_to_version = m.get('MoveToVersion')
        if m.get('RemoveFromVersion') is not None:
            self.remove_from_version = m.get('RemoveFromVersion')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        return self


class UpdateSecretVersionStageResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_name=None):
        # The name of the secret.
        self.request_id = request_id  # type: str
        # The version to which you want to apply the specified stage label.
        # 
        # > * You must specify at least one of the RemoveFromVersion and MoveToVersion parameters.
        # > * If the VersionStage parameter is set to ACSCurrent or ACSPrevious, this parameter is required.
        self.secret_name = secret_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretVersionStageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        return self


class UpdateSecretVersionStageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSecretVersionStageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSecretVersionStageResponse, self).to_map()
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
            temp_model = UpdateSecretVersionStageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCertificateRequest(TeaModel):
    def __init__(self, certificate=None, certificate_chain=None, certificate_id=None):
        # The certificate issued by the CA, which is in the Privacy Enhanced Mail (PEM) format.
        self.certificate = certificate  # type: str
        # The certificate chain issued by the CA, which is in the PEM format.
        self.certificate_chain = certificate_chain  # type: str
        # The ID of the certificate. The ID must be globally unique in Certificates Manager.
        self.certificate_id = certificate_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class UploadCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadCertificateResponseBody, self).to_map()
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


class UploadCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadCertificateResponse, self).to_map()
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
            temp_model = UploadCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


